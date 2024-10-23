"""
Ensures that `manage.py pre-commit` has been run.
"""

import json
import os.path
import sys

import jsonref

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from manage import get_metaschema, get_versioned_release_schema


def test_versioned_release_schema_is_in_sync():
    with open('schema/versioned-release-validation-schema.json') as f:
        actual = json.load(f)

    with open('schema/release-schema.json') as f:
        expected = get_versioned_release_schema(json.load(f))

    assert actual == expected, 'Run: python manage.py pre-commit'


def test_dereferenced_release_schema_is_in_sync():
    with open('schema/dereferenced-release-schema.json') as f:
        actual = json.load(f)

    with open('schema/release-schema.json') as f:
        expected = jsonref.load(f, merge_props=True)

    assert actual == expected, 'Run: python manage.py pre-commit'


def test_meta_schema_is_in_sync():
    with open('schema/meta-schema.json') as f:
        actual = json.load(f)

    assert actual == get_metaschema(), 'Run: python manage.py pre-commit'
