# Codelists

Some schema fields refer to codelists, to limit and standardize the possible values of the fields, in order to promote data interoperability.

Codelists can either be open or closed. **Closed codelists** are intended to be comprehensive; for example, the [currency](#currency) codelist covers all currencies in the world. **Open codelists** are intended to be representative, but not comprehensive.

Publishers must use the codes in the codelists, unless no code is appropriate. If no code is appropriate and the codelist is **open**, then a publisher may use a new code outside those in the codelist. If no code is appropriate and the codelist is **closed**, then a publisher is encouraged to create an issue in the [OCDS GitHub repository](https://github.com/open-contracting/standard/issues) about adding a new code.

```{admonition} Extending open codelists
:class: note

If you use new codes outside those in an open codelist, please document the codes in an [OCDS extension](../guidance/map/extensions) and in your [publication policy](../guidance/publish.md#finalize-your-publication-policy). Please also create an issue in the [OCDS GitHub repository](https://github.com/open-contracting/standard/issues), so that the codes can be considered for inclusion in the codelist.
```

The release schema, in [JSON Schema](../../build/current_lang/release-schema.json), has a `codelist` property to indicate the <a href="../../codelists/">CSV File</a> that defines the codes in the codelist (shown as tables below). It also has an `openCodelist` property, to indicate whether the codelist is open or closed.

Codes are case-sensitive, and are generally provided as English language camelCase. Codes must not be translated, though the OCDS team will work with publishers to translate code titles and definitions.

## All Codelists

### [Award Criteria](codelists/awardCriteria.md)

### [Award Final Status](codelists/awardFinalStatus.md)

### [Award Status](codelists/awardStatus.md)

### [Classification Scheme](codelists/classificationScheme.md)

### [Contract Final Status](codelists/contractFinalStatus.md)

### [Contract Status](codelists/contractStatus.md)

### [Country](codelists/country.md)

### [Currency](codelists/currency.md)

### [Document Type](codelists/documentType.md)

### [Extended Procurement Category](codelists/extendedProcurementCategory.md)

### [Initiation Type](codelists/initiationType.md)

### [Language](codelists/language.md)

### [Link Relation Type](codelists/linkRelationType.md)

### [Media Type](codelists/mediaType.md)

### [Method](codelists/method.md)

### [Milestone Status](codelists/milestoneStatus.md)

### [Milestone Type](codelists/milestoneType.md)

### [Organization Identifier Scheme](codelists/organizationIdentifierScheme.md)

### [Organization Role](codelists/partyRole.md)

### [Party Scale](codelists/partyScale.md)

### [Procurement Category](codelists/procurementCategory.md)

### [Release Tag](codelists/releaseTag.md)

### [Related Process](codelists/relatedProcess.md)

### [Related Process](codelists/relatedProcessScheme.md)

### [Submission Method](codelists/submissionMethod.md)

### [Tender Final Status](codelists/tenderFinalStatus.md)

### [Tender Status](codelists/tenderStatus.md)
