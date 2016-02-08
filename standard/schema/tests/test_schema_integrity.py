import json

from .test_validate_schema import (
    RELEASE_SCHEMA_PATH,
    VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH
)

from ..utils.make_validation_schema import get_versioned_validation_schema


def test_versioned_release_validation_schema_is_in_sync():
    # Builds the validation schema and confirms its equal to the stored schema
    with open(VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH, "r") as f:
        actual = json.loads(f.read())

    with open(RELEASE_SCHEMA_PATH, "r") as f:
        versioned_release = json.loads(f.read())

    expected = get_versioned_validation_schema(versioned_release)

    assert expected == actual
