[TOC]


## Conformance and extensions

To maximise the interoperability of data published using the Open Contracting Data Standard we have set out key principles for **conforming** to the standard. These also create space for **extensions** of the standard where particular publisher or user needs require.

### Conformance

To maximise the interoperability of data published using the Open Contracting Data Standard we have set out key principles for **conforming** to the standard, [based on the Popolo Project](http://www.popoloproject.com/specs/#conformance) approach. 

1. A conforming implementation *may* use only a subset of this specification's terms.

2. It *must not* use terms from outside this specification's terms where this specification's terms would suffice.

3. Its usage of this specification's terms *must* be consistent with the semantics of those terms.

4. It *may* use terms from outside this specification's terms where this specification's terms are insufficient.

5. If an implementation serializes to JSON, its serializations *must* [validate](http://ocds.open-contracting.org/validator/) against this specification's JSON Schema.

Whenever using terms from outside the OCDS standard, we encourage the publisher or user responsible to consult with the community on the best approach to adopt. 

### Extensions

Extensions to the standard can add new objects and properties to accommodate specific local requirements. An extension should only be created where it is not possible to model the required data using existing terms from the standard.

Extensions should be documented and shared so that other publishers and users can draw upon them, and so that extensions can be considered for inclusion in a future version of the standard.

You can find a list of proposed extensions in the [Standard Issue Tracker](https://github.com/open-contracting/standard/issues?q=is%3Aopen+is%3Aissue+label%3AExtensions). To propose a new extension please create an issue, describing the desired fields, and, where possible, providing example JSON Schema.

The schema for the standard by default allows for new fields, and does not fail validation of a file which contains unknown fields. 
