#!/usr/bin/env python
import json
from json_schema_validator.schema import Schema
from json_schema_validator.validator import Validator, ValidationError


def validate_release_schema():
    with open('json-schema-draft-4.json', 'r') as f:
        json_schema = Schema(json.loads(f.read()))
    with open('../release-schema.json', 'r') as f:
        schema = Schema(json.loads(f.read()))
    try:
        Validator.validate(schema, json_schema)
        print "SUCCESS: Schema is valid against JSON Schema Draft 4."
    except ValidationError as e:
        print e

if __name__ == "__main__":
    validate_release_schema()
