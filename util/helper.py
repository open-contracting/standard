import json
import os.path

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
schema_dir = os.path.join(base_dir, 'schema')


def json_load(filename, library=json):
    with open(os.path.join(schema_dir, filename)) as f:
        return library.load(f)


def json_dump(filename, data):
    with open(os.path.join(schema_dir, filename), 'w') as f:
        json.dump(data, f, indent=2, separators=(',', ': '))
        f.write('\n')
