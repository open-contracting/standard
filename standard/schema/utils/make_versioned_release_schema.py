import json
import os.path
import sys
import warnings
from collections import OrderedDict
from copy import deepcopy

from jsonref import JsonRef, JsonRefError

docs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'docs', 'en')
sys.path.append(docs_path)

from conf import release  # noqa


def custom_warning_formatter(message, category, filename, lineno, line=None):
    return str(message) + '\n'


warnings.formatwarning = custom_warning_formatter

versioned_template_json = '''
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
'''
versioned_template = json.loads(versioned_template_json, object_pairs_hook=OrderedDict)

common_versioned_definitions = OrderedDict([
    ('StringNullUriVersioned', OrderedDict([
        ('type', ['string', 'null']),
        ('format', 'uri'),
    ])),
    ('StringNullDateTimeVersioned', OrderedDict([
        ('type', ['string', 'null']),
        ('format', 'date-time'),
    ])),
    ('StringNullVersioned', OrderedDict([
        ('type', ['string', 'null']),
        ('format', None),
    ])),
])

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
    'versionId',
)


def get_definition_ref(item):
    for definition, keywords in common_versioned_definitions.items():
        # If the item matches the definition.
        if any(item.get(keyword) != value for keyword, value in keywords.items()):
            continue
        # And adds no keywords to the definition.
        if any(keyword not in (*keywords, *keywords_to_remove) for keyword in item):
            continue
        return OrderedDict([
            ('$ref', '#/definitions/' + definition),
        ])


def add_versioned(schema, pointer=''):
    for key, value in list(schema['properties'].items()):
        new_pointer = '{}/{}'.format(pointer, key)

        wholeListMerge = value.pop('wholeListMerge', None)
        versionId = value.pop('versionId', None)

        prop_type = value.get('type')
        if isinstance(prop_type, str):
            prop_type = [prop_type]

        if '$ref' not in value and prop_type not in recognized_types:
            warnings.warn('{} has unrecognized type {}'.format(new_pointer, prop_type))

        # For example, if $ref is used.
        if not prop_type:
            continue

        # See http://standard.open-contracting.org/latest/en/schema/merging/#versioned-data
        if key == 'id' and not versionId:
            continue

        # Reference a common versioned definition if possible, to limit the size of the schema.
        ref = get_definition_ref(value)
        if ref:
            schema['properties'][key] = ref

        # Iterate over object properties. If it has no properties, like `Organization/details`, version it as a whole.
        elif prop_type == ['object'] and 'properties' in value:
            add_versioned(value, pointer=new_pointer)

        else:
            new_value = deepcopy(value)

            if prop_type == ['array']:
                items_type = value['items'].get('type', [])
                if isinstance(items_type, str):
                    items_type = [items_type]

                # See http://standard.open-contracting.org/latest/en/schema/merging/#whole-list-merge
                if wholeListMerge:
                    # Update `$ref` to the unversioned definition.
                    if '$ref' in value['items']:
                        new_value['items']['$ref'] = value['items']['$ref'] + 'Unversioned'
                    # Otherwise, similarly, don't iterate over item properties.
                # See http://standard.open-contracting.org/latest/en/schema/merging/#lists
                elif '$ref' in value['items']:
                    # Leave `$ref` to the versioned definition.
                    continue
                # Exceptional case for deprecated `Amendment/changes`.
                elif items_type == ['object'] and new_pointer == '/Amendment/changes':
                    continue
                # Warn in case new combinations are added to the release schema.
                elif items_type != ['string']:
                    # Note: Versioning the properties of un-$ref'erenced objects in arrays isn't implemented. However,
                    # this combination hasn't occurred, with the exception of `Amendment/changes`.
                    warnings.warn("{}/items has unexpected type {}".format(new_pointer, items_type))

            versioned = deepcopy(versioned_template)
            versioned['items']['properties']['value'] = new_value
            schema['properties'][key] = versioned

    for key, value in schema.get('definitions', {}).items():
        add_versioned(value, pointer='{}/{}'.format(pointer, key))


def update_refs_to_unversioned_definitions(schema):
    for key, value in schema.items():
        if key == '$ref':
            schema[key] = value + 'Unversioned'
        elif isinstance(value, dict):
            update_refs_to_unversioned_definitions(value)


def remove_omit_when_merged(schema):
    if isinstance(schema, list):
        for item in schema:
            remove_omit_when_merged(item)
    elif isinstance(schema, dict):
        for key, value in schema.items():
            if key == 'properties':
                for k, v in list(value.items()):
                    if v.get('omitWhenMerged'):
                        value.pop(k)
                        schema['required'].remove(k)
            remove_omit_when_merged(value)


def remove_metadata_and_extended_keywords(schema):
    if isinstance(schema, list):
        for item in schema:
            remove_metadata_and_extended_keywords(item)
    elif isinstance(schema, dict):
        for key, value in schema.items():
            if key in ('definitions', 'properties'):
                for v in value.values():
                    for keyword in keywords_to_remove:
                        v.pop(keyword, None)
            remove_metadata_and_extended_keywords(value)


def get_versioned_release_schema(schema):
    definitions = schema['definitions']

    # Update schema metadata.
    release_with_underscores = release.replace('.', '__')
    schema['id'] = 'http://standard.open-contracting.org/schema/{}/versioned-release-validation-schema.json'.format(release_with_underscores)  # noqa
    schema['title'] = 'Schema for a compiled, versioned Open Contracting Release.'

    # Release IDs, dates and tags appear alongside values in the versioned release schema.
    remove_omit_when_merged(schema)

    # Create unversioned copies of all definitions.
    unversioned_definitions = {k + 'Unversioned': deepcopy(v) for k, v in schema['definitions'].items()}
    update_refs_to_unversioned_definitions(unversioned_definitions)

    # Omit `ocid` from versioning.
    ocid = schema['properties'].pop('ocid')
    add_versioned(schema)
    schema['properties']['ocid'] = ocid

    # Add the common versioned definitions.
    for definition, keywords in common_versioned_definitions.items():
        versioned = deepcopy(versioned_template)
        for keyword, value in keywords.items():
            if value:
                versioned['items']['properties']['value'][keyword] = value
        schema['definitions'][definition] = versioned

    # Add the unversioned copies of needed definitions.
    while True:
        ref = JsonRef.replace_refs(schema)
        try:
            repr(ref)
            break
        except JsonRefError as e:
            definition = e.cause.args[0]
            schema['definitions'][definition] = unversioned_definitions[definition]

    # Remove all metadata and extended keywords.
    remove_metadata_and_extended_keywords(schema)

    return schema


if __name__ == '__main__':
    schema_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(schema_dir, 'release-schema.json')) as f:
        release_schema = json.load(f, object_pairs_hook=OrderedDict)

    versioned_release_schema = get_versioned_release_schema(release_schema)

    with open(os.path.join(schema_dir, 'versioned-release-validation-schema.json'), 'w') as f:
        json.dump(versioned_release_schema, f, indent=2, separators=(',', ': '))
        f.write('\n')
