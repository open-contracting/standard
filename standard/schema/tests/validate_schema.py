#!/usr/bin/env python
import json
from jsonschema import validate, ValidationError


def validate_release_schema():
    with open('./standard/schema/tests/json-schema-draft-4.json', 'r') as f:
        json_schema = json.loads(f.read())
    with open('./standard/schema/release-schema.json', 'r') as f:
        schema = json.loads(f.read())
    validate(schema, json_schema)
    print "SUCCESS: Schema is valid against JSON Schema Draft 4."


def validate_record_schema():
    with open('./standard/schema/tests/json-schema-draft-4.json', 'r') as f:
        json_schema = json.loads(f.read())
    with open('./standard/schema/record-schema.json', 'r') as f:
        schema = json.loads(f.read())
    validate(schema, json_schema)
    print "SUCCESS: Schema is valid against JSON Schema Draft 4."
