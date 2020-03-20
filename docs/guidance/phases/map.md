# Map

This phase is about documenting your sources of contracting data, and documenting how that data "maps" to OCDS – that is, identifying which [data elements](https://en.wikipedia.org/wiki/Data_element) within your data sources match which [OCDS fields and codes](../../schema/index) from its [schema](../../schema/reference) and [codelists](../../schema/codelists).

Mapping data to OCDS is not always obvious. This phase gives members of your team (and the [OCDS Helpdesk](../../support/index)) an opportunity to catch errors early on and to identify [hard cases](#mapping-the-hard-cases) that need more attention – before any software is written in the [Build](build) phase. The documentation you produce can also later be included in your [Data User Guide](publish). This phase is critical to the implementation process.

As you make progress through this phase, we encourage you to fill in the [publication plan template](https://docs.google.com/document/d/1Cz8nDDfAZ18qdzkl2vsSvdSyiXN11JRe8W5efjh8pEs/edit) ([create a copy](https://www.open-contracting.org/resources/ocds-publication-plan-template/)), in order to help set priorities and ease communication within your team, with your stakeholders, and with the [OCDS Helpdesk](../../support/index). You can start by filling in the *Goals (design)* section.

## Involve the right people

As described in the [Field-Level Mapping Template Guidance](https://www.open-contracting.org/resources/ocds-1-1-mapping-template-guidance/) (introduced below), you will need at least:

* A technical expert who is familiar with the **IT systems** that capture and store contracting data and related documents, to identify the data elements within those systems.
* A policy expert who is familiar with **procurement legislation** and procurement processes, to help identify which data elements match which OCDS fields, at a *semantic* level.
* A technical expert who understands the **data structures** in OCDS, to help identify which data elements match which OCDS fields, at a *technical* level.

## Identify your data sources

A necessary step to implement OCDS is to identify which IT systems capture and store contracting data and related documents. The [Technical Assessment Template](https://www.open-contracting.org/resources/ocds-technical-assessment-template/) guides you through the process of identifying data sources, describing their contents, and determining how to interlink their data.

Once complete, you can:

* Ask the [OCDS Helpdesk](../../support/index) to review your Technical Assessment.
* Fill in the *Source systems* sub-section of your [Publication Plan](https://www.open-contracting.org/resources/ocds-publication-plan-template/).
* Fill in the *Systems* sheet of your Field-Level Mapping (introduced below).

## Map your data to OCDS

This is one of the longest steps of implementing OCDS. To make it easier, we provide templates to list the data elements within your data sources, and map them to either:

* OCDS [fields](../../schema/reference), using the [Field-Level Mapping Template](https://www.open-contracting.org/resources/ocds-field-level-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-mapping-template-guidance/))
* OCDS [codes](../../schema/codelists), using the [Codelist Mapping Template](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template-guidance/))

### Splitting up the work

You can complete this step in parts, while working in parallel on the [Build](build) phase. For example, you can map each of these, one at a time:

* **data source** (e-procurement system, contract management system, [financial management information system](https://www.worldbank.org/en/topic/governance/brief/financial-management-information-systems-fmis), etc.)
* **contracting process type** (open procedure, selective procedure, concession contract, framework agreement, etc.)
* **contracting process stage** (planning, tender, award, contract, implementation)
* **public notice** (tender notice, award notice, etc.)

The preferred approach is to eventually list *all* the data elements within your data sources in your Field-Level Mapping, decide whether to publish each, and then map each. The decision to publish a data element is up to you; it isn't necessary to map all your contracting data.

A limited approach is to focus on the data elements whose disclosure was prioritized by users during the [Design](design) phase. However, it's important that your eventual OCDS publication contain at least as much information as your other public datasets of contracting data; otherwise, users are less likely to use your OCDS publication.

### Mapping the hard cases

Mapping data to OCDS is not always obvious. Please refer to our [how-to guides](../../#map) to learn how to map data for specific cases:

```eval_rst
.. toctree::
   :maxdepth: 2

   ../map/related_processes
   ../map/amendments
   ../map/extensions
```

Some data elements might not match any field or code in OCDS. To cover such cases, you can add fields and codes to OCDS by [authoring extensions](../map/extensions). You can also:

* Contact the [OCDS Helpdesk](../../support/index) to get help with mapping data or authoring extensions.

### Wrapping up

Once complete, you can:

* Fill in the *Priority data (map)* and *Priority documents* sections of your [Publication Plan](https://www.open-contracting.org/resources/ocds-publication-plan-template/).
* Ask the [OCDS Helpdesk](../../support/index) to review your Field-Level Mapping and Publication Plan.

[Next phase: Build](build)
