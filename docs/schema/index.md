# Reference

The Open Contracting Data Standard is maintained using JSON Schema. 

The main sections and common objects used in the schema are [introduced in the getting started section](../getting_started/building_blocks).

In this section you will find the schema for [releases](release) along with the schemas for [release packages](release_package) and [record packages](record_package), which act as envelopes for releases and records, respectively.

The [release schema reference](reference) provides guidance on using each of the sections and building blocks in the schema, and the [record schema reference](records_reference) provides additional information on publishing records with compiled and versioned releases.

OCDS data must follow the I-JSON (Internet JSON) specification in [RFC7493](https://tools.ietf.org/html/rfc7493), according to which JSON text must be encoded using [UTF-8](https://en.wikipedia.org/wiki/UTF-8), and which introduces a number of requirements for numbers, objects and dates.

```{eval-rst}
.. toctree::
   :hidden:

   reference
   release
   release_package
   records_reference
   record_package
   merging
   identifiers
   codelists
   conformance_and_extensions
```
