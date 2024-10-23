#!/usr/bin/env python
import csv
import gettext
import json
import logging
import os
import re
import sys
import warnings
from collections import defaultdict
from contextlib import contextmanager
from copy import deepcopy
from glob import glob
from io import StringIO
from pathlib import Path

import click
import json_merge_patch
import jsonref
import lxml.etree
import lxml.html
import requests
from babel.messages.pofile import read_po
from docutils.utils import relative_path
from lxml import etree
from ocdskit.schema import add_validation_properties, get_schema_fields

basedir = Path(__file__).resolve().parent
schemadir = basedir / 'schema'
localedir = basedir / 'docs' / 'locale'

sys.path.append(str(basedir / 'docs'))

from conf import release  # noqa: E402


def custom_warning_formatter(message, category, filename, lineno, line=None):
    return str(message) + '\n'


warnings.formatwarning = custom_warning_formatter

versioned_template = json.loads("""
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "releaseDate": {
        "format": "date-time",
        "type": "string"
      },
      "releaseID": {
        "type": "string"
      },
      "value": {},
      "releaseTag": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
""")

common_versioned_definitions = {
    'StringNullUriVersioned': {
        'type': ['string', 'null'],
        'format': 'uri',
    },
    'StringNullDateTimeVersioned': {
        'type': ['string', 'null'],
        'format': 'date-time',
    },
    'StringNullVersioned': {
        'type': ['string', 'null'],
        'format': None,
    },
}

recognized_types = (
    # Array
    ['array'],
    ['array', 'null'],  # optional string arrays

    # Object
    ['object'],
    ['object', 'null'],  # /Organization/details

    # String
    ['string'],
    ['string', 'null'],

    # Literal
    ['boolean', 'null'],
    ['integer', 'null'],
    ['number', 'null'],

    # Mixed
    ['string', 'integer'],
    ['string', 'integer', 'null'],
)

keywords_to_remove = (
    # Metadata keywords
    # https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-6
    'title',
    'description',
    'default',

    # Extended keywords
    # http://os4d.opendataservices.coop/development/schema/#extended-json-schema
    'omitWhenMerged',
    'wholeListMerge',
)


def json_load(filename, library=json, **kwargs):
    """Load JSON data from the given filename."""
    with (schemadir / filename).open() as f:
        return library.load(f, **kwargs)


def json_dump(filename, data):
    """Write JSON data to the given filename."""
    with (schemadir / filename).open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def csv_load(url, delimiter=','):
    """Load CSV data into a ``csv.DictReader`` from the given URL."""
    return csv.DictReader(StringIO(get(url).text), delimiter=delimiter)


@contextmanager
def csv_dump(filename, fieldnames):
    """Write CSV headers to the given filename, and yield a ``csv.writer``."""
    f = (schemadir / 'codelists' / filename).open('w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(fieldnames)
    try:
        yield writer
    finally:
        f.close()


def get(url):
    """GET a URL and returns the response. Raise an exception if the status code is not successful."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response


def coerce_to_list(data, key):
    """Return the value of the ``key`` key in the ``data`` mapping. If the value is a string, wrap it in an array."""
    item = data.get(key, [])
    if isinstance(item, str):
        return [item]
    return item


def get_metaschema():
    """Patches and returns the JSON Schema Draft 4 metaschema."""
    return json_merge_patch.merge(json_load('metaschema/json-schema-draft-4.json'),
                                  json_load('metaschema/meta-schema-patch.json'))


def get_common_definition_ref(item):
    """
    Return a schema that references the common definition that the ``item`` matches: "StringNullUriVersioned",
    "StringNullDateTimeVersioned" or "StringNullVersioned".
    """
    for name, keywords in common_versioned_definitions.items():
        # If the item matches the definition.
        if any(item.get(keyword) != value for keyword, value in keywords.items()):
            continue
        # And adds no keywords to the definition.
        if any(keyword not in {*keywords, *keywords_to_remove} for keyword in item):
            continue
        return {'$ref': f'#/definitions/{name}'}
    return None


def add_versioned(schema, unversioned_pointers, pointer=''):
    """Call ``_add_versioned`` on each field."""
    for key, value in schema['properties'].items():
        new_pointer = f'{pointer}/properties/{key}'
        _add_versioned(schema, unversioned_pointers, new_pointer, key, value)

    for key, value in schema.get('definitions', {}).items():
        new_pointer = f'{pointer}/definitions/{key}'
        add_versioned(value, unversioned_pointers, pointer=new_pointer)


def _add_versioned(schema, unversioned_pointers, pointer, key, value):
    """
    Perform the changes to the schema to refer to versioned/unversioned definitions.

    :param schema dict: the schema of the object on which the field is defined
    :param unversioned_pointers set: JSON Pointers to ``id`` fields to leave unversioned if the object is in an array
    :param pointer str: the field's pointer
    :param key str: the field's name
    :param value str: the field's schema
    """
    # Skip unversioned fields.
    if pointer in unversioned_pointers:
        return

    types = coerce_to_list(value, 'type')

    # If a type is unrecognized, we might need to update this script.
    if (
        '$ref' not in value
        and types not in recognized_types
        and not (pointer == '/definitions/Quantity/properties/value' and types == ['string', 'number', 'null'])
    ):
        warnings.warn(f'{pointer} has unrecognized type {types}')

    # For example, if $ref is used.
    if not types:
        # Ignore the `amendment` field, which had no `id` field in OCDS 1.0.
        if 'deprecated' not in value:
            versioned_pointer = f"{value['$ref'][1:]}/properties/id"
            # If the `id` field is on an object not in an array, it needs to be versioned (e.g. buyer/properties/id).
            if versioned_pointer in unversioned_pointers:
                value['$ref'] = value['$ref'] + 'VersionedId'
        return

    # Reference a common versioned definition if possible, to limit the size of the schema.
    ref = get_common_definition_ref(value)
    if ref:
        schema['properties'][key] = ref

    # Iterate into objects with properties like `Item.unit`. Otherwise, version objects with no properties as a
    # whole, like `Organization.details`.
    elif types == ['object'] and 'properties' in value:
        add_versioned(value, unversioned_pointers, pointer=pointer)

    else:
        new_value = deepcopy(value)

        if types == ['array']:
            item_types = coerce_to_list(value['items'], 'type')

            # See https://standard.open-contracting.org/latest/en/schema/merging/#whole-list-merge
            if value.get('wholeListMerge'):
                # Update `$ref` to the unversioned definition.
                if '$ref' in value['items']:
                    new_value['items']['$ref'] = value['items']['$ref'] + 'Unversioned'
                # Otherwise, similarly, don't iterate over item properties.
            # See https://standard.open-contracting.org/latest/en/schema/merging/#lists
            elif '$ref' in value['items']:
                # Leave `$ref` to the versioned definition.
                return
            # Exceptional case for deprecated `Amendment.changes`.
            elif item_types == ['object'] and pointer == '/definitions/Amendment/properties/changes':
                return
            # Warn in case new combinations are added to the release schema.
            elif item_types != ['string']:
                # Note: Versioning the properties of un-$ref'erenced objects in arrays isn't implemented. However,
                # this combination hasn't occurred, with the exception of `Amendment/changes`.
                warnings.warn(f"{pointer}/items has unexpected type {item_types}")

        versioned = deepcopy(versioned_template)
        versioned['items']['properties']['value'] = new_value
        schema['properties'][key] = versioned


def update_refs_to_unversioned_definitions(schema):
    """Replace ``$ref`` values with unversioned definitions."""
    for key, value in schema.items():
        if key == '$ref':
            schema[key] = value + 'Unversioned'
        elif isinstance(value, dict):
            update_refs_to_unversioned_definitions(value)


def get_unversioned_pointers(schema, fields, pointer=''):
    """Return the JSON Pointers to ``id`` fields that must not be versioned if the object is in an array."""
    if isinstance(schema, list):
        for index, item in enumerate(schema):
            get_unversioned_pointers(item, fields, pointer=f'{pointer}/{index}')
    elif isinstance(schema, dict):
        # Follows the logic of _get_merge_rules in merge.py from ocds-merge.
        types = coerce_to_list(schema, 'type')

        # If an array is whole list merge, its items are unversioned.
        if 'array' in types and schema.get('wholeListMerge'):
            return
        if 'array' in types and 'items' in schema:
            item_types = coerce_to_list(schema['items'], 'type')
            # If an array mixes objects and non-objects, it is whole list merge.
            if any(item_type != 'object' for item_type in item_types):
                return
            # If it is an array of objects, any `id` fields are unversioned.
            if 'id' in schema['items']['properties']:
                if hasattr(schema['items'], '__reference__'):
                    reference = schema['items'].__reference__['$ref'][1:]
                else:
                    reference = pointer
                fields.add(f'{reference}/properties/id')

        for key, value in schema.items():
            get_unversioned_pointers(value, fields, pointer=f'{pointer}/{key}')


def remove_omit_when_merged(schema):
    """Remove properties that set ``omitWhenMerged``."""
    if isinstance(schema, list):
        for item in schema:
            remove_omit_when_merged(item)
    elif isinstance(schema, dict):
        for key, value in schema.items():
            if key == 'properties':
                for prop in list(value):
                    if value[prop].get('omitWhenMerged'):
                        del value[prop]
                        if prop in schema['required']:
                            schema['required'].remove(prop)
            remove_omit_when_merged(value)


def remove_metadata_and_extended_keywords(schema):
    """Remove metadata and extended keywords from properties and definitions."""
    if isinstance(schema, list):
        for item in schema:
            remove_metadata_and_extended_keywords(item)
    elif isinstance(schema, dict):
        for key, value in schema.items():
            if key in {'definitions', 'properties'}:
                for subschema in value.values():
                    for keyword in keywords_to_remove:
                        subschema.pop(keyword, None)
            remove_metadata_and_extended_keywords(value)


def get_versioned_release_schema(schema):
    """Return the versioned release schema."""
    # Update schema metadata.
    release_with_underscores = release.replace('.', '__')
    schema['id'] = f'https://standard.open-contracting.org/schema/{release_with_underscores}/versioned-release-validation-schema.json'
    schema['title'] = 'Schema for a compiled, versioned Open Contracting Release.'

    # Release IDs, dates and tags appear alongside values in the versioned release schema.
    remove_omit_when_merged(schema)

    # Create unversioned copies of all definitions.
    unversioned_definitions = {k + 'Unversioned': deepcopy(v) for k, v in schema['definitions'].items()}
    update_refs_to_unversioned_definitions(unversioned_definitions)

    # Determine which `id` fields occur on objects in arrays.
    unversioned_pointers = set()
    get_unversioned_pointers(jsonref.replace_refs(schema), unversioned_pointers)

    # Omit `ocid` from versioning.
    ocid = schema['properties'].pop('ocid')
    add_versioned(schema, unversioned_pointers)
    schema['properties']['ocid'] = ocid

    # Add the common versioned definitions.
    for name, keywords in common_versioned_definitions.items():
        versioned = deepcopy(versioned_template)
        for keyword, value in keywords.items():
            if value:
                versioned['items']['properties']['value'][keyword] = value
        schema['definitions'][name] = versioned

    # Add missing definitions.
    while True:
        try:
            jsonref.replace_refs(schema, lazy_load=False)
            break
        except jsonref.JsonRefError as e:
            name = e.cause.args[0]

            if name.endswith('VersionedId'):
                # Add a copy of an definition with a versioned `id` field, using the same logic as before.
                definition = deepcopy(schema['definitions'][name[:-11]])
                pointer = f'/definitions/{name[:-11]}/properties/id'
                pointers = unversioned_pointers - {pointer}
                _add_versioned(definition, pointers, pointer, 'id', definition['properties']['id'])
            else:
                # Add a copy of an definition with no versioned fields.
                definition = unversioned_definitions[name]

            schema['definitions'][name] = definition

    # Remove all metadata and extended keywords.
    remove_metadata_and_extended_keywords(schema)

    return schema


def add_key_based_validation_properties(schema):
    """
    Add validation properties based on key names.

    * "format": "email" if the key is "email"
    * "minimum": 0 to "quantity", "durationInDays" and "numberOfTenderers fields
    * "required": ["id", "name"] to "Organization" and "OrganizationReference"
    * "required": ["id"] to "Amendment" and "RelatedProcess"
    * "$ref": "#/definitions/UnitValue" to "Unit.value"

    Removes "integer" type from "id" and "projectID" fields.

    :param dict schema: a JSON schema
    """
    if isinstance(schema, list):
        for item in schema:
            add_key_based_validation_properties(item)
    elif isinstance(schema, dict):
        for key, value in schema.items():
            if key == 'email':
                value['format'] = 'email'
            elif key in ['quantity', 'durationInDays', 'numberOfTenderers']:
                value['minimum'] = 0
            elif key in ['Organization', 'OrganizationReference']:
                value['required'] = ['id', 'name']
                value['properties']['name']['type'] = "string"
                value['properties']['id']['type'] = "string"
            elif key in ['Amendment', 'RelatedProcess']:
                value['required'] = ['id']
                value['properties']['id']['type'] = "string"
            elif key in ['id', 'projectID']:
                if 'type' in value and 'integer' in value['type']:
                    value['type'].remove('integer')
            elif key == 'Unit':
                value['properties']['value']['$ref'] = '#/definitions/UnitValue'

            add_key_based_validation_properties(value)


def get_strict_schema(schema):
    """
    Return the strict version of the schema.
    """
    # Update schema metadata.
    release_with_underscores = release.replace('.', '__')
    schema['id'] = schema['id'].replace(release_with_underscores,
                                        f'{release_with_underscores}/strict')
    schema['title'] = f'Strict {schema["title"][0].lower()}{schema["title"][1:]}'
    schema['description'] = f'{schema["description"]} The strict schema adds additional validation rules planned for inclusion in OCDS 2.0. Use of the strict schema is a voluntary opportunity to improve data quality.' # noqa: E501

    # Add validation properties
    add_validation_properties(schema)

    # Add key-based validation properties
    add_key_based_validation_properties(schema)

    # Remove null types from package schemas
    if 'package' in schema['id']:
        remove_nulls(schema)

    return schema


def remove_nulls(schema):
    """
    Remove null types.
    """
    if isinstance(schema, dict):
        for key, value in schema.items():
            if key == 'type' and isinstance(value, list) and 'null' in value:
                value.remove('null')

            remove_nulls(value)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
def unused_terms(filename):
    """
    Print terms in FILENAME that don't occur in the documentation.

    Can be used to remove unused terms from a glossary.
    """
    paths = []
    for extension in ('csv', 'json', 'md'):
        paths.extend(glob(str(basedir / 'docs' / '**' / f'*.{extension}'), recursive=True))

    corpus = []
    for path in paths:
        with open(path) as f:
            # Replace punctuation with whitespace, except in abbreviations like "e.g.".
            corpus.append(re.sub(r'(?<!\b[a-z])[.,:"’[\]]', ' ', f.read()).lower())
    corpus = ' '.join(corpus)

    with open(filename) as f:
        for line in f:
            if f' {line.strip().lower()} ' not in corpus:
                click.echo(line, nl=False)


@cli.command()
@click.option('--ignore-base', help='A base branch to ignore, e.g. 1.2-dev')
def missing_changelog(ignore_base):
    """Print pull requests not mentioned in the changelog."""
    # Ignore PRs to the ppp-extension branch, which became OCDS for PPPs.
    ignore = ['ppp-extension']
    if ignore_base:
        ignore.append(ignore_base)

    # Ignore PRs to unmerged branches.
    url = 'https://api.github.com/repos/open-contracting/standard/pulls?per_page=100&state=open'
    response = get(url)
    ignore.extend(pr['head']['ref'] for pr in response.json())

    with open(basedir / 'docs' / 'history' / 'changelog.md') as f:
        prs = [int(n) for n in re.findall(r'https://github.com/open-contracting/standard/pull/(\d+)', f.read())]

    prs.extend([
        # Reverted
        971, 977,
        # Obsoleted by the Primer
        1017,
    ])

    # Ignore PRs that sync branches or that release versions/
    pattern = re.compile(r'^(?:Merge \S+ into \S+|\S+ Release)$')

    count = 0

    url = 'https://api.github.com/repos/open-contracting/standard/pulls?per_page=100&state=closed'
    while url:
        response = get(url)
        url = response.links.get('next', {}).get('url')

        for pr in response.json():
            number = pr['number']
            merged_at = pr['merged_at']
            milestone = pr['milestone'] or {}
            milestone_number = milestone.get('number')
            milestone_title = milestone.get('title')
            title = pr['title']
            base_ref = pr['base']['ref']

            # Include merged PRs, not in the "Minor:" or "1.0-RC" milestones, not syncing branches, and not ignored.
            if not merged_at or milestone_number in {26, 27, 28, 29, 2} or pattern.search(title) or base_ref in ignore:
                if number in prs:
                    click.echo(f'WARNING: #{number} should not be in changelog', file=sys.stderr)
                continue

            if number not in prs:
                count += 1
                click.echo(f"[#{number}](https://github.com/open-contracting/standard/pull/{number}) "
                           f"({milestone_title}) {merged_at[:10]}: {title} ({base_ref}:{pr['head']['ref']})")

    if count:
        click.echo(count)


@cli.command()
def pre_commit():
    """
    Update derivative schema files, and generate a CSV file of multilingual fields.

    \b
    - meta-schema.json
    - dereferenced-release-schema.json
    - versioned-release-validation-schema.json
    - strict-release-schema.json
    - strict-release-package.json
    - strict-record-package.jso
    - strict-dereferenced-release-schema.json
    - strict-versioned-release-validation-schema.json
    """
    nonmultilingual = {
        # Identifiers.
        'amendsReleaseID', 'id', 'identifier', 'identifiers', 'ocid', 'relatedItems', 'releaseID',
        # Missing format properties. https://github.com/open-contracting/standard/issues/881
        'email',
        # Published-defined formats.
        'faxNumber', 'postalCode', 'telephone',
        # Published-defined codelists.
        'code', 'scheme',
    }

    release_schema = json_load('release-schema.json')
    jsonref_release_schema = json_load('release-schema.json', jsonref, merge_props=True)

    counts = defaultdict(list)
    nonstring = ('boolean', 'integer', 'number', 'object')
    for field in get_schema_fields(jsonref_release_schema):
        name = field.path_components[-1]
        # Skip definitions (output dereferenced properties only). Skip deprecated fields.
        if field.definition_pointer_components or field.deprecated:
            continue
        multilingual = (
            # If a field can be a non-string, it is not multilingual.
            not any(t in field.schema['type'] for t in nonstring)
            and ('array' not in field.schema['type'] or not any(t in field.schema['items']['type'] for t in nonstring))
            # If a field's value is constrained to a codelist or format, it is not multilingual.
            and not any(prop in field.schema for prop in ('codelist', 'format'))
            # If an array can contain non-strings, it is not multilingual.
            and not ('array' in field.schema['type'] and 'object' in field.schema['items']['type'])
            # Specific exceptions.
            and name not in nonmultilingual
        )
        field.sep = '/'
        if name in counts and bool(counts[name]) ^ multilingual:
            if not multilingual and field.schema['type'] == 'object':
                click.secho(f'{field.path} is an object. {" & ".join(counts[name])} is/are multilingual.', fg='yellow')
            elif multilingual:
                raise click.ClickException(
                    f'{name} is multilingual at {field.path}, but not elsewhere'
                )
            else:
                raise click.ClickException(
                    f'{name} is multilingual at {" & ".join(counts[name])}, but not at {field.path}'
                )
        if multilingual:
            counts[name].append(field.path)
        else:
            counts[name] = counts[name]

    bulletlist = [
        '% STARTLIST',
        *sorted([f'- `{name}`, in any location' for name, paths in counts.items() if len(paths) > 1]),
        *sorted([f'- `{paths[0]}`' for _, paths in counts.items() if len(paths) == 1]),
        '% ENDLIST',
    ]

    path = basedir / 'docs' / 'guidance' / 'map' / 'translations.md'
    with path.open() as f:
        contents = f.read()
    with path.open('w') as f:
        f.write(re.sub(r'% STARTLIST.+% ENDLIST', '\n'.join(bulletlist), contents, flags=re.DOTALL))

    json_dump('meta-schema.json', get_metaschema())
    json_dump('dereferenced-release-schema.json', jsonref_release_schema)
    json_dump('versioned-release-validation-schema.json', get_versioned_release_schema(release_schema))

    # Strict schemas.
    directory = Path('strict')
    strict_release_schema = get_strict_schema(deepcopy(release_schema))
    json_dump(directory / 'release-schema', strict_release_schema)

    strict_dereferenced_release_schema = json_load(directory / 'release-schema', jsonref, merge_props=True)
    json_dump(directory / 'dereferenced-release-schema', strict_dereferenced_release_schema)
    json_dump(directory / 'versioned-release-validation-schema', get_versioned_release_schema(strict_release_schema))

    json_dump(directory / 'release-package-schema', get_strict_schema(json_load('release-package-schema')))
    json_dump(directory / 'record-package-schema', get_strict_schema(json_load('record-package-schema')))


@cli.command()
@click.argument('file', type=click.File())
def update_country(file):
    """
    Update country.csv from ISO 3166-1 using FILE.

    To retrieve the file:

    \b
    1. Open https://www.iso.org/obp/ui/#search/code/
    2. Open the "Network" tab of the "Web Inspector" utility (Option-Cmd-I in Safari)
    3. Set "Results per page:" to 300
    4. Click the last "UIDL" entry in the "Network" tab
    5. Copy its contents, excluding the for-loop, into a file
    """
    # https://www.iso.org/iso-3166-country-codes.html
    # https://www.iso.org/obp/ui/#search

    codes = {
        # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#User-assigned_code_elements
        'XK': 'Kosovo',
    }

    rpc = json.load(file)[0]['rpc'][0]
    offset = int(rpc[0])
    for entry in rpc[3][1]:
        d = entry['d']
        # Clean "Western Sahara*", "United Arab Emirates (the)", etc.
        codes[d[str(offset + 9)]] = re.sub(r' \(the\)|\*', '', d[str(offset + 13)])
        # The country code appears at offsets 9 and 15. Check that they are always the same.
        if d[str(offset + 9)] != d[str(offset + 15)]:
            raise AssertionError

    with open(schemadir / 'codelists' / 'country.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['Code', 'Title'])
        for code in sorted(codes):
            writer.writerow([code, codes[code]])


@cli.command()
def update_currency():
    """Update currency.csv from ISO 4217."""
    # https://www.iso.org/iso-4217-currency-codes.html
    # https://www.six-group.com/en/products-services/financial-information/data-standards.html#scrollTo=currency-codes

    # List One: Current Currency & Funds
    current_codes = {}
    url = 'https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/lists/list_one.xml'
    tree = etree.fromstring(get(url).content)  # noqa: S320 # trusted external
    for node in tree.xpath('//CcyNtry'):
        # Entries like Antarctica have no universal currency.
        if node.xpath('./Ccy'):
            code = node.xpath('./Ccy')[0].text
            title = node.xpath('./CcyNm')[0].text.strip()
            if code not in current_codes:
                current_codes[code] = title
            # We should expect currency titles to be consistent across countries.
            elif current_codes[code] != title:
                raise click.ClickException(f'expected {current_codes[code]}, got {title}')

    # List Three: Historic Denominations (Currencies & Funds)
    historic_codes = {}
    url = 'https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/lists/list_three.xml'
    tree = etree.fromstring(get(url).content)  # noqa: S320 # trusted external
    for node in tree.xpath('//HstrcCcyNtry'):
        code = node.xpath('./Ccy')[0].text
        title = node.xpath('./CcyNm')[0].text.strip()
        valid_until = node.xpath('./WthdrwlDt')[0].text
        # Use ISO8601 interval notation.
        valid_until = re.sub(r'^(\d{4})-(\d{4})$', r'\1/\2', valid_until.replace(' to ', '/'))
        if (
            code not in current_codes
            # Last condition: If the code is historical, use the most recent title and valid date.
            and (code not in historic_codes or valid_until > historic_codes[code]['Valid Until'])
        ):
                historic_codes[code] = {'Title': title, 'Valid Until': valid_until}

    with csv_dump('currency.csv', ['Code', 'Title', 'Valid Until']) as writer:
        for code in sorted(current_codes):
            writer.writerow([code, current_codes[code], None])
        for code in sorted(historic_codes):
            writer.writerow([code, historic_codes[code]['Title'], historic_codes[code]['Valid Until']])

    release_schema = json_load('release-schema.json')
    codes = sorted([*current_codes, historic_codes])
    release_schema['definitions']['Value']['properties']['currency']['enum'] = [*codes, None]

    json_dump('release-schema', release_schema)


@cli.command()
def update_language():
    """Update language.csv from ISO 639-1."""
    # https://www.iso.org/iso-639-language-codes.html
    # https://id.loc.gov/vocabulary/iso639-1.html

    with csv_dump('language.csv', ['Code', 'Title']) as writer:
        for row in csv_load('https://id.loc.gov/vocabulary/iso639-1.tsv', delimiter='\t'):
            # Remove parentheses, like "Greek, Modern (1453-)", and split alternatives.
            titles = re.split(r' *\| *', re.sub(r' \(.+\)', '', row['Label (English)']))
            # Remove duplication like "Ndebele, North |  North Ndebele" and join alternatives using a comma instead of
            # a pipe. To preserve order, a dict without values is used instead of a set.
            titles = ', '.join({' '.join(reversed(title.split(', '))): None for title in titles})
            writer.writerow([row['code'], titles])


@cli.command()
def update_media_type():
    """
    Update mediaType.csv from IANA.

    Ignores deprecated and obsolete media types.
    """
    # https://www.iana.org/assignments/media-types/media-types.xhtml

    # See "Registries included below".
    registries = [
        'application',
        'audio',
        'font',
        'image',
        'message',
        'model',
        'multipart',
        'text',
        'video',
    ]

    with csv_dump('mediaType.csv', ['Code', 'Title']) as writer:
        for registry in registries:
            # See "Available Formats" under each heading.
            for row in csv_load(f'https://www.iana.org/assignments/media-types/{registry}.csv'):
                if ' ' in row['Name']:
                    name, message = row['Name'].split(' ', 1)
                else:
                    name, message = row['Name'], None
                code = f"{registry}/{name}"
                template = row['Template']
                # All messages are expected to be about deprecation and obsoletion.
                if message:
                    logging.warning('%s: %s', message, code)
                # "x-emf" has "image/emf" in its "Template" value (but it is deprecated).
                elif template and template != code:
                    raise click.ClickException(f"expected {code}, got {template}")
                else:
                    writer.writerow([code, name])

        writer.writerow(['offline/print', 'print'])


@cli.command()
@click.pass_context
def update(ctx):
    """Update codelists except country.csv."""
    ctx.invoke(update_currency)
    ctx.invoke(update_language)
    ctx.invoke(update_media_type)


@cli.command()
@click.pass_context
def check_iso_6523(ctx):
    def text(node, xpath):
        return re.sub(r'\s+', ' ', node.xpath(xpath)[0])

    """
    Checks PEPPOL BIS Billing 3.0's ISO 6523 ICD codelist for new codes.
    """
    # We use this, because we don't know a better source for the ISO 6523 codelist.

    # As of 2022-04-19, the range is 0002-0213, skipping 0092 0103 0181 0182.
    minimum = 2
    maximum = 213
    skipped = {92, 103, 181, 182}

    response = get('https://docs.peppol.eu/poacc/billing/3.0/codelist/ICD/')

    divs = lxml.html.fromstring(response.content).xpath('//dd/div[@id]')
    if not divs:
        raise click.ClickException('The HTML markup of the data source has changed. Please update the script.')

    rows = []
    for div in divs:
        identifier = div.attrib['id']
        number = int(identifier)
        if number < minimum or number > maximum or number in skipped:
            name = text(div, './strong/text()')
            notes = text(div, './p/text()')
            issuer = ''

            # "Issuing agency: " appears at the end of the paragraph. The rest of the paragraph contains either a
            # purpose ("Intended Purpose/App. Area") or notes ("Notes on Use of Code"), with or without the label.
            notes = re.sub(r'(Notes on Use of Code|Intended Purpose/App. Area)[: ]+', '', notes)
            if 'Issuing agency: ' in notes:
                notes, issuer = notes.split('Issuing agency: ')

            rows.append([identifier, name, issuer, notes])

    if rows:
        csv.writer(sys.stdout, delimiter='\t').writerows(rows)
    else:
        click.echo('No new codes found.')


def add_translation_note(path, language, domain):
    """Add a translation note to a file."""
    base_url = 'https://standard.open-contracting.org/1.1'

    with open(path) as f:
        document = lxml.html.fromstring(f.read())

    translator = gettext.translation('theme', localedir, languages=[language])
    _ = translator.gettext

    pattern = f'{base_url}/{{}}/{domain}/'
    response = requests.get(pattern.format(language), timeout=10)

    # If it's a new page, add the note to the current version of the page.
    if response.status_code == requests.codes.not_found:
        message = _('This page was recently added to the <a href="%(url)s">English documentation</a>. '
                    'It has not yet been translated.')

    # If it's an existing page, add the note the last version of the page.
    else:
        response.raise_for_status()
        xpath = '//div[@itemprop="articleBody"]'

        replacement = lxml.html.fromstring(response.content).xpath(xpath)[0]
        replacement.make_links_absolute(f'{base_url}/{language}')

        # Remove any existing translation notes.
        parent = replacement.xpath('//h1')[0].getparent()
        for div in replacement.xpath('//h1/following-sibling::div[@class="admonition note"]'):
            parent.remove(div)

        element = document.xpath(xpath)[0]
        element.getparent().replace(element, replacement)

        message = _(
            'This page was recently changed in the <a href="%(url)s">English documentation</a>. '
            'The changes have not yet been translated.'
        )

    template = (
        '<div class="admonition note"><p class="first admonition-title">%(note)s</p><p class="last">'
        '%(message)s</p></div>'
    )

    document.xpath('//h1')[0].addnext(lxml.etree.XML(template % {
        'note': _('Note'), 'message': message % {'url': pattern.format('en')}}))

    with open(path, 'wb') as f:
        f.write(lxml.html.tostring(document, encoding='utf-8'))


@cli.command()
def add_translation_notes():
    """
    Implement the localization policy.

    "Minor, non-normative, documentation updates will be translated promptly, but may not always be translated before
    the updates are released. The documentation will clearly display when the English documentation is 'ahead' of
    translations for a particular version."

    https://standard.open-contracting.org/latest/en/governance/translation/
    """
    excluded = ('.doctrees', '_downloads', '_images', '_sources', '_static', 'codelists', 'genindex', 'search')

    for language in ('es', 'fr'):
        build_dir = basedir / 'build' / language
        language_dir = localedir / language / 'LC_MESSAGES'

        for root, dirs, files in os.walk(build_dir):
            # Skip Sphinx directories.
            for directory in excluded:
                if directory in dirs:
                    dirs.remove(directory)

            if root == str(build_dir):
                continue

            for name in files:
                # See `sphinx.transforms.i18n.Locale.apply()`.
                # https://github.com/sphinx-doc/sphinx/blob/v2.2.1/sphinx/transforms/i18n.py
                source = os.path.join(root, os.path.dirname(name))
                domain = relative_path(build_dir, source)

                path = language_dir / domain / 'index.po'
                if not path.is_file():
                    path = language_dir / f'{domain}.po'
                if not path.is_file():
                    add_translation_note(os.path.join(root, name), language, domain)
                    continue

                # Check the PO files, because Babel sets the msgstr to the msgid if the msgstr is missing.
                with open(path) as f:
                    for message in read_po(f):
                        if not message.string:
                            add_translation_note(os.path.join(root, name), language, domain)
                            break


if __name__ == '__main__':
    cli()
