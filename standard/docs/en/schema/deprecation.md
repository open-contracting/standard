# Deprecation

From time to time fields and codelist values may be removed from the Open Contracting Data Standard.

This will be either due to limited use, or because they have been replaced by alternative fields or codelists.

Before a field or codelist value is removed, it will be first marked as deprecated in a major or minor release (e.g. in 1.1), and removal will only take place, subject to the [governance](../../../support/governance/#deprecation-policy) process, in the next major version (e.g. 2.0).

Deprecated properties are marked in the JSON schema with the presence of a ```deprecated``` property and object which declares the version number in which the property was first deprecated, and provides a description of the reason for this deprecation. 

For example:

```eval_rst
.. code-block:: json
     
     {   
         "deprecated": {
            "description": "The single amendment object has been deprecated in favour of including amendments in an ammendments (plural) array.",
            "deprecatedVersion": "1.1"
          }
      }

```

Validation tools **must** report use of deprecated properties to the user, and **should** report to the user the associated description of the reason for deprecation (which may provide guidance on how to replace the property).

Consuming application targeting compatibility with a particular version of the standard (e.g. 1.1) are encouraged to support properties deprecated in **that decimal version**, but are not expected to support properties deprecated in earlier versions. 



