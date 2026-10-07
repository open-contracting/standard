# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import csv
import json
import os
from glob import glob
from pathlib import Path

import standard_theme
from docutils.nodes import make_id
from ocds_babel.translate import translate
from ocdskit.mapping_sheet import mapping_sheet
from sphinx.locale import get_translation

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Open Contracting Data Standard"
copyright = "Open Contracting Partnership"
author = "Open Contracting Partnership"

version = "1.1"
release = "1.1.5"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.ifconfig",
    "sphinxcontrib.jsonschema",
    "sphinxcontrib.opencontracting",
    "sphinxcontrib.opendataservices",
    "sphinx_design",
    "sphinx_reredirects",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/docson/[!p]**", "**/docson/package*.json"]

# Pages that moved within the documentation. Targets are relative to the docs root.
moved_pages = {
    "getting_started/building_blocks": "primer/how/",
    "getting_started/contracting_process": "primer/how/",
    "getting_started/publication_patterns": "guidance/build/hosting/",
    "getting_started/quality": "guidance/publish/quality/",
    "getting_started/releases_and_records": "primer/releases_and_records/",
    "getting_started/use_cases": "guidance/design/user_needs/",
    "getting_started/validation": "guidance/build/#check-your-data",
    "getting_started": "primer/",
    "guidance/map/awards_contracts_buyers_suppliers": "guidance/map/awards_contracts/",
    "guidance/map/award_notices_decisions": "guidance/map/awards_contracts/#awards-and-award-notices",
    "guidance/map/mapping_awards_contracts": "guidance/map/awards_contracts/#awards-and-contracts",
    "guidance/map/purchase_orders": "guidance/map/awards_contracts/#purchase-orders",
    "guidance/map/consortia": "guidance/map/buyers_suppliers/#consortia-suppliers",
    "guidance/map/frameworks": "guidance/map/framework_agreements/",
    "guidance/map/related_processes": "guidance/map/framework_agreements/",
    "guidance/map/unsuccessful_tender": "guidance/map/unsuccessful_processes/",
    "guidance/map/catalogs": "guidance/map/electronic_catalogues/",
    "extensions": "guidance/map/extensions/",
    "implementation/amendments": "guidance/map/amendments/",
    "implementation/hosting": "guidance/build/hosting/",
    "implementation/levels": "guidance/publish/quality/",
    "implementation/licensing": "guidance/publish/#license-your-data",
    "implementation/publication_policy": "guidance/publish/#finalize-your-publication-policy",
    "implementation/registration": "guidance/build/#register-an-ocid-prefix",
    "implementation/related_processes": "guidance/map/framework_agreements/",
    "implementation/serialization": "guidance/build/serialization/",
    "implementation": "guidance/",
    "schema/changelog": "history/changelog/",
    "schema/deprecation": "governance/deprecation/",
    "support/credits": "history/history_and_development/#appreciation",
    "support/governance": "governance/",
    "support/history_and_development": "history/history_and_development/",
    "support/tools": "support/",
}
# https://documatt.com/sphinx-reredirects/usage/
# The dirhtml builder writes each redirect to <source>/index.html, so the target is relative to <source>/.
redirects = {source: "../" * (source.count("/") + 1) + target for source, target in moved_pages.items()}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "standard_theme"  # 'pydata_sphinx_theme'
html_theme_path = [standard_theme.get_html_theme_path()]
html_favicon = "_static/favicon-16x16.ico"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["renderjson.js", "script.js"]


# -- Local configuration -----------------------------------------------------

_ = get_translation("theme")

profile_identifier = ""
repository_url = "https://github.com/open-contracting/standard"

# Internationalization.
gettext_compact = False
# `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = f"{profile_identifier}-" if profile_identifier else ""
locale_dirs = ["locale/", os.path.join(standard_theme.get_html_theme_path(), "locale")]
# We use single quotes for codes, which docutils will change to double quotes.
# https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/utils/smartquotes.py
smartquotes = False

# MyST configuration.
myst_enable_extensions = ["linkify"]
myst_heading_anchors = 6
myst_heading_slug_func = make_id
# https://github.com/executablebooks/MyST-Parser/issues/357
suppress_warnings = ["myst.anchor"]

# Theme customization.
navigation_with_keys = False  # restore the Sphinx default
html_context = {
    "analytics_id": "HTWZHRIZ",
}
html_theme_options = {
    "analytics_id": "HTWZHRIZ",
    "display_version": True,
    "root_url": f"/profiles/{profile_identifier}" if profile_identifier else "",
    "short_project": project.replace("Open Contracting Data Standard", "OCDS"),
    "copyright": copyright,
    "license_name": "Apache License 2.0",
    "license_url": f"{repository_url}/blob/HEAD/LICENSE",
    "repository_url": repository_url,
}
html_short_title = f"{html_theme_options['short_project']} v{release}"

# List the extension identifiers and versions that should be part of this specification. The extensions must be in
# the extension registry: https://github.com/open-contracting/extension_registry/blob/main/extension_versions.csv
default_extension_version = f"v{release}"
extension_versions = {
    "bids": default_extension_version,
    "enquiries": default_extension_version,
    "location": default_extension_version,
    "lots": default_extension_version,
    "participation_fee": default_extension_version,
    "process_title": default_extension_version,
}

# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder
# Ignore Google Sheets.
linkcheck_anchors_ignore = [r"^gid="]
linkcheck_ignore = [
    # Avoid GitHub.com rate limiting.
    r"^https://github.com/open-contracting/standard/(?:issues|pull)/\d+$",
    # Ignore irreproducible false positives.
    r"^https://www.fcny.org/fcny/$",
    r"^http://www.eprocurementtoolkit.org/sites/default/files/2016-11/OCDS_Implemetation_Methodology_0.pdf#page=27$",
    # Ignore unwanted links created by linkify.
    r"^http://vnd\.",
    # Ignore expected redirects.
    r"^https://docs.google.com/spreadsheets/d/[^/]+/pub?gid=\d+&single=true&output=csv$",
]


def setup(app):
    # The root of the repository.
    basedir = Path(__file__).resolve().parents[1]
    # `LOCALE_DIR` from `config.mk`.
    localedir = basedir / "docs" / "locale"

    language = app.config.overrides.get("language", "en")

    headers = ["Title", "Description", "Extension"]
    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = f"{gettext_domain_prefix}schema"
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = f"{gettext_domain_prefix}codelists"

    standard_dir = basedir / "schema"
    standard_build_dir = basedir / "build" / language

    branch = os.getenv("GITHUB_REF_NAME", "latest")

    translate(
        [
            # The glob patterns in `babel_ocds_schema.cfg` should match these filenames.
            (glob(str(standard_dir / "*-schema.json")), standard_build_dir, schema_domain),
            # The glob patterns in `babel_ocds_codelist.cfg` should match these.
            (glob(str(standard_dir / "codelists" / "*.csv")), standard_build_dir / "codelists", codelists_domain),
        ],
        localedir,
        language,
        headers,
        version=branch,
    )

    with (standard_build_dir / "release-schema.json").open() as f:
        fieldnames, rows = mapping_sheet(json.load(f), infer_required=True)

    with (standard_build_dir / "release-schema.csv").open("w") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(rows)
