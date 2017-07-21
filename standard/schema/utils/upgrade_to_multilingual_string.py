import json
from collections import OrderedDict
from os.path import abspath, dirname, join


def process(obj):
    if isinstance(obj, list):
        for item in obj:
            process(item)
    elif isinstance(obj, dict):
        for key, value in list(obj.items()):
            process(value)
            if key == 'patternProperties':
                for pattern in value:
                    field_name = pattern.split("_")[0][2:]
                field_info = obj['properties'][field_name]
                field_info.pop('type')
                field_info['$ref'] = "#/definitions/MultilingualString"


schema_dir = dirname(dirname(abspath(__file__)))

with open(join(schema_dir, 'release-schema.json'), 'r') as f:
    release_schema = json.loads(f.read(), object_pairs_hook=OrderedDict)

process(release_schema)

release_schema['definitions']['MultilingualString'] = {"oneOf": [
    {"type": "string"},
    {'$ref': "#/definitions/LanguageMap"},
]}

release_schema['definitions']['LanguageMap'] = {
    "type": "object",
    "properties": {},
    "patternProperties": {"^(((([A-Za-z]{2,3}(-([A-Za-z]{3}(-[A-Za-z]{3}){0,2}))?)|[A-Za-z]{4}|[A-Za-z]{5,8})(-([A-Za-z]{4}))?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-([0-9A-WY-Za-wy-z](-[A-Za-z0-9]{2,8})+))*(-(x(-[A-Za-z0-9]{1,8})+))?)|(x(-[A-Za-z0-9]{1,8})+))$": {"type": ["string", "null"]}}
}


with open(join(schema_dir, 'release-schema.json'), 'w+') as f:
    json.dump(release_schema, f, indent=4, separators=(',', ': '))
