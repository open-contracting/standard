# Release Reference

The [Release Schema](release) provides a detailed specification of the fields and data structures to use when publishing contracting data. Supplementary schemas show how to combine releases into release packages and how to compile releases into records.

Releases are immutable – presenting information about a particular event in the lifetime of a contracting process. Publishers must not edit a release after publication; a new release can be created by changing the release's `id` and `date`.

**Note: If any conflicts are found between this text, and the text within the schema, the schema takes precedence.**

```{eval-rst}
.. admonition:: Browsing the schema
   :class: note

   .. markdown::

      This page presents the release schema in tables, with additional information in paragraphs. You can also download the canonical version of the release schema as {download}`JSON Schema <../../build/current_lang/release-schema.json>`, download it as a [CSV spreadsheet](https://toucan.open-contracting.org/mapping-sheet/?source=https://standard.open-contracting.org/1.1/en/release-schema.json), view it in an [interactive browser](release), or access it through the [Field-Level Mapping Template](https://www.open-contracting.org/resources/ocds-field-level-mapping-template/).
```

## Release handling

The full OCDS data model is based on the idea of publishing a new release every time information about a contracting process changes. This way, users can gain a full view of change over time, and third-parties can  understand what needs to be updated in any system that is tracking the progress of a contracting process.

Publishers will need to choose how to generate new releases, and whether to repeat information in each release, or just to provide changes. This choice ought to be based on an understanding of the [merging process](merging) that is used to generate a snapshot record of a full contracting process.

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

Languages must be identified using language tags taken from [BCP47](http://tools.ietf.org/html/bcp47). The specification allows BCP47 values in order to accommodate variations in dialect where this is important. However, publishers **should** use the lowercase two-letter [ISO639-1 language tags](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) in the vast majority of circumstances, to avoid users having to distinguish between sub-tag variations (for example, OCDS publishers should use 'en' instead of 'en_US' or 'en_GB').

To include a language variation of a field, the field name must be suffixed with _ and the appropriate language tag. For example: `title_es` for Spanish.

### Worked example

A contract for ‘Software consultancy services’ is published in a release with the default language sent to ‘en’ (the ISO639-1 code for English). The following examples give the description of an item as English, French and Spanish.

**json**

```{eval-rst}
.. jsoninclude:: ../examples/language.json
   :jsonpointer:
   :expand: tender,item

```

**csv**

```{eval-rst}
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 65 15
   :file: ../examples/language.csv
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

Releases are given a [tag](../codelists/#release-tag) to indicate the specific stage of a contracting process they represent. However, there are no formal restrictions on when information about a stage of the contracting process can be provided.

For example, a publisher announcing the signing of a contract with a 'contract' tag might also include information in the award and tender blocks in order to provide a comprehensive picture of the contracting process to date which led to that contract being signed. 

### Package Metadata

Releases must be published within a [release package](release_package). The release package provides metadata about the release(s) that it contains.

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-package-schema.json
    :include: 
    :collapse: releases,publisher

```

See the [licensing guidance](../../guidance/publish/#license-your-data) for more details on selecting a license, and publishing license information.

See the [publication policy](../../guidance/publish/#finalize-your-publication-policy) guidance for more details on what to include in a publication policy.

### Release

All new information about a contracting process is described within a release. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :include: 
    :collapse: planning,tender,awards,contracts,parties,buyer,relatedProcesses

```

```{eval-rst}
.. extensionlist:: The following extensions are available for release
   :list: release
```

### Parties

Each of the parties (organizations or other participants) referenced in a release must be included in the parties section. 

```{eval-rst}
.. admonition:: Parties
   :class: note

   Version 1.1 of OCDS introduces a new approach to describing the buyers,  suppliers, economic operators, and other participants in a contracting process. Instead of embedding organization information at various points within an OCDS release, information on all the parties involved in a contracting process is collected together in a top-level section, and the parties indicated by a cross-reference to their id at other points. 

   This reduces repetition of information on parties who appear at multiple points in the contracting process, and supports publication of information about additional parties to the contracting process, including auditors, multiple buyers, and consortia partners of a winning bidder.

   The old, embedded data, approach to organization data is deprecated in OCDS 1.1, and will be removed in version 2.0. 

```

The following details can be provided for each party.

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Organization
    :collapse: identifier,additionalIdentifiers,address,contactPoint

```

```{eval-rst}
.. extensionlist:: The following extensions are available for parties
   :list: parties
```

Each party has a `details` object. Through extensions, this can be used to provide detailed classification of parties.

```{eval-rst}
.. extensionlist:: The following extensions are available for party details
   :list: partyDetail
```

### Planning

The planning section can be used to describe the background to a contracting process. This can include details of the budget from which funds are drawn, or related projects for this contracting process. Background documents such as a needs assessment, feasibility study and project plan can also be included in this section.

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Planning
    :collapse: budget,documents,milestones

```

Apart from documents, the majority of information is held within the budget block. This is designed to allow both machine-readable linkable data about budgets, cross-referencing to data held in other standards such as the [Fiscal Data Package](https://frictionlessdata.io/specs/fiscal-data-package/) or [International Aid Transparency Initiative Standard](http://www.iatistandard.org), and human readable description of the related budgets and projects, supporting users to understand the relationship of the contracting process to existing projects and budgets even where linked data is not available.

#### Budget 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Budget
    :collapse: amount

```

```{eval-rst}
.. extensionlist:: The following extensions are available for budget
   :list: budget
```

### Tender

The tender section includes details of the announcement that an organization intends to source some particular goods, works or services, and to establish one or more contract(s) for these.

It can contain details of a forthcoming process to receive and evaluate proposals to supply these goods and services, and can also be used to record details of a completed tender process, including details of bids received. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Tender
    :collapse: items,tenderPeriod,enquiryPeriod,awardPeriod,contractPeriod,tenderers,documents,milestones,amendment,amendments,minValue,value,procuringEntity

```

```{eval-rst}
.. extensionlist:: The following extensions are available for the tender section
   :list: tender
```

### Bids

The [Bid statistics and details](https://extensions.open-contracting.org/en/extensions/bids/v1.1.4/) extension can be used to provide bid statistics and detailed information about individual bids.

### Award

The award section is used to announce any awards issued for this tender. There can be multiple awards made. Releases can contain all, or a subset, of these awards. A related award block is required for every contract block, as the award contains information on the suppliers. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Award
    :collapse: items,value,suppliers,contractPeriod,documents,amendment,amendments

```

```{eval-rst}
.. extensionlist:: The following extensions are available for award
   :list: award
```

### Contract

The contract section is used to provide details of contracts that have been entered into. Every contract must have a related award, linked via the `awardID` field. This is because supplier information is contained within the 'award'. The framework contract details below help illustrate the reasons for this. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Contract
    :collapse: period,value,items,documents,implementation,relatedProcesses,milestones,amendment,amendments

```

```{eval-rst}
.. extensionlist:: The following extensions are available for contracts
   :list: contract
```

### Implementation

Implementation information can be updated over the course of a contract. It belongs nested within the contract it relates to. Implementation blocks include the following elements:

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Implementation
    :collapse: transactions,milestones,documents

```

```{eval-rst}
.. extensionlist:: The following extensions are available for implementation
   :list: implementation
```

Information on subcontracts is not currently included in the core OCDS schema, but might be handled by [proposed extensions](conformance_and_extensions)

#### Transaction

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Transaction
    :collapse: providerOrganization,receiverOrganization,amount,payer,payee,value

```

The transaction block is modelled on the [International Aid Transparency Initiative (IATI) transaction element](http://iatistandard.org/activity-standard/iati-activities/iati-activity/transaction/), and can be used to represent actual flows of money between organizations in relation to this contract. As with the [budget](#budget) block, this can be used to cross-reference to a third party `source` of data, and ought to re-use identifiers from that source. 

In most circumstances, the `payer` identifier will match that of the `buyer`, and the `payee` identifier will match that of the `supplier`. 


```{eval-rst}
.. extensionlist:: The following extensions are available for transactions
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

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Amendment
    :collapse: changes
    
```

#### Changes

The changes array was deprecated in OCDS 1.1. Structured information on the former value of specific fields may be provided by:

* Including releases from **before** and **after** a change within a release package;
* Using the amendment array in tender, contract or award to explicitly relate these releases to an amendment.

See the [amendment implementation guidance](../guidance/map/amendments) for more details.

## Building block reference

The following building blocks are commonly re-used throughout the standard.

### OrganizationReference

```{eval-rst}
.. admonition:: Organizations
   :class: note

   The approach to including organizations information has changed in OCDS 1.1. Instead of embedding all the details of an organization, publishers should use an organization reference to indicate the entry in the parties section that contains full details of this organization.

```

An organization reference consists of two main components:

* An `id` used to cross-reference the entry in the [parties](#parties) section that contains full information on this organization or entity;
* A `name` field that repeats the name given in the [parties](#parties) section, provided for the convenience of users viewing the data, and to support detection of mistakes in cross-referencing. 

The Organization Reference schema contains deprecated fields to prevent validation failures of OCDS 1.0 data. 

### Organization

See the [parties](#parties) section

#### Identifier

The identifier block provides a way to [identify the legal entities](../identifiers/#organization-ids) involved in a contracting process.

If a contracting process represents a contract arranged by the department or branch of a larger organization, the legal entity (usually the registered organization) should be described in the [identifier](#identifier) section, with details of the branch or department given in the name, [address](#address) and [contact point](#contactpoint) as relevant. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Identifier
    :collapse: 
    
```

#### Address

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Address
    :collapse: 
    
```

#### ContactPoint

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/ContactPoint
    :collapse: 
    
```
### Document

Documents can be attached at a number of points within the standard: to planning, tenders, awards, contracts and implementation. Each document block can consist of multiple documents, classified using the [documentType](../codelists/#document-type) codelist.

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Document
    :collapse: 
    
```

### Period

A period has a start date, end date, and/or duration. Start and end dates are represented using date-times. Durations are represented as a number of days. 

Periods can also include a `maxExtentDate` which indicates the latest possible end date of this period, or the latest date up until which the period could be extended without an amendment.

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Period
    :collapse: 
    
```

#### Date

OCDS makes use of [ISO8601](http://en.wikipedia.org/wiki/ISO_8601) date-times, following [RFC3339 §5.6](http://tools.ietf.org/html/rfc3339#section-5.6).

A time and timezone/offset must be provided in a date-time.

The following are valid date-times:

* '2014-10-21T09:30:00Z' - 9:30 am on the 21st October 2014, UTC
* '2014-11-18T18:00:00-06:00' - 6pm on 18th November 2014 CST (Central Standard Time)

The following are not valid:

* '2014-10-21' - Missing time portion
* '2014-10-21T18:00' - missing seconds in time portion.
* '2014-11-18T18:00:00' - Missing timezone/offset portion
* '11/18/2014 18:00' - Not following the pattern at all!

Accurately including the time and timezone offsets is particular important for tender deadlines and other dates which can have legal significance, and where users of the data might be from different timezones. The character Z on the end of a date-time indicates the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) (or Zero offset) timezone, whereas other timezones are indicated by their value '+/-hh:mm' UTC on the end of the date-time value. 

In the event that the system from which data is drawn only includes dates, and does not include time information, publishers should use sensible defaults for each field. For example, the startDate time of a clarification period can be set to '00:00:00Z' to indicate that clarifications can be requested from any time on the date stated, with the endDate time set to 23:59:59Z to indicate that clarifications can be sent up until the end of the endDate given. Alternatively, if clarification requests are only accepted in standard office hours, these values might be 09:00:00Z and 17:00:00Z respectively.

In the event that a date field is not bound to a specific time at all, publishers should choose a default time value of '23:59:59' and either 'Z' (for UTC) or the timezone of the publisher, indicating that the time refers to the end of the given date. 

### Item

The items block is used to list the line-items associated with a tender, award or contract. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Item
    :collapse: classification,additionalClassifications,unit
    
```

```{eval-rst}
.. extensionlist:: These are extensions related to Items.
   :list: item
```

#### Classification

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Classification
    :collapse: 
    
```
#### Unit

The `unit` block allows detailed specification of the parameters and price of units that make up a line-item.

If the [Quantities, Units, Dimensions and Data Types Ontologies](http://www.qudt.org/qudt/owl/1.0.0/unit/) unit classification scheme is used, then publishers can use its CamelCase unit names, such as "SquareMile", in the `unit.name` field.

Other unit classification schemes can be used, including those in the [unitClassificationScheme codelist](../codelists/#unit-classification-scheme).

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Item/properties/unit
    :collapse: value
    
```

### Milestone

Milestone information can be included in the [planning](#planning), [tender](#tender), [contract](#contract) and [contract implementation](#implementation) blocks. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Milestone
    :collapse: documents
    
```

Notes:

* The `dateModified` field should be changed whenever the progress towards a milestone is reviewed, and the `status` either updated, or re-confirmed. 

```{eval-rst}
.. extensionlist:: The following extensions to milestone are available
   :list: milestones
```

### Value

Financial values should be published with a currency attached. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/Value
    :collapse: 
    
```

Support for exchange rates, and tax information, can be provided using extensions.

### RelatedProcess

In OCDS each contracting process can have only one planning and tender stage. There are a number of cases where it is important to know about related planning and tendering processes, including:

* When one planning process results in many tenders;
* What a contract is awarded following two distinct, but related, tender processes, such as in national frameworks with locally run mini-competitions;
* When a contract results in the award of sub-contracts - and those sub-contracts are also tracked using OCDS;
* When a contract is coming up for renewal or replacement, and there is a contracting process to award  the renewal/replacement contract;

In all these cases, the `relatedProcess` block should be used to cross-reference between the relevant open contracting processes using their `ocid`.

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-schema.json
    :pointer: /definitions/RelatedProcess
    :collapse: 
    
```

A related process can be declared at two points in an OCDS release.

**(1) At the release level** - used to point backwards to prior processes, such as planning or framework establishment.

**(2) At the contract level** - used to point onward to sub-contracts, renewal or replacement processes that relate solely to the particular contract the field appears in.

As well as providing this machine-readable link between processes, publishers may also provide links to human-readable documentation in the relevant `documents` blocks. For example:

* When recording a `release/relatedProcess` pointing to the ocid of the planning process that resulted in a tender, a `tender/documents` entry with a `documentType` of 'procurementPlan' and a link to web pages about the procurement plan could be provided;
* When recording a `contract/relatedProcess` pointing to the ocid of a  sub-contracting process, a `contract/documents` entry with a `documentType` of 'subContract' and a title that describes it as the subcontracting process, could be provided;
* When recording a `contract/relatedProcess` pointing to the ocid of a tender process to renew a given contract, a `contract/documents` entry with a `documentType` of 'tenderNotice' and a title that describes it as the successor process, could be provided;

### Location

The [Location](https://extensions.open-contracting.org/en/extensions/location/v1.1.4/) extension can be used to provide location information.

### Publisher

The publisher block is used in release and record packages to identify the source of a dataset. 

```{eval-rst}
.. jsonschema:: ../../build/current_lang/release-package-schema.json
    :include: publisher
    :collapse: 
    
```
