import json
from collections import OrderedDict
from os.path import abspath, dirname, join

schema_dir = dirname(dirname(abspath(__file__)))

with open(join(schema_dir, 'release-schema.json'), 'r') as f:
    release_schema = json.loads(f.read(), object_pairs_hook=OrderedDict)

with open(join(schema_dir, 'release-schema.json'), 'w+') as f:
    json.dump(release_schema, f, indent=4, separators=(',', ': '))
