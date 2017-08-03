# Standard Utilities

The scripts in this folder support the creation of the versioned release schema, and standard documentation. See the root README file for virtual environment settings. 

## make_validation_schema.py

Whenever the release schema is updated, a versioned release schema has to be created from this, to support validation of versioned OCDS files. 

This can be created by running:

````shell
./make_validation_schema.py
````

There are tests set-up to ensure this has happened. 


