# Getting Started

OCDS is an open data standard for publication of structured information on all stages of a contracting process: from initiation to implementation.

The publication of OCDS data can enable greater transparency in public contracting, and can support accessible and in-depth analysis of how public resources are being used. 

To get started publishing OCDS data:

* Discuss the key [users and use cases](use_cases.md) for your OCDS project
* Identify out the data and documents you will publish from your [contracting process](contracting_process.md)
* Map your data against the OCDS [building blocks](building_blocks.md)
* Present the data in [JSON releases and records](releases_and_records.md)
* Publish your data on the web using the [publication patterns](publication_patterns.md)
* Check the [validation of your data](validation.md)

You can find [samples of OCDS data](ToDo), and [information on using OCDS](ToDo) in the implementation handbook. 

When you are done you could be producing data that looks something like this, and which is compatible with a growing range of OCDS aware tools.

```eval_rst

.. jsoninclude:: docs/en/examples/contract.json
   :jsonpointer: /releases
   :expand: releases, tender, awards, contracts, period, value, items, tag, documents

```


```eval_rst
.. toctree::
   :hidden:
   :maxdepth: 2
   :glob:

   use_cases
   contracting_process
   building_blocks
   releases_and_records
   publication_patterns
   validation
```

