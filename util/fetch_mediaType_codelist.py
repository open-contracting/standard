"""
Updates the media type codelist from the IANA media types CSV files.
"""

import csv
import logging
import os
import requests

from helper import schema_dir


def get_and_parse_csv(url):
    response = requests.get(url)
    response.raise_for_status()
    content = response.content.decode('utf-8')
    return csv.DictReader(content.splitlines(), delimiter=',')


if __name__ == '__main__':
    # https://www.iana.org/assignments/media-types lists CSV files for each registry
    registries = [
        'application',
        'audio',
        'font',
        'image',
        'message',
        'model',
        'multipart',
        'text',
        'video'
    ]

    codes = {}

    for registry in registries:
        response = requests.get(f'https://www.iana.org/assignments/media-types/{registry}.csv')
        response.raise_for_status()
        content = response.content.decode('utf-8')
        csvreader = csv.DictReader(content.splitlines(), delimiter=',')
        for row in csvreader:
            code = row['Template']
            title = row['Name']
            # If the type has no value in the template column, construct a code from the registry and name
            if code == "":
                logging.warning(f'{registry}/{title} has no value in the Template column.')
                code = f'{registry}/{title}'
            # Remove deprecated and obsoleted codes
            if 'DEPRECATED' not in title and 'OBSOLETE' not in title:
                codes[code] = title

    with open(os.path.join(schema_dir, 'codelists', 'mediaType.csv'), 'w') as fp:
        writer = csv.writer(fp, lineterminator='\n')
        writer.writerow(['Code', 'Title'])
        for code in codes.keys():
            writer.writerow([code, codes[code]])
        # Add the 'offline/print' code specified in the schema
        writer.writerow(['offline/print', 'print'])
