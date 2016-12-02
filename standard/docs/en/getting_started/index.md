# Getting Started

OCDS is an open data standard for publication of structured information on all stages of a contracting process: from planning to implementation.

The publication of OCDS data can enable greater transparency in public contracting, and can support accessible and in-depth analysis of the efficiency, effectiveness, fairness, and integrity of public contracting systems. 

The [core OCDS](http://standard.open-contracting.org) was designed with a focus on public procurement of goods, works and services, but can be extended for use in other contexts. This version of OCDS has been extended to cover all the requirements of the [World Bank Framework for Disclosure in Public Private Partnerships](http://www.worldbank.org/en/topic/publicprivatepartnerships/brief/a-framework-for-disclosure-in-public-private-partnership-projects). 

To get started using OCDS to meet the framework's disclosure requirements:

* Identify the key [users and use cases](use_cases.md) for your OCDS project
* Identify the different systems and data sources you will need to draw on across the entire PPP [contracting and implementation process](contracting_process.md) 
* Map your data against the OCDS [building blocks](building_blocks.md) and [extensions](../../extensions/)
* Present the data in [JSON releases and records](releases_and_records.md)
* Publish your data on the web using the [publication patterns](publication_patterns.md)
* Check the [validation of your data](validation.md)
* Encourage and facilitate stakeholder use of the data

When you are done you could be producing data that looks something like the contract release below, which is compatible with a growing range of OCDS aware tools (you will encounter a range of different OCDS release types in the following pages). 

With this structure data it is possible to create visualisations, extra data tables for analysis, and exchange information between OCDS aware systems.

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

