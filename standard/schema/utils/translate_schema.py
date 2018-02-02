"""
Translates the `title` and `description` values of JSON Schema files, creating new files for each language directory in
the build directory.

Usage:

    python standard/schema/utils/translate_schema.py builddir localedir language [language ...]

`builddir` is the path to the `build` directory.

`localedir` is the path to the `locale` directory.

`language` is a two-letter lowercase ISO369-1 code or BCP47 language tag.
"""

import gettext
import json
import os
import sys
from collections import OrderedDict

builddir = sys.argv[1]
localedir = sys.argv[2]
languages = sys.argv[3:]

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

    translator = gettext.translation('schema', localedir, languages=[language], fallback=language == 'en')
    languagedir = os.path.join(builddir, language)

    if not os.path.exists(languagedir):
        os.makedirs(languagedir)

    for name in json_schema_files:
        with open(os.path.join('standard', 'schema', name)) as r, open(os.path.join(languagedir, name), 'w') as w:
            data = json.load(r, object_pairs_hook=OrderedDict)
            translate_data(data)
            json.dump(data, w, indent=2, separators=(',', ': '), ensure_ascii=False)
