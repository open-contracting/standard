# Changelog

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [1.1.4]

### Advisories

* OCDS 1.0 uses the [whole-list merge](http://standard.open-contracting.org/1.1/en/schema/merging/#whole-list-merge) strategy for suppliers, whereas OCDS 1.1 uses the [identifier merge](http://standard.open-contracting.org/1.1/en/schema/merging/#identifier-merge) strategy. As a consequence, the OCDS 1.1 versioned release schema is not backward compatible with OCDS 1.0.
* [#780](https://github.com/open-contracting/standard/pull/780) All extensions have been moved to the [open-contracting-extensions](https://github.com/open-contracting-extensions) organization. No change is required, but we recommend that publishers update the URLs of extensions in release packages and record packages.
* [#831](https://github.com/open-contracting/standard/pull/831) OCDS now has a [Normative and non-normative content and changes policy](https://docs.google.com/document/d/1xjlAneqgewZvHh6_hwuQ98hbjxRcA2IUqOTJiNGcOf8/edit).
* [#744](https://github.com/open-contracting/standard/pull/744) OCDS now has a [translation and localization policy](http://standard.open-contracting.org/1.1/en/support/governance/#translation-and-localization-policy).
* [#806](https://github.com/open-contracting/standard/pull/806) [#808](https://github.com/open-contracting/standard/pull/808) [#809](https://github.com/open-contracting/standard/pull/809) The documentation is now available in Italian.
* [#717](https://github.com/open-contracting/standard/pull/717) [#734](https://github.com/open-contracting/standard/pull/734) The OCDS documentation website now has a [privacy notice](http://standard.open-contracting.org/1.1/en/privacy-notice/).

### Bugs

* [#738](https://github.com/open-contracting/standard/pull/738) 1.1.3 changed the merging and versioning behaviors of `Item.unit`, such that it could be removed by setting it to `null`, and such that it was versioned as a whole. 1.1.4 restores the behaviors from 1.1.2, such that only its sub-fields can be removed by setting them to `null`, and such that its sub-fields are versioned individually. If you are not using compiled releases or versioned releases, then this bug didn't affect you.
* [#810](https://github.com/open-contracting/standard/pull/810) `buyer.id`, `Tender.procuringEntity.id`, `Contract.implementation.payer.id` `Contract.implementation.payee.id`, `Budget.id`, `Identifier.id`, and `Classification.id` are now versioned, consistent with the documentation.
* [#769](https://github.com/open-contracting/standard/pull/769) The versioned release schema now matches the release schema in: having a `minLength` validation property for `OrganizationReference.name`; having `codelist` and `openCodelist` properties for `Tender.awardCriteria`, `Tender.awardCriteriaDetails`, `Document.documentType`, `Item.unit.scheme`, `Classification.scheme`, and `RelatedProcess.scheme`; and having a `deprecated` property for `Budget.source`. All `title` and `description` metadata properties are removed from the versioned release schema.
* [#810](https://github.com/open-contracting/standard/pull/810) `tag` is now `omitWhenMerged`, consistent with the reference implementation in OCDS Merge.

### Codelists

* [#824](https://github.com/open-contracting/standard/pull/824) Canonical codelist files are available at URLs like <http://standard.open-contracting.org/schema/1__1__4/codelists/>, and translations are available at URLs like <http://standard.open-contracting.org/1.1/en/codelists/>, for OCDS 1.1.4 and up.
* [#746](https://github.com/open-contracting/standard/pull/746) [#842](https://github.com/open-contracting/standard/pull/842) Update currency codelist for ISO4217 amendments [166](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_166.pdf), [167](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_167.pdf), [168](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_168.pdf) and [169](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_169.pdf).
* [#725](https://github.com/open-contracting/standard/pull/725) Add a 'plannedProcurementNotice' code to the `documentType` codelist, 'CUCOP' to `itemClassificationScheme`, 'interestedParty' to `partyRole`.
* [#725](https://github.com/open-contracting/standard/pull/725) Update the descriptions of the 'tenderNotice' and 'technicalSpecifications' codes in the `documentType` codelist to align with the text of the [Agreement on Government Procurement (GPA)](https://www.wto.org/english/tratop_e/gproc_e/gp_gpa_e.htm) of the World Trade Organization (WTO).
* [#725](https://github.com/open-contracting/standard/pull/725) Apply the style guide and OCDS glossary to the 'procuringEntity' and 'supplier' codes in the `partyRole` codelist.
* [#725](https://github.com/open-contracting/standard/pull/725) Add examples to the description of the 'environmentalImpact' code in the `documentType` codelist.
* [#829](https://github.com/open-contracting/standard/pull/829) Use sentence case for code titles and end code descriptions with periods.
* [#852](https://github.com/open-contracting/standard/pull/852) Use the correct normative keywords in code descriptions.

### Schema

* [#712](https://github.com/open-contracting/standard/pull/712) Add missing titles for `publisher` and `url` and description for `record` in the record package schema, and missing description for `releases` in release package schema.
* [#838](https://github.com/open-contracting/standard/pull/838) Eliminate the conflicting rule that release identifiers must be unique within release packages. Uniqueness within the scope of a release package either implies that release identifiers must be globally unique, or imposes an arbitrary restriction on the contents of release packages, as there is no rule preventing release packages from containing releases from different contracting processes. Release identifiers are only required to be locally unique within the scope of a contracting process. The `ocid` and `id` values of a release can be used together to disambiguate releases within a release package.
* [#810](https://github.com/open-contracting/standard/pull/810) Add a dereferenced release schema to ease the implementation of the merge routine.
* [#810](https://github.com/open-contracting/standard/pull/810) Add `"versionId": true` hint to `Identifier` and `Classification`.
* [#845](https://github.com/open-contracting/standard/pull/845) Remove reference to closed issue and note about field name.
* Clarify the uniqueness of release identifiers in the release schema [#838](https://github.com/open-contracting/standard/pull/838) and release package schema [#831](https://github.com/open-contracting/standard/pull/831).

### Documentation

* [#772](https://github.com/open-contracting/standard/pull/772) [#810](https://github.com/open-contracting/standard/pull/810) [#831](https://github.com/open-contracting/standard/pull/831) Clarify the merge rules for compiled releases and versioned releases.
* [#797](https://github.com/open-contracting/standard/pull/797) Fix examples of versioned releases.
* [#831](https://github.com/open-contracting/standard/pull/831) Use the correct normative keywords in the documentation.
* [#835](https://github.com/open-contracting/standard/pull/835) Display the canonical schema URLs in the documentation.
* [#838](https://github.com/open-contracting/standard/pull/838) Clarify the uniqueness of release, award and contract identifiers.
* [#831](https://github.com/open-contracting/standard/pull/831) Improve the description of iterating the release `id`.
* [#822](https://github.com/open-contracting/standard/pull/822) Integrate the [Extension Explorer](https://extensions.open-contracting.org/en/).
* [#783](https://github.com/open-contracting/standard/pull/783) Add missing email address for the standard governance working group.
* Replace ambiguous or incorrect terms:
  * [#831](https://github.com/open-contracting/standard/pull/831) Use "release `id`" and "release `date`", instead of "`releaseID`" and "`releaseDate`"
  * [#831](https://github.com/open-contracting/standard/pull/831) Use "ocid prefix", instead of "publisher prefix"
  * [#840](https://github.com/open-contracting/standard/pull/840) Use "release package and record package", instead of "data package", to avoid confusion with [Frictionless Data's Data Package specification](https://frictionlessdata.io/specs/data-package/)
  * [#831](https://github.com/open-contracting/standard/pull/831) Use "minor versions", instead of "decimal versions" on deprecation page
  * [#823](https://github.com/open-contracting/standard/pull/823) Fix incorrect uses of "records", "codelists" and "gazetteers" on identifiers and codelists pages
* Fix out-of-date content:
  * [#831](https://github.com/open-contracting/standard/pull/831) Remove sentence implying non-existence of unit classification scheme codelist on release schema reference page
  * [#831](https://github.com/open-contracting/standard/pull/831) Remove sentence using non-existent 'notice' code on release schema reference page
  * [#831](https://github.com/open-contracting/standard/pull/831) Remove reference to closed issue in API section
* Add links to:
  * [#783](https://github.com/open-contracting/standard/pull/783) Community extensions relating to party details
  * [#837](https://github.com/open-contracting/standard/pull/837) OCDS profiles
* Correct typos in the documentation [#692](https://github.com/open-contracting/standard/pull/692) [#713](https://github.com/open-contracting/standard/pull/713) [#719](https://github.com/open-contracting/standard/pull/719) [#726](https://github.com/open-contracting/standard/pull/726) [#732](https://github.com/open-contracting/standard/pull/732) [#752](https://github.com/open-contracting/standard/pull/752) [#756](https://github.com/open-contracting/standard/pull/756) [#795](https://github.com/open-contracting/standard/pull/795).
* Improve the process to build the documentation [#666](https://github.com/open-contracting/standard/pull/666) [#698](https://github.com/open-contracting/standard/pull/698) [#708](https://github.com/open-contracting/standard/pull/708) [#709](https://github.com/open-contracting/standard/pull/709) [#721](https://github.com/open-contracting/standard/pull/721) [#724](https://github.com/open-contracting/standard/pull/724) [#727](https://github.com/open-contracting/standard/pull/727) [#729](https://github.com/open-contracting/standard/pull/729) [#733](https://github.com/open-contracting/standard/pull/733) [#740](https://github.com/open-contracting/standard/pull/740) [#747](https://github.com/open-contracting/standard/pull/747) [#753](https://github.com/open-contracting/standard/pull/753) [#762](https://github.com/open-contracting/standard/pull/762) [#767](https://github.com/open-contracting/standard/pull/767) [#783](https://github.com/open-contracting/standard/pull/783) [#787](https://github.com/open-contracting/standard/pull/787) [#796](https://github.com/open-contracting/standard/pull/796) [#813](https://github.com/open-contracting/standard/pull/813) [#836](https://github.com/open-contracting/standard/pull/836).

## [1.1.3] - 2018-04-16

### Codelist updates

* Update currency codelist for ISO4217 amendment 165 (2017-12-14).

### Schema fixes 

* [#646](https://github.com/open-contracting/standard/pull/646) Disallow use of `null` as an item in the array for `Tender.additionalProcurementCategories`.
* [#639](https://github.com/open-contracting/standard/issues/639) Make `name` field optional for `OrganizationReference`.
* [#630](https://github.com/open-contracting/standard/issues/630) Allow optional field `Item.unit` to be `null`.
* [#603](https://github.com/open-contracting/standard/issues/603), [#645](https://github.com/open-contracting/standard/issues/645) Add definitions to Release, planning.budget, Milestone, Organization.address, Organization.contactPoint, Classification, Identifier, Value and Period.
* Make `record-package-schema.json` use the `codelist` property to reference `releaseTag.csv`, and update the `enum` accordingly.
* [#578](https://github.com/open-contracting/standard/issues/578) Update definition of `buyer` to cover goods, works and services, and multiple buyers.

### Documentation fixes

* [#633](https://github.com/open-contracting/standard/issues/633) Update schema reference page to display `Release.relatedProcesses`, `Planning.documents` and `Contract.relatedProcesses`.
* [#634](https://github.com/open-contracting/standard/issues/634) Clarify definitions of core, community and local extensions.

### Extension fixes 

* [#40](https://github.com/open-contracting/ocds-extensions/issues/40), [#43](https://github.com/open-contracting/ocds-extensions/issues/43), [#47](https://github.com/open-contracting/ocds-extensions/issues/47) Add missing definitions, codelists and enums to core extensions, correct typos in codelist filenames, disallow use of `null` as an item in arrays, disallow required fields from being set to `null`, allow optional fields to be `null`, use `OrganizationReference` instead of `Organization`.

Old and unused scripts have been removed from the documentation repository, and a number of script dependencies have been updated.

## [1.1.2] - 2017-11-10

### Codelist updates

* [554](https://github.com/open-contracting/standard/issues/554) - **Update currency codelist for ISO4217 amendment 163 (2017-06-09)**. Note: XBT (Bitcoin) is removed from the codelist as it is not part of ISO4217.

## [1.1.1] - 2017-07-31

### Bug fixes

* [#482](https://github.com/open-contracting/standard/issues/482) **[Allow parties.role to be set to `null`](https://github.com/open-contracting/standard/pull/502/commits/475abf598063aae5c22e07baba015d960fcc3a95)** - required by the [merging approach](http://standard.open-contracting.org/1.1/en/schema/merging/). 
* [#422](https://github.com/open-contracting/standard/issues/422) **[Including currency codelist in documentation and schema](http://standard.open-contracting.org/1.1/en/schema/codelists/#currency)** to support validation of currency values.
* [#479](https://github.com/open-contracting/standard/issues/479) **[Fixing incorrect requirement to include releases in record-package-schema.json](http://standard.open-contracting.org/1.1/en/schema/record_package/)** 
* [#475](https://github.com/open-contracting/standard/issues/475) **Adding enum arrays to all fields in the schema with a closed codelist** to support validation.

### Minor revisions

* [#471](https://github.com/open-contracting/standard/issues/471) **[Updating milestoneType codelist](http://standard.open-contracting.org/1.1/en/schema/codelists/#milestone-type)** replacing 'planning' with 'preProcurement' and 'adjudication' with 'assessment' and introducing codes for 'approval' and 'financing'. This is an open codelist, so previous codes remain valid, but publishers able to update to the new codes should do so. 
* [#473](https://github.com/open-contracting/standard/issues/473) **[Updating definition of contractSchedule in documentType codelist](http://standard.open-contracting.org/1.1/en/schema/codelists/#document-type)**

### Documentation improvements

* **Fixing typographic errors throughout the documentation and codelist descriptions**
* [#480](https://github.com/open-contracting/standard/pull/480/commits/c3c41225639a06b0b0552016b32e2fe2e901a8fe) **[Updating basic, intermediate, advanced](http://standard.open-contracting.org/1.1/en/implementation/levels/) publication guidance** - to ensure tables and text are aligned. 
* [#489](https://github.com/open-contracting/standard/issues/489) **Listing the milestone documents extension as a core extension** - and removing it from the community extensions list. This extension is only needed by publishers with legacy data containing documents at the milestone level.
* [#493](https://github.com/open-contracting/standard/issues/493) **[Updating the description of the Organization Identifier Scheme codelist](http://standard.open-contracting.org/1.1/en/schema/codelists/#organization-identifier-scheme)** to reflect that the codelist is now maintained by [org-id.guide](http://www.org-id.guide/).

### Code and build process

* [#506](https://github.com/open-contracting/standard/issues/506) **Removed make_field_definitions.py** from utility scripts as it is no longer required.
* **Addition of docstrings to key scripts**

## [1.1.0] - 2017-05-01

### Policy changes

* [#401](https://github.com/open-contracting/standard/issues/401) **[Deprecation policy](http://standard.open-contracting.org/1.1/en/schema/conformance_and_extensions/)** - The deprecation policy has been updated to support deprecation in decimal upgrades.

### Changed

#### Structural updates 

* [#368](https://github.com/open-contracting/standard/issues/368) **[Updates to organization handling in OCDS](http://standard.open-contracting.org/1.1/en/schema/reference/#parties)** - We have updated the approach to include organization information in the standard from having embedded blocks of organization information, to using embedded cross-references to a top-level 'parties' array where full organization details are stored. This change reduces duplication of organization information, and enables more flexible disclosure of information on all the parties to a contracting process, including multiple buyers.
* [#357](https://github.com/open-contracting/standard/issues/357) **[Amendment handling](http://standard.open-contracting.org/1.1/en/implementation/amendments/)** - We have replace amendment with an array of amendments, and have updated schema and guidance to remove the option of providing semi-structured changes in an amendment object. Changes between amendments should now be provided using multiple releases, with the option to explicitly declare how releases relate to an amendment included in the new amendments array. 

#### Schema validation updates 

* [#329](https://github.com/open-contracting/standard/issues/329) **[Float for Item.quantity](http://standard.open-contracting.org/1.1/en/schema/reference/#item)** - Item quantities has been updated to 'number' to support decimal values (e.g 10.5 rather than just 10)
* [#253](https://github.com/open-contracting/standard/issues/253) **[Negative amounts](http://standard.open-contracting.org/1.1/en/schema/reference/#budget)** - We have added support for negative amounts in transactions
* [#323](https://github.com/open-contracting/standard/issues/323) **[Standard should specify use of UTF-8 for encoding JSON](http://standard.open-contracting.org/1.1/en/implementation/serialization/#json)** - We now recommend use of I-JSON and UTF-8 for JSON publication
* [#166](https://github.com/open-contracting/standard/issues/166) **[Indicate encoding for CSV serializations](http://standard.open-contracting.org/1.1/en/implementation/serialization/#multi-table)** - We have added information on CSV encoding to the implementation guidance to recommend UTF-8 or Windows-1252.
* [#336](https://github.com/open-contracting/standard/issues/336) **[Codelist properties in schema](https://github.com/open-contracting/standard/commit/ee1db256d7364ee70e3553f4384d9908bff604a6)** - We have included explicit references to the codelist files (CSV versions) in the schema. This will be used in future versions of the validator to support validation against codelists.
* [#301](https://github.com/open-contracting/standard/issues/301) **[Specifying versions and extensions in package metadata](http://standard.open-contracting.org/1.1/en/schema/records_reference/#package-metadata)** - We have updated the package schemas to require that version is declared, and to provide a means of declaring extensions in use. This will be used in future versions of the validator to support validation against extensions.
* [#287](https://github.com/open-contracting/standard/issues/287) **[Remove all ocdsMerge strategies](http://standard.open-contracting.org/1.1/en/schema/merging/)** - We have remove all 'merge strategies' from the schema as these are no longer required, now that all objects in arrays contain an id element.

#### Schema definition updates 

* [#372](https://github.com/open-contracting/standard/issues/372) **[Updates to transactions terminology](http://standard.open-contracting.org/1.1/en/schema/reference/#transaction)** - We have replaced receiverOrganization and providerOrganization with payee and payer, to align with more familiar terminology, and have replaced 'amount' with 'value' for consistency with other areas of the standard.
* [#378](https://github.com/open-contracting/standard/issues/378) **[Updates to core budget block](http://standard.open-contracting.org/1.1/en/schema/reference/#budget)** - We have updated references to the Fiscal Data Package in the schema.
* [#337](https://github.com/open-contracting/standard/issues/337) **[Definition of "tenderer" to enhance clarity](http://standard.open-contracting.org/1.1/en/schema/reference/#tender)** - We have updated the definition of tenderer in the tenders block, and cross-referenced the bid extension.
* [#259](https://github.com/open-contracting/standard/issues/259) **[Enquiries](https://extensions.open-contracting.org/en/extensions/enquiries/)** - We have updated the definition of hasEnquiries.
* [#246](https://github.com/open-contracting/standard/issues/246) **[In what scope must a release ID be unique?](http://standard.open-contracting.org/1.1/en/schema/reference/#release)** - We have updated the definition of release.id to reflect the scope in which it must be unique

#### Closed codelist updates

* [#201](https://github.com/open-contracting/standard/issues/201) **[Tender status](http://standard.open-contracting.org/1.1/en/schema/codelists/#tender-status)** - New 'planning' and 'withdrawn' codes have been introduced to the tenderStatus codelist.
* [#380](https://github.com/open-contracting/standard/issues/380) **[Procurement method](http://standard.open-contracting.org/1.1/en/schema/codelists/#method)** - A new code for 'direct' has been added the procurementMethod codelist
* [#373](https://github.com/open-contracting/standard/issues/373) **[Milestone status](http://standard.open-contracting.org/1.1/en/schema/codelists/#milestone-status)** - We have updated the milestoneStatus codelist with a 'scheduled' entry and revised definitions
* [#297](https://github.com/open-contracting/standard/issues/297) **[Currency codelist external link](http://standard.open-contracting.org/1.1/en/schema/codelists/#currency)** - We have fixed the external link for currency codelists to refer to the official ISO source.

#### Open codelist updates

* [#386](https://github.com/open-contracting/standard/issues/386) **[Document type](http://standard.open-contracting.org/1.1/en/schema/codelists/#document-type)** - New codes have been added to the documentType codelist, and definitions of codes updated.
* [#322](https://github.com/open-contracting/standard/issues/322) **[Submission Method Codelist](http://standard.open-contracting.org/1.1/en/schema/codelists/#submission-method)** - The submissionMethod codelist has been updated
* [#387](https://github.com/open-contracting/standard/issues/387) **[Codelist updates: Item Classification Scheme](http://standard.open-contracting.org/1.1/en/schema/codelists/#item-classification-scheme)** - New entries have been added to the itemClassificationScheme codelist
* [#385](https://github.com/open-contracting/standard/issues/385) **[Codelist updates: awardCriteria](http://standard.open-contracting.org/1.1/en/schema/codelists/#award-criteria)** - Revising the awardCriteria codelist, with all existing codes deprecated and a new set of codes introduced. 


### Added

* [#371](https://github.com/open-contracting/standard/issues/371) **[Linking related processes](http://standard.open-contracting.org/1.1/en/schema/reference/#relatedprocess)** - We have introduced a new RelatedProcess block at the release and contract level
* [#374](https://github.com/open-contracting/standard/issues/374) **[Duration in periods](http://standard.open-contracting.org/1.1/en/schema/reference/#period)** - We have introduced fields for duration in days, and maximum extent, to the period building block
* [#374](https://github.com/open-contracting/standard/issues/374) **[Contract and Award Periods in Tender](http://standard.open-contracting.org/1.1/en/schema/reference/#tender)** - We have introduced contract period in tender and updated the definition of award period.
* [#376](https://github.com/open-contracting/standard/issues/376) **[Contract type (supplies, works and services)](http://standard.open-contracting.org/1.1/en/schema/codelists/#procurement-category)** - We have introduced a procurementCategory field to specify whether contracts are for supplies, works, services, consultancyServices or mixed
* [#373](https://github.com/open-contracting/standard/issues/373) **[Milestone types](http://standard.open-contracting.org/1.1/en/schema/codelists/#milestone-type)** - We have introduced the milestoneType property and codelist
* [#366](https://github.com/open-contracting/standard/issues/366) **[Unit of Measure - additional fields and codelist](http://standard.open-contracting.org/1.1/en/schema/reference/#unit)** - We have introduced a structured classification for unitOfMeasure on each item, with a recommendation to use UNCEFACT.

### Extensions

* [#335](https://github.com/open-contracting/standard/issues/335) **[Core and community extensions](http://standard.open-contracting.org/1.1/en/extensions/)** - We have introduced widespread use of extensions throughout the standard. An extension provides fields and data structures that are optional, either because   (a) they are only relevant in particular contexts or contracting processes; or   (b) they represent a 'stretch goal' for most data publishers, and so are not currently suitable for inclusion in the main standard.   We divide these extensions into 'core extensions' which have wide enough relevance, and technical maturity to be included in the main standard documentation (and which are versioned along with the standard documentation), and 'community extensions' which may have less technical maturity, or which might be versioned independently of the main standard.
* [#259](https://github.com/open-contracting/standard/issues/259) **[Enquiries](https://extensions.open-contracting.org/en/extensions/enquiries/)** - We have introduced a core enquiries extension for providing information on enquiries received during the tender stage.
* [#342](https://github.com/open-contracting/standard/issues/342) **[Overall contracting process description](http://standard.open-contracting.org/1.1/en/schema/reference/#release)** - We have introduced a new top-level title and description for the contracting process as a core extension.
* [#274](https://github.com/open-contracting/standard/issues/274) **[New property of contract: extendsContractID](http://standard.open-contracting.org/1.1/en/schema/reference/#contract)** - We have introduced a new field 'extendsContractID' to the Contract block to support contract cross-referencing between contracts.
* [#381](https://github.com/open-contracting/standard/issues/381) **[Lots](https://extensions.open-contracting.org/en/extensions/lots/)** - We have introduced a core extension to provide a model for contracting processes which are divided into lots.
* [#379](https://github.com/open-contracting/standard/issues/379) **[Bids and Bid Statistics](https://extensions.open-contracting.org/en/extensions/bids/)** - We have introduced a core extension which provides a top level Bids section, with BidStatistics and Bid building blocks for detailed information on individual bids. This supersedes the current tender/tenderers section.
* [#250](https://github.com/open-contracting/standard/issues/250) **[Location extension](https://extensions.open-contracting.org/en/extensions/location/)** - We have moved the location extensions to become a core extension
* [#33](https://github.com/open-contracting/standard/issues/33) **[Participation fees (bid document and submission costs)](https://extensions.open-contracting.org/en/extensions/participation_fee/)** - We have introduced a core extension for declaring the participation fees related to a contracting process.
* [#249](https://github.com/open-contracting/standard/issues/249) **[Extend contract with a supplier array](https://extensions.open-contracting.org/en/extensions/contract_suppliers/)** - We have introduced a core extension to allow inclusion of supplier information at the contract level.

### Deprecated

* [#355](https://github.com/open-contracting/standard/issues/355) **[Deprecating milestone documents](http://standard.open-contracting.org/1.1/en/schema/reference/#milestone)** - We have deprecated milestone documents from core, and added a milestone documents extension for those who wish to continue to use documents at the milestone level.
* [#368](https://github.com/open-contracting/standard/issues/368) **[Updates to organization handling in OCDS](http://standard.open-contracting.org/1.1/en/schema/reference/#parties)** - We have deprecated use of the full organization block at points other than the parties array.
* [#372](https://github.com/open-contracting/standard/issues/372) **[Updates to transactions terminology](http://standard.open-contracting.org/1.1/en/schema/reference/#transaction)** - receiverOrganization, providerOrganization and amount properties have been deprecated in favour or other terms.

## [1.0.3] - 2017-07-31

### Fixed

* [#329](https://github.com/open-contracting/standard/issues/329) - updated `item.quantity` to support decimal values (integer -> number)
* [#253](https://github.com/open-contracting/standard/issues/253) - updated `value.amount` to support negative values

## [1.0.2] - 2016-11-22

### Changed

### Fixed

- Added titles to all fields in the documentation (#362)
- Missing field `procurementMethodDetails` added to schema (#221)
- Typo fix in releaseTag (#391)
- Fixing links to Fiscal Data Package (#271)
- Description for `numberOfTenderers` (#314)
- Fixed definition of `changes` (#244)
- Updated documentation to refer to 'Object' not 'Reference' for fields (#228)

### Tidy up

- Removed the old Spanish documentation translations folders from `standard/docs/es`
- Added CSV download links for registered ocids, and publication levels
- Updated publication levels spreadsheet to reflect version 1.0.2

## [1.0.1] - 2016-03-14

Updated documentation was released. This did not make any semantic changes to the standard.

## [1.0] - 2015-07-29

### Changed

- `contractPeriod` added to `award` to allow the anticipated period of a contract to be recorded, without requiring the creation of a contract block. Discussed in [#199](https://github.com/open-contracting/standard/issues/199)

- Updated codelists

### Fixed

- Minor documentation fixes.

## [1.0.RC] - 2014-11-18

Changes prior to this point are not covered by this changelog. A non-exhaustive overview of changes between the beta release and 1.0.RC can be [found on the project blog](https://www.open-contracting.org/2014/11/18/release-of-data-standard/).
