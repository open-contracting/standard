"""
Fetches currency codelist from datahub core datasets, and picks/renames
columns.

"""

import csv
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
new_data = set()

for row in reader:
    if not row['AlphabeticCode']:
        continue
    new_data.add(tuple(
        (new_heading, row[old_heading]) for new_heading, old_heading in heading_map.items()
    ))

new_data = [dict(row) for row in new_data]
new_data.sort(key=lambda row: (row['Withdrawal Date'] != '', row['Code']))

with open('standard/schema/codelists/currency.csv', 'w') as fp:
    writer = csv.DictWriter(fp, fieldnames=heading_map.keys(), lineterminator='\n')
    writer.writeheader()

    for row in new_data:
        writer.writerow(row)
