set -e
mkdir -p standard/docs/field_definitions
python standard/schema/utils/make_field_definitions.py
cd standard
sphinx-build -b dirhtml docs/en ../build/en
sphinx-build -b gettext docs/en ../build/locale
sphinx-intl -c docs/en/conf.py update -p ../build/locale -l es
sphinx-build -b dirhtml -D language='es' docs/en ../build/es
cd ..
cp -r standard/assets build
