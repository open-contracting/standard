import requests
## This script should:
import requests
import shutil
import flattentool
import json
import collections


# 1. Download the excel file below
# 2. Convert to JSON with flatten tool
# 3. Place in standard/docs/en/examples/ppp/full.json
# 4. Split out each of the releases into it's own file named after the OCID

url = 'https://docs.google.com/spreadsheets/d/1gvzLoImbnWvty7lfe5mx2h3v3cELj2rsJHBhj_Yo9Cs/pub?output=xlsx'
response = requests.get(url, stream=True)
with open('download.xlsx', 'wb+') as out_file:
    shutil.copyfileobj(response.raw, out_file)


flattentool.unflatten(
  'download.xlsx',
  output_name='standard/docs/en/examples/ppp/full.json',
  input_format='xlsx',
  root_list_path='releases',
  root_id='ocid',
  encoding='utf-8'
)

with open('standard/docs/en/examples/ppp/full.json') as full_file:
    full = json.load(full_file)

    split_releases = collections.defaultdict(list)

    for release in full['releases']:
        if 'id' not in release:
            print('Warning, release without an id')
            print(json.dumps(release, indent=2))
            continue
        split_releases[release['id']].append(release)

    for key, value in split_releases.items():
        with open('standard/docs/en/examples/ppp/{}.json'.format(key), 'w+') as release_file:
            json.dump({"releases": value}, release_file, indent=2)
