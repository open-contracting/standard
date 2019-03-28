import json
import os.path
from collections import OrderedDict

import jsonref


if __name__ == '__main__':
    schema_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(schema_dir, 'release-schema.json')) as f:
        dereferenced_release_schema = jsonref.load(f, object_pairs_hook=OrderedDict)

    with open(os.path.join(schema_dir, 'dereferenced-release-schema.json'), 'w') as f:
        json.dump(dereferenced_release_schema, f, indent=2, separators=(',', ': '))
        f.write('\n')
