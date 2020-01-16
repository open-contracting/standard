import json
import os.path

import jsonref

from helper import schema_dir

if __name__ == '__main__':
    with open(os.path.join(schema_dir, 'release-schema.json')) as f:
        dereferenced_release_schema = jsonref.load(f)

    with open(os.path.join(schema_dir, 'dereferenced-release-schema.json'), 'w') as f:
        json.dump(dereferenced_release_schema, f, indent=2, separators=(',', ': '))
        f.write('\n')
