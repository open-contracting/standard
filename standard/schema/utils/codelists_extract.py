"""
Babel extractor used in setup.py
"""

import csv
import io


def convert_fieldname(name):
    for heading in ('Title', 'Description'):
        if heading in name:
            return heading
    return name


def extract(fileobj, keywords, comment_tags, options):
    reader = csv.DictReader(io.StringIO(fileobj.read().decode()))
    for field in reader.fieldnames:
        yield 0, '', convert_fieldname(field), ''

    for row_number, row in enumerate(reader):
        for key, value in row.items():
            if 'title' in key.lower() or 'description' in key.lower() or 'name' in key.lower():
                if value:
                    yield row_number + 1, '', value, [key]
