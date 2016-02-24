Open Contracting Data standard
==============================

For view-only access to the standard and documentation please visit [http://ocds.open-contracting.org/standard/](http://ocds.open-contracting.org/standard/)

## Working with the standard

[![Build Status](https://travis-ci.org/open-contracting/standard.svg?branch=master)](https://travis-ci.org/open-contracting/standard)

To run tests locally:

````
pip install -r requirements.txt
py.test
````

**NOTE:** If you make a change to release-schema.json, you must update the versioned-release-validation-schema.json by:

````
cd standard/schema/utils
./make_validation_schema.py
````

The tests, which run automatically on every commit, check that this process has been done.

## Virtual Environment

```
virtualenv -p /usr/local/bin/python3.4 .ve
source .ve/bin/activate
pip install -r requirements.txt
```

(update with the path to your python executable)


## Documentation

Documentation is written in Markdown syntax with [recommonmark](https://recommonmark.readthedocs.org/en/latest/) building on [Commonmark](http://commonmark.org/)

The documentation is built by sphinx from the ```build_docs.sh``` script. 

Within the virtual environment run ```./build_docs.sh``` and the documentation will be available in the /build/ folder.

To view, run a local web server. For example, from within /build/ run python -m SimpleHTTPServer

### Auto-regenerating docs

Sphinx does not watch directories for changes, but can be linked with other scripts to regenerate docs whenever anything changes. On a mac with fswatch installed:

```
fswatch -0 standard/docs/ | xargs -0 -n 1 -I {} ./build_docs.sh
```

### Translations

When a new version of the docs text is ready, a new transifex project needs to be made called eg. ocds-docs-1.0.0.  This is done on the transifex web interface.

Make sure the build is run above, then run (making sure the poject name is the same as the one made above) 

```
sphinx-intl update-txconfig-resources --transifex-project-name open-contracting-standard-1-0 --pot-dir build/locale --locale-dir standard/docs/locale
```

This will update the .tx/config file and this file should be added to the git repository. This will only have to be run again if there is a new/deleted doc page or if a file name has changed name.

In order to push any changes in text to transifex run:

```
tx push -s
```

When the translations are filled in transifex you need to run:

```
tx pull -a
```

After this the build script will need to be run again.

If translations are added locally, these can also be pushed up to Transifex:

```
tx push -t --skip
```

Note that the [theme needs to be translated seperately](https://github.com/open-contracting/standard_theme#translations).


### Theme

The OCDS Docs Theme files are held in a seperate GitHub repository. Consult [the README there](https://github.com/open-contracting/standard_theme#open-contracting-standard-sphinx-theme) for more information.

The theme files are pulled into your virtual envronment during the `pip install -r requirements.txt` step. You will find them in the `.ve/src/standard-theme` directory (where .ve is the name of your virtual environment directory).

