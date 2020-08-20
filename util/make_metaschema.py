import json_merge_patch

from helper import json_dump, json_load


def get_metaschema():
    return json_merge_patch.merge(json_load('metaschema/json-schema-draft-4.json'),
                                  json_load('metaschema/meta-schema-patch.json'))


if __name__ == '__main__':
    json_dump('meta-schema.json', get_metaschema())
