# Extensions

This directory holds proposed and accepted extensions to the standard. Eventually 
accepted extensions may make it into the core standard as part of the governance process.

## Proposed Extensions

A proposed extension is a directory with the prefix proposed_ contains:
* README.md - information about the extension including use cases, existing uses etc.
* schema.json - the schema for the extension in [jsonpatch](http://jsonpatch.com) format
* codelists - a directory that contains any relevant codelists, that would be added to the main schema/codelists directory on acceptance

As proposed extensions are being worked on there may be competing extensions that satisfy different use cases.

In this case, the format is as follows:
* README.md - identifies the separate use cases
* schema_usecase_1.json - a proposed extension that satisfies use case 1
* schema_usecase_2.json - a proposed extension that satisfies use case 2
* codelists

The schema suffixes that describe the use case can be more expressive than _1 _2
e.g. schema_usecase_deliveryOfItems.json

## Extensions
Accepted extensions have the proposed_ prefix removed from them and should be used
if they satisfy a publishers requirements as per the [conformance](http://ocds.open-contracting.org/standard/r/1__0__RC/en/key_concepts/conformance/)
section of the standard.
