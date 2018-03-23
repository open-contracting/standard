# Update this file from a profile with:
# curl -O https://raw.githubusercontent.com/open-contracting/standard_profile_template/master/include/common.mk

# See https://github.com/datamade/data-making-guidelines

# See http://clarkgrubb.com/makefile-style-guide#phony-target-arg
FORCE:

# http://blog.jgc.org/2007/06/escaping-comma-and-space-in-gnu-make.html
COMMA := ,
SPACE :=
SPACE +=
COMMA_SEPARATED_TRANSLATIONS=$(subst $(SPACE),$(COMMA),$(TRANSLATIONS:.%=%))

# See http://clarkgrubb.com/makefile-style-guide#phony-targets
.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
	rm -rf $(EXTRA_BUILD_FILES)
	rm -f $(LOCALE_DIR)/*/LC_MESSAGES/*.mo
	rm -f $(LOCALE_DIR)/*/LC_MESSAGES/*/*.mo

.PHONY: clean_dist
clean_dist:
	if [ -n "$(DIST_FILES)" ]; then bash -O extglob -c "rm -rf $(DIST_FILES)"; fi

### Directories

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(POT_DIR):
	mkdir -p $(POT_DIR)

### Message catalogs

.PHONY: extract_codelists
extract_codelists: $(POT_DIR)
	pybabel -q extract -F .babel_codelists . -o $(POT_DIR)/$(DOMAIN_PREFIX)codelists.pot

.PHONY: extract_schema
extract_schema: $(POT_DIR)
	pybabel -q extract -F .babel_schema . -o $(POT_DIR)/$(DOMAIN_PREFIX)schema.pot

# The codelist CSV files and JSON Schema files must be present for the `csv-table-no-translate` and `jsonschema`
# directives to succeed, but the contents of the files have no effect on the generated .pot files.
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.gettext.MessageCatalogBuilder
.PHONY: extract_markdown
extract_markdown: current_lang.en
	sphinx-build -q -b gettext $(DOCS_DIR) $(POT_DIR)

.PHONY: extract
extract: extract_codelists extract_schema extract_markdown clean_current_lang

### Transifex

.PHONY: update_txconfig
update_txconfig:
	sphinx-intl update-txconfig-resources --transifex-project-name $(TRANSIFEX_PROJECT) --pot-dir $(POT_DIR) --locale-dir $(LOCALE_DIR)

# Builds and pushes the .pot files (`source_file` in .tx/config) to Transifex.
.PHONY: push
push: extract
	tx push -s

# Also pushes the translation .po files (`file_filter` in .tx/config) to Transifex.
.PHONY: force_push_all
force_push_all: extract
	tx push -s -t -f -l $(COMMA_SEPARATED_TRANSLATIONS) --no-interactive

pull.%: FORCE
	tx pull -f -l $*

.PHONY: pull
pull:
	tx pull -f -l $(COMMA_SEPARATED_TRANSLATIONS)

### Current language

# Create a symlink for the language, so that file paths in `jsonschema` directives resolve.
# (Don't use clean_current_lang as a prerequisite, as then it won't run as a prerequisite later.)
$(LANGUAGES:.%=current_lang.%): current_lang.%: FORCE
	rm -f $(BUILD_DIR)/current_lang
	rm -f $(BUILD_DIR)/codelists/current_lang
	mkdir -p $(BUILD_DIR)/codelists
	ln -s $* $(BUILD_DIR)/current_lang
	ln -s $* $(BUILD_DIR)/codelists/current_lang

# Deploy script complains if current_lang is present.
.PHONY: clean_current_lang
clean_current_lang:
	rm $(BUILD_DIR)/current_lang
	rm $(BUILD_DIR)/codelists/current_lang

### Build

# Build the source documentation.
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.html.DirectoryHTMLBuilder
.PHONY: build_source
build_source: current_lang.en
	sphinx-build -q -b dirhtml $(DOCS_DIR) $(BUILD_DIR)/en

# Build the translated documentation. (Same as source, but with a language configuration setting.)
$(TRANSLATIONS:.%=build.%): build.%: current_lang.%
	sphinx-build -q -b dirhtml $(DOCS_DIR) $(BUILD_DIR)/$* -D language="$*"

# Copy the assets into the build directory.
.PHONY: assets
assets: $(BUILD_DIR)
	if [ -n "$(ASSETS_DIR)" ]; then cp -r $(ASSETS_DIR) $(BUILD_DIR); fi

.PHONY: source
source: assets | build_source clean_current_lang

$(TRANSLATIONS:.%=%): %: assets | build_source compile build.% clean_current_lang

.PHONY: all
all: assets | build_source compile $(TRANSLATIONS:.%=build.%) clean_current_lang
