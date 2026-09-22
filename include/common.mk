# See https://github.com/datamade/data-making-guidelines

# See https://clarkgrubb.com/makefile-style-guide#phony-target-arg
FORCE:

# https://blog.jgc.org/2007/06/escaping-comma-and-space-in-gnu-make.html
COMMA := ,
SPACE :=
SPACE +=
COMMA_SEPARATED_TRANSLATIONS=$(subst $(SPACE),$(COMMA),$(TRANSLATIONS:.%=%))

# See https://clarkgrubb.com/makefile-style-guide#phony-targets
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

.PHONY: extract_theme
extract_theme: $(POT_DIR)
	pybabel extract . -o $(POT_DIR)/$(DOMAIN_PREFIX)theme.pot

.PHONY: extract_codelists
extract_codelists: $(POT_DIR)
	pybabel extract -F babel_ocds_codelist.cfg . -o $(POT_DIR)/$(DOMAIN_PREFIX)codelists.pot

.PHONY: extract_schema
extract_schema: $(POT_DIR)
	pybabel extract -F babel_ocds_schema.cfg . -o $(POT_DIR)/$(DOMAIN_PREFIX)schema.pot

# The codelist CSV files and JSON Schema files must be present for the `csv-table-no-translate` and `jsonschema`
# directives to succeed, but the contents of the files have no effect on the generated .pot files.
# See https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.gettext.MessageCatalogBuilder
.PHONY: extract_markdown
extract_markdown:
	sphinx-build -nW --keep-going -q -b gettext $(DOCS_DIR) $(POT_DIR)

.PHONY: extract
extract: extract_theme extract_codelists extract_schema $(EXTRACT_TARGETS) extract_markdown

$(TRANSLATIONS:.%=docs/locale/%): docs/locale/%: FORCE
	sphinx-intl update -p $(POT_DIR) -d $(LOCALE_DIR) -l "$*"

.PHONY: docs/locale
docs/locale: $(TRANSLATIONS:.%=docs/locale/%)

.PHONY: pocount
pocount:
	find $(LOCALE_DIR) -name LC_MESSAGES -exec pocount --incomplete --short "{}" +

### Build

# Build the source documentation.
# See https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.html.DirectoryHTMLBuilder
.PHONY: build_source
build_source:
	sphinx-build -nW --keep-going -q -b dirhtml $(DOCS_DIR) $(BUILD_DIR)/en

# Build the translated documentation. (Same as source, but with a language configuration setting.)
$(TRANSLATIONS:.%=build.%): build.%:
	sphinx-build -nW --keep-going -q -b dirhtml $(DOCS_DIR) $(BUILD_DIR)/$* -D language="$*"

.PHONY: source
source: build_source

$(TRANSLATIONS:.%=%): %: build_source compile build.%

.PHONY: all
all: build_source compile $(TRANSLATIONS:.%=build.%)

### Development

.PHONY: autobuild
autobuild:
	sphinx-autobuild $(SPHINX_AUTOBUILD_EXTRA_ARGS) -nW -q -b dirhtml $(DOCS_DIR) $(BUILD_DIR)/en

.PHONY: update
update: clean_dist
	python manage.py update

### Test

# "-" ignores the exit status. Schema files might contain old URLs that redirect, which can only be updated in a new version.

.PHONY: linkcheck_source
linkcheck_source:
	-sphinx-build -q -b linkcheck $(DOCS_DIR) $(BUILD_DIR)/en

$(TRANSLATIONS:.%=linkcheck.%): linkcheck.%:
	-sphinx-build -q -b linkcheck $(DOCS_DIR) $(BUILD_DIR)/$* -D language="$*"

.PHONY: linkcheck
linkcheck: linkcheck_source compile $(TRANSLATIONS:.%=linkcheck.%)

### PDF generation

$(LANGUAGES:.%=pdf.%): pdf.%: FORCE
	wkhtmltopdf \
		--no-stop-slow-scripts \
		--javascript-delay $(PDF_DELAY) \
		--disable-smart-shrinking \
		--print-media-type \
		toc https://standard.open-contracting.org$(PDF_ROOT)/$*/$(PDF_PAGES) $*.pdf

.PHONY: pdf
pdf: $(LANGUAGES:.%=pdf.%)
