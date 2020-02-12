# Map

This phase is about identifying your sources of contracting data, and "mapping" that data to OCDS – that is, identifying which [data elements](https://en.wikipedia.org/wiki/Data_element) within your data sources match which [OCDS fields and codes](../../schema/index) from its schema and codelists.

As you make progress through this phase, we encourage you to fill in the [publication plan template](https://docs.google.com/document/d/1Cz8nDDfAZ18qdzkl2vsSvdSyiXN11JRe8W5efjh8pEs/edit) ([create a copy](https://www.open-contracting.org/resources/ocds-publication-plan-template/)), in order to help set priorities and ease communication within your team, with your stakeholders, and with the [OCDS Helpdesk](../../support/index). You can start by filling in the *Goals (design)* section.

## Identify your data sources

A necessary step to implement OCDS is to identify which systems capture and store contracting data and related documents. The [Technical Assessment Template](https://www.open-contracting.org/resources/ocds-technical-assessment-template/) guides you through the process of identifying data sources, describing their contents, and determining how to interlink their data.

Once complete, you can:

* Ask the OCDS Helpdesk to [review your Technical Assessment](../../support/index).
* Fill in the *Source systems* sub-section of the publication plan template.
* Fill in the *Systems* sheet of your Field-Level Mapping (introduced below).

## Map your data to OCDS

This is one of the longest steps of implementing OCDS. To make it easier, we provide templates to list the data elements within your data sources, and map them to either:

* OCDS fields, using the [Field-Level Mapping Template](https://www.open-contracting.org/resources/ocds-field-level-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-mapping-template-guidance/))
* OCDS codes, using the [Codelist Mapping Template](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template-guidance/))

### Splitting up the work

You can complete this step in parts, while working in parallel on the [Build](build) phase. For example, you can map each of these, one at a time:

* data source (e-procurement system, contract management system, [financial management information system](https://www.worldbank.org/en/topic/governance/brief/financial-management-information-systems-fmis), etc.)
* contracting process type (open procedure, selective procedure, framework agreement, concession contract, etc.)
* contracting process stage (planning, tender, award, contract, implementation)
* public notice (tender notice, award notice, etc.)

The preferred approach is to eventually list *all* the data elements within your data sources, decide whether to publish each, and then map each. A limited approach is to focus on the data elements whose disclosure was prioritized by users during the [Design](design) phase. However, it's important that your eventual OCDS publication contain at least as much information as your other public datasets of contracting data; otherwise, users are less likely to use your OCDS publication.

### Mapping the hard cases

Mapping data to OCDS is not always obvious. Please refer to our [how-to guides](../../#map-how-to-guides) to learn how to map data for specific cases. Some data elements might not match any field or code in OCDS. To cover such cases, you can [author extensions](../map/extensions) to OCDS. You can also:

* Contact the OCDS Helpdesk to [get help with mapping data or authoring extensions](../../support/index).

### Wrapping up

Once complete, you can:

* Ask the OCDS Helpdesk to [review your Field-Level Mapping](../../support/index).
* Fill in the *Priority data (map)* and *Priority documents* sections of the publication plan template.

[Next phase: Build](build)
