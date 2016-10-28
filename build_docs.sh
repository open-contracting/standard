#!/bin/bash
set -e

cp standard/schema/release-schema.json standard/schema/release-schema.json.backup
python apply-extensions.py

mkdir -p standard/docs/field_definitions
cd standard
python schema/utils/make_field_definitions.py
CODELIST_LANG=en python schema/utils/translate_codelists.py
sphinx-build -b dirhtml docs/en ../build/en


## Commenting out localisation code for now
#   sphinx-build -b gettext docs/en ../build/locale
#   # Remove messages from CSVs from Sphinx's own translations as we translate the
#   # schema and codelists separately.
#   for name in reference records_reference; do
#       msggrep -v -N '../../standard/docs/field_definitions/*.csv'  ../build/locale/schema/${name}.pot > TMP
#       mv TMP ../build/locale/schema/${name}.pot
#   done
#   msggrep -v -N '../../standard/schema/codelists_translated/*.csv'  ../build/locale/schema/codelists.pot > TMP
#   mv TMP ../build/locale/schema/codelists.pot
#   msggrep -v -N '../../standard/docs/en/examples/*.csv'  ../build/locale/implementation/serialization.pot > TMP
#   mv TMP ../build/locale/implementation/serialization.pot
#   msggrep -v -N '../../standard/example/*.csv'  ../build/locale/schema/reference.pot > TMP
#   mv TMP ../build/locale/schema/reference.pot
#   
#   pybabel extract -F .babel_schema . -o ../build/locale/schema.pot
#   pybabel extract -F .babel_codelists . -o ../build/locale/codelists.pot
#   pybabel compile -d docs/locale -D schema 
#   pybabel compile -d docs/locale -D codelists
#   
   cd ..
   cp -r standard/assets build
   cp standard/schema/*.json build/en/
#   # can put multiple languages i.e translate_schema.py en fr
#   python standard/schema/utils/translate_schema.py es
#   
#   cd standard
#   # all these need to be run per language
#   SCHEMA_LANG=es python schema/utils/make_field_definitions.py
#   CODELIST_LANG=es python schema/utils/translate_codelists.py
#   sphinx-build -b dirhtml -D language='es' docs/en ../build/es

# cd ..
cp standard/schema/release-schema.json.backup standard/schema/release-schema.json
rm standard/schema/release-schema.json.backup