import jsonref

from helper import json_dump, json_load

if __name__ == '__main__':
    json_dump('dereferenced-release-schema.json', json_load('release-schema.json', jsonref))
