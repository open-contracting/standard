# Normative and non-normative content and changes

```
This document contains our policy on normative and non-normative content and changes within the standard's documentation. 
```

## Key concepts

**Normative**: [Normative content](https://en.wikipedia.org/wiki/Normative#Standards_documents) is the prescriptive part of a standard. It sets the rules to be followed in order to be evaluated as compliant with the standard, and from which no deviation is permitted. 

**Non-normative**: Non-normative content is the non-prescriptive, or ‘descriptive’, part of a standard. This may include analogies, synonyms, explanations, illustrations, context, and examples. In the event non-normative content contradicts normative content, the normative content is to be followed. (For examples of non-normative content, see [Non-normative content](#non-normative-content).)

**Compliant**: Something that is evaluated as fulfilling the criteria (i.e. following the rules) set by the normative content of a standard. It is synonymous withfconformant**.

**Open Contracting Data Standard (OCDS)**: The Open Contracting Data Standard is the normative content at [standard.open-contracting.org](https://standard.open-contracting.org). (For a list of normative content, see [Normative content](#normative-content).)

**OCDS data**: Data that complies with OCDS.

**Content**: Content is anything meaningful, whether it is text (e.g. a sentence on a web page or in a Markdown file; a JSON fragment; a CSV field), an image or otherwise.

## Which content is covered?

The file paths below are based on the structure of the ‘[standard’ repository](https://github.com/open-contracting/standard) as of version 1.1.3.

### Normative content

As stated in the [Translation and localization policy](https://docs.google.com/document/d/1GLwWTpgDDkKmMr1hZE4D75LI8VQtFiD0VA7TF_FvY_Q/edit), “The authoritative language for the standard is English. All translations into other languages are provided for the convenience of users, and in case of conflict or ambiguity, the English text supersedes all translations.” In other words, the content listed below is normative within each translation, but must be consistent with the English source.

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
* Accessible under [https://standard.open-contracting.org/latest/en/](https://standard.open-contracting.org/latest/en/) ([example](https://standard.open-contracting.org/latest/en/release-schema.json))
* Rendered as tables and using Docson under [Schema Reference](https://standard.open-contracting.org/latest/en/schema/) ([example](https://standard.open-contracting.org/latest/en/schema/release/))
* Located in the [`schema` directory](https://github.com/open-contracting/standard/tree/1.1-dev/schema)

These files link to web pages, including:

* Non-normative documentation pages ([Publication policies](https://standard.open-contracting.org/latest/en/implementation/publication_policy/))
* External codelists ([ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), [BCP47](https://www.w3.org/International/articles/language-tags/), [IANA Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml), [QUDT Units](https://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html))
* Normative links ([Open Definition Conformant Licenses](http://opendefinition.org/licenses/))
* Non-normative links ([Fiscal Data Package](http://fiscal.dataprotocols.org/), [IATI Transactions](http://iatistandard.org/activity-standard/iati-activities/iati-activity/transaction/), [OpenCorporates](http://www.opencorporates.com))

#### Codelist CSV files

These files are presently:

* Rendered as tables on the [Codelists page](https://standard.open-contracting.org/latest/en/schema/codelists/)
* Located in the [`schema/codelists` directory](https://github.com/open-contracting/standard/tree/1.1-dev/schema/codelists)

The JSON Schema files determine whether a codelist is closed or open.

#### Schema reference Markdown files

These files are presently:

* Rendered as web pages under, and including, the [Schema Reference page](https://standard.open-contracting.org/latest/en/schema/)
* Located in the [`docs/schema` directory](https://github.com/open-contracting/standard/tree/1.1-dev/docs/schema)

These files link to non-normative documentation pages, including:

* Getting Started: [Building blocks](https://standard.open-contracting.org/latest/en/getting_started/building_blocks/), [Releases and records](https://standard.open-contracting.org/latest/en/getting_started/releases_and_records/)
* Guidance: [Licensing](https://standard.open-contracting.org/latest/en/implementation/licensing/), [Publication policies](https://standard.open-contracting.org/latest/en/implementation/publication_policy/), [Registration](https://standard.open-contracting.org/latest/en/implementation/registration/), [Amendments](https://standard.open-contracting.org/latest/en/implementation/amendments/), [Extensions](https://standard.open-contracting.org/latest/en/extensions/)
* Getting Help: [Support](https://standard.open-contracting.org/latest/en/support/)

#### Other Markdown files

The [Governance page](https://standard.open-contracting.org/latest/en/support/governance/) ([in repository](https://github.com/open-contracting/standard/blob/1.1-dev/docs/schema/governance.md)), except the [upgrade_process_feb_2016.png](https://github.com/open-contracting/standard/blob/1.1-dev/docs/_static/png/upgrade_process_feb_2016.png) image, which is superseded by accompanying text in case of conflict or ambiguity.

#### License files

`LICENSE` or `LICENSE.md`.

#### Core extensions

The same JSON Schema files, codelist CSV files and license files as described above are normative within each unlabelled (i.e. X.X.X but not X.X.X-alpha) release of each core extension.

### Non-normative content

Non-normative content may describe any concepts not described by the standard, for example: [data licensing](https://standard.open-contracting.org/latest/en/implementation/licensing/) and [alternative serializations](https://standard.open-contracting.org/latest/en/implementation/serialization/#csv). It may support the standard’s implementation and the use of standardized data in different contexts or scenarios, for example: [framework agreements](https://standard.open-contracting.org/latest/en/implementation/related_processes/).

It is useful to explicitly list some of the non-normative content, to be clear that it was not omitted in error from the ‘normative content’ section above:

* `extension.json` in any extension
* All images in the standard repository
* The [extension registry](https://github.com/open-contracting/extension_registry)
* The [Extension Explorer](https://extensions.open-contracting.org/en/)
* The [extension template](https://github.com/open-contracting/standard_extension_template)
* Unregistered extensions

The following may become normative content in future versions. If so, it should be moved to the standard repository, distributed at [standard.open-contracting.org](https://standard.open-contracting.org), and rendered as part of the documentation:

* [extension-schema.json](https://raw.githubusercontent.com/open-contracting/standard-maintenance-scripts/master/schema/extension-schema.json)
* [codelist-schema.json](https://raw.githubusercontent.com/open-contracting/standard-maintenance-scripts/master/schema/codelist-schema.json)

The following [Implementation guidance](https://standard.open-contracting.org/latest/en/implementation/) may contain content that should be moved to a [Schema reference Markdown file](#schema-reference-markdown-files):

* [Serialization](https://standard.open-contracting.org/latest/en/implementation/serialization/), including the requirement to use the [I-JSON format](https://standard.open-contracting.org/latest/en/implementation/serialization/#json)

## Normative and non-normative changes

### Normative changes

Normative changes are changes to normative content, except:

* Changes that produce no visible changes to outputs, the outputs being:
    * [standard.open-contracting.org](https://standard.open-contracting.org/) HTML pages. If a change to a Markdown file results in no change to translations, then it is considered invisible.
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
* Changes to markup that result in no change to meaning or behavior. For example, moving a normative statement into a [‘hint’ admonition](http://ocds-standard-development-handbook.readthedocs.io/en/latest/meta/style_guide/#admonitions) would change meaning. Using a monospace font for a field’s name wouldn’t change meaning. 
* Corrections of links broken by changes in the structure of the documentation or of third-party sites. If a broken link is within a normative statement, or if the target of a broken link is normative content, either the new target must make no normative changes to the old target, or the new target should be an archived copy of the old target, to avoid changing the meaning of the link.

### Non-normative changes

All other changes are non-normative changes.

## Change management

Normative content must not change without a clear process and sufficient notice, to ensure relevant stakeholders are involved. Changes to normative content, and the impact on stakeholders, must be communicated. The [governance process](https://standard.open-contracting.org/latest/en/support/governance/) presently assures this.

On the other hand, it should be possible to add or improve non-normative content based on implementation experience on an ongoing basis, without triggering the governance process, which may stall these changes.

Whether a change requires a PATCH, MINOR or MAJOR version is described in the [Versions](https://standard.open-contracting.org/latest/en/support/governance/#versions) section of the Governance page. (Note: This section will be [expanded](https://github.com/open-contracting/standard/pull/674/files).)

The pull requests for all changes, regardless of the process they follow, SHOULD be approved by at least one person knowledgeable of the standard, other than the author.

### Non-normative changes

Non-normative changes are permitted at any time, whether in a new version or a released version. Pull requests SHOULD still be approved as above to ensure that the changes are indeed non-normative and do not conflict with normative content.

### Normative changes

#### JSON Schema files

* All normative changes to these files MUST be made in a new version.

#### Codelist CSV files

* The [currency codelist](https://standard.open-contracting.org/latest/en/schema/codelists/#currency) is closed, but mirrors the [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html), and therefore MAY be updated to mirror those codes in a PATCH version.
* A code MAY be added to, or removed from, an open codelist in a PATCH version.
* Any other normative changes to these files MUST be made in a new version.

#### Schema reference Markdown files

* All normative changes to these files MUST be made in a new version.

#### Other Markdown files

The change management process for the [Governance page](https://standard.open-contracting.org/latest/en/support/governance/) is not yet defined.

#### License files

The change management process for the [standard’s LICENSE file](https://github.com/open-contracting/standard/blob/1.1-dev/LICENSE) is not yet defined.

#### Core extensions

* All normative changes to these files MUST be made in a new version.

## Next steps

* Clearly mark documentation pages or sections as normative or non-normative. [[GitHub #846](https://github.com/open-contracting/standard/issues/846)]
* Use [RFC 2119](https://tools.ietf.org/html/rfc2119) keywords (MUST, SHOULD, MAY, etc.) where appropriate. [[GitHub #830](https://github.com/open-contracting/standard/issues/830)]
* Expand the [conformance statement](https://standard.open-contracting.org/latest/en/schema/conformance_and_extensions/) with a summary of OCDS norms. [[GitHub #580](https://github.com/open-contracting/standard/issues/580)]
* Update the [Governance page](https://standard.open-contracting.org/latest/en/support/governance/) with more detail on versioning. [[GitHub #674](https://github.com/open-contracting/standard/pull/674)]
* Update the [Governance page](https://standard.open-contracting.org/latest/en/support/governance/) with detail on how the governance process itself can be updated, including changes to the license and copyright holder of the standard. [[GitHub #832](https://github.com/open-contracting/standard/issues/832)]
* Part or all of the `README.md` and `docs/` files of _core_ extensions _may_ be normative. There is presently no formal division between normative and non-normative content in an extension’s documentation. This document should be updated once a formal division is made.

## Changelog

### 2020-02-25

* Updated links and descriptions of content to match changes to documentation

### 2019-06-25

* First version (OCDS 1.1.4).
