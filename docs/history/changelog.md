# Changelog

These release notes describe what's new in each version. OCDS adheres to [Semantic Versioning](https://semver.org/).

## Iterative improvements

Per the [normative and non-normative content and changes policy](https://docs.google.com/document/d/1xjlAneqgewZvHh6_hwuQ98hbjxRcA2IUqOTJiNGcOf8/edit), iterative improvements to non-normative content can be made outside the release cycle.

### Documentation

* Getting Started section:
  * [#980](https://github.com/open-contracting/standard/pull/980) Remove references to ☆ levels.
  * [#1017](https://github.com/open-contracting/standard/pull/1017) Add link to bulk downloads in Guidance section.
* [#955](https://github.com/open-contracting/standard/pull/955) Split the Guidance section into sub-sections. Add a new History section, and move the Changelog, Credits, and History and Development pages to it.
* [#958](https://github.com/open-contracting/standard/pull/958) Governance page: Change responsibility for prioritization review to OCP's Head of Data Products & Services. Change "technical team" to "standard development team".
* Guidance section:
  * [#986](https://github.com/open-contracting/standard/pull/986) Add implementation guidance from OCP website.
  * [#1013](https://github.com/open-contracting/standard/pull/1013) Replace guidance on publication levels.
  * [#963](https://github.com/open-contracting/standard/pull/963) Remove guidance on web discovery.
  * [#1016](https://github.com/open-contracting/standard/pull/1016) Add links to OCDS profiles and linked standards.
  * [#986](https://github.com/open-contracting/standard/pull/986) Merge Registration page into Build page.
  * [#986](https://github.com/open-contracting/standard/pull/986) [#1012](https://github.com/open-contracting/standard/pull/1012) Merge Publication policy and Licensing pages into Publish page.
  * Add worked examples for the Map phase [#947](https://github.com/open-contracting/standard/pull/947) [#948](https://github.com/open-contracting/standard/pull/948) [#950](https://github.com/open-contracting/standard/pull/950) [#974](https://github.com/open-contracting/standard/pull/974) [#990](https://github.com/open-contracting/standard/pull/990) [#999](https://github.com/open-contracting/standard/pull/999) [#1007](https://github.com/open-contracting/standard/pull/1007).
  * Add worked examples for the Build phase [#951](https://github.com/open-contracting/standard/pull/951) [#997](https://github.com/open-contracting/standard/pull/997).
  * [#1150](https://github.com/open-contracting/standard/pull/1150) Align language in Build phase with language in Map phase.
* [#960](https://github.com/open-contracting/standard/pull/960) Support section: Merge Tools page into Support page.
* [#959](https://github.com/open-contracting/standard/pull/959) History section: Merge Credits and History of OCDS pages into Development and Appreciation page. Update history from present perspective.
* [#908](https://github.com/open-contracting/standard/pull/908) Rename Validator to Data Review Tool.
* [#975](https://github.com/open-contracting/standard/pull/975) Add a Make target to generate PDFs of the documentation.
* Copy-edit and re-organize non-normative pages [#979](https://github.com/open-contracting/standard/pull/979) [#1018](https://github.com/open-contracting/standard/pull/1018) [#1023](https://github.com/open-contracting/standard/pull/1023).
* Update the changelog [#932](https://github.com/open-contracting/standard/pull/932) [#976](https://github.com/open-contracting/standard/pull/976).
* Make changes to how the documentation is built [#880](https://github.com/open-contracting/standard/pull/880) [#886](https://github.com/open-contracting/standard/pull/886) [#889](https://github.com/open-contracting/standard/pull/889) [#905](https://github.com/open-contracting/standard/pull/905) [#915](https://github.com/open-contracting/standard/pull/915) [#916](https://github.com/open-contracting/standard/pull/916) [#923](https://github.com/open-contracting/standard/pull/923) [#935](https://github.com/open-contracting/standard/pull/935) [#944](https://github.com/open-contracting/standard/pull/944) [#945](https://github.com/open-contracting/standard/pull/945) [#946](https://github.com/open-contracting/standard/pull/946) [#953](https://github.com/open-contracting/standard/pull/953) [#962](https://github.com/open-contracting/standard/pull/962) [#964](https://github.com/open-contracting/standard/pull/964) [#1002](https://github.com/open-contracting/standard/pull/1002) [#1003](https://github.com/open-contracting/standard/pull/1003).

## [1.1.5] - 2020-08-20

* The [Translation and localization policy](../../governance/#translation-and-localization-policy) is amended to read "normative content will be translated into all core supported languages *as soon as possible*" instead of "*before the release*". A Spanish translation is ready for release, and a French translation will be ready as soon as possible.

### Codelists

* `itemClassificationScheme.csv`:
  * [#998](https://github.com/open-contracting/standard/pull/998) Add 'NAICS', 'PSC' and 'HS' codes.
  * [#967](https://github.com/open-contracting/standard/pull/967) Remove the discouragement of the 'UNSPSC' code.
  * [#1033](https://github.com/open-contracting/standard/pull/1033) Add a `Category` column to indicate the context in which the classification scheme is used.
* `milestoneType.csv`:
  * [#1000](https://github.com/open-contracting/standard/pull/1000) Update description of 'financing' code, and add 'payment' code.

### Schema

* [#969](https://github.com/open-contracting/standard/pull/969) Clarify the instruction for setting the `Unit.id` field.
* [#995](https://github.com/open-contracting/standard/pull/995) Clarify the instruction for setting the `Release.date` field.
* [#996](https://github.com/open-contracting/standard/pull/996) Fix a typo in the `versionedRelease` field.

### Documentation

* [#966](https://github.com/open-contracting/standard/pull/966) Move Governance and Deprecation pages to new Governance section.
* [#968](https://github.com/open-contracting/standard/pull/968) [#1032](https://github.com/open-contracting/standard/pull/1032) Use "field" to refer to OCDS fields and "property" to refer to JSON Schema properties.
* [#970](https://github.com/open-contracting/standard/pull/970) Add links to access the release schema as a CSV spreadsheet and via the Field-Level Mapping Template. Add notes to describe the alternatives for browsing the schemas.
* [#965](https://github.com/open-contracting/standard/pull/965) Release Reference page: Add extensions list for the Transaction object.
* [#970](https://github.com/open-contracting/standard/pull/970) Release Schema page: Correct the description of compiled releases.
* [#996](https://github.com/open-contracting/standard/pull/996) Record Reference page: Rewrite page to improve clarity.
* Codelists page:
  * [#971](https://github.com/open-contracting/standard/pull/971) [#1032](https://github.com/open-contracting/standard/pull/1032) Remove the suggestion to use X prefixes, for the reasons expressed by the [IETF](https://tools.ietf.org/html/rfc6648#appendix-B).
  * [#972](https://github.com/open-contracting/standard/pull/972) Clarify the norms around open and closed codelists.
  * [#973](https://github.com/open-contracting/standard/pull/973) Describe the `openCodelist` and `codelist` JSON Schema properties.
  * [#1036](https://github.com/open-contracting/standard/pull/1036) Add instruction for OCDS publishers to contact the OCDS Helpdesk to add list codes to org-id.guide.

### Extensions

See the changelogs for:

* [Bid statistics and details](https://extensions.open-contracting.org/en/extensions/bids/master/#changelog)
* [Enquiries](https://extensions.open-contracting.org/en/extensions/enquiries/master/#changelog)
* [Location](https://extensions.open-contracting.org/en/extensions/location/master/#changelog)
* [Lots](https://extensions.open-contracting.org/en/extensions/lots/master/#changelog)
* [Milestone documents](https://extensions.open-contracting.org/en/extensions/milestone_documents/master/#changelog)
* [Participation fees](https://extensions.open-contracting.org/en/extensions/participation_fee/master/#changelog)
* [Process level title and description](https://extensions.open-contracting.org/en/extensions/process_title/master/#changelog)

## [1.1.4] - 2019-06-25

### Advisories

* OCDS 1.0 uses the [whole-list merge](https://standard.open-contracting.org/1.1/en/schema/merging/#whole-list-merge) strategy for `Award.suppliers`, whereas OCDS 1.1 uses the [identifier merge](https://standard.open-contracting.org/1.1/en/schema/merging/#identifier-merge) strategy. As a consequence, the OCDS 1.1 versioned release schema is not backward compatible with OCDS 1.0.
  * **Action:** Versioned releases respecting the OCDS 1.0 schema that set `Award.suppliers` will need to be re-created to validate against the OCDS 1.1 schema.
* [#780](https://github.com/open-contracting/standard/pull/780) All extensions authored by the Open Contracting Partnership have been moved to the [open-contracting-extensions](https://github.com/open-contracting-extensions) organization.
  * **Action:** No change is required, but we recommend that publishers update the URLs of these extensions in their release packages and record packages.
* [#831](https://github.com/open-contracting/standard/pull/831) OCDS now has a [Normative and non-normative content and changes policy](https://docs.google.com/document/d/1xjlAneqgewZvHh6_hwuQ98hbjxRcA2IUqOTJiNGcOf8/edit).
* [#744](https://github.com/open-contracting/standard/pull/744) OCDS now has a [Translation and localization policy](https://standard.open-contracting.org/1.1/en/schema/governance/#translation-and-localization-policy).
* [#806](https://github.com/open-contracting/standard/pull/806) [#808](https://github.com/open-contracting/standard/pull/808) [#809](https://github.com/open-contracting/standard/pull/809) The documentation is now available in Italian.
* [#717](https://github.com/open-contracting/standard/pull/717) [#734](https://github.com/open-contracting/standard/pull/734) The OCDS documentation website now has a [privacy notice](https://standard.open-contracting.org/1.1/en/privacy-notice/).

### Bugs

* [#738](https://github.com/open-contracting/standard/pull/738) 1.1.3 changed the merging and versioning behaviors of `Item.unit`, such that it could be removed by setting it to `null`, and such that it was versioned as a whole. 1.1.4 restores the behaviors from 1.1.2, such that only its sub-fields can be removed by setting them to `null`, and such that its sub-fields are versioned individually.
  * **Action:** If you had upgraded to OCDS 1.1.3, then compiled releases and versioned releases that set `Item.unit` will likely need to be re-created to validate against the OCDS 1.1.4 schema.
* [#810](https://github.com/open-contracting/standard/pull/810) `buyer.id`, `Tender.procuringEntity.id`, `Contract.implementation.payer.id` `Contract.implementation.payee.id`, `Budget.id`, `Identifier.id`, and `Classification.id` are now versioned, consistent with the documentation.
  * **Action:** Versioned releases that set these fields will likely need to be re-created to validate against the OCDS 1.1.4 schema.
* [#769](https://github.com/open-contracting/standard/pull/769) The versioned release schema now matches the release schema in: having a `minLength` validation property for `OrganizationReference.name`; having `codelist` and `openCodelist` properties for `Tender.awardCriteria`, `Tender.awardCriteriaDetails`, `Document.documentType`, `Item.unit.scheme`, `Classification.scheme`, and `RelatedProcess.scheme`; and having a `deprecated` property for `Budget.source`. All `title` and `description` metadata properties are removed from the versioned release schema.
* [#810](https://github.com/open-contracting/standard/pull/810) `tag` is now `omitWhenMerged`, consistent with the reference implementation in OCDS Merge.

### Codelists

* [#824](https://github.com/open-contracting/standard/pull/824) Canonical codelist files are available at URLs like <https://standard.open-contracting.org/schema/1__1__5/codelists/>, and translations are available at URLs like <https://standard.open-contracting.org/1.1/en/codelists/>, for OCDS 1.1.4 and up.
* [#746](https://github.com/open-contracting/standard/pull/746) [#842](https://github.com/open-contracting/standard/pull/842) Update the currency codelist for ISO4217 amendments [166](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_166.pdf), [167](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_167.pdf), [168](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_168.pdf) and [169](https://www.currency-iso.org/dam/downloads/dl_currency_iso_amendment_169.pdf).
* [#725](https://github.com/open-contracting/standard/pull/725) Add a 'plannedProcurementNotice' code to the `documentType` codelist, 'CUCOP' to `itemClassificationScheme`, 'interestedParty' to `partyRole`.
* [#725](https://github.com/open-contracting/standard/pull/725) Update the descriptions of the 'tenderNotice' and 'technicalSpecifications' codes in the `documentType` codelist to align with the text of the [Agreement on Government Procurement (GPA)](https://www.wto.org/english/tratop_e/gproc_e/gp_gpa_e.htm) of the World Trade Organization (WTO).
* [#725](https://github.com/open-contracting/standard/pull/725) Apply the style guide and OCDS glossary to the 'procuringEntity' and 'supplier' codes in the `partyRole` codelist.
* [#725](https://github.com/open-contracting/standard/pull/725) Add examples to the description of the 'environmentalImpact' code in the `documentType` codelist.
* [#829](https://github.com/open-contracting/standard/pull/829) Use sentence case for code titles and end code descriptions with periods.
* [#852](https://github.com/open-contracting/standard/pull/852) Use the correct normative keywords in code descriptions.

### Schema

* [#712](https://github.com/open-contracting/standard/pull/712) Add missing titles for `publisher` and `url` and description for `record` in the record package schema, and missing description for `releases` in release package schema.
* [#838](https://github.com/open-contracting/standard/pull/838) Eliminate the conflicting rule that release identifiers must be unique within release packages. Uniqueness within the scope of a release package either implies that release identifiers must be globally unique, or imposes an arbitrary restriction on the contents of release packages, as there is no rule preventing release packages from containing releases from different contracting processes. Release identifiers are only required to be locally unique within the scope of a contracting process. The `ocid` and `id` values of a release can be used together to disambiguate releases within a release package.
* Clarify the uniqueness of release identifiers in the release schema [#838](https://github.com/open-contracting/standard/pull/838) and release package schema [#831](https://github.com/open-contracting/standard/pull/831).
* [#810](https://github.com/open-contracting/standard/pull/810) Add a dereferenced release schema to ease the implementation of the merge routine.
* [#810](https://github.com/open-contracting/standard/pull/810) Add `"versionId": true` hint to `Identifier` and `Classification`.
* [#845](https://github.com/open-contracting/standard/pull/845) Remove a reference to a closed issue and a note about a field name.
* [#855](https://github.com/open-contracting/standard/pull/855) Use the correct normative keywords in field descriptions.
* [#855](https://github.com/open-contracting/standard/pull/855) Rephrase field descriptions as definitions rather than instructions.
* [#855](https://github.com/open-contracting/standard/pull/855) Align the descriptions of the `license` fields in the release package schema and record package schema.

### Documentation

* [#772](https://github.com/open-contracting/standard/pull/772) [#810](https://github.com/open-contracting/standard/pull/810) [#831](https://github.com/open-contracting/standard/pull/831) Clarify the merge rules for compiled releases and versioned releases.
* [#797](https://github.com/open-contracting/standard/pull/797) Fix examples of versioned releases.
* [#831](https://github.com/open-contracting/standard/pull/831) Use the correct normative keywords in the documentation.
* [#869](https://github.com/open-contracting/standard/pull/869) Move normative statements into normative sections.
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
* Correct typos in the documentation [#692](https://github.com/open-contracting/standard/pull/692) [#713](https://github.com/open-contracting/standard/pull/713) [#719](https://github.com/open-contracting/standard/pull/719) [#726](https://github.com/open-contracting/standard/pull/726) [#732](https://github.com/open-contracting/standard/pull/732) [#752](https://github.com/open-contracting/standard/pull/752) [#756](https://github.com/open-contracting/standard/pull/756) [#795](https://github.com/open-contracting/standard/pull/795) [#867](https://github.com/open-contracting/standard/pull/867).
* Make changes to how the documentation is built [#666](https://github.com/open-contracting/standard/pull/666) [#698](https://github.com/open-contracting/standard/pull/698) [#708](https://github.com/open-contracting/standard/pull/708) [#709](https://github.com/open-contracting/standard/pull/709) [#721](https://github.com/open-contracting/standard/pull/721) [#724](https://github.com/open-contracting/standard/pull/724) [#727](https://github.com/open-contracting/standard/pull/727) [#729](https://github.com/open-contracting/standard/pull/729) [#733](https://github.com/open-contracting/standard/pull/733) [#740](https://github.com/open-contracting/standard/pull/740) [#747](https://github.com/open-contracting/standard/pull/747) [#753](https://github.com/open-contracting/standard/pull/753) [#762](https://github.com/open-contracting/standard/pull/762) [#767](https://github.com/open-contracting/standard/pull/767) [#783](https://github.com/open-contracting/standard/pull/783) [#787](https://github.com/open-contracting/standard/pull/787) [#796](https://github.com/open-contracting/standard/pull/796) [#813](https://github.com/open-contracting/standard/pull/813) [#836](https://github.com/open-contracting/standard/pull/836) [#875](https://github.com/open-contracting/standard/pull/875).

### Extensions

See the changelogs for:

* [Bid statistics and details](https://extensions.open-contracting.org/en/extensions/bids/master/#changelog)
* [Enquiries](https://extensions.open-contracting.org/en/extensions/enquiries/master/#changelog)
* [Location](https://extensions.open-contracting.org/en/extensions/location/master/#changelog)
* [Lots](https://extensions.open-contracting.org/en/extensions/lots/master/#changelog)
* [Participation fees](https://extensions.open-contracting.org/en/extensions/participation_fee/master/#changelog)
* [Process level title and description](https://extensions.open-contracting.org/en/extensions/process_title/master/#changelog)

## [1.1.3] - 2018-04-16

### Bugs

* [#646](https://github.com/open-contracting/standard/pull/646) Disallow use of `null` as an entry in the array for `Tender.additionalProcurementCategories`.
* [#639](https://github.com/open-contracting/standard/issues/639) Make `name` field optional for `OrganizationReference`.
* [#630](https://github.com/open-contracting/standard/issues/630) Allow optional field `Item.unit` to be `null`. **(Reverted in 1.1.4)**
* [a75c1c5](https://github.com/open-contracting/standard/pull/667/commits/a75c1c50379881f618df97ed3b9967297ed2edca) Make `record-package-schema.json` use the `codelist` property to reference `releaseTag.csv`, and update the `enum` accordingly.

### Codelists

* Update the currency codelist for ISO4217 amendment 165 (2017-12-14).

### Schema

* [#603](https://github.com/open-contracting/standard/issues/603), [#645](https://github.com/open-contracting/standard/issues/645) Add definitions to `Release`, `planning.budget`, `Milestone`, `Organization.address`, `Organization.contactPoint`, `Classification`, `Identifier`, `Value` and `Period`.
* [#578](https://github.com/open-contracting/standard/issues/578) Update the definition of the `buyer` field to cover goods, works and services, and multiple buyers.

### Documentation

* [#633](https://github.com/open-contracting/standard/issues/633) Update schema reference page to display `Release.relatedProcesses`, `Planning.documents` and `Contract.relatedProcesses`.
* [#634](https://github.com/open-contracting/standard/issues/634) Clarify definitions of core, community and local extensions.
* Old and unused scripts have been removed from the documentation repository, and a number of script dependencies have been updated.

### Extensions

* [#40](https://github.com/open-contracting/ocds-extensions/issues/40), [#43](https://github.com/open-contracting/ocds-extensions/issues/43), [#47](https://github.com/open-contracting/ocds-extensions/issues/47) Add missing definitions, codelists and enums to core extensions, correct typos in codelist filenames, disallow use of `null` as an item in arrays, disallow required fields from being set to `null`, allow optional fields to be `null`, use `OrganizationReference` instead of `Organization`.

## [1.1.2] - 2017-11-10

### Codelists

* [#554](https://github.com/open-contracting/standard/issues/554) Update the currency codelist for ISO4217 amendment 163 (2017-06-09). XBT (Bitcoin) is removed from the codelist as it is not part of ISO4217.

## [1.1.1] - 2017-07-31

### Bugs

* [#482](https://github.com/open-contracting/standard/issues/482) Allow optional field `parties.role` to be `null`.
* [#479](https://github.com/open-contracting/standard/issues/479) Remove `releases` as a required field in [`record-package-schema.json`](https://standard.open-contracting.org/1.1/en/schema/record_package/).
* [#475](https://github.com/open-contracting/standard/issues/475) Add an `enum` property to every field in the schema with a closed codelist.

### Codelists

* [#422](https://github.com/open-contracting/standard/issues/422) Include a [currency codelist](https://standard.open-contracting.org/1.1/en/schema/codelists/#currency) in the documentation and schema.
* [#471](https://github.com/open-contracting/standard/issues/471) Update the [milestoneType codelist](https://standard.open-contracting.org/1.1/en/schema/codelists/#milestone-type), replacing 'planning' with 'preProcurement' and 'adjudication' with 'assessment', and introducing 'approval' and 'financing'. This is an open codelist, so the old codes remain valid, but publishers able to update to the new codes should do so.
* [#473](https://github.com/open-contracting/standard/issues/473) Update the definition of the 'contractSchedule' code in the [documentType codelist](https://standard.open-contracting.org/1.1/en/schema/codelists/#document-type).

### Documentation

* [#480](https://github.com/open-contracting/standard/pull/480/commits/c3c41225639a06b0b0552016b32e2fe2e901a8fe) Align the tables and text in the [publication levels](https://standard.open-contracting.org/1.1/en/implementation/levels/) guidance.
* [#489](https://github.com/open-contracting/standard/issues/489) Change the milestone documents extension to a core extension. This extension is only needed by publishers with legacy data containing documents within milestones.
* [#493](https://github.com/open-contracting/standard/issues/493) Update the description of the [Organization Identifier Scheme codelist](https://standard.open-contracting.org/1.1/en/schema/codelists/#organization-identifier-scheme), to reflect that it is now maintained by [org-id.guide](http://www.org-id.guide/).
* [#506](https://github.com/open-contracting/standard/issues/506) Remove `make_field_definitions.py` from the utility scripts, as it is no longer required.
* Fix typographic errors throughout the documentation and codelist descriptions.
* Add docstrings to utility scripts.

## [1.1.0] - 2017-05-01

### Policy changes

* [#401](https://github.com/open-contracting/standard/issues/401) **[Deprecation policy](https://standard.open-contracting.org/1.1/en/schema/conformance_and_extensions/)** - The deprecation policy has been updated to support deprecation in decimal upgrades.

### Changed

#### Structural updates 

* [#368](https://github.com/open-contracting/standard/issues/368) **[Updates to organization handling in OCDS](https://standard.open-contracting.org/1.1/en/schema/reference/#parties)** - We have updated the approach to include organization information in the standard from having embedded blocks of organization information, to using embedded cross-references to a top-level 'parties' array where full organization details are stored. This change reduces duplication of organization information, and enables more flexible disclosure of information on all the parties to a contracting process, including multiple buyers.
* [#357](https://github.com/open-contracting/standard/issues/357) **[Amendment handling](https://standard.open-contracting.org/1.1/en/implementation/amendments/)** - We have replace amendment with an array of amendments, and have updated schema and guidance to remove the option of providing semi-structured changes in an amendment object. Changes between amendments should now be provided using multiple releases, with the option to explicitly declare how releases relate to an amendment included in the new amendments array. 

#### Schema validation updates 

* [#329](https://github.com/open-contracting/standard/issues/329) **[Float for Item.quantity](https://standard.open-contracting.org/1.1/en/schema/reference/#item)** - Item quantities has been updated to 'number' to support decimal values (e.g 10.5 rather than just 10)
* [#253](https://github.com/open-contracting/standard/issues/253) **[Negative amounts](https://standard.open-contracting.org/1.1/en/schema/reference/#budget)** - We have added support for negative amounts in transactions
* [#323](https://github.com/open-contracting/standard/issues/323) **[Standard should specify use of UTF-8 for encoding JSON](https://standard.open-contracting.org/1.1/en/implementation/serialization/#json)** - We now recommend use of I-JSON and UTF-8 for JSON publication
* [#166](https://github.com/open-contracting/standard/issues/166) **[Indicate encoding for CSV serializations](https://standard.open-contracting.org/1.1/en/implementation/serialization/#multi-table)** - We have added information on CSV encoding to the implementation guidance to recommend UTF-8 or Windows-1252.
* [#336](https://github.com/open-contracting/standard/issues/336) **[Codelist properties in schema](https://github.com/open-contracting/standard/commit/ee1db256d7364ee70e3553f4384d9908bff604a6)** - We have included explicit references to the codelist files (CSV versions) in the schema. This will be used in future versions of the validator to support validation against codelists.
* [#301](https://github.com/open-contracting/standard/issues/301) **[Specifying versions and extensions in package metadata](https://standard.open-contracting.org/1.1/en/schema/records_reference/#package-metadata)** - We have updated the package schemas to require that version is declared, and to provide a means of declaring extensions in use. This will be used in future versions of the validator to support validation against extensions.
* [#287](https://github.com/open-contracting/standard/issues/287) **[Remove all ocdsMerge strategies](https://standard.open-contracting.org/1.1/en/schema/merging/)** - We have remove all 'merge strategies' from the schema as these are no longer required, now that all objects in arrays contain an id element.

#### Schema definition updates 

* [#372](https://github.com/open-contracting/standard/issues/372) **[Updates to transactions terminology](https://standard.open-contracting.org/1.1/en/schema/reference/#transaction)** - We have replaced receiverOrganization and providerOrganization with payee and payer, to align with more familiar terminology, and have replaced 'amount' with 'value' for consistency with other areas of the standard.
* [#378](https://github.com/open-contracting/standard/issues/378) **[Updates to core budget block](https://standard.open-contracting.org/1.1/en/schema/reference/#budget)** - We have updated references to the Fiscal Data Package in the schema.
* [#337](https://github.com/open-contracting/standard/issues/337) **[Definition of "tenderer" to enhance clarity](https://standard.open-contracting.org/1.1/en/schema/reference/#tender)** - We have updated the definition of tenderer in the tenders block, and cross-referenced the bid extension.
* [#259](https://github.com/open-contracting/standard/issues/259) **[Enquiries](https://extensions.open-contracting.org/en/extensions/enquiries/)** - We have updated the definition of hasEnquiries.
* [#246](https://github.com/open-contracting/standard/issues/246) **[In what scope must a release ID be unique?](https://standard.open-contracting.org/1.1/en/schema/reference/#release)** - We have updated the definition of release.id to reflect the scope in which it must be unique

#### Closed codelist updates

* [#201](https://github.com/open-contracting/standard/issues/201) **[Tender status](https://standard.open-contracting.org/1.1/en/schema/codelists/#tender-status)** - New 'planning' and 'withdrawn' codes have been introduced to the tenderStatus codelist.
* [#380](https://github.com/open-contracting/standard/issues/380) **[Procurement method](https://standard.open-contracting.org/1.1/en/schema/codelists/#method)** - A new code for 'direct' has been added the procurementMethod codelist
* [#373](https://github.com/open-contracting/standard/issues/373) **[Milestone status](https://standard.open-contracting.org/1.1/en/schema/codelists/#milestone-status)** - We have updated the milestoneStatus codelist with a 'scheduled' entry and revised definitions
* [#297](https://github.com/open-contracting/standard/issues/297) **[Currency codelist external link](https://standard.open-contracting.org/1.1/en/schema/codelists/#currency)** - We have fixed the external link for currency codelists to refer to the official ISO source.

#### Open codelist updates

* [#386](https://github.com/open-contracting/standard/issues/386) **[Document type](https://standard.open-contracting.org/1.1/en/schema/codelists/#document-type)** - New codes have been added to the documentType codelist, and definitions of codes updated.
* [#322](https://github.com/open-contracting/standard/issues/322) **[Submission Method Codelist](https://standard.open-contracting.org/1.1/en/schema/codelists/#submission-method)** - The submissionMethod codelist has been updated
* [#387](https://github.com/open-contracting/standard/issues/387) **[Codelist updates: Item Classification Scheme](https://standard.open-contracting.org/1.1/en/schema/codelists/#item-classification-scheme)** - New entries have been added to the itemClassificationScheme codelist
* [#385](https://github.com/open-contracting/standard/issues/385) **[Codelist updates: awardCriteria](https://standard.open-contracting.org/1.1/en/schema/codelists/#award-criteria)** - Revising the awardCriteria codelist, with all existing codes deprecated and a new set of codes introduced. 

### Added

* [#371](https://github.com/open-contracting/standard/issues/371) **[Linking related processes](https://standard.open-contracting.org/1.1/en/schema/reference/#relatedprocess)** - We have introduced a new RelatedProcess block at the release and contract level
* [#374](https://github.com/open-contracting/standard/issues/374) **[Duration in periods](https://standard.open-contracting.org/1.1/en/schema/reference/#period)** - We have introduced fields for duration in days, and maximum extent, to the period building block
* [#374](https://github.com/open-contracting/standard/issues/374) **[Contract and Award Periods in Tender](https://standard.open-contracting.org/1.1/en/schema/reference/#tender)** - We have introduced contract period in tender and updated the definition of award period.
* [#376](https://github.com/open-contracting/standard/issues/376) **[Contract type (supplies, works and services)](https://standard.open-contracting.org/1.1/en/schema/codelists/#procurement-category)** - We have introduced a procurementCategory field to specify whether contracts are for supplies, works, services, consultancyServices or mixed
* [#373](https://github.com/open-contracting/standard/issues/373) **[Milestone types](https://standard.open-contracting.org/1.1/en/schema/codelists/#milestone-type)** - We have introduced the milestoneType property and codelist
* [#366](https://github.com/open-contracting/standard/issues/366) **[Unit of Measure - additional fields and codelist](https://standard.open-contracting.org/1.1/en/schema/reference/#unit)** - We have introduced a structured classification for unitOfMeasure on each item, with a recommendation to use UNCEFACT.

### Extensions

* [#335](https://github.com/open-contracting/standard/issues/335) **[Core and community extensions](https://standard.open-contracting.org/1.1/en/extensions/)** - We have introduced widespread use of extensions throughout the standard. An extension provides fields and data structures that are optional, either because   (a) they are only relevant in particular contexts or contracting processes; or   (b) they represent a 'stretch goal' for most data publishers, and so are not currently suitable for inclusion in the main standard.   We divide these extensions into 'core extensions' which have wide enough relevance, and technical maturity to be included in the main standard documentation (and which are versioned along with the standard documentation), and 'community extensions' which may have less technical maturity, or which might be versioned independently of the main standard.
* [#259](https://github.com/open-contracting/standard/issues/259) **[Enquiries](https://extensions.open-contracting.org/en/extensions/enquiries/)** - We have introduced a core enquiries extension for providing information on enquiries received during the tender stage.
* [#342](https://github.com/open-contracting/standard/issues/342) **[Overall contracting process description](https://standard.open-contracting.org/1.1/en/schema/reference/#release)** - We have introduced a new top-level title and description for the contracting process as a core extension.
* [#274](https://github.com/open-contracting/standard/issues/274) **[New property of contract: extendsContractID](https://standard.open-contracting.org/1.1/en/schema/reference/#contract)** - We have introduced a new field 'extendsContractID' to the Contract block to support contract cross-referencing between contracts.
* [#381](https://github.com/open-contracting/standard/issues/381) **[Lots](https://extensions.open-contracting.org/en/extensions/lots/)** - We have introduced a core extension to provide a model for contracting processes which are divided into lots.
* [#379](https://github.com/open-contracting/standard/issues/379) **[Bids and Bid Statistics](https://extensions.open-contracting.org/en/extensions/bids/)** - We have introduced a core extension which provides a top level Bids section, with BidStatistics and Bid building blocks for detailed information on individual bids. This supersedes the current tender/tenderers section.
* [#250](https://github.com/open-contracting/standard/issues/250) **[Location extension](https://extensions.open-contracting.org/en/extensions/location/)** - We have moved the location extensions to become a core extension
* [#33](https://github.com/open-contracting/standard/issues/33) **[Participation fees (bid document and submission costs)](https://extensions.open-contracting.org/en/extensions/participation_fee/)** - We have introduced a core extension for declaring the participation fees related to a contracting process.
* [#249](https://github.com/open-contracting/standard/issues/249) **[Extend contract with a supplier array](https://extensions.open-contracting.org/en/extensions/contract_suppliers/)** - We have introduced a core extension to allow inclusion of supplier information at the contract level.

### Deprecated

* [#355](https://github.com/open-contracting/standard/issues/355) **[Deprecating milestone documents](https://standard.open-contracting.org/1.1/en/schema/reference/#milestone)** - We have deprecated milestone documents from core, and added a milestone documents extension for those who wish to continue to use documents at the milestone level.
* [#368](https://github.com/open-contracting/standard/issues/368) **[Updates to organization handling in OCDS](https://standard.open-contracting.org/1.1/en/schema/reference/#parties)** - We have deprecated use of the full organization block at points other than the parties array.
* [#372](https://github.com/open-contracting/standard/issues/372) **[Updates to transactions terminology](https://standard.open-contracting.org/1.1/en/schema/reference/#transaction)** - receiverOrganization, providerOrganization and amount properties have been deprecated in favour or other terms.

## [1.0.3] - 2017-07-31

### Bugs

* [#329](https://github.com/open-contracting/standard/issues/329) Update `Item.quantity` to allow decimal values.
* [#253](https://github.com/open-contracting/standard/issues/253) Update `Value.amount` to allow negative values.

## [1.0.2] - 2016-11-22

### Schema

* [#362](https://github.com/open-contracting/standard/issues/362) Add a `title` property to all fields.
* [#221](https://github.com/open-contracting/standard/issues/221) Add the missing `procurementMethodDetails` field.
* [#391](https://github.com/open-contracting/standard/issues/391) Fix typo in `description` property of `releaseTag` field.
* [#271](https://github.com/open-contracting/standard/issues/271) Fix link to Fiscal Data Package.
* [#314](https://github.com/open-contracting/standard/issues/314) Add a `description` property to the `numberOfTenderers` field.
* [#244](https://github.com/open-contracting/standard/issues/244) Fix the `description` property of the `changes` field.

### Documentation

* [#228](https://github.com/open-contracting/standard/issues/228) Update the documentation to use "Object" not "Reference" in Format column of field tables.
* Add CSV download links for registered ocids and publication levels.
* Update the publication levels spreadsheet to reflect above changes.
* Remove the old Spanish documentation translations from `standard/docs/es`.

## [1.0.1] - 2016-03-14

### Bugs

* [#300](https://github.com/open-contracting/standard/issues/300) Remove `"format": "uri"` from `publisher.scheme` field.
* [#295](https://github.com/open-contracting/standard/issues/295) Allow optional fields `Award.status` and `Contract.status` to be `null`.
* [#267](https://github.com/open-contracting/standard/issues/267) Rename codes in documentType codelist: 'Tender notice' to 'tenderNotice', 'Award notice' to 'awardNotice', 'Contract notice' to 'contractNotice'.
* Fix bugs in versioned release schema.

### Codelists

* Remove reference to non-existent `statusDescription` field in awardStatus codelist.

### Schema

* Add or update `title` and `description` properties.
* [#283](https://github.com/open-contracting/standard/issues/283) Remove `"mergeStrategy": "ocdsVersion"` from `planning.budget` field.

### Documentation

* Restructure the documentation, including: expanding Getting Started section, adding more examples.
* Fix broken links.
* Make changes to how the documentation is built, including: improving the translation process, adding some schema tests.

## [1.0.0] - 2015-07-29

### Codelists

* Update `documentType` and `organizationIdentifierRegistrationAgency_iati` codelists.

### Schema

* [#199](https://github.com/open-contracting/standard/issues/199) Add the `Award.contractPeriod` field, to disclose the anticipated contract period without creating a `Contract` object.
* Update the `description` property of the `Award.date` field.

### Documentation

* Fix typos in Markdown text and JSON examples.
* Add changelog.

## [1.0.RC] - 2014-11-18

Changes prior to this release are not covered here. Please see the [overview of changes](https://www.open-contracting.org/2014/11/18/release-of-data-standard/) between the beta and 1.0.RC releases.
