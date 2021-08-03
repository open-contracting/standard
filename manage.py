#!/usr/bin/env python
import csv
import gettext
import json
import logging
import os
import re
import sys
import warnings
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
from jsonref import JsonRef, JsonRefError
from lxml import etree

basedir = Path(__file__).resolve().parent
schemadir = basedir / 'schema'
localedir = basedir / 'docs' / 'locale'

sys.path.append(str(basedir / 'docs'))

from conf import release  # noqa isort:skip


def custom_warning_formatter(message, category, filename, lineno, line=None):
    return str(message) + '\n'


warnings.formatwarning = custom_warning_formatter

versioned_template = json.loads('''
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
''')

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


def json_load(filename, library=json):
    """
    Loads JSON data from the given filename.
    """
    with (schemadir / filename).open() as f:
        return library.load(f)


def json_dump(filename, data):
    """
    Writes JSON data to the given filename.
    """
    with (schemadir / filename).open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def csv_load(url, delimiter=','):
    """
    Loads CSV data into a ``csv.DictReader`` from the given URL.
    """
    reader = csv.DictReader(StringIO(get(url).text), delimiter=delimiter)
    return reader


@contextmanager
def csv_dump(filename, fieldnames):
    """
    Writes CSV headers to the given filename, and yields a ``csv.writer``.
    """
    f = (schemadir / 'codelists' / filename).open('w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(fieldnames)
    try:
        yield writer
    finally:
        f.close()


def get(url):
    """
    GETs a URL and returns the response. Raises an exception if the status code is not successful.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response


def coerce_to_list(data, key):
    """
    Returns the value of the ``key`` key in the ``data`` mapping. If the value is a string, wraps it in an array.
    """
    item = data.get(key, [])
    if isinstance(item, str):
        return [item]
    return item


def get_metaschema():
    """
    Patches and returns the JSON Schema Draft 4 metaschema.
    """
    return json_merge_patch.merge(json_load('metaschema/json-schema-draft-4.json'),
                                  json_load('metaschema/meta-schema-patch.json'))


def get_common_definition_ref(item):
    """
    Returns a schema that references the common definition that the ``item`` matches: "StringNullUriVersioned",
    "StringNullDateTimeVersioned" or "StringNullVersioned".
    """
    for name, keywords in common_versioned_definitions.items():
        # If the item matches the definition.
        if any(item.get(keyword) != value for keyword, value in keywords.items()):
            continue
        # And adds no keywords to the definition.
        if any(keyword not in (*keywords, *keywords_to_remove) for keyword in item):
            continue
        return {'$ref': f'#/definitions/{name}'}


def add_versioned(schema, unversioned_pointers, pointer=''):
    """
    An outer function that calls ``_add_versioned`` on each field.
    """
    for key, value in schema['properties'].items():
        new_pointer = f'{pointer}/properties/{key}'
        _add_versioned(schema, unversioned_pointers, new_pointer, key, value)

    for key, value in schema.get('definitions', {}).items():
        new_pointer = f'{pointer}/definitions/{key}'
        add_versioned(value, unversioned_pointers, pointer=new_pointer)


def _add_versioned(schema, unversioned_pointers, pointer, key, value):
    """
    An inner function that performs the changes to the schema to refer to versioned/unversioned definitions.

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
    if '$ref' not in value and types not in recognized_types:
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
    """
    Replaces ``$ref`` values with unversioned definitions.
    """
    for key, value in schema.items():
        if key == '$ref':
            schema[key] = value + 'Unversioned'
        elif isinstance(value, dict):
            update_refs_to_unversioned_definitions(value)


def get_unversioned_pointers(schema, fields, pointer=''):
    """
    Returns the JSON Pointers to ``id`` fields that must not be versioned if the object is in an array.
    """
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
    """
    Removes properties that set ``omitWhenMerged``.
    """
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
    """
    Removes metadata and extended keywords from properties and definitions.
    """
    if isinstance(schema, list):
        for item in schema:
            remove_metadata_and_extended_keywords(item)
    elif isinstance(schema, dict):
        for key, value in schema.items():
            if key in ('definitions', 'properties'):
                for subschema in value.values():
                    for keyword in keywords_to_remove:
                        subschema.pop(keyword, None)
            remove_metadata_and_extended_keywords(value)


def get_versioned_release_schema(schema):
    """
    Returns the versioned release schema.
    """
    # Update schema metadata.
    release_with_underscores = release.replace('.', '__')
    schema['id'] = f'https://standard.open-contracting.org/schema/{release_with_underscores}/versioned-release-validation-schema.json'  # noqa
    schema['title'] = 'Schema for a compiled, versioned Open Contracting Release.'

    # Release IDs, dates and tags appear alongside values in the versioned release schema.
    remove_omit_when_merged(schema)

    # Create unversioned copies of all definitions.
    unversioned_definitions = {k + 'Unversioned': deepcopy(v) for k, v in schema['definitions'].items()}
    update_refs_to_unversioned_definitions(unversioned_definitions)

    # Determine which `id` fields occur on objects in arrays.
    unversioned_pointers = set()
    get_unversioned_pointers(JsonRef.replace_refs(schema), unversioned_pointers)

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
        ref = JsonRef.replace_refs(schema)
        try:
            repr(ref)
            break
        except JsonRefError as e:
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


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
def unused_terms(filename):
    """
    Print terms from the provided filename that do not occur in the documentation.
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
def pre_commit():
    """
    Update meta-schema.json, dereferenced-release-schema.json and versioned-release-validation-schema.json.
    """
    release_schema = json_load('release-schema.json')

    json_dump('meta-schema.json', get_metaschema())
    json_dump('dereferenced-release-schema.json', json_load('release-schema.json', jsonref))
    json_dump('versioned-release-validation-schema.json', get_versioned_release_schema(release_schema))


@cli.command()
@click.argument('path')
def update_country(path):
    """
    Update schema/codelists/country.csv from PATH.
    """
    # https://www.iso.org/iso-3166-country-codes.html
    # https://www.iso.org/obp/ui/#search
    directory = Path(os.path.dirname(os.path.realpath(__file__)))

    codes = {
        # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#User-assigned_code_elements
        'XK': 'Kosovo',
    }

    with open(path) as f:
        rpc = json.load(f)[0]['rpc'][0]
        offset = int(rpc[0])

        for entry in rpc[3][1]:
            d = entry['d']
            codes[d[str(offset + 9)]] = re.sub(r' \(the\)|\*', '', d[str(offset + 13)])

            assert d[str(offset + 9)] == d[str(offset + 15)]

    with open(directory / 'schema' / 'codelists' / 'country.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['Code', 'Title'], lineterminator='\n')
        writer.writeheader()

        for code in sorted(codes):
            writer.writerow({
                'Code': code,
                'Title': codes[code],
            })


@cli.command()
def update_currency():
    """
    Update schema/codelists/currency.csv from ISO 4217.
    """
    # https://www.iso.org/iso-4217-currency-codes.html
    # https://www.six-group.com/en/products-services/financial-information/data-standards.html#scrollTo=currency-codes

    # "List One: Current Currency & Funds"
    current_codes = {}
    url = 'https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/lists/list_one.xml'  # noqa: E501
    tree = etree.fromstring(get(url).content)
    for node in tree.xpath('//CcyNtry'):
        match = node.xpath('./Ccy')
        # Entries like Antarctica have no universal currency.
        if match:
            code = node.xpath('./Ccy')[0].text
            title = node.xpath('./CcyNm')[0].text.strip()
            if code not in current_codes:
                current_codes[code] = title
            # We should expect currency titles to be consistent across countries.
            elif current_codes[code] != title:
                raise Exception(f'expected {current_codes[code]}, got {title}')

    # "List Three: Historic Denominations (Currencies & Funds)"
    historic_codes = {}
    url = 'https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/lists/list_three.xml'  # noqa: E501
    tree = etree.fromstring(get(url).content)
    for node in tree.xpath('//HstrcCcyNtry'):
        code = node.xpath('./Ccy')[0].text
        title = node.xpath('./CcyNm')[0].text.strip()
        valid_until = node.xpath('./WthdrwlDt')[0].text
        # Use ISO8601 interval notation.
        valid_until = re.sub(r'^(\d{4})-(\d{4})$', r'\1/\2', valid_until.replace(' to ', '/'))
        if code not in current_codes:
            if code not in historic_codes:
                historic_codes[code] = {'Title': title, 'Valid Until': valid_until}
            # If the code is historical, use the most recent title and valid date.
            elif valid_until > historic_codes[code]['Valid Until']:
                historic_codes[code] = {'Title': title, 'Valid Until': valid_until}

    with csv_dump('currency.csv', ['Code', 'Title', 'Valid Until']) as writer:
        for code in sorted(current_codes.keys()):
            writer.writerow([code, current_codes[code], None])
        for code in sorted(historic_codes.keys()):
            writer.writerow([code, historic_codes[code]['Title'], historic_codes[code]['Valid Until']])

    release_schema = json_load('release-schema.json')
    codes = sorted(list(current_codes.keys()) + list(historic_codes.keys()))
    release_schema['definitions']['Value']['properties']['currency']['enum'] = codes + [None]

    json_dump('release-schema.json', release_schema)


@cli.command()
def update_language():
    """
    Update schema/codelists/language.csv from ISO 639-1.
    """
    # https://www.iso.org/iso-639-language-codes.html
    # https://id.loc.gov/vocabulary/iso639-1.html

    with csv_dump('language.csv', ['Code', 'Title']) as writer:
        reader = csv_load('https://id.loc.gov/vocabulary/iso639-1.tsv', delimiter='\t')
        for row in reader:
            # Remove parentheses, like "Greek, Modern (1453-)", and split alternatives.
            titles = re.split(r' *\| *', re.sub(r' \(.+\)', '', row['Label (English)']))
            # Remove duplication like "Ndebele, North |  North Ndebele" and join alternatives using a comma instead of
            # a pipe. To preserve order, a dict without values is used instead of a set.
            titles = ', '.join({' '.join(reversed(title.split(', '))): None for title in titles})
            writer.writerow([row['code'], titles])


@cli.command()
def update_media_type():
    """
    Update schema/codelists/mediaType.csv from IANA.

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
            reader = csv_load(f'https://www.iana.org/assignments/media-types/{registry}.csv')
            for row in reader:
                if ' ' in row['Name']:
                    name, message = row['Name'].split(' ', 1)
                else:
                    name, message = row['Name'], None
                code = f"{registry}/{name}"
                template = row['Template']
                # All messages are expected to be about deprecation and obsoletion.
                if message:
                    logging.warning(f'{message}: {code}')
                # "x-emf" has "image/emf" in its "Template" value (but it is deprecated).
                elif template and template != code:
                    raise Exception(f"expected {code}, got {template}")
                else:
                    writer.writerow([code, name])

        writer.writerow(['offline/print', 'print'])


@cli.command()
@click.argument('country_path')
@click.pass_context
def update(ctx, country_path):
    """
    Update external codelists (country, currency, language, media type).

    COUNTRY_PATH is the path to the file containing the ISO3166 codes.
    """
    ctx.invoke(update_country, path=country_path)
    ctx.invoke(update_currency)
    ctx.invoke(update_language)
    ctx.invoke(update_media_type)


def add_translation_note(path, language, domain):
    """
    Adds a translation note to a file.
    """
    base_url = 'https://standard.open-contracting.org/1.1'

    with open(path) as f:
        document = lxml.html.fromstring(f.read())

    translator = gettext.translation('theme', localedir, languages=[language])
    _ = translator.gettext

    pattern = '{}/{{}}/{}/'.format(base_url, domain)
    response = requests.get(pattern.format(language))

    # If it's a new page, add the note to the current version of the page.
    if response.status_code == 404:
        message = _('This page was recently added to the <a href="%(url)s">English documentation</a>. '
                    'It has not yet been translated.')

    # If it's an existing page, add the note the last version of the page.
    else:
        response.raise_for_status()
        xpath = '//div[@itemprop="articleBody"]'

        replacement = lxml.html.fromstring(response.content).xpath(xpath)[0]
        replacement.make_links_absolute('{}/{}'.format(base_url, language))

        # Remove any existing translation notes.
        parent = replacement.xpath('//h1')[0].getparent()
        for div in replacement.xpath('//h1/following-sibling::div[@class="admonition note"]'):
            parent.remove(div)

        element = document.xpath(xpath)[0]
        element.getparent().replace(element, replacement)

        message = _('This page was recently changed in the <a href="%(url)s">English documentation</a>. '
                    'The changes have not yet been translated.')

    template = '<div class="admonition note"><p class="first admonition-title">%(note)s</p><p class="last">' \
               '%(message)s</p></div>'

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

    https://standard.open-contracting.org/1.1/en/governance/#translation-and-localization-policy
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
