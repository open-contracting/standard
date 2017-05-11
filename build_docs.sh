#!/bin/bash
set -e
mkdir -p standard/docs/field_definitions
cd standard
python schema/utils/make_field_definitions.py
CODELIST_LANG=en python schema/utils/translate_codelists.py

mkdir -p ../build/en/ || true
cp schema/*.json ../build/en/
# Create a symlink for the current language, so we can reference the
# translated JSON schema from Sphinx directives
rm ../build/current_lang || true
ln -s ../build/en ../build/current_lang

sphinx-build -b dirhtml docs/en ../build/en
sphinx-build -b gettext docs/en ../build/locale
# Remove messages from CSVs from Sphinx's own translations as we translate the
# schema and codelists separately.
for name in reference records_reference; do
    msggrep -v -N '../../standard/docs/field_definitions/*.csv'  ../build/locale/schema/${name}.pot > TMP
    mv TMP ../build/locale/schema/${name}.pot
done
msggrep -v -N '../../standard/schema/codelists_translated/*.csv'  ../build/locale/schema/codelists.pot > TMP
mv TMP ../build/locale/schema/codelists.pot
msggrep -v -N '../../standard/docs/en/examples/*.csv'  ../build/locale/implementation/serialization.pot > TMP
mv TMP ../build/locale/implementation/serialization.pot
msggrep -v -N '../../standard/example/*.csv'  ../build/locale/schema/reference.pot > TMP
mv TMP ../build/locale/schema/reference.pot

pybabel extract -F .babel_schema . -o ../build/locale/schema.pot
pybabel extract -F .babel_codelists . -o ../build/locale/codelists.pot
pybabel compile -d docs/locale -D schema 
pybabel compile -d docs/locale -D codelists

cd ..
cp -r standard/assets build
# can put multiple languages i.e translate_schema.py en fr
python standard/schema/utils/translate_schema.py es fr

cd standard
for lang in es fr; do
    SCHEMA_LANG=$lang python schema/utils/make_field_definitions.py
    CODELIST_LANG=$lang python schema/utils/translate_codelists.py
    # Create a symlink for the current language, so we can reference the
    # translated JSON schema from Sphinx directives
    rm ../build/current_lang
    ln -s ../build/$lang ../build/current_lang
    sphinx-build -b dirhtml -D language="$lang" docs/en ../build/$lang
done

# Our deploy script doesn't like it if this still exists
rm ../build/current_lang
