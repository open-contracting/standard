import os
import json
import ocdsmerge
from collections import OrderedDict
from datetime import tzinfo, timedelta, datetime

releases = []
release_list = []
packages = []
package = None

# Get all the JSON files in this directory
for fname in sorted(os.listdir(".")):
    if fname.endswith('json'):
        with open(fname, 'r') as jsonfile:
            package = json.load(jsonfile, object_pairs_hook=OrderedDict)
            for release in package['releases']:
                packages.append( package['uri'] + '#' + release['id'])
                releases.append({
                    'url': package['uri'] + '#' + release['id'],
                    'date': release['date'],
                    'tag': release['tag']
                })
                release_list.append(release)

compiled_release = ocdsmerge.merge(release_list)

versioned_release = ocdsmerge.merge_versioned(release_list)

with open("merged.json", 'w') as f:
    json.dump({
        'uri': 'http://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json',
        'packages': packages,
        'publisher': package['publisher'],
        'publishedDate': '2016-03-05T13:02:00Z',
        'records': [{
            'ocid': 'ocds-213czf-000-00002',
            'releases': releases,
            'compiledRelease': compiled_release,
        }]
    }, f, indent=3, sort_keys=True)

with open("versioned.json", 'w') as f:
    json.dump({
        'uri': 'http://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json',
        'packages': packages,
        'publisher': package['publisher'],
        'publishedDate': '2016-03-05T13:02:00Z',
        'records': [{
            'ocid': 'ocds-213czf-000-00002',
            'releases': releases,
            'compiledRelease': compiled_release,
            'versionedRelease': versioned_release,
        }]
    }, f, indent=3, sort_keys=True)
