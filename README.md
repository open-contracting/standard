Open Contracting Data standard
==============================

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
