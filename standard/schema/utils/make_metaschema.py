import json_merge_patch
import json
from collections import OrderedDict
from os.path import abspath, dirname, join

schema_dir = dirname(dirname(abspath(__file__)))
metaschema_dir = join(schema_dir, 'metaschema')
draft4_path = join(metaschema_dir, 'json-schema-draft-4.json')
patch_path = join(metaschema_dir, 'meta-schema-patch.json')
metaschema_path = join(schema_dir, 'meta-schema.json')


def make_metaschema():
    with open(draft4_path, 'r') as draft4, open(patch_path, 'r') as patch:
        draft4_schema = json.load(draft4, object_pairs_hook=OrderedDict)
        patch_schema = json.load(patch, object_pairs_hook=OrderedDict)

    return json_merge_patch.merge(draft4_schema, patch_schema)


if __name__ == "__main__":

    with open(metaschema_path, 'w') as f:
        f.write(json.dumps(make_metaschema(), indent=4))
