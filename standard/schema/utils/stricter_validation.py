import json
from collections import OrderedDict
from os.path import abspath, dirname, join


def add_stricter(obj):
    if isinstance(obj, list):
        for item in obj:
            add_stricter(item)
    elif isinstance(obj, dict):
        if 'required' in obj:
            for field in obj['required']:
                field_obj = obj['properties'][field]
                if ("string" in field_obj['type'] and
                    'enum' not in field_obj and
                    'format' not in field_obj):
                    field_obj['minLength'] = 1
                elif "array" in field_obj['type']:
                    field_obj['minItems'] = 1
                
        for key, value in list(obj.items()):
            add_stricter(value)



schema_dir = dirname(dirname(abspath(__file__)))

with open(join(schema_dir, 'release-schema.json'), 'r') as f:
    release_schema = json.loads(f.read(), object_pairs_hook=OrderedDict)

add_stricter(release_schema)

with open(join(schema_dir, 'release-schema.json'), 'w+') as f:
    json.dump(release_schema, f, indent=4, separators=(',', ': '))
