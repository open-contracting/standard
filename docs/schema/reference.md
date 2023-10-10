# Release Reference

The [Release Schema](release) provides a detailed specification of the fields and data structures to use when publishing contracting data. Supplementary schemas show how to combine releases into release packages and how to compile releases into records.

Releases are immutable – presenting information about a particular event in the lifetime of a contracting (or planning) process. Publishers must not edit a release after publication; a new release can be created by changing the release's `id` and `date`.

**Note: If any conflicts are found between this text, and the text within the schema, the schema takes precedence.**

```{admonition} Browsing the schema
:class: note

This page presents the release schema in tables, with additional information in paragraphs. You can also download the canonical version of the release schema as [JSON Schema](../../build/current_lang/release-schema.json), download it as a [CSV spreadsheet](../../build/current_lang/release-schema.csv), view it in an [interactive browser](release), or access it through the [Field-Level Mapping Template](https://www.open-contracting.org/resources/ocds-field-level-mapping-template/).
```

## Release handling

The full OCDS data model is based on the idea of publishing a new release every time information about a contracting (or planning) process changes. This way, users can gain a full view of change over time, and third-parties can understand what needs to be updated in any system that is tracking the progress of a contracting (or planning) process.

Publishers will need to choose how to generate new releases, and whether to repeat information in each release, or just to provide changes. This choice ought to be based on an understanding of the [merging process](merging) that is used to generate a snapshot record of a full contracting (or planning) process.

In this model, publishers need to to pay careful attention to null values and missing fields.

### Empty fields

Fields that are not being used, or that have no value, should be excluded in their entirety (key and value) from a published file.

Only including fields which have values will keep versioned datasets cleaner.

### Emptying fields and values

There can be cases where a publisher needs to remove, rather than update, a value which was set in a previous release. In this case, the fields must be set to `null`. See the [merging documentation](merging) for more details.

## Language

Many publishers need to be able to share key data in multiple languages. All free-text title and description fields in the Open Contracting Data Standard can be given in one or more languages.

Language variations are included by a copy of multi-lingual fields, suffixed with a language code.

E.g. `title` and `title_es`

In order to allow users to identify the language used in non-suffixed fields, OCDS release and records should declare the default language in the `language` field.

Languages must be identified using language tags taken from [BCP47](https://tools.ietf.org/html/bcp47). The specification allows BCP47 values in order to accommodate variations in dialect where this is important. However, publishers **should** use the lowercase two-letter [ISO639-1 language tags](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) in the vast majority of circumstances, to avoid users having to distinguish between sub-tag variations (for example, OCDS publishers should use 'en' instead of 'en_US' or 'en_GB').

To include a language variation of a field, the field name must be suffixed with _ and the appropriate language tag. For example: `title_es` for Spanish.

### Worked example

A contract for ‘Software consultancy services’ is published in a release with the default language sent to ‘en’ (the ISO639-1 code for English). The following examples give the description of an item as English, French and Spanish.

**json**

```{jsoninclude} ../examples/language_localization/language.json
:jsonpointer:
:expand: tender,item
```

**csv**

```{csv-table-no-translate}
:header-rows: 1
:file: ../examples/language_localization/language.csv
```

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

A release has a [tag](codelists.md#release-tag) to indicate whether it is about a planning process or a contracting process and, if it is about the latter, to indicate the stage of the contracting process to which it relates. However, there are no formal restrictions on when information about a stage of the process can be provided.

For example, a publisher announcing the signing of a contract with a 'contract' tag might also include information in the award and tender blocks in order to provide a comprehensive picture of the contracting process to date which led to that contract being signed. 

### Package Metadata

Releases must be published within a [release package](release_package). The release package provides metadata about the release(s) that it contains.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer:
:expand: publisher
:title: package
```
````

```{jsonschema} ../../build/current_lang/release-package-schema.json
:collapse: releases,publisher
```

See the [licensing guidance](../guidance/publish.md#license-your-data) for more details on selecting a license, and publishing license information.

See the [publication policy](../guidance/publish.md#finalize-your-publication-policy) guidance for more details on what to include in a publication policy.

### Release

All new information about a contracting (or planning) process is described within a release. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0
:title: release
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:collapse: planning,tender,awards,contracts,parties,buyer,relatedProcesses
```

```{extensionlist} The following extensions are available for release
:list: release
```

```{workedexamplelist} The following worked examples are available for releases
:tag: release
```

### Parties

Each of the organizations referenced in a release must be included in the parties section. 

```{versionadded} 1.1
In OCDS 1.0, the details (address, contact point, etc.) of the organizations involved in a contracting process were repeated across many fields (`tenderers`, `suppliers`, etc.). In OCDS 1.1, these details are instead collected under a top-level `parties` array, with the other fields referencing entries in this array, using [organization references](#organizationreference). This reduces repetition and supports publication of information about additional organizations: for example, multiple buyers.

Note that the organization references allow, but deprecate, the fields for organization details.
```

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/parties
:expand: roles
:title: parties
```
````

The following details can be provided for each organization.

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Organization
:collapse: identifier,additionalIdentifiers,address,contactPoint
```

```{extensionlist} The following extensions are available for organizations
:list: parties
```

Each organization has a `details` object. Through extensions, this can be used to provide detailed classification of organizations.

```{extensionlist} The following extensions are available for organization details
:list: partyDetail
```

```{workedexamplelist} The following worked examples are available for organizations
:tag: parties
```

### Planning

The planning section is used in a planning process. This includes information about, for example, needs identification, budget planning and market research. Background documents such as feasibility studies and project plans can also be included in this section.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/planning
:title: planning
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Planning
:collapse: budget,documents,milestones
```

```{extensionlist} The following extensions are available for planning
:list: planning
```

```{workedexamplelist} The following worked examples are available for plannings
:tag: planning
```

#### Budget 

Apart from documents, the majority of planning information is held within the budget block. This is designed to allow both machine-readable linkable data about budgets, cross-referencing to data held in other standards such as the [Fiscal Data Package](https://specs.frictionlessdata.io/fiscal-data-package/) or [International Aid Transparency Initiative Standard](https://iatistandard.org/en/), and human readable description of the related budgets and projects, supporting users to understand the relationship of the contracting (or planning) process to existing projects and budgets even where linked data is not available.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/planning/budget
:title: budget
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Budget
:collapse: amount
```

```{extensionlist} The following extensions are available for budget
:list: budget
```

### Tender

The tender section includes details of the announcement that an organization intends to source some particular goods, services or works and to establish one or more contract(s) for these.

It can contain details of a forthcoming process to receive and evaluate proposals to supply these goods, services or works and can also be used to record details of a completed tender stage, including details of bids received. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/tender
:title: tender
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Tender
:collapse: items,tenderPeriod,enquiryPeriod,awardPeriod,contractPeriod,tenderers,documents,milestones,amendment,amendments,minValue,value,procuringEntity
```

```{extensionlist} The following extensions are available for the tender section
:list: tender
```

```{workedexamplelist} The following worked examples are available for tenders
:tag: tender
```

### Bids

The [Bid statistics and details](https://extensions.open-contracting.org/en/extensions/bids/v1.1.4/) extension can be used to provide bid statistics and detailed information about individual bids.

### Award

The award section is used to announce any awards issued for this tender. There can be multiple awards made. Releases can contain all, or a subset, of these awards. A related award block is required for every contract block, as the award contains information on the suppliers. In particular cases there can be multiple suppliers for a single award: for example, in the case of [consortia](../guidance/map/buyers_suppliers.md#consortia-suppliers) and in [framework agreements](../guidance/map/framework_agreements).

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/awards/0
:title: award
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Award
:collapse: items,value,suppliers,contractPeriod,documents,amendment,amendments
```

```{extensionlist} The following extensions are available for award
:list: award
```

```{workedexamplelist} The following worked examples are available for awards
:tag: award
```

### Contract

The contract section is used to provide details of contracts that have been entered into. Every contract must have a related award, linked via the `awardID` field. This is because supplier information is contained within the 'award'. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/contracts/0
:title: contract
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Contract
:collapse: period,value,items,documents,implementation,relatedProcesses,milestones,amendment,amendments
```

```{extensionlist} The following extensions are available for contracts
:list: contract
```

```{workedexamplelist} The following worked examples are available for contracts
:tag: contract
```

### Implementation

Implementation information can be updated over the course of a contract. It belongs nested within the contract it relates to. Implementation blocks include the following elements:

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/contracts/0/implementation
:title: implementation
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Implementation
:collapse: transactions,milestones,documents
```

```{extensionlist} The following extensions are available for implementation
:list: implementation
```

Information on subcontracts is not currently included in the core OCDS schema, but might be handled by [proposed extensions](conformance_and_extensions)

```{workedexamplelist} The following worked examples are available for implementations
:tag: implementation
```

#### Transaction

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/contracts/0/implementation/transactions/0
:title: transaction
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Transaction
:collapse: providerOrganization,receiverOrganization,amount,payer,payee,value
```

The transaction block is modelled on the [International Aid Transparency Initiative (IATI) transaction element](https://iatistandard.org/en/iati-standard/203/activity-standard/iati-activities/iati-activity/transaction/), and can be used to represent actual flows of money between organizations in relation to this contract. As with the [budget](#budget) block, this can be used to cross-reference to a third party `source` of data, and ought to reuse identifiers from that source.

```{note}
To represent planned payments, use [Milestones](#milestones) instead.
```

In most circumstances, the `payer` identifier will match that of the `buyer`, and the `payee` identifier will match that of the `supplier`. 

```{extensionlist} The following extensions are available for transactions
:list: transaction
```

#### Milestones

See [milestone](#milestone) reference below.

The implementation milestones should be updated to reflect when they are met. 

#### Documents

Documents related to contract implementation are stored here. This can include subcontracts.

See [document](#document) reference below. 

### Amendment

A release may amend values from a previous release. Whilst the release & record model of OCDS offers the opportunity to keep a full versioned history of changes, in many cases it is important for changes to a tender, award or contract to be explicitly declared.

The amendment array in a tender, award or contract block provides the ability to detail the amendments that have taken place with dates, rationale and free-text descriptions of the change, as well as to point to the releases that contain information from before and after the amendment.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/tender/amendments/0
:title: amendments
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Amendment
:collapse: changes
```

```{workedexamplelist} The following worked examples are available for amendments
:tag: amendment
```

#### Changes

```{deprecated} 1.1
Structured information on the former value of specific fields may be provided instead by:

* Including releases from **before** and **after** a change within a release package;
* Using the amendment array in tender, contract or award to explicitly relate these releases to an amendment.

See the [amendment implementation guidance](../guidance/map/amendments) for more details.
```

## Building block reference

The following building blocks are commonly re-used throughout the standard.

### OrganizationReference

```{versionadded} 1.1
See the [parties](#parties) section.
```

An organization reference consists of two main components:

* An `id` used to cross-reference the entry in the [parties](#parties) section that contains full information on this organization;
* A `name` field that repeats the name given in the [parties](#parties) section, provided for the convenience of users viewing the data, and to support detection of mistakes in cross-referencing. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/buyer
:title: organizationReference
```
````

```{workedexamplelist} The following worked examples are available for organization reference
:tag: organization_reference
```

### Organization

See the [parties](#parties) section.

#### Identifier

The identifier block provides a way to [identify the legal entities](identifiers.md#organization-identifiers) involved in a contracting (or planning) process.

If a contracting process represents a contract arranged by the department or branch of a larger organization, the legal entity (usually the registered organization) should be described in the [identifier](#identifier) section, with details of the branch or department given in the name, [address](#address) and [contact point](#contactpoint) as relevant. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/parties/0
:expand: identifier
:title: party
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Identifier
```

#### Address

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/parties/0
:expand: address
:title: party
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Address
```

#### ContactPoint

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/parties/0
:expand: contactPoint
:title: party
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/ContactPoint
```

### Document

Documents can be attached at a number of points within the standard: to planning, tenders, awards, contracts and implementation. Each document block can consist of multiple documents, classified using the [documentType](codelists.md#document-type) codelist.

Documents related to contracting (or planning) processes should be public by default. For more information, see the Open Contracting Partnership's report [Mythbusting Confidentiality in Public Contracting](https://www.open-contracting.org/resources/mythbusting-confidentiality-public-contracting/) and the Center for Global Development's [Principles on Commercial Transparency in Public Contracts](https://www.cgdev.org/publication/principles-commercial-transparency-public-contracts).

Documents should be published at their own stable URLs, accessible for free and without the need to search or login, and available at the time of publication of the OCDS release that refers to them.

OCDS allows summarizing information in the document's `description` field. Providing clear summaries is a good practice, as it allows applications to display this information in a user-interface and thus enables users to read key facts without having to search through the whole document.

If a document contains multiple languages, use the `languages` field to list the languages used in the document. If there are multiple versions of a document, each in a different language, add a separate `Document` object for each version of the document.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/tender/documents/0
:title: document
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Document
```

```{extensionlist} The following extensions are available for document
:list: document
```

### Period

A period has a start date, end date, and/or duration. Start and end dates are represented using date-times. Durations are represented as a number of days. 

Periods can also include a `maxExtentDate` which indicates the latest possible end date of this period, or the latest date up until which the period could be extended without an amendment.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/awards/0/contractPeriod
:title: period
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Period
```

#### Date

OCDS makes use of [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) date-times, following [RFC3339 §5.6](https://tools.ietf.org/html/rfc3339#section-5.6).

A time and timezone/offset must be provided in a date-time.

The following are valid date-times:

* '2014-10-21T09:30:00Z' - 9:30 am on the 21st October 2014, UTC
* '2014-11-18T18:00:00-06:00' - 6pm on 18th November 2014 CST (Central Standard Time)

The following are not valid:

* '2014-10-21' - Missing time portion
* '2014-10-21T18:00' - missing seconds in time portion.
* '2014-11-18T18:00:00' - Missing timezone/offset portion
* '11/18/2014 18:00' - Not following the pattern at all!

Accurately including the time and timezone offsets is particular important for tender deadlines and other dates which can have legal significance, and where users of the data might be from different timezones. The character Z on the end of a date-time indicates the [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) (or Zero offset) timezone, whereas other timezones are indicated by their value '+/-hh:mm' UTC on the end of the date-time value.

In the event that the system from which data is drawn only includes dates, and does not include time information, publishers should use sensible defaults for each field. For example, the startDate time of a clarification period can be set to '00:00:00Z' to indicate that clarifications can be requested from any time on the date stated, with the endDate time set to 23:59:59Z to indicate that clarifications can be sent up until the end of the endDate given. Alternatively, if clarification requests are only accepted in standard office hours, these values might be 09:00:00Z and 17:00:00Z respectively.

In the event that a date field is not bound to a specific time at all, publishers should choose a default time value of '00:00:00' and either 'Z' (for UTC) or the timezone of the publisher. However, if the date is an endDate in a period object the default time value should be set to '23:59:59', indicating that the time refers to the end of the given date.

### Item

The items block is used to list the line-items associated with a tender, award or contract. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/tender/items/0
:title: items
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Item
:collapse: classification,additionalClassifications,unit
```

```{extensionlist} These are extensions related to Items.
:list: item
```

#### Unit

The `unit` block allows detailed specification of the parameters and price of units that make up a line-item.

If the [Quantities, Units, Dimensions and Data Types Ontologies](https://www.qudt.org) unit classification scheme is used, then publishers can use its CamelCase unit names, such as "SquareMile", in the `unit.name` field.

Other unit classification schemes can be used, including those in the [unitClassificationScheme codelist](codelists.md#unit-classification-scheme).

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/tender/items/0
:expand: unit
:title: unit
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Item/properties/unit
:collapse: value
```

### Classification

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/tender/items/0/classification
:title: classification
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Classification
```

### Milestone

Milestone information can be included in the [planning](#planning), [tender](#tender), [contract](#contract) and [contract implementation](#implementation) blocks.

The `dateModified` field should be changed whenever the progress towards a milestone is reviewed, and the `status` either updated, or re-confirmed. 

```{seealso}
[How to represent planned payments](../guidance/map/milestones.md#delivery-and-payment-data)
```

For delivery milestones, if there is a time frame for delivery, use `.dueAfterDate` for the start date and `.dueDate` for the end date.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/planning/milestones/0
:title: milestones
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Milestone
:collapse: documents
```

```{extensionlist} The following extensions to milestone are available
:list: milestones
```

```{workedexamplelist} The following worked examples are available for milestones
:tag: milestone
```

### Value

Financial values should be published with a currency attached. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/awards/0/value
:title: value
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Value
```

Support for exchange rates, and tax information, can be provided using extensions.

### RelatedProcess

In OCDS each contracting process can have only one tender stage. There are a number of cases where it is important to know about related contracting processes, including:

* When one planning process results in many tenders;
* When a contract is awarded following two distinct, but related, tender processes, such as in national frameworks with locally run mini-competitions;
* When a contract results in the award of sub-contracts - and those sub-contracts are also tracked using OCDS;
* When a contract is coming up for renewal or replacement, and there is a contracting process to award  the renewal/replacement contract;

In all these cases, the `relatedProcess` block should be used to cross-reference between the relevant contracting processes using their `ocid`.

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /releases/0/relatedProcesses
:title: relatedProcesses
```
````

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/RelatedProcess
```

A related process can be declared at two points in an OCDS release.

**(1) At the release level** - used to point backwards to prior processes, such as planning or framework establishment.

**(2) At the contract level** - used to point onward to sub-contracts, renewal or replacement processes that relate solely to the particular contract the field appears in.

As well as providing this machine-readable link between processes, publishers may also provide links to human-readable documentation in the relevant `documents` blocks. For example:

* When recording a `release/relatedProcess` pointing to the ocid of the planning process that resulted in a tender, a `tender/documents` entry with a `documentType` of 'procurementPlan' and a link to web pages about the procurement plan could be provided;
* When recording a `contract/relatedProcess` pointing to the ocid of a  sub-contracting process, a `contract/documents` entry with a `documentType` of 'subContract' and a title that describes it as the subcontracting process, could be provided;
* When recording a `contract/relatedProcess` pointing to the ocid of a contracting process to renew a given contract, a `contract/documents` entry with a `documentType` of 'tenderNotice' and a title that describes it as the successor process, could be provided;

### Location

The [Location](https://extensions.open-contracting.org/en/extensions/location/v1.1.4/) extension can be used to provide location information.

### Publisher

The publisher block is used in release and record packages to identify the source of a dataset. 

````{admonition} Example
:class: hint

```{jsoninclude} ../examples/release_schema_reference/release_package.json
:jsonpointer: /publisher
:title: publisher
```
````

```{jsonschema} ../../build/current_lang/release-package-schema.json
:include: publisher
```

### Link

The entries of the top-level `links` array are `Link` objects:

```{field-description} ../../build/current_lang/release-schema.json /properties/links
```

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/Link
```

### SimpleIdentifier

```{field-description} ../../build/current_lang/release-schema.json /definitions/SimpleIdentifier
```

```{jsonschema} ../../build/current_lang/release-schema.json
:pointer: /definitions/SimpleIdentifier
```
