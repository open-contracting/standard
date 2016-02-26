set -e
mkdir -p standard/docs/field_definitions
cd standard
python schema/utils/make_field_definitions.py
CODELIST_LANG=en python schema/utils/translate_codelists.py
sphinx-build -b dirhtml docs/en ../build/en
sphinx-build -b gettext docs/en ../build/locale
pybabel extract -F .babel_schema . -o ../build/locale/schema.pot
pybabel extract -F .babel_codelists . -o ../build/locale/codelists.pot
pybabel compile -d docs/locale -D schema 
pybabel compile -d docs/locale -D codelists

cd ..
cp -r standard/assets build
cp standard/schema/*.json build/en/
# can put multiple languages i.e translate_schema.py en fr
python standard/schema/utils/translate_schema.py es

cd standard
# all these need to be run per language
SCHEMA_LANG=es python schema/utils/make_field_definitions.py
CODELIST_LANG=es python schema/utils/translate_codelists.py
sphinx-build -b dirhtml -D language='es' docs/en ../build/es
