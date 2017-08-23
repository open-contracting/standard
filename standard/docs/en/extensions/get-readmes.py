import requests

GIT_REF = "v1.1.1"
location = "http://standard.open-contracting.org/extension_registry/{}/extensions.json".format(GIT_REF)
extension_json = requests.get(location).json()

for extension in extension_json['extensions']:
    if extension['core']:
        extension_readme = requests.get(extension['url'].rstrip("/") + "/" + "README.md")
        with open(
                    '/home/bjwebb/opendataservices/open-contracting/standard/standard/docs/en/extensions/'
                    + extension['slug'] + '.md',
                    'w'
                ) as readme:
            readme.write(extension_readme.text)
