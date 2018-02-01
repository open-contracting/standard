"""
Translates the values of `title` and `description` properties of JSON Schema files, creating new files in language's
build directory.

Usage:

    python standard/schema/utils/translate_schema.py language [language ...]

`language` is a two-letter lowercase ISO369-1 code or BCP47 language tag.
"""

import gettext
import sys
import json
import os
from collections import OrderedDict

languages = sys.argv[1:]

json_schema_files = [
    'record-package-schema.json',
    'release-package-schema.json',
    'release-schema.json',
    'versioned-release-validation-schema.json',
]

version = os.environ.get('TRAVIS_BRANCH', 'latest')

for language in languages:
    def translate_data(data):
        if isinstance(data, list):
            for item in data:
                translate_data(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                if key in ('title', 'description') and isinstance(value, str):
                    data[key] = translator.gettext(value).replace('{{version}}', version).replace('{{lang}}', language)
                translate_data(value)

    print('Translating schema to language {}'.format(language))

    translator = gettext.translation('schema', 'standard/docs/locale', languages=[language], fallback=language == 'en')
    build_dir = os.path.join('build', language)

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    for name in json_schema_files:
        with open(os.path.join('standard', 'schema', name)) as r, open(os.path.join(build_dir, name), 'w') as w:
            data = json.load(r, object_pairs_hook=OrderedDict)
            translate_data(data)
            json.dump(data, w, indent=2, ensure_ascii=False)
