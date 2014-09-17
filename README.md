Open Contracting Data standard
==============================

[![Build Status](https://travis-ci.org/open-contracting/standard.svg?branch=master)](https://travis-ci.org/open-contracting/standard)

To run tests locally:

````
pip install -r requirements.txt
py.test
````

To produce a new versioned-release-validation-schema:

````
cd standard/schema/utils
./make_validation_schema.py
````

Some things to bear in mind:

* If you make a change to release-schema.json, you must also make a change to
  versioned-release-schema.json as they should always be in sync. Versioned
release schema exists to layout the mergeStrategies for merging releases, but
it must have the correct types in it from release schema.
* If you make a change to versioned-release-schema, you must update the
  versioned-release-validation-schema.json.

The tests, which run automatically on every commit, check for both of these
points of consistency.
