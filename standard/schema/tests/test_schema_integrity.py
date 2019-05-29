"""
Ensures that `make_versioned_release_schema.py` and `make_metaschema.py` has been run.
"""

import json
from pathlib import Path

import jsonref

from ..utils.make_versioned_release_schema import get_versioned_release_schema
from ..utils.make_metaschema import make_metaschema, metaschema_path

RELEASE_SCHEMA_PATH = Path(__file__).parents[1] / 'release-schema.json'
VERSIONED_RELEASE_SCHEMA_PATH = Path(__file__).parents[1] / 'versioned-release-validation-schema.json'
DEREFERENCED_RELEASE_SCHEMA_PATH = Path(__file__).parents[1] / 'dereferenced-release-schema.json'


def test_versioned_release_schema_is_in_sync():
    with open(VERSIONED_RELEASE_SCHEMA_PATH) as f:
        actual = json.load(f)

    with open(RELEASE_SCHEMA_PATH) as f:
        expected = get_versioned_release_schema(json.load(f))

    assert actual == expected, 'Run: python standard/schema/utils/make_versioned_release_schema.py'


def test_dereferenced_release_schema_is_in_sync():
    with open(DEREFERENCED_RELEASE_SCHEMA_PATH) as f:
        actual = json.load(f)

    with open(RELEASE_SCHEMA_PATH) as f:
        expected = jsonref.load(f)

    assert actual == expected, 'Run: python standard/schema/utils/make_dereferenced_release_schema.py'


def test_metaschema_is_in_sync():
    with open(metaschema_path) as f:
        actual = json.load(f)

    assert actual == make_metaschema()
