"""
Translates each header and the `Title` and `Description` values of codelist CSV files, creating new files in a
relative `codelists_translated` directory.

Usage:

    python standard/schema/utils/translate_codelists.py directory localedir language

`directory` is the path to the directory that contains the `codelists` directory containing codelist CSV files, and in
which a `codelists_translated` directory will be created.

`localedir` is the path to the `locale` directory.

`language` is a two-letter lowercase ISO369-1 code or BCP47 language tag.
"""

import csv
import gettext
import glob
import os
import sys


directory = sys.argv[1]
localedir = sys.argv[2]
language = sys.argv[3]
codelists_output_dir = os.path.join(directory, 'codelists_translated')

if not os.path.exists(codelists_output_dir):
    os.makedirs(codelists_output_dir)

print('Translating codelists in {} to language {}'.format(directory, language))

translator = gettext.translation('codelists', localedir, languages=[language], fallback=language == 'en')

for file in glob.glob(os.path.join(directory, 'codelists', '*.csv')):
    new_file = os.path.join(codelists_output_dir, os.path.basename(file))
    with open(file) as r, open(new_file, 'w') as w:
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
