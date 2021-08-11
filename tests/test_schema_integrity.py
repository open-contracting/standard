"""
Ensures that `manage.py pre-commit` has been run.
"""

import json
import os.path
import sys
from collections import OrderedDict

import jsonref

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from manage import (get_dereferenced_release_schema, get_metaschema, get_versioned_release_schema,  # noqa isort:skip
                    sort_keywords)

message = 'Run: python manage.py pre-commit'


def test_release_schema_is_ordered():
    with open('schema/release-schema.json') as f:
        actual = json.load(f, object_pairs_hook=OrderedDict)

    expected = sort_keywords(actual)

    assert actual == expected, message


def test_versioned_release_schema_is_in_sync():
    with open('schema/versioned-release-validation-schema.json') as f:
        actual = json.load(f)

    with open('schema/release-schema.json') as f:
        expected = get_versioned_release_schema(json.load(f))

    assert actual == expected, message


def test_dereferenced_release_schema_is_in_sync():
    with open('schema/dereferenced-release-schema.json') as f:
        actual = json.load(f)

    with open('schema/release-schema.json') as f:
        expected = sort_keywords(get_dereferenced_release_schema(jsonref.load(f, object_pairs_hook=OrderedDict)))

    assert actual == expected, message


def test_meta_schema_is_in_sync():
    with open('schema/meta-schema.json') as f:
        actual = json.load(f)

    assert actual == get_metaschema(), message
