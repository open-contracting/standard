# Edit these variables as appropriate.

# The space-separated, period-prefixed translations to build (for easier substitutions).
TRANSLATIONS=.es .fr
# The source language and translations to build.
LANGUAGES=.en $(TRANSLATIONS)

# Directory of documentation files to build with Sphinx.
DOCS_DIR=docs
# Directory of catalog files.
LOCALE_DIR=docs/locale
# Directory in which to build documentation files.
BUILD_DIR=build
# Extra build files or directories. (These should match paths in .gitignore.)
EXTRA_BUILD_FILES=chromedriver*
# Files that are built and distributed (you may use Bash extended globbing).
DIST_FILES=
# Directory in which to build .pot files.
POT_DIR=$(BUILD_DIR)/locale
# The prefix, if any, to the schema and codelists domains.
DOMAIN_PREFIX=
# The Transifex project name.
TRANSIFEX_PROJECT=open-contracting-standard-1-1
# Any additional extract targets.
EXTRACT_TARGETS=extract_notes

# The path to the branch of the documentation to print to PDF.
PDF_ROOT=/1.1-dev
# The pattern of pages to print to PDF. Update if the documentation adds, removes or renames pages.
PDF_PAGES={,primer/{,what/,how/,releases_and_records/,next/},guidance/{,design/,map/{,amendments/,awards_contracts_buyers_suppliers/,award_notices_decisions/,mapping_awards_contracts/,consortia/,related_processes/,purchase_orders/,beneficial_ownership/,milestones/,organization_classifications/,organization_identifiers/,organization_personal_identifiers/,organization_reference/,organizational_units/,pre-qualification/,related_processes/,unsuccessful_tender/,extensions/,linked_standards/},build/{,data_collection_tools/,system_architectures/,change_history/,easy_releases/,merging/,serialization/,hosting/},publish/{,quality/}},schema/{,reference/,release/,release_package/,records_reference/,record_package/,merging/,identifiers/,codelists/,conformance_and_extensions/},support/,history/{,changelog/,history_and_development/},governance/{,deprecation/}}
# 15000 may warn: "Warning: Received createRequest signal on a disposed ResourceObject's NetworkAccessManager. This might
# be an indication of an iframe taking too long to load."
PDF_DELAY=20000

# Compile PO files for codelists and schema to MO files, so that `translate` succeeds.
.PHONY: compile
compile:
	pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)schema
	pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)codelists

# Put local targets below.
