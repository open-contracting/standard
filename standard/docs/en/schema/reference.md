# Release Reference

The [Release Schema](release.md) provides a detailed specification of the fields and data structures to use when publishing contracting data. Supplementary schemas show how to combine releases into data packages and how to compile releases into records. 

**Note: If any conflicts are found between this text, and the text within the schema, the schema takes precedence**

## Release structure

The majority of OCDS data is held within a release structure. One or more releases can be published within a release package. Releases are made up of a number of sections, arranged in the following structure.

* [package](#package-metadata)
  * [release](#release)
    * [parties](#parties) 
    * [planning](#planning)
    * [tender](#tender) 
    * [award](#award)
    * [contract](#contract)
      * [implementation](#implementation)

Releases are given a [tag](../../codelists/#release-tag) to indicate the specific stage of a contracting process they represent. However, there are no formal restrictions on when information about a stage of the contracting process may be provided. 

For example, a publisher announcing the signing of a contract with a 'contract' tag, may also include information in the award and tender blocks in order to provide a comprehensive picture of the contracting process to date which led to that contract being signed. 

### Package Metadata

Releases must be published within a [release package](release_package.md). The release package provides meta-data about the release(s) that it contains. 

```eval_rst

.. jsonschema:: ../../../schema/release-package-schema.json
    :include: 
    :collapse: releases,publisher

```

See the [licensing guidance](../implementation/licensing.md) for more details on selecting a license, and publishing license information. 

See the [publication policy](../implementation/publication_policy.md) guidance for more details on what to include in a publication policy.

### Release

All new information about a contracting process is described within a release. 

```eval_rst

.. jsonschema:: ../../../schema/release-schema.json
    :include: 
    :collapse: planning,tender,award,contract,parties,buyer,relatedProcess

```

```eval_rst
.. extensionlist:: The following extensions are available for release
   :list: release
```

### Parties

Each of the parties (organizations or other participants) referenced in a release must be included in the parties section. 

```eval_rst
.. note:: 

   Version 1.1 of OCDS introduces a new approach to describing the buyers,  suppliers, economic operators, and other participants in a contracting process. Instead of embedding organization information at various points within an OCDS release, information on all the parties involved in a contracting process is collected together in a top-level section, and the parties indicated by a cross-reference to their id at other points. 

   This reduces repetition of information on parties who appear at multiple points in the contracting process, and supports publication of information about additional parties to the contracting process, including auditors, multiple buyers, and consortia partners of a winning bidder.

   The old, embedded data, approach to organization data is deprecated in OCDS 1.1, and will be removed in version 2.0. 

```

The following details can be provided for each party.

```eval_rst

.. jsonschema:: ../../../schema/release-schema.json
    :include: parties
    :collapse: parties/identifier,parties/additionalIdentifiers,parties/address,parties/contactPoint

```

Detailed classification of parties can be provided using one or more [party detail extensions](../../../extensions/party_details/).

```eval_rst
.. extensionlist:: The following extensions are available for parties
   :list: parties
```

### Planning

The planning section can be used to describe the background to a contracting process. This may include details of the budget from which funds are drawn, or related projects for this contracting process. Background documents such as a needs assessment, feasibility study and project plan can also be included in this section.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-planning.csv
```   

```eval_rst
.. extensionlist:: The following extensions are available for planning
   :list: planning
```

Apart from documents, the majority of information is held within the budget block. This is designed to allow both machine-readable linkable data about budgets, cross-referencing to data held in other standards such as the [Fiscal Data Package](http://fiscal.dataprotocols.org/) or [International Aid Transparency Initiative Standard](http://www.iatistandard.org), and human readable description of the related budgets and projects, supporting users to understand the relationship of the contracting process to existing projects and budgets even where linked data is not available.

#### Budget 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-budget.csv
```

```eval_rst
.. extensionlist:: The following extensions are available for budget
   :list: budget
```

### Tender

The tender section includes details of the announcement that an organization intends to source some particular goods, works or services, and to establish one or more contract(s) for these.

It may contain details of a forthcoming process to receive and evaluate proposals to supply these goods and services, and may also be used to record details of a completed tender process, including details of bids received. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-tender.csv
```

```eval_rst
.. extensionlist:: The following extensions are available for the tender section
   :list: tender
```

Notes: 

* ```tender.id``` - see the [identifiers guidance](../../identifiers/#tender_award_and_contract) for further information on the tender identifier. In most cases this can be the same as the ocid.
* ```procuringEntity``` - in some cases the organization managing the procurement process may be different from the organization whose budget is being used for the procurement (the 'buyer' in OCDS terminology). If this is the case, then the details of this procuring organization should be provided here. 
* ```title``` and ```description``` - tender title and description are optional. The details of items to be procured should always be provided in ```items```. Descriptions should not be used in place of providing structured data on items, dates and other details. Instead, title and description should be used to provide a brief overview of the tender. Publishers should consider adopting a 'tweet length' title, and should avoid ALL UPPERCASE titles, or titles containing code words or other artefacts from internal databases. The goal of these fields is to give users a clear idea of the nature of a tender. 
* ```items``` - publishers should provide details of each of the items to be procured under this tender. 
* ```milestones``` - publishers should list any relevant [milestones](#milestone) associated with the delivery of the goods and services covered by this tender. These are the milestones against which the whole contracting process will be evaluated. Publishers may include information about key milestones during the tender process itself, but should not use this in place of ```tenderPeriod```, ```enquiryPeriod``` or ```awardPeriod```.
* ```value``` and ```minValue``` - the total upper estimated value of a procurement should be given in ```value```. For publishers who also specify a estimate minimum value, this can be placed in ```minValue```.
*  ```procurementMethod``` and ```procurementMethodRationale```. Tendering processes can use a variety of methods. Publishers should map their methods to one of the approved codes according to the [GPA definitions](http://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) of open, selective or limited. A free text explanation of why a given method was appropriate to this tender can be provided in ```procurementMethodRationale```. 
* ```awardCriteria``` and ```awardCriteriaDetails``` - The [award criteria code list](../../codelists/#award-criteria) describes the basis on which contract awards will be made. This is an open codelist, and so may be extended with new codes. Free text describing the basis on which bids will be judged, and made, can be provided in the ```awardCriteriaDetail``` field. Publishers wishing to provide more structured information about selection, shortlisting and award criteria should propose [extensions](conformance_and_extensions.md) for this. 
* ```documents``` - supporting documentation should be attached to the tender. This may include official legal notices of tender, as well as technical specifications, evaluation criteria, and, as a tender process progresses, clarifications, replies to queries and copies of bids submitted or listings of shortlisted firms. See the [attachments](#attachments) section for more details of how to include documents, and consult the [documentType codelist](codelists.md/#document-type) for suggested documents to include for basic, intermediate or advanced publication.

Information on bidders against a contract will be handled by an [extension](conformance_and_extensions.md) during the period of the standard release candidate. Publishers wishing to provide detailed information on bidders should [contact support](../support/index.md).


### Bids

```eval_rst
.. extensionlist:: The optional bids extension can be used to provide summary and detailed information about bids.
   :list: bids
```

### Award

The award section is used to announce any awards issued for this tender. There may be multiple awards made. Releases can contain all, or a subset, of these awards. A related award block is required for every contract, as it contains information on the suppliers. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-award.csv
```

```eval_rst
.. extensionlist:: The following extensions are available for award
   :list: award
```

### Contract

The contract section is used to provide details of contracts that have been entered into. Every contract needs to have a related award, linked via the ```awardID``` property. This is because supplier information is contained within the 'award'. The framework contract details below help illustrate the reasons for this. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-contract.csv
```

```eval_rst
.. extensionlist:: The following extensions are available for contracts
   :list: contract
```

#### Framework contracts

A framework is an agreement with suppliers to establish terms governing contracts that may be awarded during the life of the agreement[*](http://www.constructingexcellence.org.uk/tools/frameworkingtoolkit/whatis.jsp). 

Framework **agreements** can be represented by [awards](#award), which would each detail a supplier participating in the framework, the line items that the agreement covers with this supplier, and any maximum value for the agreement over time.  

Each call-off purchase against a framework agreement would result in a [contract](#contract), related to the framework agreement [award](#award) via ```awardID```. 

As a result, [award](#award) and [contract](#contract) each contain an [items](#items) block, allowing the award to describe the possible goods and services that can be supplied, whilst the contract describes those that are to be supplied in any particular instance. 


### Implementation

Implementation information can be updated over the course of a contract. It belongs nested within the contract it relates to. Implementation blocks include the following elements:

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-implementation.csv
```

```eval_rst
.. extensionlist:: The following extensions are available for implementation
   :list: implementation
```

Information on subcontracts is not currently included in the release candidate schema, but may be handled by [proposed extensions](conformance_and_extensions.md)

#### Transaction

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-transaction.csv
```

The transaction block is modelled on the [International Aid Transparency Initiative (IATI) transaction element](http://iatistandard.org/activity-standard/iati-activities/iati-activity/transaction/), and can be used to represent actual flows of money between organisations in relation to this contract. As with the [budget](#budget) block, this may be used to cross-reference to a third party ```source``` of data, and can re-use identifiers from that source. 

In most circumstances, the ```providerOrganization``` identifier should match that of the ```buyer```, and the ```recieverOrganization``` identifier should match that of the ```supplier```. 

#### Milestones

See [milestone](#milestone) reference below.

The implementation milestones should be updated to reflect when they are met. 

#### Documents

Documents related to contract implementation should be stored here. This may include subcontracts.

See [document](#document) reference below. 

### Amendment

A release may amend properties from a previous release. Whilst the release & record model of OCDS offers the opportunity to keep a full versioned history of changes, in many cases it is important for changes to a tender, award or contract to be explicitly declared. 

The amendment array in a tender, award or contract block provides the ability to detail the amendments that have taken place with dates, rationale and free-text descriptions of the change, as well as to point to the releases that contain information from before and after the amendment.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-amendment.csv
```

#### Changes

The changes array was deprecated in OCDS 1.1. Structured information on the former value of specific fields should be provided by:

* Including releases from **before** and **after** a change within a release package;
* Using the amendment array in tender, contract or award to explicitly relate these releases to an amendment.

## Field reference

### OrganizationReference

```eval_rst
.. note::

The approach to including organizations information has changed in OCDS 1.1. Instead of embedding all the details of an organization, publishers should use an organization reference to indicate the entry in the parties section that contains full details of this organization.

```

An organization reference consists of two main components:

* An ```id``` used to cross-reference the entry in the [parties](#parties) section that contains full information on this organization or entity;
* A ```name``` field that repeats the name given in the [parties](#parties) section, provided for the convenience of users viewing the data, and to support detection of mistakes in cross-referencing. 

The Organization Reference schema contains deprecated fields to prevent validation failures of OCDS 1.0 data. 

### Organization

See the [parties](#parties) section


#### Identifier

The identifier block provides a way to [identify the legal entities](../../identifiers/#organizations) involved in a contracting process. If a Contracting Process represents a contract arranged by the department or branch of a larger organization, the legal entity (usually the registered organization) should be described in the [identifier](#identifier) section, with details of the branch or department given in the name, [address](#address) and [contact point](#contactpoint) as relevant. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-identifier.csv
```

#### Address
```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-address.csv
```

#### ContactPoint

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-contact-point.csv
```

### Document

Documents may be attached at a number of points within the standard: to planning, tenders, awards, contracts and implementation Each document block can consist of multiple documents, classified using the [documentType](../../codelists/#document-type) codelist.

The document block is also used to link to legal notices, which should have a documentType of 'notice'.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-document.csv
```

```eval_rst
.. extensionlist:: The following extensions are available for document
   :list: document
```

### Date

OCDS makes use of [ISO8601](http://en.wikipedia.org/wiki/ISO_8601) date-times, following [RFC3339 §5.6](http://tools.ietf.org/html/rfc3339#section-5.6).

A time and timezone/offset MUST always be provided in a date-time.

The following are valid date-times:

* '2014-10-21T09:30:00Z' - 9:30 am on the 21st October 2014, UTC
* '2014-11-18T18:00:00-06:00' - 6pm on 18th November 2014 CST (Central Standard Time)

The following are not valid:

* '2014-10-21' - Missing time portion
* '2014-10-21T18:00' - missing seconds in time portion.
* '2014-11-18T18:00:00' - Missing timezone/offset portion
* '11/18/2014 18:00' - Not following the pattern at all!

Accurately including the time and timezone offsets is particular important for tender deadlines and other dates which may have legal significance, and where users of the data may be from different timezones. The character Z on the end of a date-time indicates the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) (or Zero offset) timezone, whereas other timezones are indicated by their value '+/-hh:mm' UTC on the end of the date-time value. 

In the event that the system from which data is drawn only includes dates, and does not include time information, publishers should consider sensible defaults for each field. For example, the startDate time of a clarification period may be set to '00:00:00Z' to indicate that clarifications can be requested from any time on the date stated, with the endDate time set to 23:59:59Z to indicate that clarifications can be sent up until the end of the endDate given. Alternatively, if clarification requests are only accepted in standard office hours, these values might be 09:00:00Z and 17:00:00Z respectively.

In the event that a date field is not bound to a specific time at all, publishers should choose a default time value of '23:59:59' and either 'Z' (for UTC) or the timezone of the publisher, indicating that the time refers to the end of the given date. 

#### Period

A period has a start date, end date, and/or duration. Start and end dates are represented using date-times. Durations are represented as a number of days. 

Periods may also include a ```maxExtentDate``` which indicates the latest possible end date of this period, or the latest date up until which the period could be extended without an amendment.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-period.csv
```

```eval_rst
.. extensionlist:: The following extensions are available for period
   :list: period
```

### Item

The items block is used to list the line-items associated with a tender, award or contract. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-item.csv
```

```eval_rst
.. extensionlist:: These are extensions related to Items.
   :list: item
```



Notes: 

* The [proposed location extension](../extensions/location.md) can be attached to items, allowing the point of delivery for a given item or the site of works to be completed to be indicated in both the tender, award and contract stage.
* Items should be classified according to an established scheme of codes. A single primary ```classification``` can be given, although an array of ```additionalClassification``` can be provided.

#### Classification

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-classification.csv
```

#### Unit

The ```unit``` block allows detailed specification of the parameters and price of units that make up a line-item. Although no code list for units has been established in the current release of the standard, publishers may consider using the Units provided by the [Quantities, Units, Dimensions and Data Types Ontologies](http://www.qudt.org/qudt/owl/1.0.0/unit/) in the ```unit.name``` field (drawing on the CamelCase unit names, such as SquareMile), in order to provide detailed information the cost per unit of a line-item. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-item-unit.csv
```

### Milestone

Milestone information can be included in the [planning](#planning), [tender](#tender), [contract](#contract) and [contract implementation](#implementation) blocks. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-milestone.csv
```

Notes:

* The ```dateModified``` field should be changed whenever the progress towards a milestone is reviewed, and the ```status``` either updated, or re-confirmed. 

```eval_rst
.. extensionlist:: The following extensions to milestone are available
   :list: milestones
```

<!-- ToDo: Add example -->

### Value

Financial values should always be published with a currency attached. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/release-value.csv
```

Support for exchange rates, and tax information, can be provided using extensions.

```eval_rst
.. extensionlist:: The following extensions for value are available
   :list: value
```

### RelatedProcess

In OCDS each contracting process can have only one planning and tender stage. There are a number of cases where it is important to know about related planning and tendering processes, including:

* When one planning process results in many tenders;
* What a contract is awarded following two or more invitation to tender processes, such as in some processes involving pre-qualification, of frameworks with mini-competitions;
* When a contract results in the award of sub-contracts also tracked through OCDS data;
* When a contract is coming up for renewal or replacement, and there is a contracting process to award  the renewal/replacement contract;

In all these cases, the ```relatedProcess``` block can be used to cross-reference between the relevant open contracting processes using their ```OCID```.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/related-process.csv
```

A related process can be declared at two points in an OCDS release.

**(1) At the release level** - used to point backwards to prior processes, such as planning, PQQ or framework establishment.

**(2) At the contract level** - used to point onwards to sub-contracts, renewal or replacement processes that relate solely to the particular contract the property appears in.  

As well as providing this machine-readable link between processes, publishers may also provide links to human-readable documentation in the relevant ```documents``` blocks. For example:

* When recording a ```release/relatedProcess``` pointing to the ocid of the planning process that resulted in a tender, a ```tender/documents``` entry with a ```documentType``` of 'procurementPlan' and a link to web pages about the procurement plan could be provided;
* When recording a ```contract/relatedProcess``` pointing to the ocid of a  sub-contracting process, a ```contract/documents``` entry with a ```documentType``` of 'subContract' and a title that describes it as the subcontracting process, could be provided;
* When recording a ```contract/relatedProcess``` pointing to the ocid of a tender process to renew a given contract, a ```contract/documents``` entry with a ```documentType``` of 'tenderNotice' and a title that describes it as the successor process, could be provided;


### Location

The addition of location information is currently handled through a [proposed extension](../extensions/location.md) to the standard.

### Publisher

The publisher block is used in release and record packages to identify the source of a dataset. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/field_definitions/publisher.csv
```

## Language

Many publishers need to be able to share key data in multiple languages. All free-text title and description fields in the Open Contracting Data Standard can be given in one or more languages.

Language variations are included by a copy of multi-lingual fields, suffixed with a language code.

E.g. ```title``` and ```title_es```

In order to allow users to identify the language used in non-suffixed fields, OCDS release and records should declare the default language in the ```language``` field. 

Languages should be identified using language tags taken from [BCP47](http://tools.ietf.org/html/bcp47). The specification allows BCP47 values in order to accommodate variations in dialect where this is important. However, publishers **should** use the two letter [ISO-639-1 two-digit language tags](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) in the vast majority of circumstances, and should not assume that the users are able to distinguish between sub-tag variations (for example, OCDS publishers should strongly prefer 'en' over 'en_US' or 'en_GB'). 

To include a language variation of a field, the field name should be suffixed with _ and the appropriate language tag. For example: ```title_es``` for Spanish.

### Worked example

A contract for ‘Software consultancy services’ may be published in a release with the default language sent to ‘en’ (the ISO-639-1 code for English). The following examples give the description of an item as English, French and Spanish.

**json**

```eval_rst

.. jsoninclude:: docs/en/examples/language.json
   :jsonpointer: 
   :expand: 

```

**csv** 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: standard/docs/en/examples/language.csv
```

## Release handling

The full OCDS data model is based on the idea of publishing a new release every time information about a contracting process changes. This way, users can gain a full view of change over time, and third-parties can  understand what needs to be updated in any system that is tracking the progress of a contracting process.

Publishers will need to choose how to generate new releases, and whether to repeat information in each release, or just to provide changes. This choice should be based on an understanding the [merging process](merging.md) that is used to generate a snapshot record of a full contracting process.

This model also requires publishers to pay careful attention to null values and missing fields. 

### Empty fields

Fields that are not being used, or that have no value, can be excluded in their entirety (key and value) from a published file. 

Only including fields which have values will keep versioned datasets cleaner. 

### Emptying fields and values

There may be cases where a publisher needs to remove, rather than update, a value which was set in a previous release. In this case, the fields should explicitly be set to null. 

The following describes how null values will be handled in the compilation of a record:

* If a field is included with a value in one release, and then set to ```null``` in a subsequent release, that field will be recorded as null in the compiled record (though past values of it should remain in the versioned section of the record).
* If a field is set to null in one release, and is also set to ```null``` in a subsequent release, it will be recorded as null as per the original release, and the record will not show any change based on the subsequent release I.e. fields that are set to null are recorded as such and then only changed if the value is set.
* If a field is set to ```null``` in one release, and then has a value in a subsequent release, it will first appear in the record, and the version section of the record as ```null``` and then with the subsequent value.
* If a field does not appear in one release, and then appears with a value in a subsequent release, it will first appear in the record, and the version section of the record, when the first release that contains it is compiled into the record.
