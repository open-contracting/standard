# Deprecation

From time to time fields and codelist values might be removed from the Open Contracting Data Standard.

This will be either due to limited use, or because they have been replaced by alternative fields or codelists.

Before a field or codelist value is removed, it will be first marked as deprecated in a major or minor release (e.g. in 1.1), and removal will only take place, subject to the [governance](../#deprecation-policy) process, in the next major version (e.g. 2.0).

Deprecated fields are marked in the JSON schema with the presence of a `deprecated` property and object which declares the version number in which the field was first deprecated, and provides a description of the reason for this deprecation.

For example:

```{eval-rst}
.. code-block:: json
     
     {   
         "deprecated": {
            "description": "The single amendment object has been deprecated in favour of including amendments in an amendments (plural) array.",
            "deprecatedVersion": "1.1"
          }
      }

```

Validation tools **must** report use of deprecated fields to the user, and **should** report to the user the associated description of the reason for deprecation (which might provide guidance on how to replace the field).

Consuming applications targeting compatibility with a minor version of the standard (e.g. 1.1) **must** support fields that were deprecated in that minor version, and **may** support fields that were removed.
