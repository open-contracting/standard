# Extensions

OCDS provides a common core of [sections and building blocks](../getting_started/building_blocks.md) for describing contracting processes. 

Many publishers will have additional data that they could publish. Instead of ignoring this data and leaving it unpublished, OCDS encourages publishers to collaborate on the creation of **extensions** to the standard. 

Extensions are divided into two types:

* **Core** extensions are maintained as part of the standard governance process, documented as part of the standard and reviewed by the OCDS technical team with each version upgrade of OCDS. They are likely to be relevant to a large number of publishers and users.

* **Community** and local extension are maintained by third-parties, or are maintained outside of the standard governance process. They may provide features required by only a small number of publishers or users, or may be used to document a publisher's additional fields or codelist values.

All core and community extensions are listed in the [Extension Explorer](https://extensions.open-contracting.org/en/). The [standard technical team](../support/governance.md) approves extensions for inclusion in the registry (distinguishing community from local extensions) and for inclusion in the governance process (distinguishing core from community extensions).

## Using existing extensions

Extensions are applied by adding their URLs to the `extensions` array in the release package or record package. You can discover extensions, read their documentation and find the URL to add using the [Extension Explorer](https://extensions.open-contracting.org/en/).

This version of OCDS uses these specific versions of core extensions:

```eval_rst
 .. extensionexplorerlinklist::

```

Groups of extensions can be combined into **profiles**. Profiles are adaptations of OCDS to suit the disclosure requirements and user needs of a particular sector, type of contracting process or legal framework. [View the list of profiles.](https://www.open-contracting.org/data-standard/profiles-and-guidance/)

## Developing new extensions

If you have additional fields which cannot be mapped to the OCDS schema or an existing extension, you should include these in your OCDS data and create a new extension to document their structure and meaning.

### Extension template

You can find the [extension template](https://github.com/open-contracting/standard_extension_template) on GitHub. It contains guidance on creating an extension.
