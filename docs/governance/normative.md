# Normative and non-normative content and changes

```{admonition} Summary
This document contains our policy on normative and non-normative content and changes within the standard's documentation.
```

## Key concepts

**Normative**: [Normative content](https://en.wikipedia.org/wiki/Normative#Standards_documents) is the prescriptive part of a standard. It sets the rules to be followed in order to be evaluated as compliant with the standard, and from which no deviation is permitted.

**Non-normative**: Non-normative content is the non-prescriptive, or "descriptive", part of a standard. This may include analogies, synonyms, explanations, illustrations, context, and examples. In the event non-normative content contradicts normative content, the normative content is to be followed. (For examples of non-normative content, see [Non-normative content](#non-normative-content).)

**Compliant**: Something that is evaluated as fulfilling the criteria (i.e. following the rules) set by the normative content of a standard. It is synonymous with **conformant**.

**Open Contracting Data Standard (OCDS)**: The Open Contracting Data Standard is the normative content at [standard.open-contracting.org](https://standard.open-contracting.org). (For a list of normative content, see [Normative content](#normative-content).)

**OCDS data**: Data that complies with OCDS.

**Content**: Content is anything meaningful, whether it is text (e.g. a sentence on a web page or in a Markdown file; a JSON fragment; a CSV field), an image or otherwise.

## Which content is covered?

### Normative content

As stated in the [Translation and localization policy](translation), "The authoritative language for the standard is English. All translations into other languages are provided for the convenience of users, and in case of conflict or ambiguity, the English text supersedes all translations." In other words, the content listed below is normative within each translation, but must be consistent with the English source.

Hyperlinks from normative content to non-normative content should be audited to ensure that the destinations do not, in fact, contain normative content that is not found elsewhere.

The following content is considered normative:

#### JSON Schema files

Specifically:

* `release-schema.json`
* `release-package-schema.json`
* `record-package-schema.json`
* `versioned-release-validation-schema.json`

These files are presently:

* Accessible at [https://standard.open-contracting.org/schema/](https://standard.open-contracting.org/schema/)
* Accessible under [https://standard.open-contracting.org/latest/en/](../index) ([example](../../build/current_lang/release-schema.json))
* Rendered as tables and using Docson under [Reference](../schema/index) ([example](../schema/release))
* Located in the [`schema` directory](https://github.com/open-contracting/standard/tree/HEAD/schema)

These files link to web pages, including:

* Non-normative documentation pages ([Finalize your publication policy](../guidance/publish.md#finalize-your-publication-policy))
* External codelists ([BCP47](https://www.w3.org/International/articles/language-tags/))
* Normative links ([Open Definition Conformant Licenses](https://opendefinition.org/licenses/))
* Non-normative links ([Fiscal Data Package](https://specs.frictionlessdata.io/fiscal-data-package/), [IATI Transactions](https://iatistandard.org/en/iati-standard/203/activity-standard/iati-activities/iati-activity/transaction/), [OpenCorporates](https://opencorporates.com))

#### Codelist CSV files

These files are presently:

* Rendered as tables under, and including, the [Codelists page](../schema/codelists)
* Located in the [`schema/codelists` directory](https://github.com/open-contracting/standard/tree/HEAD/schema/codelists)

The JSON Schema files determine whether a codelist is closed or open.

#### Schema reference Markdown files

These files are presently:

* Rendered as web pages under, and including, the [Reference page](../schema/index)
* Located in the [`docs/schema` directory](https://github.com/open-contracting/standard/tree/HEAD/docs/schema)

These files link to non-normative documentation pages, including:

* [Guidance](../guidance/index) pages
* [Support](../support/index) page

#### Other Markdown files

The [Governance page](index) ([in repository](https://github.com/open-contracting/standard/blob/HEAD/docs/governance/index.md)), except the [upgrade_process.png](https://github.com/open-contracting/standard/blob/HEAD/docs/_static/png/upgrade_process.png) image, which is superseded by accompanying text in case of conflict or ambiguity.

#### License files

`LICENSE` or `LICENSE.md`.

#### Core extensions

The same JSON Schema files, codelist CSV files and license files as described above are normative within each unlabelled (i.e. X.X.X but not X.X.X-alpha) release of each core extension.

### Non-normative content

Non-normative content may describe any concepts not described by the standard, for example: [data licensing](../guidance/publish.md#license-your-data) and [alternative serializations](../guidance/build/serialization.md#csv). It may support the standard's implementation and the use of standardized data in different contexts or scenarios, for example: [framework agreements](../guidance/map/framework_agreements).

It is useful to explicitly list some of the non-normative content, to be clear that it was not omitted in error from the "normative content" section above:

* `extension.json` in any extension
* All images in the standard repository
* The [extension registry](https://github.com/open-contracting/extension_registry)
* The [Extension Explorer](https://extensions.open-contracting.org/en/)
* The [extension template](https://github.com/open-contracting/standard_extension_template)
* Unregistered extensions

The following may become normative content in future versions. If so, it should be moved to the standard repository, distributed at [standard.open-contracting.org](https://standard.open-contracting.org), and rendered as part of the documentation:

* [extension-schema.json](https://raw.githubusercontent.com/open-contracting/standard-maintenance-scripts/master/schema/extension-schema.json)
* [codelist-schema.json](https://raw.githubusercontent.com/open-contracting/standard-maintenance-scripts/master/schema/codelist-schema.json)

## Normative and non-normative changes

### Normative changes

Normative changes are changes to normative content, except:

* Changes that produce no visible changes to outputs, the outputs being:
    * [standard.open-contracting.org](https://standard.open-contracting.org) HTML pages. If a change to a Markdown file results in no change to translations, then it is considered invisible.
    * Codelist CSV files
    * JSON Schema files
        * `release-schema.json`
        * `release-package-schema.json`
        * `record-package-schema.json`
        * `versioned-release-validation-schema.json`
    * Extension metadata file (`extension.json`)
    * `LICENSE` and `LICENSE.md` files
* Whitespace changes that produce no non-whitespace changes to outputs. Indentation changes in JSON files are allowed.
* Fixes of typographical and markup errors that result in no change to meaning or behavior. For example, fixing a typo in a code in a codelist CSV file, or in a field name like `uniqueItems` in a JSON Schema file, would change behavior. Fixing typos in `description` columns or `description` fields wouldn't change behavior.
* Changes to markup that result in no change to meaning or behavior. For example, moving a normative statement into a "hint" admonition would change meaning. Using a monospace font for a field's name wouldn't change meaning.
* Corrections of links broken by changes in the structure of the documentation or of third-party sites. If a broken link is within a normative statement, or if the target of a broken link is normative content, either the new target must make no normative changes to the old target, or the new target should be an archived copy of the old target, to avoid changing the meaning of the link.

### Non-normative changes

All other changes are non-normative changes.

## Change management

Normative content must not change without a clear process and sufficient notice, to ensure relevant stakeholders are involved. Changes to normative content, and the impact on stakeholders, must be communicated. The [governance process](index) presently assures this.

On the other hand, it should be possible to add or improve non-normative content based on implementation experience on an ongoing basis, without triggering the governance process, which may stall these changes.

Whether a change requires a PATCH, MINOR or MAJOR version is described in the [Versions](index.md#versions) section of the Governance page.

The pull requests for all changes, regardless of the process they follow, SHOULD be approved by at least one person knowledgeable of the standard, other than the author.

### Non-normative changes

Non-normative changes are permitted at any time, whether in a new version or a released version. Pull requests SHOULD still be approved as above to ensure that the changes are indeed non-normative and do not conflict with normative content.

### Normative changes

#### JSON Schema files

* All normative changes to these files MUST be made in a new version.

#### Codelist CSV files

* The [currency codelist](../schema/codelists.md#currency) is closed, but mirrors the [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html), and therefore MAY be updated to mirror those codes in a PATCH version.
* A code MAY be added to, or removed from, an open codelist in a PATCH version.
* Any other normative changes to these files MUST be made in a new version.

#### Schema reference Markdown files

* All normative changes to these files MUST be made in a new version.

#### Other Markdown files

The change management process for the [Governance page](index) is not yet defined.

#### License files

The change management process for the [standard's LICENSE file](https://github.com/open-contracting/standard/blob/HEAD/LICENSE) is not yet defined.

#### Core extensions

* All normative changes to these files MUST be made in a new version.
