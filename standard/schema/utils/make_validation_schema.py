#!/usr/bin/env python
import jsonmerge
import json


def get_versioned_validation_schema(versioned_release):
    merger = jsonmerge.Merger(versioned_release)

    versioned_validation_schema = merger.get_schema()
    versioned_validation_schema["id"] = "http://ocds.open-contracting.org/standard/r/1__0__RC/versioned-release-validation-schema.json"  # nopep8
    versioned_validation_schema["$schema"] = "http://json-schema.org/draft-04/schema#"  # nopep8
    versioned_validation_schema["title"] = "Schema for a compiled, versioned Open Contracting Release."  # nopep8

    return versioned_validation_schema


if __name__ == "__main__":
    from os.path import abspath, dirname, join

    schema_dir = dirname(dirname(abspath(__file__)))

    with open(join(schema_dir, 'release-schema.json'), 'rb') as f:
        vr = json.loads(f.read())

    new_validation_schema = get_versioned_validation_schema(vr)

    with open(join(schema_dir, 'versioned-release-validation-schema.json'), 'wb') as f:
        f.write(json.dumps(new_validation_schema, indent=4))
