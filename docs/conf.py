# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
from glob import glob
from pathlib import Path

import standard_theme
from ocds_babel.translate import translate

# -- Project information -----------------------------------------------------

project = 'Open Contracting Data Standard'
copyright = 'Open Contracting Partnership'
author = 'Open Contracting Partnership'

version = '1.1'
release = '1.1.5'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.jsonschema',
    'sphinxcontrib.opencontracting',
    'sphinxcontrib.opendataservices',
    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_static/docson/*.md', '_static/docson/integration/*.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'standard_theme'
html_theme_path = [standard_theme.get_html_theme_path()]
html_favicon = '_static/favicon-16x16.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Local configuration -----------------------------------------------------

repository_url = 'https://github.com/open-contracting/standard'
smartquotes = False

html_theme_options = {
    'display_version': True,
    'root_url': '',
    'short_project': project.replace('Open Contracting Data Standard', 'OCDS'),
    'copyright': copyright,
    'license_name': 'Apache License 2.0',
    'license_url': '{}/blob/HEAD/LICENSE'.format(repository_url),
    'repository_url': repository_url,
}

# The `LOCALE_DIR` from `config.mk`, plus the theme's locale.
locale_dirs = ['locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]

gettext_compact = False

# The `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = ''

# List the extension identifiers and versions that should be part of the standard. The extensions must be available in
# the extension registry: https://github.com/open-contracting/extension_registry/blob/main/extension_versions.csv
default_extension_version = 'v{}'.format(release)
extension_versions = {
    'bids': default_extension_version,
    'enquiries': default_extension_version,
    'location': default_extension_version,
    'lots': default_extension_version,
    'milestone_documents': default_extension_version,
    'participation_fee': default_extension_version,
    'process_title': default_extension_version,
}

# Disable dollarmath, which uses MathJax for a string like: "If Alice has $100 and Bob has $1..."
# https://myst-parser.readthedocs.io/en/latest/using/intro.html#sphinx-configuration-options
myst_enable_extensions = []


def setup(app):
    # The root of the repository.
    basedir = Path(os.path.realpath(__file__)).parents[1]
    # The `LOCALE_DIR` from `config.mk`.
    localedir = basedir / 'docs' / 'locale'

    language = app.config.overrides.get('language', 'en')

    headers = ['Title', 'Description', 'Extension']
    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = '{}schema'.format(gettext_domain_prefix)
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = '{}codelists'.format(gettext_domain_prefix)

    standard_dir = basedir / 'schema'
    standard_build_dir = basedir / 'build' / language

    branch = os.getenv('TRAVIS_BRANCH', os.getenv('GITHUB_REF', 'latest').rsplit('/', 1)[-1])

    translate([
        # The glob patterns in `babel_ocds_schema.cfg` should match these filenames.
        (glob(str(standard_dir / '*-schema.json')), standard_build_dir, schema_domain),
        # The glob patterns in `babel_ocds_codelist.cfg` should match these.
        (glob(str(standard_dir / 'codelists' / '*.csv')), standard_build_dir / 'codelists', codelists_domain),
    ], localedir, language, headers, version=branch)
