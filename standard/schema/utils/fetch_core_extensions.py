"""
Download extension README.md files and add them to this directory.
Add an extra Metadata section to the top of each file.
Download codelists used by documentation to extension /codelists/
"""

import os.path
import re
import sys

import requests

docs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'docs', 'en')
sys.path.append(docs_path)

from conf import extension_registry_git_ref  # noqa


url = 'http://standard.open-contracting.org/extension_registry/{}/extensions.json'
extension_json = requests.get(url.format(extension_registry_git_ref)).json()

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
        match = re.match('https://raw.githubusercontent.com/open-contracting/([^/]*)/', extension['url'])
        repo_url = 'https://github.com/open-contracting/{}'.format(match.group(1))

        response = requests.get(extension['url'].rstrip('/') + '/' + 'README.md')
        lines = response.text.split('\n')
        heading = '\n'.join(lines[:1])
        body = '\n'.join(lines[1:])
        body = body.replace('\n##', '\n###')
        text = heading + metadata.format(extension['url'], repo_url, repo_url) + body

        with open(os.path.join(path, extension['slug'] + '.md'), 'w') as f:
            f.write(text)

        extension_json = requests.get(extension['url'].rstrip('/') + '/' + 'extension.json').json()
        for codelist in extension_json.get('codelists', []):
            response = requests.get(extension['url'].rstrip('/') + '/codelists/' + codelist)
            with open(os.path.join(path, 'codelists', codelist), 'w') as f:
                f.write(response.text)
