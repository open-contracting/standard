# Conformance and extensions

To maximize the interoperability of data published using the Open Contracting Data Standard we have set out key principles for **conforming** to the standard. These also create space for **extensions** of the standard to respond to particular publisher or user needs.

## Conformance

### Publication conformance

1. A conforming implementation *must* respect the normative statements in the [reference section](index) of this specification's documentation, in its JSON Schema files, and in its CSV codelist files. Normative statements are expressions containing [RFC 2119 keywords](https://datatracker.ietf.org/doc/html/rfc2119) in lowercase.
1. It *may* use only a subset of this specification's terms.
1. It *must not* use terms from outside this specification's terms where this specification's terms would suffice.
1. Its usage of this specification's terms *must* be consistent with the semantics of those terms.
1. It *may* use terms from outside this specification's terms where this specification's terms are insufficient.
1. If an implementation serializes to JSON, its serializations *must* [validate](https://review.standard.open-contracting.org/) against this specification's JSON Schema.

Whenever using terms from outside the OCDS standard, we encourage the publisher or user responsible to consult with the community on the best approach to adopt.

(Our publication conformance section is [based on the Popolo Project](https://www.popoloproject.com/specs/#conformance) approach.)

## Extensions

If you have additional fields which cannot be mapped to the OCDS schema or an existing extension, you should include these in your OCDS data and [create a new extension](../guidance/map/extensions) to document their structure and meaning. Extensions ought to be documented and shared so that other publishers and users can draw upon them, and so that extensions can be considered for inclusion in a future version of the standard. The [Extension Explorer](../guidance/map/extensions) publishes details of known extensions.

Extensions to the standard may add new objects and fields to accommodate specific local requirements. An extension must not be created if it is possible to use existing terms from the standard. It must be possible to access an extension's schema and codelist files by replacing `extension.json` in the extension's URL with a file's path, e.g. `release-schema.json` or `codelists/codelist.csv`. For more information, refer to the Extension Explorer's [guidance on documenting extensions](https://extensions.open-contracting.org/en/publishers/#document).

The schema for the standard by default allows for new fields, and does not fail validation of a file which contains unknown fields.

Conformant extensions should respect the following guidelines:

### Core fields

* Extensions *should not* delete fields from the core schema
* Extensions *should not* change the properties of fields from the core schema. If an extension desires to document further usage of a core standard field, it should do so through documentation, rather than changing the field's `description` property.

### Structure

* All definitions and properties *must* set a `title`, `description` and `type`, unless they are originally defined in the core schema or in another extension in which case they *must* set a `$ref` to the existing object
* If a field's `type` is "array", `items` *must* be set
* If using `items`, its `type` *must* only include "array", "number" and/or "string"
* If an array field's `wholeListMerge` and `omitWhenMerged` properties are not used or are set to `false`, the object fields under it *must* have an `id` field and this `id` field *must* be required

### Codelists

* If `openCodelist` is `true`, `enum` *must not* be set
* If `openCodelist` is `false`, `enum` *must* be set
* If a field has an `enum`, this *must* be expressed as a csv codelist
* If a field has an `enum`, `codelist` and `openCodelist` *must* be set
* If adding codes to an existing codelist the codelist filename *must* append `+` to the start of the core codelist filename, for example `+documentType.csv`

### Field and code names

* Definition names *must* be UpperCamelCase
* Field names *must* be lowerCamelCase
* Definition and field names *must* contain only ASCII alphabetical letters
* If an acronym is used within a field or definition name, the acronym *should* be all UPPERCASE, unless it is at the beginning of the name, in which case it *should* be all lowercase.
