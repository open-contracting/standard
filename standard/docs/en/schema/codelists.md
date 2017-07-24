# Codelists

The Open Contracting Data Standard schema references a number of codelists in order to enable the interoperability of data. There are two kinds of codelist, **open** and **closed**.

An **open codelist** provides **suggested codes**, but publishers can extend these lists with new codes on the basis of consensus with other publishers, or by using a codes prefixed with 'x\_' to indicate that it is a local 'eXtensions' to the codelist. 

For example, OCDS provide a list of the types of documents which may be attached to tenders, awards, contracts and milestones. However, a group of publishers may discover they have need to identify another kind of document. These publishers would not need to wait for a future version of the standard to agree upon and add a new code to an open codelist, although they should consult with the community through the [mailing list and GitHub platform](../../../support/), and should suggest the code for formal incorporation into the codelists.

A **closed codelist** provides **mandatory codes** and publishers should only use values provided in the official list. Changes to closed codelists should take place through the governance and revision process for the schema. 

Codes are case sensitive, and are generally provided as English language camelCase. Codes values should not be translated, through the OCDS team will work with publishers to provide alternative translations of code titles and definitions.

## Open Codelists

### Party Role

The organizations, economic operators or other participants in a contracting process are listed in the [parties section](../../reference/#parties). A single party may have one or more roles in the contracting process. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/partyRole.csv
```


### Item Classification Scheme

Items should be classified using existing gazetteers and codelists, such as the [EC Common Procurement Vocabulary (CPV)](http://simap.europa.eu/codes-and-nomenclatures/codes-cpv/codes-cpv_en.htm). Open codelists are strongly preferred. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/itemClassificationScheme.csv
```

This is an open codelist, and new values may be suggested outside of the main revision process for the standard, or local codes (prefixed by x\_) added by a publisher. Publishers should include details of any additional codes they use, and their definitions in their [publication policy](../implementation/publication_policy.md). 

### Unit Classification Scheme

Item quantities may be provided using an established codelist for units of measurement. Codelists may provide human-readable descriptions of units, or symbols for use in input and display interfaces.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/unitClassificationScheme.csv
```

### Organization Identifier Scheme

The Organization Identifier Scheme currently uses the codes from the International Aid Transparency Initiative ['Organisation Registration Agency' codelist](http://iatistandard.org/codelists/OrganisationRegistrationAgency/). See the identifiers section for [more information on organization identifiers](../../identifiers/#organization-identifiers)


```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/organizationIdentifierRegistrationAgency_iati.csv
```

This list can be extended in consultation with IATI. 

### Document Type

The following list describes documents and documentation recommended for publication as part of an open contracting implementation. The codelist indicates whether documents are considered 'basic', 'intermediate' or 'advanced', and the section of an OCDS release they are most likely to be applicable within. 

The code descriptions are necessarily broad, to cover their usage in a range of contracting processes, including for goods, works and services, and in other contexts, such as public private partnerships, infrastructure or concession contracts. 

Implementers may wish to map their existing document codes to this list, or, if using this list within a user-interface, to re-write the codelist titles and descriptions appropriately for the context they are being used in. 

This is an open codelist, and additional entries can be included with a x\_ prefix. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 10 10 10 20 50
   :file: ../../../schema/codelists_translated/documentType.csv
```

### Award Criteria

The award criteria codelist describes the basis on which contract awards will be made. 

```eval_rst
.. note:: 

  This codelist was revised in OCDS 1.1, deprecating earlier codes and introducing a new set of codelist entries. Publishes may need to review the mapping from their internal systems to this updated list of award criteria.

```

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 50 10
   :file: ../../../schema/codelists_translated/awardCriteria.csv
```

This is an open codelist, and new values may be suggested outside of the main revision process for the standard, or local codes (prefixed by x\_) added by a publisher. Publishers should include details of any additional codes they use, and their definitions in their [publication policy](../implementation/publication_policy.md). 

### Submission Method

The submission method codelist is used to identify the mechanism through which a submission may be made. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/submissionMethod.csv
```

This is an open codelist, and new values may be suggested outside of the main revision process for the standard, or local codes (prefixed by x\_) added by a publisher. Publishers should include details of any additional codes they use, and their definitions in their [publication policy](../implementation/publication_policy.md). 

### Related Process

The related process block is used at the release level to point backwards to prior processes, such as planning, PQQ or framework establishment, and at the contract level to point onward to sub-contracts, renewal or replacement processes. The related process codelist determines the kind of relationship that is being described.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/relatedProcess.csv
```

### Related Process Scheme

The related process scheme describes the kind of identifier used to cross-reference another process. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/relatedProcessScheme.csv
```


### Milestone Type

The milestone block can be used to represent a wide variety of events in the lifetime of a contracting process. The milestone type codelist is used to indicate the nature of each milestone.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/milestoneType.csv
```

### Extended Procurement Category

The extended procurement category codelist is used to provide additional detail about the focus of a contracting process. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/extendedProcurementCategory.csv
```


## Closed Codelists 

### Release Tag

A contracting process may result in a number of releases of information over time. These should be tagged to indicate the stage of the contracting process they relate to. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/releaseTag.csv
```

### Initiation Type

Contracting processes may be formed under a number of different processes. Currently, only 'tender' is supported in this codelist. Future versions of the standard may support other Initiation Types. The initiation type may be provide information to consuming applications on the different blocks of data and releases they should expect from a contracting process.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/initiationType.csv
```

### Tender Status

The `tender.status` field is used to indicate the current status of a tender process. The following options are available:

```eval_rst
.. csv-table-no-translate:: 
   :header-rows: 1
   :file: ../../../schema/codelists_translated/tenderStatus.csv
```

```eval_rst
.. note:: 
   The 'planning' status was introduced in version 1.1.
```

### Method

A contracting process aims to fulfill the requirements identified at the planning stage. The procurement method is the procedure used to purchase the relevant works, goods or services. The method codelist draws upon [the definitions of open, selective and limited provided by the WTO Government Procurement Agreement](http://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm), and adds an additional 'direct' code for awards without competition.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/method.csv
```

Note: The 'direct' code was introduced in Version 1.1. Publishers who completed a codelist mapping prior to 1.1 may have included direct procurement within limited, and may need to review their mappings.

### Procurement Category

The procurement category codelist is used to indicate the **primary** focus of a contracting process. Where a contracting process covers more than one of the options below, publishers can use the ```additionalProcurementCategories``` field with an array of entries from the open [extendedProcurementCategory](#extended-procurement-category) codelist.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/procurementCategory.csv
```

### Award Status

An award move through multiple states. Releases over time may update the status of an award. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/awardStatus.csv
```

The ```awardStatus``` field and codelist is used to indicate when a tender did not result in an award (through the ```"awardStatus":"unsuccessful"``` value)

### Contract Status

Contracts can move through multiple states. Releases over time may update the status of a contract.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/contractStatus.csv
```

### Currency

The currency for each amount should always be specified using the uppercase 3-letter currency code from [ISO4217](http://www.iso.org/iso/home/standards/currency_codes.htm).

A full list is available from the ISO. 

### Milestone Status

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/milestoneStatus.csv
```
