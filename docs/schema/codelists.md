# Codelists

Some schema fields refer to codelists, to limit and standardize the possible values of the fields, in order to promote data interoperability.

Codelists can either be open or closed;

* **Closed codelists** are intended to be comprehensive; for example, the [currency](codelists/currency.md) codelist covers all currencies in the world.
* **Open codelists** are intended to be representative, but not comprehensive.

Publishers must use the codes in the codelists, unless no code is appropriate. If no code is appropriate and the codelist is **open**, then a publisher may use a new code outside those in the codelist. If no code is appropriate and the codelist is **closed**, then a publisher is encouraged to create an issue in the [OCDS GitHub repository](https://github.com/open-contracting/standard/issues) about adding a new code.

```{admonition} Extending open codelists
:class: note

If you use new codes outside those in an open codelist, please document the codes in an [OCDS extension](../guidance/map/extensions) and in your [publication policy](../guidance/publish.md#finalize-your-publication-policy). Please also create an issue in the [OCDS GitHub repository](https://github.com/open-contracting/standard/issues), so that the codes can be considered for inclusion in the codelist.
```

The release schema, in [JSON Schema](../../build/current_lang/release-schema.json), has a `codelist` property to indicate the <a href="../../codelists/">CSV File</a> that defines the codes in the codelist (shown as tables below). It also has an `openCodelist` property, to indicate whether the codelist is open or closed.

Codes are case-sensitive, and are generally provided as English language camelCase. Codes must not be translated, though the OCDS team will work with publishers to translate code titles and definitions.

```{toctree}
:hidden:

codelists/awardCriteria
codelists/awardFinalStatus
codelists/awardStatus
codelists/classificationScheme
codelists/contractFinalStatus
codelists/contractStatus
codelists/country
codelists/currency
codelists/documentType
codelists/extendedProcurementCategory
codelists/initiationType
codelists/language
codelists/linkRelationType
codelists/mediaType
codelists/method
codelists/milestoneStatus
codelists/milestoneType
codelists/organizationIdentifierScheme
codelists/partyRole
codelists/partyScale
codelists/procurementCategory
codelists/relatedProcess
codelists/relatedProcessScheme
codelists/releaseTag
codelists/submissionMethod
codelists/tenderFinalStatus
codelists/tenderStatus
codelists/unitClassificationScheme
```

## Uncategorized

[Release Tag](codelists/releaseTag.md)

[Classification Scheme](codelists/classificationScheme.md)

[Document Type](codelists/documentType.md)

[Milestone Type](codelists/milestoneType.md)

[Initiation Type](codelists/initiationType.md) {bdg-danger}`deprecated`

## Status

[Tender Final Status](codelists/tenderFinalStatus.md)

[Award Final Status](codelists/awardFinalStatus.md)

[Contract Final Status](codelists/contractFinalStatus.md)

[Milestone Status](codelists/milestoneStatus.md)

[Tender Status](codelists/tenderStatus.md) {bdg-danger}`deprecated`

[Award Status](codelists/awardStatus.md) {bdg-danger}`deprecated`

[Contract Status](codelists/contractStatus.md) {bdg-danger}`deprecated`

## Organization

[Organization Role](codelists/partyRole.md)

[Organization Identifier Scheme](codelists/organizationIdentifierScheme.md)

[Party Scale](codelists/partyScale.md)

## Tender

[Method](codelists/method.md)

[Procurement Category](codelists/procurementCategory.md)

[Extended Procurement Category](codelists/extendedProcurementCategory.md)

[Award Criteria](codelists/awardCriteria.md)

[Submission Method](codelists/submissionMethod.md) {bdg-danger}`deprecated`

## Related process

[Related Process](codelists/relatedProcess.md)

[Related Process](codelists/relatedProcessScheme.md)

## External

[Country](codelists/country.md) ([ISO 3166-1 alpha-2](https://www.iso.org/iso-3166-country-codes.html))

[Currency](codelists/currency.md) ([ISO4217](https://www.iso.org/iso-4217-currency-codes.html))

[Language](codelists/language.md) ([ISO639-1](https://id.loc.gov/vocabulary/iso639-1.html))

[Link Relation Type](codelists/linkRelationType.md) ([IANA Link Relation Types](https://www.iana.org/assignments/link-relations/link-relations.xhtml))

[Media Type](codelists/mediaType.md) ([IANA Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml))
