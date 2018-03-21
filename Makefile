# See https://github.com/datamade/data-making-guidelines

# See http://clarkgrubb.com/makefile-style-guide#prologue
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

# See http://clarkgrubb.com/makefile-style-guide#phony-target-arg
FORCE:

# The space-separated, period-prefixed translations to build (for easier substitutions).
TRANSLATIONS=.es .fr
# The source language and translations to build.
LANGUAGES=.en $(TRANSLATIONS)

# Directory of documentation files to build with Sphinx.
DOCS_DIR=standard/docs/en
# Directory of catalog files.
CATALOGS_DIR=standard/docs/locale
# Directory in which to build documentation files.
BUILD_DIR=build
# Directory in which to build .pot files.
LOCALE_DIR=$(BUILD_DIR)/locale

# http://blog.jgc.org/2007/06/escaping-comma-and-space-in-gnu-make.html
COMMA := ,
SPACE :=
SPACE +=
COMMA_SEPARATED_TRANSLATIONS=$(subst $(SPACE),$(COMMA),$(TRANSLATIONS:.%=%))

# See http://clarkgrubb.com/makefile-style-guide#phony-targets
.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
	rm -f $(CATALOGS_DIR)/*/LC_MESSAGES/*.mo
	rm -f $(CATALOGS_DIR)/*/LC_MESSAGES/*/*.mo

### Message catalogs

$(LOCALE_DIR):
	mkdir -p $(LOCALE_DIR)

.PHONY: extract_codelists
extract_codelists: $(LOCALE_DIR)
	pybabel -q extract -F .babel_codelists . -o $(LOCALE_DIR)/codelists.pot

.PHONY: extract_schema
extract_schema: $(LOCALE_DIR)
	pybabel -q extract -F .babel_schema . -o $(LOCALE_DIR)/schema.pot

# The codelist CSV files and JSON Schema files must be present for the `csv-table-no-translate` and `jsonschema`
# directives to succeed, but the contents of the files have no effect on the generated .pot files.
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.gettext.MessageCatalogBuilder
.PHONY: extract_markdown
extract_markdown: prebuild.en
	sphinx-build -q -b gettext $(DOCS_DIR) $(LOCALE_DIR)

.PHONY: extract
extract: extract_codelists extract_schema extract_markdown clean_current_lang

### Transifex

# Builds and pushes the .pot files (`source_file` in .tx/config) to Transifex.
.PHONY: push
push: extract
	tx push -s

# Also pushes the translation .po files (`file_filter` in .tx/config) to Transifex.
.PHONY: force_push_all
force_push_all: extract
	tx push -s -t -l $(COMMA_SEPARATED_TRANSLATIONS) -f --no-interactive

pull.%: FORCE
	tx pull -l $* -f

.PHONY: pull
pull:
	tx pull -l $(COMMA_SEPARATED_TRANSLATIONS) -f

### Pre-build

# Create translated codelist CSV files, referenced by `csv-table-no-translate` directives.
translate_codelists.%: FORCE
	python standard/schema/utils/translate_codelists.py standard/schema/codelists $(BUILD_DIR)/codelists $(CATALOGS_DIR) $*
	python standard/schema/utils/translate_codelists.py $(DOCS_DIR)/extensions/codelists $(BUILD_DIR)/codelists $(CATALOGS_DIR) $*

# Create translated JSON Schema files in the language's build directory, referenced by `jsonschema` directives.
translate_schema.%: FORCE
	python standard/schema/utils/translate_schema.py standard/schema $(BUILD_DIR) $(CATALOGS_DIR) $*

# Create a symlink for the language, so that file paths in `jsonschema` directives resolve.
# (Don't use clean_current_lang as a prerequisite, as then it won't run as a prerequisite later.)
current_lang.%: FORCE
	rm -f $(BUILD_DIR)/current_lang
	rm -f $(BUILD_DIR)/codelists/current_lang
	ln -s $* $(BUILD_DIR)/current_lang
	ln -s $* $(BUILD_DIR)/codelists/current_lang

$(LANGUAGES:.%=prebuild.%): prebuild.%: translate_codelists.% translate_schema.% current_lang.%

### Build

# Build the source documentation.
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.html.DirectoryHTMLBuilder
.PHONY: build_source
build_source: prebuild.en
	sphinx-build -q -b dirhtml $(DOCS_DIR) $(BUILD_DIR)/en

# Build the translated documentation. (Same as source, but with a language configuration setting.)
$(TRANSLATIONS:.%=build.%): build.%: prebuild.%
	sphinx-build -q -b dirhtml $(DOCS_DIR) $(BUILD_DIR)/$* -D language="$*"

# Deploy script complains if current_lang is present.
.PHONY: clean_current_lang
clean_current_lang:
	rm $(BUILD_DIR)/current_lang
	rm $(BUILD_DIR)/codelists/current_lang

# Copy the assets into the build directory.
.PHONY: assets
assets:
	mkdir -p $(BUILD_DIR)
	cp -r standard/assets $(BUILD_DIR)

.PHONY: source
source: assets | build_source clean_current_lang

$(TRANSLATIONS:.%=%): %: assets | build_source build.% clean_current_lang

.PHONY: all
all: assets | build_source $(TRANSLATIONS:.%=build.%) clean_current_lang
