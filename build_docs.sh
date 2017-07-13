#!/bin/bash
set -e
mkdir -p standard/docs/field_definitions
cd standard
python schema/utils/make_field_definitions.py
CODELIST_LANG=en python schema/utils/translate_codelists.py schema
CODELIST_LANG=en python schema/utils/translate_codelists.py docs/en/extensions

mkdir -p ../build/en/ || true
cp schema/*.json ../build/en/
# Create a symlink for the current language, so we can reference the
# translated JSON schema from Sphinx directives
rm ../build/current_lang || true
ln -s ../build/en ../build/current_lang

sphinx-build -b dirhtml docs/en ../build/en
sphinx-build -b gettext docs/en ../build/locale

pybabel extract -F .babel_schema . -o ../build/locale/schema.pot
pybabel extract -F .babel_codelists . -o ../build/locale/codelists.pot
pybabel compile --use-fuzzy -d docs/locale -D schema
pybabel compile --use-fuzzy -d docs/locale -D codelists

cd ..
cp -r standard/assets build
# can put multiple languages i.e translate_schema.py en fr
python standard/schema/utils/translate_schema.py es fr

cd standard
for lang in es fr; do
    SCHEMA_LANG=$lang python schema/utils/make_field_definitions.py
    CODELIST_LANG=$lang python schema/utils/translate_codelists.py schema
    CODELIST_LANG=$lang python schema/utils/translate_codelists.py docs/en/extensions
    # Create a symlink for the current language, so we can reference the
    # translated JSON schema from Sphinx directives
    rm ../build/current_lang
    ln -s ../build/$lang ../build/current_lang
    sphinx-build -b dirhtml -D language="$lang" docs/en ../build/$lang
done

# Our deploy script doesn't like it if this still exists
rm ../build/current_lang
