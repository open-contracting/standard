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
new_data = {}

for row in reader:
    if not row['AlphabeticCode']:
        continue
    unique_fields = (row['AlphabeticCode'], row['Currency'])
    if unique_fields not in new_data or row['WithdrawalDate'] < new_data[unique_fields]:
        new_data[unique_fields] = row['WithdrawalDate']

new_data = [{
    'Code': code,
    'Title': title,
    'Withdrawal Date': withdrawal,
} for (code, title), withdrawal in new_data.items()]
new_data.sort(key=lambda row: (row['Withdrawal Date'] != '', row['Code']))

with open('standard/schema/codelists/currency.csv', 'w') as fp:
    writer = csv.DictWriter(fp, fieldnames=heading_map.keys(), lineterminator='\n')
    writer.writeheader()

    for row in new_data:
        writer.writerow(row)
