#!/usr/bin/env python
import json
from collections import OrderedDict
import copy

version_template = OrderedDict({
    "type": "array",
    "items": {
        "properties": {
            "releaseDate": {
                "format": "date-time",
                "type": "string"
            },
            "releaseID": {
                "type": "string"
            },
            "value": {
            },
            "releaseTag": {
                "type": "array",
                "items": {"type": "string"}
            }
        }
   }
})

def add_versions(schema, location=''):
    for key, value in list(schema['properties'].items()):
        prop_type = value.get('type')
        value.pop("title", None)
        value.pop("description", None)
        value.pop("mergeStrategy", None)
        value.pop("mergeOptions", None)
        value.pop("omitWhenMerged", None)
        value.pop("wholeListMerge", None)
        if not prop_type:
            continue
        if key == 'id':
            if location not in ("Budget", "Tender", "Classification", "Identifier"):
                continue
        if prop_type == ["string", "null"] and "enum" not in value:
            new_value = {}
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
            if key in ('tenderers', 'suppliers'):
                version_properties["value"] = {"type": "array",
                                               "items": {"$ref": "#/definitions/OrganizationUnversioned"},
                                               "uniqueItems": True}
                schema['properties'][key] = version
            if key == 'additionalIdentifiers':
                version_properties["value"] = {"type": "array",
                                               "items": {"$ref": "#/definitions/IdentifierUnversioned"},
                                               "uniqueItems": True}
                schema['properties'][key] = version
            if key == 'additionalClassifications':
                version_properties["value"] = {"type": "array",
                                               "items": {"$ref": "#/definitions/ClassificationUnversioned"},
                                               "uniqueItems": True}
                schema['properties'][key] = version
            if key == 'changes':
                version_properties["value"] = {"type": "array",
                                               "items": value["items"]}
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
    for item, format in {"StringNullUriVersioned": "uri", 
                         "StringNullDateTimeVersioned": "date-time",
                         "StringNullVersioned": None}.items():
        version = copy.deepcopy(version_template)
        version_properties = version["items"]["properties"]
        version_properties["value"] = {"type": ["string", "null"]}
        if format:
            version_properties["value"]["format"] = format
        schema['definitions'][item] = version


def get_versioned_validation_schema(versioned_release):
    versioned_release["id"] = "http://standard.open-contracting.org/schema/1__0__2/versioned-release-validation-schema.json"  # nopep8
    versioned_release["$schema"] = "http://json-schema.org/draft-04/schema#"  # nopep8
    versioned_release["title"] = "Schema for a compiled, versioned Open Contracting Release."  # nopep8

    definitions = versioned_release['definitions']
    for key, value in definitions.items():
        value.pop("title", None)
        value.pop("description", None)
        for prop_value in value['properties'].values():
            prop_value.pop("mergeStrategy", None)
            prop_value.pop("mergeOptions", None)
            prop_value.pop("title", None)
            prop_value.pop("description", None)
            prop_value.pop("omitWhenMerged", None)
            prop_value.pop("wholeListMerge", None)

    OrganizationUnversioned = copy.deepcopy(definitions['Organization'])
    IdentifierUnversioned = copy.deepcopy(definitions['Identifier'])
    ClassificationUnversioned = copy.deepcopy(definitions['Classification'])
    AddressUnversioned = copy.deepcopy(definitions['Address'])
    ContactPointUnversioned = copy.deepcopy(definitions['ContactPoint'])

    ocid = versioned_release['properties'].pop("ocid")
    versioned_release['properties'].pop("date")
    versioned_release['properties'].pop("id")
    versioned_release['properties'].pop("tag")

    versioned_release['required'] = [
        "ocid",
        "initiationType"
    ]

    #types_count = Counter()
    #get_types(versioned_release, types_count)
    add_versions(versioned_release)

    versioned_release['properties']["ocid"] = ocid
    definitions['IdentifierUnversioned'] = IdentifierUnversioned
    definitions['ClassificationUnversioned'] = ClassificationUnversioned
    definitions['AddressUnversioned'] = AddressUnversioned
    definitions['ContactPointUnversioned'] = ContactPointUnversioned
    OrganizationUnversioned["properties"]["identifier"]["$ref"] = "#/definitions/IdentifierUnversioned"
    OrganizationUnversioned["properties"]["additionalIdentifiers"]["items"]["$ref"] = "#/definitions/IdentifierUnversioned"
    OrganizationUnversioned["properties"]["address"]["$ref"] = "#/definitions/AddressUnversioned"
    OrganizationUnversioned["properties"]["contactPoint"]["$ref"] = "#/definitions/ContactPointUnversioned"
    definitions['OrganizationUnversioned'] = OrganizationUnversioned
    add_string_definitions(versioned_release)

    return versioned_release


if __name__ == "__main__":
    from os.path import abspath, dirname, join
    schema_dir = dirname(dirname(abspath(__file__)))

    with open(join(schema_dir, 'release-schema.json'), 'r') as f:
        release_schema = json.loads(f.read(), object_pairs_hook=OrderedDict)

    new_validation_schema = get_versioned_validation_schema(release_schema)

    with open(join(schema_dir, 'versioned-release-validation-schema.json'), 'w') as f:
        f.write(json.dumps(new_validation_schema, indent=4))
