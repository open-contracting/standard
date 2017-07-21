import json
from collections import OrderedDict
from os.path import abspath, dirname, join


def remove_keys(obj):
    if isinstance(obj, list):
        for item in obj:
            remove_keys(item)
    elif isinstance(obj, dict):
        for key, value in list(obj.items()):
            if key in ('mergeStrategy', 'mergeOptions'):
                obj.pop(key)
            remove_keys(value)


schema_dir = dirname(dirname(abspath(__file__)))

with open(join(schema_dir, 'release-schema.json'), 'r') as f:
    release_schema = json.loads(f.read(), object_pairs_hook=OrderedDict)

remove_keys(release_schema)

with open(join(schema_dir, 'release-schema.json'), 'w+') as f:
    json.dump(release_schema, f, indent=4, separators=(',', ': '))
