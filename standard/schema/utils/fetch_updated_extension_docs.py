"""
Download extension README.md files and add them to this directory.
Add an extra Metadata section to the top of each file.
Download codelists used by documentation to extension /codelists/
"""

import os
import re
import sys

import requests

docs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'docs', 'en')
sys.path.append(docs_path)

from conf import extension_registry_git_ref  # noqa


location = 'http://standard.open-contracting.org/extension_registry/{}/extensions.json'
extension_json = requests.get(location.format(extension_registry_git_ref)).json()

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


path = os.path.join(docs_path, 'extensions')
for extension in extension_json['extensions']:
    if extension['core']:
        extension_readme = requests.get(extension['url'].rstrip('/') + '/' + 'README.md')
        with open(os.path.join(path, extension['slug'] + '.md'), 'w') as readme:
            m = re.match('https://raw.githubusercontent.com/open-contracting/([^/]*)/', extension['url'])
            github_repo_url = 'https://github.com/open-contracting/{}'.format(m.group(1))
            lines = extension_readme.text.split('\n')
            header_rows = 1 if lines[0].startswith('#') else 2
            heading = '\n'.join(lines[:header_rows])
            body = '\n'.join(lines[header_rows:])
            body = body.replace('\n##', '\n###')
            text = heading + metadata.format(extension['url'], github_repo_url, github_repo_url) + body
            readme.write(text)

        extension_json = requests.get(extension['url'].rstrip('/') + '/' + 'extension.json').json()
        for codelist in extension_json.get('codelists', []):
            codelist_csv = requests.get(extension['url'].rstrip('/') + '/codelists/' + codelist)
            with open(os.path.join(path, 'codelists', codelist), 'w') as codelist_file:
                codelist_file.write(codelist_csv.text)
