# Codelists

The Open Contracting Data Standard schema references a number of codelists in order to enable the interoperability of data. There are two kinds of codelist, **open** and **closed**.

An **open codelist** provides **suggested codes**, but publishers can extend these lists with new codes on the basis of consensus with other publishers, or by using a codes prefixed with 'x\_' to indicate that it is a local 'eXtensions' to the codelist. 

For example, OCDS provide a list of the types of documents which may be attached to tenders, awards, contracts and milestones. However, a group of publishers may discover they have need to identify another kind of document. These publishers would not need to wait for a future version of the standard to agree upon and add a new code to an open codelist, although they should consult with the community through the [mailing list and GitHub platform](../../../support/), and should suggest the code for formal incorporation into the codelists.

A **closed codelist** provides **mandatory codes** and publishers should only use values provided in the official list. Changes to closed codelists should take place through the governance and revision process for the schema. 

Codes are case sensitive, and are generally provided as english language camelCase. Codes values should not be translated, through the OCDS team will work with publishers to provide alternative translations of code titles and definitions.

## Open Codelists

### Item Classification Scheme

Items should be classified using existing gazetteers and codelists, such as the [EC Common Procurement Vocabulary (CPV)](http://simap.europa.eu/codes-and-nomenclatures/codes-cpv/codes-cpv_en.htm). Open codelists are strongly preferred. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/itemClassificationScheme.csv
```

This is an open codelist, and new values may be suggested outside of the main revision process for the standard, or local codes (prefixed by x\_) added by a publisher. Publishers should include details of any additional codes they use, and their definitions in their [publication policy](../implementation/publication_policy.md). 

### Organization Identifier Scheme

The Organization Identifier Scheme currently uses the codes from the International Aid Transparency Initiative ['Organisation Registration Agency' codelist](http://iatistandard.org/codelists/OrganisationRegistrationAgency/). See the identifiers section for [more information on organization identifiers](../../identifiers/#organization-identifiers)


```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/organizationIdentifierRegistrationAgency_iati.csv
```

This list can be extended in consultation with IATI. 

### Document Type

The following list describes documents and documentation recommended for publication as part of an open contracting implementation. The codelist indicates whether documents are considered 'basic', 'intermediate' or 'advanced', and the section of an OCDS release they are most likely to be applicable within. 

The code descriptions are neccessarily broad, to cover their usage in a range of contracting processes, including for goods, works and services, and in other contexts, such as public private partnerships, infrastructure or concession contracts. 

Implementers may wish to map their existing document codes to this list, or, if using this list within a user-interface, to re-write the codelist titles and descriptions apporiately for the context they are being used in. 

This is an open codelist, and additional entries can be included with a x\_ prefix. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 10 10 10 20 50
   :file: standard/schema/codelists_translated/documentType.csv
```

### Award Criteria

The award criteria code list describes the basis on which contract awards will be made. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/awardCriteria.csv
```

This is an open codelist, and new values may be suggested outside of the main revision process for the standard, or local codes (prefixed by x\_) added by a publisher. Publishers should include details of any additional codes they use, and their definitions in their [publication policy](../implementation/publication_policy.md). 

### Submission Method

The submission method codelist is used to identify the mechanism through which a submission may be made. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/submissionMethod.csv
```

This is an open codelist, and new values may be suggested outside of the main revision process for the standard, or local codes (prefixed by x\_) added by a publisher. Publishers should include details of any additional codes they use, and their definitions in their [publication policy](../implementation/publication_policy.md). 

## Closed Codelists 

### Release Tag

A contracting process may result in a number of releases of information over time. These should be tagged to indicate the stage of the contracting process they relate to. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/releaseTag.csv
```

### Initiation Type

Contracting processes may be formed under a number of different processes. Currently, only 'tender' is supported in this codelist. Future versions of the standard may support other Initiation Types. The initiation type may be provide information to consuming applications on the different blocks of data and releases they should expect from a contracting process.

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/initiationType.csv
```

### Tender Status

The `tender.status` field is used to indicate the current status of a tender process. The following options are available:

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/tenderStatus.csv
```

### Method

The method codelist is based upon the [GPA Definitions provided here](http://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm).

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/method.csv
```

### Award Status

An award move through multiple states. Releases over time may update the status of an award. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/awardStatus.csv
```

The ```awardStatus``` field and code-list is used to indicate when a tender did not result in an award (through the ```"awardStatus":"unsuccessful"``` value)

### Contract Status

Contracts can move through multiple states. Releases over time may update the status of a contract.

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/contractStatus.csv
```

### Currency

The currency for each amount should always be specified using the uppercase 3-letter currency code from [ISO4217](http://www.iso.org/iso/home/standards/currency_codes.htm).

A full list is available from the ISO. 

### Milestone Status

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/schema/codelists_translated/milestoneStatus.csv
```
