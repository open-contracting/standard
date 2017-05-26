

# Conformance and extensions

<span class="lead">To maximise the interoperability of data published using the Open Contracting Data Standard we have set out key principles for **conforming** to the standard. These also create space for **extensions** of the standard where particular publisher or user needs require.</span>

## Conformance 

### Publication conformance

1. A conforming implementation *may* use only a subset of this specification's terms.
1. It *must not* use terms from outside this specification's terms where this specification's terms would suffice.
1. Its usage of this specification's terms *must* be consistent with the semantics of those terms.
1. It *may* use terms from outside this specification's terms where this specification's terms are insufficient.
1. If an implementation serializes to JSON, its serializations *must* [validate](http://ocds.open-contracting.org/validator/) against this specification's JSON Schema.

Whenever using terms from outside the OCDS standard, we encourage the publisher or user responsible to consult with the community on the best approach to adopt. 

(Our publication conformance section is [based on the Popolo Project](http://www.popoloproject.com/specs/#conformance) approach.)

### Validator and application conformance

As of version 1.1, release/record packages should contain a version property explicitly declaring their version. All packages without an explicit version declared should be validated against the version 1.0 schema unless othewise instructed by the user.  

Validators and applications should:

* Report to the user when it encounters a version of the data it does not support;

* Reject data from a higher integer version than it supports, unless otherwise instructed by the user; 

* Report to the user when it encounters extensions it does not support;

Validators **must** report a warning to the user when they encounter properties not covered by the version of the schema and extensions that they are validating against. 

Applications **may** report a warning to use the user when they encounter properties they do not support, or **may** discard these properties.

The handling of additional properties and deprecated properties is implementation defined.

See also the [deprecation guidance](deprecation.md). 

## Extensions

Extensions to the standard can add new objects and properties to accommodate specific local requirements. An extension should only be created where it is not possible to model the required data using existing terms from the standard.

Extensions should be documented and shared so that other publishers and users can draw upon them, and so that extensions can be considered for inclusion in a future version of the standard.

The [extensions registry](../../extensions/) records details of known extensions. 

The schema for the standard by default allows for new fields, and does not fail validation of a file which contains unknown fields. 
