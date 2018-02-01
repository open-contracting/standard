#!/bin/bash
set -e

# Compile catalogs 'codelists.po' to 'codelists.mo' and 'schema.po' to 'schema.mo', so that translate_codelists.py and
# translate_schema.py can succeed for translations.
pybabel compile --use-fuzzy -d standard/docs/locale -D codelists
pybabel compile --use-fuzzy -d standard/docs/locale -D schema

echo "Building en..."

# Create translated codelist CSV files for the language, which will be referenced by `csv-table-no-translate`
# directives.
python standard/schema/utils/translate_codelists.py standard/schema standard/docs/locale en
python standard/schema/utils/translate_codelists.py standard/docs/en/extensions standard/docs/locale en

# Create translated JSON Schema files in the root of the language's build directory, which will be referenced by
# `jsonschema` directives.
python standard/schema/utils/translate_schema.py standard/docs/locale en

# Create a symlink for the language, so that the references in `jsonschema` directives work.
rm -f build/current_lang
ln -s en build/current_lang

# Build the language's documentation (but without the language configuration setting used below).
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.html.DirectoryHTMLBuilder
sphinx-build -q -a -E -b dirhtml standard/docs/en build/en

echo "... done"

# Copy the assets into the build directory.
cp -r standard/assets build

# Build the translations. (Same as English, but with a language configuration setting.)
for lang in es fr; do
    echo "Building $lang..."

    python standard/schema/utils/translate_codelists.py standard/schema standard/docs/locale $lang
    python standard/schema/utils/translate_codelists.py standard/docs/en/extensions standard/docs/locale $lang

    python standard/schema/utils/translate_schema.py standard/docs/locale $lang

    rm build/current_lang
    ln -s $lang build/current_lang

    sphinx-build -q -a -E -b dirhtml -D language="$lang" standard/docs/en build/$lang

    echo "... done"
done

# The deploy script doesn't like it if this still exists.
rm build/current_lang
