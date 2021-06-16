"""
Updates the document format codelist from the IANA media types CSV files.
"""

import csv
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
        csvreader = get_and_parse_csv(f'https://www.iana.org/assignments/media-types/{registry}.csv')
        next(csvreader)
        for row in csvreader:
            code = row['Template']
            title = row['Name']
            # If the type has no value in the template column, construct a code from the registry and name
            if code == "":
                code = f'{registry}/{title}'
            # Some titles contain notes, separated by ' - ', except vnd.geo+json, in which the notes are in parentheses
            if ' - ' in title:
                title, notes = title.split(' - ', 1)
            elif ' (' in title:
                title, notes = title.split(' (', 1)
            else:
                notes = None
            codes[code] = {'Title': title, 'Notes': notes}

    with open(os.path.join(schema_dir, 'codelists', 'documentFormat.csv'), 'w') as fp:
        writer = csv.writer(fp, lineterminator='\n')
        writer.writerow(['Code', 'Title', 'Notes'])
        for code in codes.keys():
            writer.writerow([code, codes[code]['Title'], codes[code]['Notes']])
        # Add the 'offline/print' code specified in the schema
        writer.writerow(['offline/print', 'print', None])
