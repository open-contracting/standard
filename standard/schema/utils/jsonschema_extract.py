"""
Babel extractor used in setup.py
"""

import json


def gather_text(schema, pointer=''):
    if isinstance(schema, list):
        for index, item in enumerate(schema):
            yield from gather_text(item, pointer='{}/{}'.format(pointer, index))
    elif isinstance(schema, dict):
        for key, value in schema.items():
            if key in ('title', 'description') and isinstance(value, str):
                yield value, '{}/{}'.format(pointer, key)
            yield from gather_text(value, pointer='{}/{}'.format(pointer, key))


def extract(fileobj, keywords, comment_tags, options):
    """
    Yields the values of "title" and "description" properties.
    """
    schema = json.loads(fileobj.read().decode())
    for text, pointer in gather_text(schema):
        yield 1, '', text, [pointer]
