"""
Translates the `title` and `description` fields of JSON Schema files.

Usage:

    python standard/schema/utils/translate_schema.py <language> ...

`language` is a two-letter lowercase ISO369-1 code or BCP47 language tag.
"""

import gettext
import sys
import json
import os
from collections import OrderedDict

languages = sys.argv[1:]

file_names = ['record-package-schema.json',
             'release-package-schema.json',
             'versioned-release-validation-schema.json',
             'release-schema.json']
    
for language in languages:
    print("Translating schema to language " + language)
    translator = gettext.translation('schema', 'standard/docs/locale', languages=[language])

    def translate_data(data):
        for key, value in list(data.items()):
            if key in ('title', 'description') and isinstance(value, str):
                data[key] = translator.gettext(value)
            if isinstance(value, dict):
                translate_data(value)

    for name in file_names:
        data = json.load(open('standard/schema/' + name), object_pairs_hook=OrderedDict)
        translate_data(data)
        directory_name = 'build/' + language 
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        json.dump(data, open(directory_name + '/' + name, 'w+'), indent=4, ensure_ascii=False)

