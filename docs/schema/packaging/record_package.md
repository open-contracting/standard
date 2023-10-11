# Record Package Schema

The record package schema describes the structure of the container for publishing records. The package contains important metadata.

````{admonition} Example
:class: hint

```{jsoninclude} ../../examples/merging/updates/versioned.json
:jsonpointer:
:title: Record package
```
````

For this version of OCDS, the canonical URL for the record package schema is <https://standard.open-contracting.org/schema/1__1__5/record-package-schema.json> and for the versioned release schema is <https://standard.open-contracting.org/schema/1__1__5/versioned-release-validation-schema.json>. Using the canonical URL guarantees that your software, documentation or other resources will always refer to the specific version of the schema with which they were authored and tested.

In addition to publishing the structured metadata described by the record package schema, you ought to license your data and provide guidance for data users. For more information, see the [licensing guidance](../../guidance/publish.md#license-your-data) and [publication policy guidance](../../guidance/publish.md#finalize-your-publication-policy).

```{admonition} Browsing the schema
:class: note

This page presents the record package schema in an interactive browser and in a table, with additional information in paragraphs. You can also download the canonical version of the record package schema as [JSON Schema](../../../build/current_lang/record-package-schema.json).
```

## Schema browser

Click on schema elements to expand the tree, or use the '+' icon to expand all elements. Use { } to view the underlying schema for any section. Required fields are indicated in **bold**. [Deprecated fields](../../governance/deprecation) and [multilingual fields](../reference.md#language) are omitted.

<script src="../../../_static/docson/public/js/widget.js" data-schema="../../../../record-package-schema.json"></script>

## Reference table

```{jsonschema} ../../../build/current_lang/record-package-schema.json
:collapse: records
```
