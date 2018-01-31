#!/usr/bin/env python3
import os
import re

import requests

'''
Download extension README.md files and add them to this directory.
Add an extra Metadata section to the top of each file.
Download codelists used by documentation to extension /codelists/
'''

# REGISTRY_GIT_REF and EXTENSION_GIT_REF should be equal, unless testing.
REGISTRY_GIT_REF = "master"
EXTENSION_GIT_REF = "v1.1.3"
location = "http://standard.open-contracting.org/extension_registry/{}/extensions.json".format(REGISTRY_GIT_REF)
extension_json = requests.get(location).json()

metadata = '''

## Metadata

To use this extension, include its URL in the `extension` array of your release or record package.

```json
{{
    "extensions": ["{}extension.json"],
    "releases": []
}}
```

This extension is maintained at [{}]({})

## Documentation
'''


path = os.path.abspath(os.path.dirname(__file__))
for extension in extension_json['extensions']:
    if extension['core']:
        extension_readme = requests.get(extension['url'].rstrip("/") + "/" + "README.md")
        with open(os.path.join(path, extension['slug'] + '.md'), 'w') as readme:
            m = re.match('https://raw.githubusercontent.com/open-contracting/([^/]*)/', extension['url'])
            github_repo_url = 'https://github.com/open-contracting/{}'.format(m.group(1))
            lines = extension_readme.text.split('\n')
            header_rows = 1 if lines[0].startswith('#') else 2
            heading = '\n'.join(lines[:header_rows])
            body = '\n'.join(lines[header_rows:])
            body = body.replace('\n##', '\n###')
            url = extension['url']
            if REGISTRY_GIT_REF != EXTENSION_GIT_REF:
                url = url.replace(REGISTRY_GIT_REF, EXTENSION_GIT_REF)
            text = heading + metadata.format(url, github_repo_url, github_repo_url) + body
            readme.write(text)

        extension_json = requests.get(extension['url'].rstrip('/') + '/' + 'extension.json').json()
        try:
            for codelist in extension_json['codelists']:
                print(codelist)
                codelist_csv = requests.get(extension['url'].rstrip('/') + '/codelists/' + codelist)
                with open(os.path.join(path, 'codelists', codelist, 'w')) as codelist_file:
                    codelist_file.write(codelist_csv.text)
        except Exception as e:
            pass
