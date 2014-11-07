[TOC]

# Codelists

<span class="lead">The Open Contracting Data Standard schema references a number of codelists in order to enable the interoperability of data. There are to kinds of codelist, **open** and **closed**</span>

* An open codelist provides **suggested codes**, but publishers can extend these lists with new codes on the basis of consensus with other publishers, or by using a codes prefixed with 'x\_' to indicate that it is a local 'eXtensions' to the codelist. 

<span class="well">For example, OCDS provide a list of the types of documents which may be attached to tenders, awards, contracts and milestones. However, a group of publishers may discover they have need to identify another kind of document. These publishers would not need to wait for a future version of the standard to agree upon and add a new code to an open codelist, although they should consult with the community through the [mailing list and GitHub platform](../../standard/support), and should suggest the code for formal incorporation into the codelists.</span>

* A closed codelist provides **mandatory codes** and publishers should only use values provided in the official list. Changes to closed codelists should take place through the governance and revision process for the schema. 

Codes are case sensitive, and are generally provided as english language camelCase. Codes values should not be translated, through the OCDS team will work with publishers to provide alternative translations of code titles and definitions.

## Open Codelists

### Award Criteria

The award criteria code list describes the basis on which contract awards will be made. 

<div class="include-csv" data-src="standard/schema/codelists/awardCriteria.csv" data-table-class="table table-striped schema-table"></div>

This is an open codelist, and new values may be suggested outside of the main revision process for the standard, or local codes (prefixed by x\_) added by a publisher. Publishers should include details of any additional codes they use, and their definitions in their [publication policy](../../implementation/publication_patterns#publication_guidance). 

## Closed Codelists 

### Award Status

An award move through multiple states. Releases over time may update the status of an award. The ```awardStatus``` field is also used to indicate when a tender did not result in an award (through the ```"awardStatus":"unsuccessful"`)

<div class="include-csv" data-src="standard/schema/codelists/awardStatus.csv" data-table-class="table table-striped schema-table"></div>