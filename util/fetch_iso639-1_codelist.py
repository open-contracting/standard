"""
Updates the ISO639-1 codelist from the Library of Congress TSV file.
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
        uri = row['URI']
        codes[code] = {'Title': title, 'URI': uri}

    with open(os.path.join(schema_dir, 'codelists', 'iso639-1.csv'), 'w') as fp:
        writer = csv.writer(fp, lineterminator='\n')
        writer.writerow(['Code', 'Title', 'URI'])
        for code in codes.keys():
            writer.writerow([code, codes[code]['Title'], codes[code]['URI']])
