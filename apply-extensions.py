## ToDo: Replace requests JSON get with ordered dictionary
## Get process to make it's own backup and switch this back in at the end.

import requests
import json
import json_merge_patch
from collections import OrderedDict

extensions_to_merge = ['ppp','location','parties','requirements','budget','budget_project','documentation_details','metrics','risk_allocation','shareholders','related_process','equity_transfer_caps','finance','milestones','tariffs']

GIT_REF = "master"
location = "http://standard.open-contracting.org/extension_registry/{}/extensions.json".format(GIT_REF)
extension_json = requests.get(location).json()

with open('standard/schema/release-schema.json') as schema_file:
    schema = json.load(schema_file,object_pairs_hook=OrderedDict)

for extension in extension_json['extensions']:
    try:
        if extension['slug'] in extensions_to_merge:
            print("Merging " + extension['slug'] )
            extension_patch = requests.get(extension['url'].rstrip("/") + "/" + "release-schema.json").json()
            schema = json_merge_patch.merge(schema, extension_patch)


            extension_readme = requests.get(extension['url'].rstrip("/") + "/" + "README.md")
            with open('standard/docs/en/extensions/' + extension['slug'] + '.md','w') as readme:
                readme.write(extension_readme.text)

    except KeyError:
        print("Nothing")
        pass

with open('standard/schema/release-schema.json','w') as schema_file:
    json.dump(schema,schema_file,indent=4)
