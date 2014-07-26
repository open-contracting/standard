#!/usr/bin/env python
import json
from jsonschema import validate, ValidationError

from validate_schema import validate_release_schema


def test_validate_release_schema():
    validate_release_schema()
