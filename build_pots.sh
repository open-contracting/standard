#!/bin/bash
set -e

# Build the pot files. These are the source files in .tx/config that can be pushed to Transifex.
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.gettext.MessageCatalogBuilder
sphinx-build -q -a -E -b gettext standard/docs/en build/locale
pybabel -q extract -F standard/.babel_schema . -o build/locale/schema.pot
pybabel -q extract -F standard/.babel_codelists . -o build/locale/codelists.pot
