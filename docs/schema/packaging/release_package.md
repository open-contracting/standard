# Release Package Schema

The release package schema describes a container for releases.

````{admonition} Example
:class: hint

```{jsoninclude} ../../examples/release_schema_reference/release_package.json
:jsonpointer:
:title: Release package
```
````

For this version of OCDS, the canonical URL of the release package schema is: <https://standard.open-contracting.org/schema/1__1__5/release-package-schema.json>. Using the canonical URL guarantees that your software, documentation or other resources will always refer to the specific version of the schema with which they were authored and tested.

In addition to publishing the metadata described by the release package schema, you ought to license your data and guide data users. For more information, see the [licensing](../../guidance/publish.md#license-your-data) and [publication policy](../../guidance/publish.md#finalize-your-publication-policy) guidance.

```{admonition} Browsing the schema
:class: note

This page presents the release package schema in an interactive browser and in a table. You can also download the canonical version of the release package schema as [JSON Schema](../../../build/current_lang/release-package-schema.json).
```

## Schema browser

Click on schema elements to expand the tree, or use the '+' icon to expand all elements. Use { } to view the underlying schema for any section. Required fields are indicated in **bold**. [Deprecated fields](../../governance/deprecation) and [multilingual fields](../reference.md#language) are omitted.

<script src="../../../_static/docson/public/js/widget.js" data-schema="../../../release-package-schema.json"></script>

## Reference table

```{jsonschema} ../../../build/current_lang/release-package-schema.json
:collapse: releases
```
