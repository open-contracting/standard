"""
Ensures that `manage.py pre-commit` has been run.
"""

import json
import sys
from pathlib import Path

import jsonref
from ocdsextensionregistry import get_versioned_release_schema

basedir = Path(__file__).resolve().parent.parent

sys.path.extend([str(basedir), str(basedir / "docs")])

from conf import release  # noqa: E402

from manage import get_metaschema  # noqa: E402


def test_versioned_release_schema_is_in_sync():
    with open("schema/versioned-release-validation-schema.json") as f:
        actual = json.load(f)

    with open("schema/release-schema.json") as f:
        expected = get_versioned_release_schema(json.load(f), release.replace(".", "__"))

    assert actual == expected, "Run: python manage.py pre-commit"


def test_dereferenced_release_schema_is_in_sync():
    with open("schema/dereferenced-release-schema.json") as f:
        actual = json.load(f)

    with open("schema/release-schema.json") as f:
        expected = jsonref.load(f, merge_props=True)

    assert actual == expected, "Run: python manage.py pre-commit"


def test_meta_schema_is_in_sync():
    with open("schema/meta-schema.json") as f:
        actual = json.load(f)

    assert actual == get_metaschema(), "Run: python manage.py pre-commit"
