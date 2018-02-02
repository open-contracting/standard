"""
Babel extractor used in setup.py
"""

import csv
import os.path
from io import StringIO


def extract(fileobj, keywords, comment_tags, options):
    """
    Yields each header, and the Title and Description values of a codelist CSV file.
    """
    reader = csv.DictReader(StringIO(fileobj.read().decode()))
    for header in reader.fieldnames:
        yield 0, '', header.strip(), ''

    if os.path.basename(fileobj.name) != 'currency.csv':
        for row_number, row in enumerate(reader, 1):
            for key, value in row.items():
                if key in ('Title', 'Description') and value:
                    yield row_number, '', value.strip(), [key]
