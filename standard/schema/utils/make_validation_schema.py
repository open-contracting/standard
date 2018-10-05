import copy
import json
import os.path
import sys
import warnings
from collections import OrderedDict

docs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'docs', 'en')
sys.path.append(docs_path)

from conf import release  # noqa


def custom_warning_formatter(message, category, filename, lineno, line=None):
    return str(message) + '\n'


warnings.formatwarning = custom_warning_formatter

versioned_template = OrderedDict([
    ("type", "array"),
    ("items", OrderedDict([
        ("type", "object"),
        ("properties", OrderedDict([
            ("releaseDate", OrderedDict([
                ("format", "date-time"),
                ("type", "string"),
            ])),
            ("releaseID", OrderedDict([
                ("type", "string"),
            ])),
            ("value", OrderedDict([
            ])),
            ("releaseTag", OrderedDict([
                ("type", "array"),
                ("items", OrderedDict([
                    ("type", "string"),
                ])),
            ])),
        ])),
    ])),
])

versioned_string_definitions = OrderedDict([
    ('uri', 'StringNullUriVersioned'),
    ('date-time', 'StringNullDateTimeVersioned'),
    (None, 'StringNullVersioned'),
])


def add_versioned(schema, pointer=''):
    for key, value in list(schema['properties'].items()):
        # Remove `title`, `description` and merging properties.
        for k in ('title', 'description', 'omitWhenMerged'):
            value.pop(k, None)
        wholeListMerge = value.pop("wholeListMerge", None)
        versionId = value.pop("versionId", None)

        prop_type = value.get('type')

        if not prop_type:
            if '$ref' not in value:
                warnings.warn('{}/{} has no type or $ref - behavior is undefined'.format(pointer, key))
            continue

        # See http://standard.open-contracting.org/latest/en/schema/merging/#versioned-data
        if key == 'id' and not versionId:
            continue

        # If the string is nullable and isn't an `enum`, reference a versioned string definition.
        if prop_type == ["string", "null"] and "enum" not in value:
            schema['properties'][key] = OrderedDict([
                ('$ref', '#/definitions/' + versioned_string_definitions[value.get('format')]),
            ])

        # See http://standard.open-contracting.org/latest/en/schema/merging/#whole-list-merge
        elif prop_type == "array":
            if wholeListMerge:
                # If `items` contains `$ref`, update `$ref` to the unversioned definition.
                new_value = copy.deepcopy(value)
                if '$ref' in new_value['items']:
                    new_value['items']["$ref"] = value['items']['$ref'] + "Unversioned"

                versioned = copy.deepcopy(versioned_template)
                versioned['items']['properties']['value'] = new_value
                schema['properties'][key] = versioned

        # If the field is an object, iterate over its properties.
        elif prop_type == "object":
            add_versioned(value, pointer='{}/{}'.format(pointer, key))

        # If the field isn't any of the above, make it versioned.
        else:
            versioned = copy.deepcopy(versioned_template)
            versioned['items']['properties']['value'] = value
            schema['properties'][key] = versioned

    for key, value in schema.get('definitions', {}).items():
        add_versioned(value, pointer='{}/{}'.format(pointer, key))


def update_refs_to_unversioned_definitions(schema):
    for key, value in schema.items():
        if key == '$ref':
            schema[key] = value + 'Unversioned'
        if isinstance(value, dict):
            update_refs_to_unversioned_definitions(value)


def get_versioned_release_schema(schema):
    definitions = schema['definitions']

    # Update schema metadata.
    release_with_underscores = release.replace('.', '__')
    schema['id'] = 'http://standard.open-contracting.org/schema/{}/versioned-release-validation-schema.json'.format(release_with_underscores)  # noqa
    schema['title'] = 'Schema for a compiled, versioned Open Contracting Release.'

    # Release IDs, dates and tags appear alongside values in the versioned release schema.
    fields_to_remove = ('id', 'date', 'tag')
    for key in fields_to_remove:
        del schema['properties'][key]
        schema['required'].remove(key)

    # Create unversioned copies of all definitions.
    unversioned_definitions = OrderedDict()
    for key, value in schema['definitions'].items():
        unversioned_definitions[key + 'Unversioned'] = copy.deepcopy(value)
    update_refs_to_unversioned_definitions(unversioned_definitions)

    # Omit "ocid" from versioning.
    ocid = schema['properties'].pop('ocid')
    add_versioned(schema)
    schema['properties']['ocid'] = ocid

    # Add the unversioned copies of all definitions.
    definitions.update(unversioned_definitions)

    # Add the definitions for versioned strings.
    for format, key in versioned_string_definitions.items():
        versioned = copy.deepcopy(versioned_template)
        versioned['items']['properties']['value']['type'] = ['string', 'null']
        if format:
            versioned['items']['properties']['value']['format'] = format
        schema['definitions'][key] = versioned

    # Remove all remaining `title` and `description` properties.
    for key, value in definitions.items():
        for key in ('title', 'description'):
            value.pop(key, None)
        if 'properties' not in value:
            continue
        # Remove all remaining merging properties.
        for prop_value in value['properties'].values():
            for key in ('title', 'description', 'omitWhenMerged', 'wholeListMerge', 'versionId'):
                prop_value.pop(key, None)

    return schema


if __name__ == "__main__":
    schema_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(schema_dir, 'release-schema.json')) as f:
        release_schema = json.load(f, object_pairs_hook=OrderedDict)

    versioned_release_schema = get_versioned_release_schema(release_schema)

    with open(os.path.join(schema_dir, 'versioned-release-validation-schema.json'), 'w') as f:
        json.dump(versioned_release_schema, f, indent=2, separators=(',', ': '))
        f.write('\n')
