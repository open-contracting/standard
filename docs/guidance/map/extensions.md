# Extensions

OCDS provides a common core of [sections](../../schema/reference.md#release-structure) and [sub-schemas](../../schema/reference.md#sub-schema-reference) for describing contracting (or planning) processes.

Many publishers will have additional data that they could publish. Instead of ignoring this data and leaving it unpublished, OCDS encourages publishers to collaborate on the creation of **extensions** to the standard.

Some extensions are maintained by the Open Contracting Partnership (OCP). Those that are likely to be relevant to a large number of publishers and users follow the [governance process](../../governance/index). The standard development team decides which extensions follow the governance process.

Other extensions are maintained by third parties, like OCDS publishers, and do not follow the governance process. These extensions might provide features which are needed by only a small number of publishers or users, or they might be used to document a specific publisher's additional fields or codelist values.

All OCP extensions and many third-party extensions are documented in the [Extension Explorer](https://extensions.open-contracting.org/en/). The [standard development team](../../governance/index) decides which extensions are registered in the [Extension Registry](https://github.com/open-contracting/extension_registry#readme), which controls which extensions appear in the Extension Explorer.

You are encouraged to consider using the extensions tagged as *Recommended* in the Extension Explorer.

## Using existing extensions

Extensions are applied by adding their URLs to the `extensions` array in the release package or record package. You can discover extensions, read their documentation and find the URL to add using the [Extension Explorer](https://extensions.open-contracting.org/en/).

This version of OCDS uses these specific versions of the following extensions:

```{extensionexplorerlinklist}
```

## Developing new extensions

If you have additional fields which cannot be mapped to the OCDS schema or an existing extension, you ought to include these in your OCDS data and create a new extension to document their structure and meaning.

### Extension template

You can find the [extension template](https://github.com/open-contracting/standard_extension_template) on GitHub. It contains guidance on creating an extension.

## Profiles

Groups of extensions can be combined into **profiles**. OCDS provides a common core for describing contracting (or planning) processes, which profiles expand to suit the disclosure requirements and user needs of a particular sector or legal framework.

### OCDS for Public-Private Partnerships

[OCDS for Public-Private Partnerships](https://standard.open-contracting.org/profiles/ppp/latest/en/) (PPPs) describes how to use OCDS to publish information about PPPs. The profile extends OCDS to offer a data format that follows the World Bank Group's [Framework for Disclosure in Public-Private Partnership Projects](https://www.worldbank.org/en/topic/publicprivatepartnerships/brief/ppp-tools#T1).

### OCDS for the European Union

[OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/) describes how to express, in OCDS, the information in Tenders Electronic Daily (TED) notices as obliged by law within the EU.

### OCDS for the Agreement on Government Procurement

[OCDS for the Agreement on Government Procurement](https://standard.open-contracting.org/profiles/gpa/latest/en/) (GPA) describes how to use OCDS to publish information as obliged by the World Trade Organization's [Agreement on Government Procurement](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm).
