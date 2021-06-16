# Extensions

OCDS provides a common core of [sections and building blocks](../../getting_started/building_blocks) for describing contracting processes.

Many publishers will have additional data that they could publish. Instead of ignoring this data and leaving it unpublished, OCDS encourages publishers to collaborate on the creation of **extensions** to the standard. 

Extensions are divided into two types:

* **Core** extensions are maintained as part of the standard governance process, documented as part of the standard and reviewed by the OCDS technical team with each version upgrade of OCDS. They are likely to be relevant to a large number of publishers and users.

* **Community** and local extension are maintained by third-parties, or are maintained outside of the standard governance process. They might provide features needed by only a small number of publishers or users, or might be used to document a publisher's additional fields or codelist values.

All core and community extensions are listed in the [Extension Explorer](https://extensions.open-contracting.org/en/). The [standard technical team](../../governance/index) approves extensions for inclusion in the Extension Explorer (distinguishing community from local extensions) and for inclusion in the governance process (distinguishing core from community extensions).

## Using existing extensions

Extensions are applied by adding their URLs to the `extensions` array in the release package or record package. You can discover extensions, read their documentation and find the URL to add using the [Extension Explorer](https://extensions.open-contracting.org/en/).

This version of OCDS uses these specific versions of core extensions:

```{extensionexplorerlinklist}
```

## Developing new extensions

If you have additional fields which cannot be mapped to the OCDS schema or an existing extension, you ought to include these in your OCDS data and create a new extension to document their structure and meaning.

### Extension template

You can find the [extension template](https://github.com/open-contracting/standard_extension_template) on GitHub. It contains guidance on creating an extension.

## Profiles

Groups of extensions can be combined into **profiles**. OCDS provides a common core for describing contracting processes, which profiles expand to suit the disclosure requirements and user needs of a particular sector or legal framework.

### OCDS for Public-Private Partnerships

[OCDS for Public-Private Partnerships](https://standard.open-contracting.org/profiles/ppp/latest/en/) (PPPs) describes how to use OCDS to publish information about PPPs. The profile extends OCDS to offer a data format that follows the World Bank Group’s [Framework for Disclosure in Public-Private Partnership Projects](https://www.worldbank.org/en/topic/publicprivatepartnerships/brief/ppp-tools#T1).

### OCDS for the European Union

[OCDS for the European Union](https://standard.open-contracting.org/profiles/eu/latest/en/) describes how to express, in OCDS, the information in Tenders Electronic Daily (TED) notices as obliged by law within the EU.

### OCDS for the Agreement on Government Procurement

[OCDS for the Agreement on Government Procurement](https://standard.open-contracting.org/profiles/gpa/latest/en/) (GPA) describes how to use OCDS to publish information as obliged by the World Trade Organization’s [Agreement on Government Procurement](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm).
