"""
Download extension README.md files and add them to this directory.
Add an extra Metadata section to the top of each file.
Download codelists used by documentation to extension /codelists/
"""

import csv
import os.path
import sys
from io import StringIO
from urllib.parse import urlparse

import requests
from ocdsextensionregistry import ExtensionRegistry

docs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'docs', 'en')
sys.path.append(docs_path)

from conf import extension_versions  # noqa

metadata = """

## Metadata

To use this extension, include its URL in the `extension` array of your release or record package.

```json
{{
    "extensions": ["{}extension.json"],
    "releases": []
}}
```

This extension is maintained at <{}>

## Documentation
"""


extensions_path = os.path.join(docs_path, 'extensions')

extensions_url = 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/extensions.csv'
extension_versions_url = 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/extension_versions.csv'  # noqa

extension_registry = ExtensionRegistry(extension_versions_url, extensions_url)

# At present, all core extensions are included in the standard's documentation.
for version in extension_registry.filter(core=True):
    if version.id not in extension_versions:
        raise Exception('{} is a core extension but is not included in the standard'.format(version.id))

for identifier, version in extension_versions.items():
    extension = extension_registry.get(id=identifier, version=version)
    response = requests.get(extension.base_url + 'README.md')
    lines = response.text.split('\n')
    heading = '\n'.join(lines[:1])
    body = '\n'.join(lines[1:])
    body = body.replace('\n##', '\n###')
    text = heading + metadata.format(extension.base_url, extension.repository_html_page) + body

    with open(os.path.join(extensions_path, '{}.md'.format(extension.id)), 'w') as f:
        f.write(text)

    for codelist in extension.metadata.get('codelists', []):
        response = requests.get(extension.base_url + 'codelists/' + codelist)
        with open(os.path.join(extensions_path, 'codelists', codelist), 'w') as f:
            f.write(response.text)
