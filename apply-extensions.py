## ToDo: Replace requests JSON get with ordered dictionary
## Get process to make it's own backup and switch this back in at the end.

import requests
import json
import json_merge_patch
from collections import OrderedDict

extensions_to_merge = ['ppp','location','parties','requirements','budget','budget_project']

GIT_REF = "gh-pages"
location = "https://raw.githubusercontent.com/open-contracting/extension_registry/{}/extensions.json".format(GIT_REF)
extension_json = requests.get(location).json()

with open('standard/schema/release-schema.json') as schema_file:
    schema = json.load(schema_file,object_pairs_hook=OrderedDict)

for extension in extension_json['extensions']:
    try:
        if extension['slug'] in extensions_to_merge:
            extension_patch = requests.get(extension['url'].rstrip("/") + "/" + "release-schema.json").json()
            schema = json_merge_patch.merge(schema, extension_patch)
            print("Merging " + extension['slug'] )
    except KeyError:
        print("Nothing")
        pass

with open('standard/schema/release-schema.json','w') as schema_file:
    json.dump(schema,schema_file,indent=4)
