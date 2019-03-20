# Extensions

OCDS provides a common core of [sections and building blocks](../getting_started/building_blocks.md) for describing contracting processes. 

Many publishers will have additional data that they could publish. Instead of ignoring this data and leaving it unpublished, OCDS encourages publishers to collaborate on the creation of **extensions** to the standard. 

Extensions are divided into two types:

* **Core** extensions are maintained as part of the standard governance process, documented as part of the standard and reviewed by the OCDS technical team with each version upgrade of OCDS. They are likely to be relevant to a large number of publishers and users.

* **Community** and local extension are maintained by third-parties, or are maintained outside of the standard governance process. They may provide features required by only a small number of publishers or users, or may be used to document a publisher's additional fields or codelist values.

All core and community extensions are listed in the [extensions registry](https://github.com/open-contracting/extension_registry) and in the documentation here. The [standard technical team](../support/governance.md) approves extensions for inclusion in the registry (distinguishing community from local extensions) and for inclusion in the governance process (distinguishing core from community extensions).

## Using extensions

Extensions are applied by adding their URLs to the `extensions` array in the release or record package. To use one or more extensions, select them from the extension lists below and include the following in your release or record package metadata:

<style><!--
#using-extensions div[class^='highlight'] pre {
   white-space: pre-wrap;  
   white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
   white-space: -pre-wrap;      /* Opera 4-6 */
   white-space: -o-pre-wrap;    /* Opera 7 */
   word-wrap: break-word;       /* Internet Explorer 5.5+ */
}
--></style> 

```json
{
    "extensions":[],
    "releases":[]
}
```

## Core extensions

```eval_rst
.. extensionselectortable::
   :group: core
```

## Community extensions

```eval_rst
.. extensionselectortable::
   :group: community
```


## More information

```eval_rst
.. toctree::
   :maxdepth: 2

   developing
   community

```

### Core extension documentation pages

```eval_rst
.. toctree::
   :maxdepth: 1
   :glob:

   party_details

```

