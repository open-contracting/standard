# Conformance and extensions

To maximize the interoperability of data published using the Open Contracting Data Standard we have set out key principles for **conforming** to the standard. These also create space for **extensions** of the standard to respond to particular publisher or user needs.

## Conformance 

### Publication conformance

1. A conforming implementation *may* use only a subset of this specification's terms.
1. It *must not* use terms from outside this specification's terms where this specification's terms would suffice.
1. Its usage of this specification's terms *must* be consistent with the semantics of those terms.
1. It *may* use terms from outside this specification's terms where this specification's terms are insufficient.
1. If an implementation serializes to JSON, its serializations *must* [validate](https://review.standard.open-contracting.org/) against this specification's JSON Schema.

Whenever using terms from outside the OCDS standard, we encourage the publisher or user responsible to consult with the community on the best approach to adopt. 

(Our publication conformance section is [based on the Popolo Project](https://www.popoloproject.com/specs/#conformance) approach.)

### Validator and application conformance

As of OCDS 1.1, release/record packages must include a `version` field to explicitly declare their version. All packages without an explicit version declared should be validated against the version 1.0 schema unless otherwise instructed by the user.

Validators and applications should:

* Report to the user when it encounters a version of the data it does not support;

* Reject data from a higher integer version than it supports, unless otherwise instructed by the user; 

* Report to the user when it encounters extensions it does not support;

Validators **must** report a warning to the user when they encounter fields not covered by the version of the schema and extensions that they are validating against.

Applications **may** report a warning to use the user when they encounter fields they do not support, or **may** discard these fields.

The handling of additional fields and deprecated fields is implementation defined.

For behaviours that are implementation defined, applications should clearly document their chosen approach. 

See also the [deprecation guidance](../governance/deprecation).

## Extensions

If you have additional fields which cannot be mapped to the OCDS schema or an existing extension, you should include these in your OCDS data and [create a new extension](../guidance/map/extensions) to document their structure and meaning.

Extensions to the standard can add new objects and fields to accommodate specific local requirements. An extension must not be created if it is possible to use existing terms from the standard.

Extensions ought to be documented and shared so that other publishers and users can draw upon them, and so that extensions can be considered for inclusion in a future version of the standard.

The [Extension Explorer](../guidance/map/extensions) publishes details of known extensions.

The schema for the standard by default allows for new fields, and does not fail validation of a file which contains unknown fields. 
