import json


def gather_text(schema, current_path):
    for key, value in schema.items():
        if key in ('title', 'description') and isinstance(value, str):
            yield value, current_path + '/' + key
        if isinstance(value, dict):
            yield from gather_text(value, current_path + '/' + key)


def extract(fileobj, keywords, comment_tags, options):
    schema = json.loads(fileobj.read().decode())
    for text, current_path in gather_text(schema, ''):
        yield 1, '', text, [current_path]

#    for lineno, funcname, messages, comments in results:
