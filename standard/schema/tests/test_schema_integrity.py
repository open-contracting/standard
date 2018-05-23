"""
Ensures that `make_validation_schema.py` and `make_metaschema.py` has been run.
"""

import json
from path import path

from ..utils.make_validation_schema import get_versioned_validation_schema
from ..utils.make_metaschema import make_metaschema, metaschema_path

RELEASE_SCHEMA_PATH = path(__file__).parent.parent / 'release-schema.json'
VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH = path(__file__).parent.parent / 'versioned-release-validation-schema.json'


def test_versioned_release_validation_schema_is_in_sync():
    with open(VERSIONED_RELEASE_VALIDATION_SCHEMA_PATH) as f:
        actual = json.load(f)

    with open(RELEASE_SCHEMA_PATH) as f:
        release_schema = json.load(f)

    assert actual == get_versioned_validation_schema(release_schema)


def test_metaschema_is_in_sync():
    with open(metaschema_path) as f:
        actual = json.load(f)

    assert actual == make_metaschema()
