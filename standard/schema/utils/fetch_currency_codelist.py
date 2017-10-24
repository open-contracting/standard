"""
Fetches currency codelist from datahub core datasets, and picks/renames
columns.

"""

import csv
import json
import requests
from collections import OrderedDict

heading_map = OrderedDict([
    ('Code', 'AlphabeticCode'),
    ('Title', 'Currency'),
    ('Withdrawal Date', 'WithdrawalDate'),
])

req = requests.get('https://raw.githubusercontent.com/datasets/currency-codes/master/data/codes-all.csv')
lines = req.text.split('\n')
reader = csv.DictReader(lines)
new_data = OrderedDict()

for row in reader:
    if not row['AlphabeticCode']:
        continue
    if (row['AlphabeticCode'] not in new_data
            or (
                row['WithdrawalDate'] > new_data[row['AlphabeticCode']]['Withdrawal Date']
                and new_data[row['AlphabeticCode']]['Withdrawal Date'] != ''
            )):
        new_data[row['AlphabeticCode']] = {
            new_heading: row[old_heading] for new_heading, old_heading in heading_map.items()
        }

codes = list(sorted(new_data.keys()))
new_data = list(new_data.values())
new_data.sort(key=lambda row: (row['Withdrawal Date'] != '', row['Code']))

with open('standard/schema/codelists/currency.csv', 'w') as fp:
    writer = csv.DictWriter(fp, fieldnames=heading_map.keys(), lineterminator='\n')
    writer.writeheader()

    for row in new_data:
        writer.writerow(row)

with open('standard/schema/release-schema.json') as fp:
    release_schema = json.load(fp, object_pairs_hook=OrderedDict)

release_schema['definitions']['Value']['properties']['currency']['enum'] = codes + [None]

with open('standard/schema/release-schema.json', 'w') as fp:
    json.dump(release_schema, fp, indent='  ')
