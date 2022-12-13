# Map

```{ifconfig} language != 'es'
<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3Q_fQBsju6Y" title="Matching your data to OCDS fields" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```
```{ifconfig} language == 'es'
<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/wL0wiTaEpW4" title="Mapeo de sus datos con los campos OCDS" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```

This phase is about documenting your sources of contracting data, and documenting how that data "maps" to OCDS – that is, identifying which [data elements](https://en.wikipedia.org/wiki/Data_element) within your data sources match which OCDS [fields](../../schema/reference) and [codes](../../schema/codelists). The mapping phase is one of the longest and most important steps in the implementation process. 

When starting out, consider working in parallel on the map and build phases, because the choices you make at the build stage might affect how you need to map your data. For example, your choice of architecture might determine whether you are able to publish a change history using releases and records.

If your contracting (or planning) processes are managed on paper, using local spreadsheets or via unstructured electronic documents, and you’re reusing one of the existing [tools for collecting OCDS data](build/data_collection_tools), then please [get in touch with the OCDS Helpdesk](../support/index.md#ocds-helpdesk) for guidance on how to identify which OCDS fields match your local concepts.

Mapping data to OCDS is not always easy. Before writing any software, this phase is an opportunity to:

* Catch errors early on
* Identify [hard cases](#deal-with-the-hard-cases) that need more attention
* Get input from the [OCDS Helpdesk](../../support/index)

The documentation you produce can also later be included in your [Data User Guide](publish.md#finalize-your-publication-policy).

As you make progress through this phase, we encourage you to maintain a project plan, in order to help set priorities and ease communication within your team, with your stakeholders, and with the OCDS Helpdesk.

## Involve the right people

As described in the [Field-Level Mapping Template Guidance](https://www.open-contracting.org/resources/ocds-1-1-mapping-template-guidance/) (introduced below), you will need at least:

* A data expert who is familiar with the **IT systems** that capture and store contracting data and related documents, to identify the data elements within those systems.
* A procurement expert who is familiar with **procurement legislation** and procedures, to identify which data elements match which OCDS fields, at a *semantic* level.
* A technical expert who understands the **data structures** in OCDS, to help identify which data elements match which OCDS fields, at a *technical* level.

## Identify your data sources

To implement OCDS you need to first identify which IT systems capture and store contracting data and related documents. You also need to identify how to connect data held in different systems, to get a complete picture of the contracting (and planning) processes. The [Technical Assessment Template](https://www.open-contracting.org/resources/technical-assessment-template/) guides you through this process.

If your contracting (or planning) processes are managed on paper, using local spreadsheets or via unstructured electronic documents, you should use the template to identify those data sources, too.

Once complete, you can:

* Ask the [OCDS Helpdesk](../../support/index) to review your Technical Assessment.
* Fill in the _Systems_ sheet of your Field-Level Mapping (introduced below).

## Localize OCDS to your context

Before mapping individual fields and codes, consider whether to first [localize OCDS](map/localization) to your context. Localization can be useful when you need to map several different systems, or when multiple organizations will work on implementing OCDS in your country.

```{toctree}
:hidden:

map/localization
```

## Download the mapping templates

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gVk-Gw-3iP0" title="The field-level mapping template" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

To make the mapping easier we provide templates to list the data elements within your data sources, and map them to either:

* OCDS [fields](../../schema/reference), using the [Field-Level Mapping Template](https://www.open-contracting.org/resources/ocds-field-level-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-mapping-template-guidance/))
* OCDS [codes](../../schema/codelists), using the [Codelist Mapping Template](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template/) ([read the tutorial](https://www.open-contracting.org/resources/ocds-1-1-codelist-mapping-template-guidance/))

If your contracting data is managed on paper or in unstructured electronic documents, you should use the templates to list the data elements in those data sources and map them to OCDS.

You can [contact the OCDS Helpdesk](../support/index.md#ocds-helpdesk) for support and guidance on using the mapping templates.

## Complete the mapping

You can complete the mapping in parts. For example, you might choose to split your mapping by any of the following:

* **data source** (e-procurement system, contract management system, [financial management information system](https://www.worldbank.org/en/topic/governance/brief/financial-management-information-systems-fmis), etc.)
* **contracting process type** (open procedure, selective procedure, concession contract, framework agreement, etc.)
* **contracting process stage** (planning, tender, award, contract, implementation)
* **public notice** (tender notice, award notice, etc.)

The preferred approach is to eventually list *all* the data elements within your data sources in your Field-Level Mapping, decide whether to publish each, and then map each. The decision to publish a data element is up to you; it isn't necessary to map all your contracting data.

It is also important to focus on the data elements whose disclosure was prioritized by users during the [design](design) phase. If you have not determined which data elements are a priority, you ought to do this now, based on your user needs.

Whichever approach you take, it's important that your eventual OCDS publication contain at least as much information as your other public datasets of contracting data; otherwise, users are less likely to use your OCDS publication.

## Deal with the hard cases

Mapping data to OCDS is not always obvious. Please refer to our how-to guides and worked examples to learn how to map data for specific hard cases:

```{toctree}
:maxdepth: 2
:titlesonly:

map/contracting_planning_processes
map/unsuccessful_processes
map/framework_agreements
map/pre-qualification
map/awards_contracts
map/contract_suspension
map/electronic_catalogues
map/amendments
map/milestones
map/buyers_suppliers
map/organization_reference
map/organization_identifiers
map/organization_personal_identifiers
map/organizational_units
map/organization_classifications
map/beneficial_ownership
```

## Consider using extensions

Some data elements might not match any field or code in OCDS. To cover such cases, you can add fields and codes to OCDS using [extensions](map/extensions).

Before using extensions, double-check whether the data elements can be disclosed using existing fields. For example, to disclose the date by which the buyer or procuring entity will respond to enquiries, you can use the `tender.milestones` field, instead of adding a new field.

```{seealso}
* [Worked example: Milestones](map/organization_classifications)
* [Worked example: Organization classification](map/organization_classifications)
```

If you do need to use an extension, consider whether the new fields will affect how users interpret existing fields. If so, you can add information to existing fields, to avoid misinterpretation – in addition to adding the new fields.

For example, you have created an extension to add a new field to indicate whether a contracting process is about the disposal of a state asset (like a vehicle). If the `tender.title` field refers only to the vehicle, then users who are unaware of the new field might misinterpret the contracting process as being about its purchase. To avoid misinterpretation, you can add a "Disposal: " prefix to the `tender.title` field.

**Resource:** [Localizing OCDS: Translations, Terminology & Extensions](https://www.open-contracting.org/2016/07/26/localising-ocds-translations-terminology-extensions/)

**Resource** [OCDS Glossary](https://github.com/open-contracting/glossary)

**Action:** [Contact the OCDS Helpdesk](../../support/index) to get help with mapping data or authoring extensions.

**Action:** If you are stuck on a particular concept and are concerned about how it is modelled in OCDS, search the issues in our [GitHub tracker](https://github.com/open-contracting/standard/issues) to see what others in the community are saying about the topic. If you do not see your issue, create a new one!

```{toctree}
:hidden:

map/extensions
```

## Link OCDS with other standards

Not all information that is related to a contracting (or planning) process belongs in OCDS. For example, a company's annual filings and incorporation status are typically managed in a company registry, outside the lifecycle of a contracting process.

For guidance on integrating your OCDS data with these related datasets, refer to [Linked standards](map/linked_standards).

```{toctree}
:hidden:

map/linked_standards
```

## Wrap up

Once complete, you can:

* Ask the [OCDS Helpdesk](../../support/index) to review your Field-Level Mapping and Technical Assessment Template.

[Next phase: Build](build)
