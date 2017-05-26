# Extensions

OCDS provides a common core of [sections and building blocks](../../../getting_started/building_blocks.md) for describing contracting processes. 

Many publishers will have additional data that they could publish. Instead of ignoring this data and leaving it unpublished, OCDS encourages publishers to collaborate on the creation of **extensions** to the standard. 

Extensions are divided into two types:

* **Core** extensions are documented as part of the standard and reviewed by the OCDS technical team with each version upgrade of OCDS. They are likely to be relevant to a large number of publishers and users.

* **Community** extension are maintained by third-parties, or are maintained outside of the standard governance process. They may provide features required by only a small number of publishers or users.

Some extensions with wide adoption may be considered for inclusion as part of the core standard in future versions. Others may be maintained independently by particular communities that need to align the publication of particular additional information.


## Using extensions

Extension are applied by adding their URLs to the ```extensions``` array in the release or record package. To use one or more extensions, select them from the extension lists below and include the following in your release or record package meta-data:

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

**Core extensions**

```eval_rst
.. extensionselectortable::
   :group: core
```

**Community extensions**

```eval_rst
.. extensionselectortable::
   :group: community
```


## More about extensions

```eval_rst
.. toctree::
   :maxdepth: 2

   developing
   community

```

## Core extensions

```eval_rst
.. toctree::
   :maxdepth: 1
   :glob:

   bids
   enquiries
   location
   lots
   milestone_documents
   participation_fee
   party_details
   process_title

```
