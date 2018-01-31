#!/bin/bash
set -e

cd standard

python schema/utils/translate_codelists.py schema en
python schema/utils/translate_codelists.py docs/en/extensions en

# Compile message catalogs in the "schema" and "codelists" domains to MO files.
pybabel compile --use-fuzzy -d docs/locale -D schema
pybabel compile --use-fuzzy -d docs/locale -D codelists

cd ..

# Add translated JSON Schema files to the build directory.
python standard/schema/utils/translate_schema.py en es fr

# Create a symlink for the current language, so we can reference the source JSON Schema from Sphinx directives.
rm -f build/current_lang
ln -s en build/current_lang

cd standard

# Build the English documentation and message catalogs.
sphinx-build -q -b dirhtml docs/en ../build/en
sphinx-build -q -b gettext docs/en ../build/locale

# Use the Babel extractors.
pybabel -q extract -F .babel_schema . -o ../build/locale/schema.pot
pybabel -q extract -F .babel_codelists . -o ../build/locale/codelists.pot

cd ..

# Copy the assets into the build directory.
cp -r standard/assets build

cd standard

for lang in es fr; do
    echo "Building $lang..."

    # Translate the schema and codelists for the language.
    python schema/utils/translate_codelists.py schema $lang
    python schema/utils/translate_codelists.py docs/en/extensions $lang

    # Create a symlink for the current language, so we can reference the translated JSON Schema from Sphinx directives.
    rm ../build/current_lang
    ln -s ../build/$lang ../build/current_lang

    # Build the language's documentation.
    sphinx-build -q -b dirhtml -D language="$lang" docs/en ../build/$lang
done

# The deploy script doesn't like it if this still exists.
rm ../build/current_lang
