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

## Docs guidelines

The name of the file, becomes the name of the tab


When writing docs, every page should have:

1) an h1 header with the name of the page, that matches the title of the tab/file
1) a consistent flow down always h2, then h3 etc. - don't start at h3
