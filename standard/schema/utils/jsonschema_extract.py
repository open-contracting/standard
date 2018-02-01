"""
Babel extractor used in setup.py
"""

import json


def gather_text(data, pointer=''):
    if isinstance(data, list):
        for index, item in enumerate(data):
            yield from gather_text(item, pointer='{}/{}'.format(pointer, index))
    elif isinstance(data, dict):
        for key, value in data.items():
            if key in ('title', 'description') and isinstance(value, str):
                yield value, '{}/{}'.format(pointer, key)
            yield from gather_text(value, pointer='{}/{}'.format(pointer, key))


def extract(fileobj, keywords, comment_tags, options):
    """
    Yields the "title" and "description" values of a JSON Schema file.
    """
    data = json.loads(fileobj.read().decode())
    for text, pointer in gather_text(data):
        yield 1, '', text, [pointer]
