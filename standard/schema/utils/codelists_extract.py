"""
Babel extractor used in setup.py
"""

import csv
from io import StringIO


def extract(fileobj, keywords, comment_tags, options):
    """
    Yields each CSV header, and the values in the Title and Description columns.
    """
    reader = csv.DictReader(StringIO(fileobj.read().decode()))
    for header in reader.fieldnames:
        yield 0, '', header, ''

    for row_number, row in enumerate(reader, 1):
        for key, value in row.items():
            if key in ('Title', 'Description') and value:
                yield row_number, '', value, [key]
