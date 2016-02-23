set -e
mkdir -p standard/docs/field_definitions
python standard/schema/utils/make_field_definitions.py
cd standard
sphinx-build -b dirhtml docs/en ../build/en
sphinx-build -b gettext docs/en ../build/locale
pybabel extract -F .babel . -o ../build/locale/schema.pot
sphinx-intl -c docs/en/conf.py update -p ../build/locale -l es

cd ..
cp -r standard/assets build
cp standard/schema/*.json build/en/
# can put multiple languages i.e translate_schema.py en fr
python standard/schema/utils/translate_schema.py es

cd standard
# both these need to be run per language
SCHEMA_LANG=es python schema/utils/make_field_definitions.py
sphinx-build -b dirhtml -D language='es' docs/en ../build/es
