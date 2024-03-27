# Reference

The Open Contracting Data Standard is maintained using JSON Schema. 

In this section you will find the schemas for [releases](release) and [records](record) along with the schemas for [packaging](packaging/index.md), which act as envelopes for releases and records.

The [release schema reference](reference) provides guidance on using each of the [sections](reference.md#release-structure) and [subschemas](reference.md#subschema-reference) in the schema, and the [record schema reference](records_reference) provides additional information on publishing records with compiled and versioned releases.

OCDS data must follow the I-JSON (Internet JSON) specification in [RFC7493](https://tools.ietf.org/html/rfc7493), according to which JSON text must be encoded using [UTF-8](https://en.wikipedia.org/wiki/UTF-8), and which introduces a number of requirements for numbers, objects and dates.

```{toctree}
:hidden:

reference
release
records_reference
record
packaging/index
merging
identifiers
codelists
conformance_and_extensions
```
