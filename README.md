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

```fswatch -0 standard/docs/ | xargs -0 -n 1 -I {} ./build_docs.sh```

