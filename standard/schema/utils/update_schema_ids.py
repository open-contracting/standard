import os.path
import re
import sys
from collections import OrderedDict

docs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'docs', 'en')
sys.path.append(docs_path)

from conf import release  # noqa

if __name__ == '__main__':
    schema_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    replacement = '/{}/'.format(release.replace('.', '__'))


    for name in os.listdir(schema_dir):
        if name.endswith('.json'):
            with open(os.path.join(schema_dir, name)) as f:
                schema = f.read()

            pattern = r'/\d+__\d+__\d+/'
            if re.search(pattern, schema):
                schema = re.sub(pattern, replacement, schema)

                with open(os.path.join(schema_dir, name), 'w') as f:
                    f.write(schema)
