"""
Ensures that `make_validation_schema.py` and `make_metaschema.py` has been run.
"""

import json

from .test_validate_schema import (
    RELEASE_SCHEMA_PATH,
    VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH
)

from ..utils.make_validation_schema import get_versioned_validation_schema
from ..utils.make_metaschema import make_metaschema, metaschema_path


def test_versioned_release_validation_schema_is_in_sync():
    # Builds the validation schema and confirms it's equal to the stored schema
    with open(VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH, "r") as f:
        actual = json.loads(f.read())

    with open(RELEASE_SCHEMA_PATH, "r") as f:
        versioned_release = json.loads(f.read())

    expected = get_versioned_validation_schema(versioned_release)

    assert expected == actual


def test_metaschema_is_in_sync():

    with open(metaschema_path, "r") as f:
        actual = json.loads(f.read())

        assert actual == make_metaschema()
