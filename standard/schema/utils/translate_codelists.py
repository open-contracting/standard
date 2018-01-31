"""
Translates each header and the `Title` and `Description` values of codelist CSV files, creating new files in a
`codelists_translated` directory.

Usage:

    cd standard
    python schema/utils/translate_codelists.py schema <language>
    python schema/utils/translate_codelists.py docs/en/extensions <language>

`path` is the path to the codelist CSV files.

`language` is a two-letter lowercase ISO369-1 code or BCP47 language tag.
"""

import gettext
import glob
import csv
import sys
import os


language = sys.argv[2]
translator = gettext.translation('codelists', 'docs/locale', languages=[language], fallback=language == 'en')
codelists_output_dir = os.path.join(sys.argv[1], 'codelists_translated')

if not os.path.exists(codelists_output_dir):
    os.makedirs(codelists_output_dir)


for file in glob.glob(os.path.join(sys.argv[1], 'codelists', '*.csv')):
    new_file = os.path.join(codelists_output_dir, os.path.basename(file))
    with open(file) as r, open(new_file, 'w') as w:
        reader = csv.DictReader(r)
        fieldnames = [translator.gettext(fieldname) for fieldname in reader.fieldnames]

        writer = csv.DictWriter(w, fieldnames)
        writer.writeheader()

        for row in reader:
            new_row = {}
            for key, value in row.items():
                if key in ('Title', 'Description') and value:
                    value = translator.gettext(value)
                new_row[translator.gettext(key)] = value
            writer.writerow(new_row)
