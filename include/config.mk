# Compare this file to:
# https://github.com/open-contracting/standard_profile_template/blob/master/include/config.mk

# Edit these variables as appropriate.

# The space-separated, period-prefixed translations to build (for easier substitutions).
TRANSLATIONS=.es .fr .it
# The source language and translations to build.
LANGUAGES=.en $(TRANSLATIONS)

# Directory of documentation files to build with Sphinx.
DOCS_DIR=docs
# Directory of catalog files.
LOCALE_DIR=locale
# Directory in which to build documentation files.
BUILD_DIR=build
# Extra build files or directories. (These should match paths in .gitignore.)
EXTRA_BUILD_FILES=
# Files that are built and distributed (you may use Bash extended globbing).
DIST_FILES=
# Directory in which to build .pot files.
POT_DIR=$(BUILD_DIR)/locale
# The prefix, if any, to the schema and codelists domains.
DOMAIN_PREFIX=
# Directory containing assets to copy to the build directory (no trailing slash).
ASSETS_DIR=assets
# The Transifex project name.
TRANSIFEX_PROJECT=open-contracting-standard-1-1
# Any additional extract targets.
EXTRACT_TARGETS=extract_notes

# Compile PO files for codelists and schema to MO files, so that `translate` succeeds.
.PHONY: compile
compile:
	pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)schema
	pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)codelists

# Put local targets below.
.PHONY: extract_notes
extract_notes: $(POT_DIR)
	pybabel extract -F babel_ocds_notes.cfg . -o $(POT_DIR)/$(DOMAIN_PREFIX)notes.pot
