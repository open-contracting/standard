"""
Updates the language codelist from the Library of Congress ISO639-1 TSV file.
"""

import csv
import os
import re
import requests

from helper import schema_dir


if __name__ == '__main__':

    codes = {}

    # https://www.iso.org/iso-639-language-codes.html links to loc.gov.
    response = requests.get('http://id.loc.gov/vocabulary/iso639-1.tsv')
    response.raise_for_status()
    content = response.content.decode('utf-8')
    csvreader = csv.DictReader(content.splitlines(), delimiter='\t')
    for row in csvreader:
        code = row['code']
        titles = row['Label (English)']
        # Change entries like "Ndebele, North |  North Ndebele", but not like "Greek, Modern (1453-)".
        if '|' in titles:
            titles = re.split(r' *\| *', row['Label (English)'])
            # Remove duplication like "Ndebele, North |  North Ndebele" and use a comma instead of a pipe for
            # alternatives. To preserve order, a dict without values is used instead of a set.
            titles = ', '.join({' '.join(reversed(title.split(', '))): None for title in titles})
        codes[code] = titles

    with open(os.path.join(schema_dir, 'codelists', 'language.csv'), 'w') as fp:
        writer = csv.writer(fp, lineterminator='\n')
        writer.writerow(['Code', 'Title'])
        for code in codes.keys():
            writer.writerow([code, codes[code]])
