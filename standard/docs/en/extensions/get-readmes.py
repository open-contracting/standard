#!/usr/bin/env python3
import requests
import re

'''
Download extension README.md files and add them to this directory.
Add an extra Metadata section to the top of each file.
'''

EXTENSION_GIT_REF = "v1.1.3"
REGISTRY_GIT_REF = "master"
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


for extension in extension_json['extensions']:
    if extension['core']:
        extension_readme = requests.get(extension['url'].rstrip("/") + "/" + "README.md")
        with open('standard/docs/en/extensions/' + extension['slug'] + '.md', 'w') as readme:
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
