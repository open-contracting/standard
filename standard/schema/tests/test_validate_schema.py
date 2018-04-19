"""
Validates release package, record package, release, and versioned release
schemas against JSON Schema Draft 4, and ensures that the JSON contains no
duplicate keys.
"""

import json
from collections import UserDict

from jsonschema import validate
from path import path


class RejectingDict(UserDict):
    """
    A dict that only allows a key to set once.
    Lets us raise an error on duplicate keys in JSON.
    """

    def __setitem__(self, k, v):
        if k in self.keys():
            raise ValueError("Duplicate key in JSON")
        else:
            return super().__setitem__(k, v)


def object_pairs_hook(pairs):
    rejecting_dict = RejectingDict(pairs)
    # We must return the wrapped dict, and not the RejectingDict object itself
    # because JSON schema checks the type
    return rejecting_dict.data


OCDS_METASCHEMA = path(__file__).parent.parent / 'meta-schema.json'
RELEASE_SCHEMA_PATH = path(__file__).parent.parent / 'release-schema.json'
RECORD_SCHEMA_PATH = path(__file__).parent.parent / 'record-package-schema.json'
RELEASE_PACKAGE_SCHEMA_PATH = path(__file__).parent.parent / 'release-package-schema.json'
VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH = path(__file__).parent.parent / 'versioned-release-validation-schema.json'


def validate_schema(schema_to_validate_path):
    with open(OCDS_METASCHEMA) as f:
        draft_schema = json.load(f)
    with open(schema_to_validate_path) as f:
        schema = json.load(f, object_pairs_hook=object_pairs_hook)
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
