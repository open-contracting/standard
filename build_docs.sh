mkdir standard/docs/field_definitions
python standard/schema/utils/make_field_definitions.py
sphinx-build -b dirhtml standard/docs/en build/en
# sphinx-build -b dirhtml -D language='es' standard/docs/en build/es
