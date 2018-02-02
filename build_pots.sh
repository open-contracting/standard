#!/bin/bash
set -e

# Compile catalogs 'codelists.po' to 'codelists.mo' and 'schema.po' to 'schema.mo', so that translate_codelists.py and
# translate_schema.py can succeed for translations.
pybabel compile --use-fuzzy -d standard/docs/locale -D codelists
pybabel compile --use-fuzzy -d standard/docs/locale -D schema

# Create codelist CSV files, referenced by `csv-table-no-translate` directives, for `sphinx-build` to succeed.
python standard/schema/utils/translate_codelists.py standard/schema standard/docs/locale en
python standard/schema/utils/translate_codelists.py standard/docs/en/extensions standard/docs/locale en

# Create JSON Schema files, referenced by `jsonschema` directives, for `sphinx-build` to succeed.
python standard/schema/utils/translate_schema.py standard/docs/locale en

# Create a symlink for the source language, so that the references in `jsonschema` directives work.
rm -f build/current_lang
ln -s en build/current_lang

# Build the pot files. These are the source files in .tx/config that can be pushed to Transifex.
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.gettext.MessageCatalogBuilder
sphinx-build -q -a -E -b gettext standard/docs/en build/locale
pybabel -q extract -F .babel_schema . -o build/locale/schema.pot
pybabel -q extract -F .babel_codelists . -o build/locale/codelists.pot
