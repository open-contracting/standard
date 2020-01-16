import json
import os.path

import json_merge_patch

from helper import schema_dir

draft4_path = os.path.join(schema_dir, 'metaschema', 'json-schema-draft-4.json')
patch_path = os.path.join(schema_dir, 'metaschema', 'meta-schema-patch.json')
metaschema_path = os.path.join(schema_dir, 'meta-schema.json')


def make_metaschema():
    with open(draft4_path) as draft4, open(patch_path) as patch:
        draft4_schema = json.load(draft4)
        patch_schema = json.load(patch)

    return json_merge_patch.merge(draft4_schema, patch_schema)


if __name__ == '__main__':
    with open(metaschema_path, 'w') as f:
        json.dump(make_metaschema(), f, indent=2, separators=(',', ': '))
        f.write('\n')
