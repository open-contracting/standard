Open Contracting Data standard
==============================

For view-only access to the standard and documentation please visit [http://standard.open-contracting.org](http://standard.open-contracting.org)

## Versions

The standard website is now versioned MAJOR.MINOR, whereas the schema URIs are versioned MAJOR__MINOR__PATCH. e.g. http://standard.open-contracting.org/1.0/en/ vs http://standard.open-contracting.org/schema/1__0__1/release-schema.json. (Previously both were versioned as MAJOR__MINOR__PATCH).

The standard website version corresponds to a [branch](https://github.com/open-contracting/standard/branches), whereas the schema URI version corresponds to a [release](https://github.com/open-contracting/standard/releases). This allows us to make updates the documentation without having to make a new patch release. On the other hand, there's a need for predictable machine consumption of the content at schema URIs, so we ensure this doesn't change.

There are also one or more development branches, e.g. http://standard.open-contracting.org/1.0-dev/en/

The default standard website is 'latest' - http://standard.open-contracting.org/latest/en/ - which corresponds to the latest released version of the standard. This makes it possible to construct URLs to this that will track the latest version of the standard.

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

If this is your first time using Transifex, run (replacing `USERNAME` and `PASSWORD`):

```shell
sphinx-intl create-transifexrc --transifex-username USERNAME --transifex-password PASSWORD
```

When a new major/minor version of the docs text is ready, a new Transifex project needs to be made called e.g. open-contracting-standard-x.y  This is done on the Transifex web interface. The ```.tx/config``` file also needs to be emptied.

Make sure the build is run above, then run (making sure the project name is the same as the one made above) 

```
sphinx-intl update-txconfig-resources --transifex-project-name open-contracting-standard-1-1 --pot-dir build/locale --locale-dir standard/docs/locale
```

This will update the .tx/config file and this file should be added to the git repository. This will only have to be run again if there is a new/deleted doc page or if a file name has changed name.

In order to push any changes in text to Transifex run:

```
tx push -s
```

When the translations are filled in Transifex you need to run:

```
tx pull -a -f
```

After this the build script will need to be run again.

If translations are added locally, these can also be pushed up to Transifex. (Be aware that this will clobber edits made on Transifex since last time they were pulled):

```
tx push -t --skip
```

Note that the [theme needs to be translated seperately](https://github.com/open-contracting/standard_theme#translations).


### Theme

The OCDS Docs Theme files are held in a separate GitHub repository. Consult [the README there](https://github.com/open-contracting/standard_theme#open-contracting-standard-sphinx-theme) for more information.

The theme files are pulled into your virtual environment during the `pip install -r requirements.txt` step. You will find them in the `.ve/src/standard-theme` directory (where .ve is the name of your virtual environment directory).

