import json
import jsonmerge

from .test_validate_schema import (
    RELEASE_SCHEMA_PATH,
    VERSIONED_RELEASE_SCHEMA_PATH,
    VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH
)

from ..utils.make_validation_schema import get_versioned_validation_schema


def test_versioned_release_validation_schema_is_in_sync():
    # Builds the validation schema and confirms its equal to the stored schema
    with open(VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH, "rb") as f:
        actual = json.loads(f.read())

    with open(VERSIONED_RELEASE_SCHEMA_PATH, "rb") as f:
        versioned_release = json.loads(f.read())

    expected = get_versioned_validation_schema(versioned_release)

    assert expected == actual


def test_versioned_release_schema_and_release_schema_types_are_in_sync():
    # Versioned release schema has additional merge strategies and small
    # tweaks, but should be the same as release schema, so need to confirm.

    with open(RELEASE_SCHEMA_PATH, "rb") as f:
        release = json.loads(f.read())

    with open(VERSIONED_RELEASE_SCHEMA_PATH, "rb") as f:
        versioned_release = json.loads(f.read())

    def recurse(original, should_be_equal, k):
        keywords_to_not_recurse = ["title",
                                   "description",
                                   "mergeStrategy",
                                   "$ref",
                                   "__comment"]

        if isinstance(original, dict):
            if original.get("__skip_validation"):
                print "skipping validation for %s" % original
            else:
                for k in original:
                    if k not in keywords_to_not_recurse:
                        recurse(original[k], should_be_equal[k], k)
        else:
            if k in ['type', 'enum']:
                assert original == should_be_equal

    recurse(release, versioned_release, None)
    recurse(versioned_release, release, None)
