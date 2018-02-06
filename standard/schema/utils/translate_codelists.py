"""
Translates each header and the `Title` and `Description` values of codelist CSV files and writes files in each
language's directory within the build directory.

Usage:

    python standard/schema/utils/translate_codelists.py sourcedir builddir localedir language [language ...]

`sourcedir` is the path to the directory containing the codelist CSV files.

`builddir` is the path to the build directory.

`localedir` is the path to the `locale` directory.

`language` is a two-letter lowercase ISO369-1 code or BCP47 language tag.
"""

import csv
import gettext
import glob
import os
import sys


sourcedir = sys.argv[1]
builddir = sys.argv[2]
localedir = sys.argv[3]
languages = sys.argv[4:]

for language in languages:
    print('Translating codelists in {} to language {}'.format(sourcedir, language))

    translator = gettext.translation('codelists', localedir, languages=[language], fallback=language == 'en')

    languagedir = os.path.join(builddir, language)
    if not os.path.exists(languagedir):
        os.makedirs(languagedir)

    for file in glob.glob(os.path.join(sourcedir, '*.csv')):
        with open(file) as r, open(os.path.join(languagedir, os.path.basename(file)), 'w') as w:
            reader = csv.DictReader(r)
            fieldnames = [translator.gettext(fieldname) for fieldname in reader.fieldnames]

            writer = csv.DictWriter(w, fieldnames, lineterminator='\n')
            writer.writeheader()

            for row in reader:
                new_row = {}
                for key, value in row.items():
                    if key in ('Title', 'Description') and value:
                        value = translator.gettext(value)
                    new_row[translator.gettext(key)] = value
                writer.writerow(new_row)
