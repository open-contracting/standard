#!/usr/bin/env python
import json
from path import path
from jsonschema import validate, ValidationError


DRAFT_SCHEMA_PATH = path(__file__).parent / 'json_schema/json-schema-draft-4.json'
RELEASE_SCHEMA_PATH = path(__file__).parent.parent / 'release-schema.json'


def validate_release_schema():
    with open(DRAFT_SCHEMA_PATH, 'r') as f:
        draft_schema = json.loads(f.read())
    with open(RELEASE_SCHEMA_PATH, 'r') as f:
        release_schema = json.loads(f.read())
    validate(release_schema, draft_schema)
    print "SUCCESS: Schema is valid against JSON Schema Draft 4."


def test_validate_release_schema():
    validate_release_schema()
