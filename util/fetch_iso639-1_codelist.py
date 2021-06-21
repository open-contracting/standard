"""
Updates the language codelist from the Library of Congress ISO639-1 TSV file.
"""

import csv
import os
import requests

from helper import schema_dir


if __name__ == '__main__':

    codes = {}

    response = requests.get('http://id.loc.gov/vocabulary/iso639-1.tsv')
    response.raise_for_status()
    content = response.content.decode('utf-8')
    csvreader = csv.DictReader(content.splitlines(), delimiter='\t')
    for row in csvreader:
        code = row['code']
        title = row['Label (English)']
        codes[code] = title

    with open(os.path.join(schema_dir, 'codelists', 'language.csv'), 'w') as fp:
        writer = csv.writer(fp, lineterminator='\n')
        writer.writerow(['Code', 'Title'])
        for code in codes.keys():
            writer.writerow([code, codes[code]])
