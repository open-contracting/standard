import copy
import json
import os.path
import sys
from collections import OrderedDict

docs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'docs', 'en')
sys.path.append(docs_path)

from conf import release  # noqa

version_template = OrderedDict([
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


def add_versions(schema, location=''):
    for key, value in list(schema['properties'].items()):
        prop_type = value.get('type')
        value.pop("title", None)
        value.pop("description", None)
        value.pop("omitWhenMerged", None)
        wholeListMerge = value.pop("wholeListMerge", None)
        versionId = value.pop("versionId", None)
        if not prop_type:
            continue
        if key == 'id' and not versionId:
            continue
        if prop_type == ["string", "null"] and "enum" not in value:
            new_value = OrderedDict()
            format = value.get('format')
            if format == 'uri':
                new_value["$ref"] = "#/definitions/StringNullUriVersioned"
            elif format == 'date-time':
                new_value["$ref"] = "#/definitions/StringNullDateTimeVersioned"
            else:
                new_value["$ref"] = "#/definitions/StringNullVersioned"
            schema['properties'][key] = new_value
        elif prop_type == "array":
            version = copy.deepcopy(version_template)
            version_properties = version["items"]["properties"]
            if wholeListMerge:
                new_value = copy.deepcopy(value)

                if '$ref' in new_value['items']:
                    new_value['items']["$ref"] = value['items']['$ref'] + "Unversioned"
                version_properties["value"] = new_value
                schema['properties'][key] = version

        elif prop_type == "object":
            add_versions(value, key)
        else:
            version = copy.deepcopy(version_template)
            version_properties = version["items"]["properties"]
            version_properties["value"] = value
            schema['properties'][key] = version

    for key, value in schema.get('definitions', {}).items():
        add_versions(value, key)


def update_refs_to_unversioned_definitions(schema):
    for key, value in schema.items():
        if key == '$ref':
            schema[key] = value + 'Unversioned'
        if isinstance(value, dict):
            update_refs_to_unversioned_definitions(value)


def get_versioned_release_schema(schema):
    release_with_underscores = release.replace('.', '__')
    schema["id"] = "http://standard.open-contracting.org/schema/{}/versioned-release-validation-schema.json".format(release_with_underscores)  # noqa nopep8
    schema["$schema"] = "http://json-schema.org/draft-04/schema#"  # nopep8
    schema["title"] = "Schema for a compiled, versioned Open Contracting Release."  # nopep8

    definitions = schema['definitions']

    new_definitions = OrderedDict()
    for key, value in copy.deepcopy(schema['definitions']).items():
        new_definitions[key + 'Unversioned'] = value

    update_refs_to_unversioned_definitions(new_definitions)

    ocid = schema['properties'].pop("ocid")
    schema['properties'].pop("date")
    schema['properties'].pop("id")
    schema['properties'].pop("tag")

    schema['required'] = [
        "ocid",
        "initiationType"
    ]

    add_versions(schema)

    schema['properties']["ocid"] = ocid

    definitions.update(new_definitions)

    # Add definitions for versioned strings.
    for key, format in [('StringNullUriVersioned', 'uri'),
                        ('StringNullDateTimeVersioned', 'date-time'),
                        ('StringNullVersioned', None)]:
        schema['definitions'][key] = copy.deepcopy(version_template)
        value = definition['items']['properties']['value']
        value['type'] = ['string', 'null']
        if format:
            value['format'] = format

    for key, value in definitions.items():
        value.pop("title", None)
        value.pop("description", None)
        if 'properties' not in value:
            continue
        for prop_value in value['properties'].values():
            prop_value.pop("title", None)
            prop_value.pop("description", None)
            prop_value.pop("omitWhenMerged", None)
            prop_value.pop("wholeListMerge", None)
            prop_value.pop("versionId", None)

    return schema


if __name__ == "__main__":
    schema_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(schema_dir, 'release-schema.json')) as f:
        release_schema = json.load(f, object_pairs_hook=OrderedDict)

    versioned_release_schema = get_versioned_release_schema(release_schema)

    with open(os.path.join(schema_dir, 'versioned-release-validation-schema.json'), 'w') as f:
        json.dump(versioned_release_schema, f, indent=2, separators=(',', ': '))
        f.write('\n')
