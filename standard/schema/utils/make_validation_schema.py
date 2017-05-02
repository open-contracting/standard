#!/usr/bin/env python
import json
from collections import OrderedDict
import copy

version_template = OrderedDict([
    ("type", "array"),
    ("items", OrderedDict([
        ("properties", OrderedDict([
            ("releaseDate", OrderedDict([
                ("format", "date-time"),
                ("type", "string")
            ])),
            ("releaseID", {
                "type": "string"
            }),
            ("value", {
            }),
            ("releaseTag", OrderedDict([
                ("type", "array"),
                ("items", {"type": "string"})
            ]))
        ]))
   ]))
])

def add_versions(schema, location=''):
    for key, value in list(schema['properties'].items()):
        prop_type = value.get('type')
        value.pop("title", None)
        value.pop("description", None)
        omitWhenMerged = value.pop("omitWhenMerged", None)
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
                version_properties["value"] =  new_value
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

            
def add_string_definitions(schema):
    for item, format in [("StringNullUriVersioned", "uri"), 
                         ("StringNullDateTimeVersioned", "date-time"),
                         ("StringNullVersioned", None)]:
        version = copy.deepcopy(version_template)
        version_properties = version["items"]["properties"]
        version_properties["value"] = OrderedDict([("type", ["string", "null"])])
        if format:
            version_properties["value"]["format"] = format
        schema['definitions'][item] = version

def unversion_refs(schema):
    for key, value in schema.items():
        if key == '$ref':
            schema[key] = value + 'Unversioned' 
        if isinstance(value, dict):
            unversion_refs(value)


def get_versioned_validation_schema(versioned_release):
    versioned_release["id"] = "http://standard.open-contracting.org/schema/1__0__2/versioned-release-validation-schema.json"  # nopep8
    versioned_release["$schema"] = "http://json-schema.org/draft-04/schema#"  # nopep8
    versioned_release["title"] = "Schema for a compiled, versioned Open Contracting Release."  # nopep8

    definitions = versioned_release['definitions']

    new_definitions = OrderedDict()
    for key, value in copy.deepcopy(versioned_release['definitions']).items():
        new_definitions[key + 'Unversioned'] = value

    unversion_refs(new_definitions)


    ocid = versioned_release['properties'].pop("ocid")
    versioned_release['properties'].pop("date")
    versioned_release['properties'].pop("id")
    versioned_release['properties'].pop("tag")

    versioned_release['required'] = [
        "ocid",
        "initiationType"
    ]

    add_versions(versioned_release)

    versioned_release['properties']["ocid"] = ocid

    definitions.update(new_definitions)
    add_string_definitions(versioned_release)

    for key, value in definitions.items():
        value.pop("title", None)
        value.pop("description", None)
        if not 'properties' in value:
            continue
        for prop_value in value['properties'].values():
            prop_value.pop("title", None)
            prop_value.pop("description", None)
            prop_value.pop("omitWhenMerged", None)
            prop_value.pop("wholeListMerge", None)
            prop_value.pop("versionId", None)

    return versioned_release


if __name__ == "__main__":
    from os.path import abspath, dirname, join
    schema_dir = dirname(dirname(abspath(__file__)))

    with open(join(schema_dir, 'release-schema.json'), 'r') as f:
        release_schema = json.loads(f.read(), object_pairs_hook=OrderedDict)

    new_validation_schema = get_versioned_validation_schema(release_schema)

    with open(join(schema_dir, 'versioned-release-validation-schema.json'), 'w') as f:
        f.write(json.dumps(new_validation_schema, indent=4))
