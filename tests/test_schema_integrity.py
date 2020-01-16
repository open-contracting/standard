"""
Ensures that `make_versioned_release_schema.py` and `make_metaschema.py` has been run.
"""

import json

import jsonref

from util.make_metaschema import make_metaschema, metaschema_path
from util.make_versioned_release_schema import get_versioned_release_schema


def test_versioned_release_schema_is_in_sync():
    with open('schema/versioned-release-validation-schema.json') as f:
        actual = json.load(f)

    with open('schema/release-schema.json') as f:
        expected = get_versioned_release_schema(json.load(f))

    assert actual == expected, 'Run: python utils/make_versioned_release_schema.py'


def test_dereferenced_release_schema_is_in_sync():
    with open('schema/dereferenced-release-schema.json') as f:
        actual = json.load(f)

    with open('schema/release-schema.json') as f:
        expected = jsonref.load(f)

    assert actual == expected, 'Run: python utils/make_dereferenced_release_schema.py'


def test_metaschema_is_in_sync():
    with open(metaschema_path) as f:
        actual = json.load(f)

    assert actual == make_metaschema()
