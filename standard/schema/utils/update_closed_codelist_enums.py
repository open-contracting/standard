"""
Updates the schema enum lists for closed codelists with the values from the codelists folder.

This is currently run manually.
"""

import json
import csv
from collections import OrderedDict
from os.path import abspath, dirname, join


def get_enum(codelist, includeNull=False):
    codes = []
    with open(join(schema_dir, 'codelists', codelist), 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            codes.append(row['Code'])
    if includeNull:
        codes.append(None)
    return codes


schema_dir = dirname(dirname(abspath(__file__)))

with open(join(schema_dir, 'release-schema.json'), 'r') as f:
    release_schema = json.loads(f.read(), object_pairs_hook=OrderedDict)

release_schema['properties']['tag']['items']['enum'] = get_enum("releaseTag.csv")
release_schema['properties']['initiationType']['enum'] = get_enum("initiationType.csv")
release_schema['definitions']['Tender']['properties']['status']['enum'] = get_enum("tenderStatus.csv", True)
release_schema['definitions']['Tender']['properties']['procurementMethod']['enum'] = get_enum("method.csv", True)
release_schema['definitions']['Tender']['properties']['mainProcurementCategory']['enum'] = get_enum(
    "procurementCategory.csv", True)
release_schema['definitions']['Award']['properties']['status']['enum'] = get_enum("awardStatus.csv", True)
release_schema['definitions']['Contract']['properties']['status']['enum'] = get_enum("contractStatus.csv", True)
release_schema['definitions']['Milestone']['properties']['status']['enum'] = get_enum("milestoneStatus.csv", True)
release_schema['definitions']['Value']['properties']['currency']['enum'] = get_enum("currency.csv", True)

with open(join(schema_dir, 'release-schema.json'), 'w+') as f:
    json.dump(release_schema, f, indent=2, separators=(',', ': '))
