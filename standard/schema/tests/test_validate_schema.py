#!/usr/bin/env python
import json
from path import path
from jsonschema import validate


DRAFT_SCHEMA_PATH = path(__file__).parent / 'json-schema-draft-4.json'
RELEASE_SCHEMA_PATH = path(__file__).parent.parent / 'release-schema.json'
RECORD_SCHEMA_PATH = path(__file__).parent.parent / 'record-package-schema.json'
RELEASE_PACKAGE_SCHEMA_PATH = path(__file__).parent.parent / 'release-package-schema.json'
VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH = path(__file__).parent.parent / 'versioned-release-validation-schema.json'


def validate_schema(schema_to_validate_path):
    with open(DRAFT_SCHEMA_PATH, 'r') as f:
        draft_schema = json.loads(f.read())
    with open(schema_to_validate_path, 'r') as f:
        schema = json.loads(f.read())
    validate(schema, draft_schema)
    print("SUCCESS: Schema is valid against JSON Schema Draft 4.")


def test_validate_release_schema():
    validate_schema(RELEASE_SCHEMA_PATH)


def test_validate_record_schema():
    validate_schema(RECORD_SCHEMA_PATH)


def test_validate_release_package_schema():
    validate_schema(RELEASE_PACKAGE_SCHEMA_PATH)


def test_validate_versioned_release_validation_schema():
    validate_schema(VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH)
