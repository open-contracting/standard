# Map

This phase is about documenting your sources of contracting data, and documenting how that data "maps" to OCDS – that is, identifying which [data elements](https://en.wikipedia.org/wiki/Data_element) within your data sources match which OCDS [fields](../../schema/reference) and [codes](../../schema/codelists). The mapping phase is one of the longest and most important steps in the implementation process.

If your contracting processes are managed on paper, using local spreadsheets or via unstructured electronic documents, and you’re reusing one of the existing [tools for collecting OCDS data](build/data_collection_tools), then please [get in touch with the OCDS Helpdesk](../../support/#ocds-helpdesk) for guidance on how to identify which OCDS fields match your local concepts.

Mapping data to OCDS is not always easy. Before writing any software, this phase is an opportunity to:

* Catch errors early on
* Identify [hard cases](#mapping-the-hard-cases) that need more attention
* Get input from the [OCDS Helpdesk](../../support/index)

The documentation you produce can also later be included in your [Data User Guide](../publish/#finalize-your-publication-policy).

As you make progress through this phase, we encourage you to update your [publication plan](../design/#develop-your-publication-plan), in order to help set priorities and ease communication within your team, with your stakeholders, and with the OCDS Helpdesk. You can start by filling in the _Goals (design)_ section.

## Involve the right people

As described in the [Field-Level Mapping Template Guidance](https://www.open-contracting.org/resources/ocds-1-1-mapping-template-guidance/) (introduced below), you will need at least:

* A technical expert who is familiar with the **IT systems** that capture and store contracting data and related documents, to identify the data elements within those systems.
* A policy expert who is familiar with **procurement legislation** and procurement processes, to help identify which data elements match which OCDS fields, at a *semantic* level.
* A technical expert who understands the **data structures** in OCDS, to help identify which data elements match which OCDS fields, at a *technical* level.

## Identify your data sources

To implement OCDS you need to first identify which IT systems capture and store contracting data and related documents. You also need to identify how to connect data held in different systems, to get a complete picture of the contracting process. The [Technical Assessment Template](https://www.open-contracting.org/resources/ocds-technical-assessment-template/) guides you through this process.

If your contracting processes are managed on paper, using local spreadsheets or via unstructured electronic documents, you should use the template to identify those data sources, too.

Once complete, you can:

* Ask the [OCDS Helpdesk](../../support/index) to review your Technical Assessment.
* Fill in the _Source systems_ sub-section of your [Publication Plan](https://www.open-contracting.org/resources/ocds-publication-plan-template/).
* Fill in the _Systems_ sheet of your Field-Level Mapping (introduced below).

## Map your data to OCDS

To make this step easier we provide templates to list the data elements within your data sources, and map them to either:

* OCDS [fields](../../schema/reference), using the [Field-Level Mapping Template](https://www.open-contracting.org/resources/ocds-field-level-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-mapping-template-guidance/))
* OCDS [codes](../../schema/codelists), using the [Codelist Mapping Template](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template-guidance/))

If your contracting data is managed on paper or in unstructured electronic documents, you should use the templates to list the data elements in those data sources and map them to OCDS.

You can [contact the OCDS Helpdesk](../../support/#ocds-helpdesk) for support and guidance on using the mapping templates.

Before working on mapping individual fields and codes, consider whether to first [localize OCDS](map/localization) to your context. Localization can be useful when you need to map several different systems, or when multiple organizations will work on implementing OCDS in your country.

```{eval-rst}
.. toctree::
   :hidden:

   map/localization
```

### Mapping organization identifiers

[Organization identifiers](../../schema/identifiers/#organization-ids) in OCDS are made up of two parts:

* An org-id code, identifying the register from the which the identifier is drawn
* The identifier for the organization, drawn from the register

The [organization identifiers worked example](../guidance/map/organization_identifiers) shows how this works in practice.

Use [org-id.guide](http://org-id.guide/) to find the code for the register your identifiers are drawn from. If no code exists for the register, contact the [OCDS Helpdesk](../../support/index).

### Working in parallel

Working in parallel on the map and build phases can be useful, because the choices you make at the build stage might affect how you need to map your data. For example, your choice of architecture might determine whether you are able to publish a change history using releases and records.

### Splitting up the work

You can complete this step in parts. For example, you might choose to split your mapping by any of the following:

* **data source** (e-procurement system, contract management system, [financial management information system](https://www.worldbank.org/en/topic/governance/brief/financial-management-information-systems-fmis), etc.)
* **contracting process type** (open procedure, selective procedure, concession contract, framework agreement, etc.)
* **contracting process stage** (planning, tender, award, contract, implementation)
* **public notice** (tender notice, award notice, etc.)

The preferred approach is to eventually list *all* the data elements within your data sources in your Field-Level Mapping, decide whether to publish each, and then map each. The decision to publish a data element is up to you; it isn't necessary to map all your contracting data.

It is also important to focus on the data elements whose disclosure was prioritized by users during the [design](design) phase. If you have not determined which data elements are a priority, you ought to do this now, based on your user needs.

Whichever approach you take, it's important that your eventual OCDS publication contain at least as much information as your other public datasets of contracting data; otherwise, users are less likely to use your OCDS publication.

### Mapping the hard cases

Mapping data to OCDS is not always obvious. Please refer to our how-to guides and worked examples to learn how to map data for specific cases:

```{eval-rst}
.. toctree::
   :maxdepth: 2
   :titlesonly:

   map/amendments
   map/awards_contracts_buyers_suppliers
   map/milestones
   map/organization_classifications
   map/organization_identifiers
   map/organization_personal_identifiers
   map/organization_reference
   map/organizational_units
   map/pre-qualification
   map/related_processes
   map/unsuccessful_tender
```

## Extensions

Some data elements might not match any field or code in OCDS. To cover such cases, you can add fields and codes to OCDS using [extensions](map/extensions).

**Resource:** [Localizing OCDS: Translations, Terminology & Extensions](https://www.open-contracting.org/2016/07/26/localising-ocds-translations-terminology-extensions/)

**Resource:** [What to do when fields don't map?](https://www.open-contracting.org/2018/01/30/fields-dont-map-first/)

**Resource** [OCDS Glossary](https://github.com/open-contracting/glossary)

**Action:** [Contact the OCDS Helpdesk](../../support/index) to get help with mapping data or authoring extensions.

**Action:** If you are stuck on a particular concept and are concerned about how it is modelled in OCDS, search the issues in our [Github tracker](https://github.com/open-contracting/standard/issues) to see what others in the community are saying about the topic. If you do not see your issue, create a new one!

```{eval-rst}
.. toctree::
   :hidden:

   map/extensions
```

## Wrapping up

Once complete, you can:

* Fill in the *Priority data (map)* and *Priority documents* sections of your [Publication Plan](https://www.open-contracting.org/resources/ocds-publication-plan-template/).
* Ask the [OCDS Helpdesk](../../support/index) to review your Field-Level Mapping and Publication Plan.

[Next phase: Build](build)
