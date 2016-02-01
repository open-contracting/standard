# Release Reference

The [Release Schema](release.md) provides a detailed specification of the fields and data structures to use when publishing contracting data. Supplementary schemas show how to combine releases into data packages and how to compile releases into records. 

This reference page provides key information on using the release schema.

**Note: If any conflicts are found between this text, and the text within the schema, the schema takes precedence**

## Release structure

The majority of OCDS data is held within a release structure. One or more releases can be published within a release package. Releases are made up of a number of sections, including:

* [planning](#planning)
* [tender](#tender)
* [award](#award)
* [contract](#contract)
* [implementation](#implementation)

A release can only contain one tender section, but may contain multiple award, contract and implementation sections. This is because each OCDS release relates to [a single contracting process](../getting_started/contracting_process.md), and we define contracting processes by their unique initiation (tender) stage.

Releases are given a [tag](#release-tag) to indicate the specific stage of a contracting process they represent. However, there are no formal restrictions on when information about a stage of the contracting process may be provided. 

For example, a publisher announcing the signing of a contract with a 'contract' tag, may also include information in the award and tender blocks in order to provide a comprehensive picture of the contracting process to date which led to that contract being signed. 

### Package Metadata

Releases must be published within a [release package](release_package.md), which can contain one or more releases. The release package, modelled on the [Data Package](http://dataprotocols.org/data-packages/) protocol, provides meta-data about the release(s) it contains, the publisher, and data licensing information. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-package.csv
```

Notes:

* The uri should uniquely identify this release package. Publishers should provide a [dereferenceable HTTP URI](http://en.wikipedia.org/wiki/Dereferenceable_Uniform_Resource_Identifier) wherever possible and should host the data package at this URI, enabling users to look-up and verify the contents of a release package from its original source. 
* The [publishedDate](#date) on which this package was published. If a package is automatically generated and re-published on a regular basis, this date should reflect the date of the last change to the contents of the package. 
* The publisher [publisher](#publisher) block provides space for an organisation name and identifier.
* ````license```` - See the [licensing guidance](../implementation/licensing.md) for more details on selecting and publishing license information. 
* ````publicationPolicy```` - See the [publication policy](../implementation/publication_policy.md) guidance for more details.

### Release

The top level of a release consists of the following fields and objects:

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-toplevel.csv
```

Notes:

* ```ocid``` - Providing each [contracting process](../getting_started/contracting_process.md) with a unique identifier is essential to enable data about contracts to be linked up across different releases. Open Contracting IDs are composed of a prefix assigned to each publisher, and a local identifier drawn from their internal systems that can be used to tie together tenders, awards, contracts and other key data points from a specific contracting process. See the [Open Contracting Identifier guidance](identifiers.md) for details of how to construct an OCID. 
* ```tag``` - The release tag is used to identify the nature of the release being made. This can be used by consuming applications to filter releases, or may in future be used for advanced validation. A release which updates or amends previous data must always use the appropriate update or amendment release tag. Values must be drawn from the [releaseTag codelist](codelists.md#release-tag).
* ```date``` - The release [date](#date) should reflect the point in time at which the information in this release was disclosed. A release package may contain release with different release dates. 
* ```language``` - see the section on [multi-language support](#language) for information on language handling.
* ```buyer``` - The buyer details are published using an [organization](#entity) block.

Further details on each of the blocks contained within release are below. 

### Planning

The planning section can be used to describe the background to a contracting process. This may include details of the budget from which funds are drawn, or related projects for this contracting process. Background documents such as a needs assessment, feasibility study and project plan can also be included in this section.

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-planning.csv
```

Apart from documents, the majority of information is held within the budget block. This is designed to allow both machine-readable linkable data about budgets, cross-referencing to data held in other standards such as the [Fiscal Data Package](http://fiscal.dataprotocols.org/) or [International Aid Transparency Initiative Standard](http://www.iatistandard.org), and human readable description of the related budgets and projects, supporting users to understand the relationship of the contracting process to existing projects and budgets even where linked data is not available.

#### Budget 
```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-budget.csv
```

### Tender

The tender section includes details of the announcement that an organization intends to source some particular goods, works or services, and to establish one or more contract(s) for these.

It may contain details of a forthcoming process to receive and evaluate proposals to supply these goods and services, and may also be used to record details of how a completed tender process, including details of bids received. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-tender.csv
```

Notes: 

* ```tender.id``` - see the [identifiers guidance](identifiers.md#tender_award_and_contract) for further information on the tender identifier. In most cases this can be the same as the ocid.
* ```procuringEntity``` - in some cases the organization managing the procurement process may be different from the organization whose budget is being used for the procurement (the 'buyer' in OCDS terminology). If this is the case, then the details of this procuring organization should be provided here. 
* ```title``` and ```description``` - tender title and description are optional. The details of items to be procured should always be provided in ```items```. Descriptions should not be used in place of providing structured data on items, dates and other details. Instead, title and description should be used to provide a brief overview of the tender. Publishers should consider adopting a 'tweet length' title, and should avoid ALL UPPERCASE titles, or titles containing code words or other artefacts from internal databases. The goal of these fields is to give users a clear idea of the nature of a tender. 
* ```items``` - publishers should provide details of each of the items to be procured under this tender. 
* ```milestones``` - publishers should list any relevant [milestones](#milestone) associated with the delivery of the goods and services covered by this tender. These are the milestones against which the whole contracting process will be evaluated. Publishers may include information about key milestones during the tender process itself, but should not use this in place of ```tenderPeriod```, ```enquiryPeriod``` or ```awardPeriod```.
* ```value``` and ```minValue``` - the total upper estimated value of a procurement should be given in ```value```. For publishers who also specify a estimate minimum value, this can be placed in ```minValue```.
*  ```procurementMethod``` and ```procurementMethodRationale```. Tendering processes can use a variety of methods. Publishers should map their methods to one of the approved codes according to the [GPA definitions](http://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) of open, selective or limited. A free text explanation of why a given method was appropriate to this tender can be provided in ```procurementMethodRationale```. 
* ```awardCriteria``` and ```awardCriteriaDetails``` - The [award criteria code list](../../codelists/#award-criteria) describes the basis on which contract awards will be made. This is an open codelist, and so may be extended with new codes. Free text describing the basis on which bids will be judged, and made, can be provided in the ```awardCriteriaDetail``` field. Publishers wishing to provide more structured information about selection, shortlisting and award criteria should propose [extensions](../implementation/conformance_and_extensions.md) for this. 
* ```documents``` - supporting documentation should be attached to the tender. This may include official legal notices of tender, as well as technical specifications, evaluation criteria, and, as a tender process progresses, clarifications, replies to queries and copies of bids submitted or listings of shortlisted firms. See the [attachments](#attachments) section for more details of how to include documents, and consult the [documentType codelist](codelists.md/#document-type) for suggested documents to include for basic, intermediate or advanced publication.

Information on bidders against a contract will be handled by an [extension](../implementation/conformance_and_extensions.md) during the period of the standard release candidate. Publishers wishing to provide detailed information on bidders should [contact support](../support/index.md).

### Award

The award section is used to announce any awards issued for this tender. There may be multiple awards made. Releases can contain all, or a subset, of these awards. A related award block is required for every contract, as it contains information on the suppliers. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-award.csv
```


### Contract

The contract section is used to provide details of contracts that have been entered into. Every contract needs to have a related award, linked via the ```awardID``` property. This is because supplier information is contained within the 'award'. The framework contract details below help illustrate the reasons for this. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-contract.csv
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
   :file: standard/docs/field_definitions/release-implementation.csv
```

Information on subcontracts is not currently included in the release candidate schema, but may be handled by [proposed extensions](../implementation/conformance_and_extensions.md)

#### Transaction

```eval_rst
.. csv-table::
   :header-rows: 1
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

The amendment block in each of tender, award and contract blocks provides the ability to explicitly declare changed fields, their former values, to provide an explanation for the change, and attach or reference relevant documentation.

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-amendment.csv
```

Amendment information should not be included in compiled records, as it is not possible to indicate __all__ the former values of a field, only the most recent known value: whereas the version history of a full record can show all previous values.

#### Changes

Within each amendment block, publishers should provide an array of items that have changed, along with their former values. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-changes.csv
```

## Field reference


### Organization

The organization block can be used to provide a legal identifier for an organization, and to give [address](#address) and [contact point](#contact-point) information.

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-organization.csv
```

#### Identifier

The identifier block provides a way to [identify the legal entities](identifiers.md#organizations) involved in a contracting process. If a Contracting Process represents a contract arranged by the department or branch of a larger organization, the legal entity (usually the registered organization) should be described in the [identifier](#identifier) section, with details of the branch or department given in the name, [address](#address) and [contact point](#contactpoint) as relevant. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-identifier.csv
```

#### Address
```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-address.csv
```

#### ContactPoint

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-contact-point.csv
```

### Document

Documents may be attached at a number of points within the standard: to planning, tenders, awards, contracts and milestones. Each document block can consist of multiple documents, classified using the [documentType](codelists.md#document-type) codelist.

The document block is also used to link to legal notices, which should have a documentType of 'notice'.

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-document.csv
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

In the event that the system from which data is drawn only includes dates, and does not include time information, publishers should consider sensible defaults for each field. For example, the startDate time of a clarification period may be set to '00:00:00Z' to indicate that clarifications can be requested from any time on the date stated, with the endDate time set to 23:23:59Z to indicate that clarifications can be sent up until the end of the endDate given. Alternatively, if clarification requests are only accepted in standard office hours, these values might be 09:00:00Z and 17:00:00Z respectively. 

In the event that a date field is not bound to a specific time at all, publishers should choose a default time value of '23:23:59' and either 'Z' (for UTC) or the timezone of the publisher, indicating that the time refers to the end of the given date. 

#### Period

A period is an object consisting of a start date and end date, represented as date-times.

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-period.csv
```

### Item

The items block is used to list the line-items associated with a tender, award or contract. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-item.csv
```

Notes: 

* The [proposed location extension](../extensions/location.md) can be attached to items, allowing the point of delivery for a given item or the site of works to be completed to be indicated in both the tender, award and contract stage.
* Items should be classified according to an established scheme of codes. A single primary ```classification``` can be given, although an array of ```additionalClassification``` can be provided.

#### Classification

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-classification.csv
```

#### Unit

The ```unit``` block allows detailed specification of the parameters and price of units that make up a line-item. Although no code list for units has been established in the current release of the standard, publishers may consider using the Units provided by the [Quantities, Units, Dimensions and Data Types Ontologies](http://www.qudt.org/qudt/owl/1.0.0/unit/) in the ```unit.name``` field (drawing on the CamelCase unit names, such as SquareMile), in order to provide detailed information the cost per unit of a line-item. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-item-unit.csv
```


### Milestone

Milestone information can be included in the [tender](#tender) and [contract implementation](#implementation) blocks. 

In the context of a tender block, milestones describe the key deliverables of a contract, or key points during the lifetime of the contract. These may have associated documentation. 

In the context of a contract implementation block, milestones are used to track progress towards those deliverables and key events set out in the tender. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-milestone.csv
```

Notes:

* The ```dateModified``` field should be changed whenever the progress towards a milestone is reviewed, and the ```status``` either updated, or re-confirmed. 

<!-- ToDo: Add example -->

### Value

Financial values should always be published with a currency attached. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/docs/field_definitions/release-value.csv
```

During the period of the 1.0 RC, if information on taxation related to a value is required, this may be handled by an extension. A [discussion of handling taxation can be found on GitHub](https://github.com/open-contracting/standard/issues/112).

### Location

The addition of location information is currently handled through a [proposed extension](../extensions/location.md) to the standard.

### Publisher

The publisher block is used in release and record packages to identify the source of a dataset. 

```eval_rst
.. csv-table::
   :header-rows: 1
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

A contract is for ‘Software consultancy services’ may be published in a release with the default language sent to ‘en’ (the ISO-639-1 code for English). The following examples give the description of an item as English, French and Spanish.

**json**

```eval_rst

.. jsoninclude:: example/language.json
   :jsonpointer: 
   :expand: 

```

**csv** 

```eval_rst
.. csv-table::
   :header-rows: 1
   :file: standard/example/language.csv
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
