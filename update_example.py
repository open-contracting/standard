import requests
## This script should:

# 1. Download the excel file below
# 2. Convert to JSON with flatten tool
# 3. Place in standard/docs/en/examples/ppp/full.json
# 4. Split out each of the releases into it's own file named after the OCID


url = "https://docs.google.com/spreadsheets/d/1gvzLoImbnWvty7lfe5mx2h3v3cELj2rsJHBhj_Yo9Cs/pub?output=xlsx"


resp = requests.get(url)
output = open('standard/docs/en/examples/ppp/full.xlsx', 'wb')
output.write(resp.content)
output.close()