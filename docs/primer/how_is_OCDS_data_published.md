# How is OCDS data published?
```{eval-rst}
.. admonition:: Objectives
   :class: note

   .. markdown::

Open Contracting Data Standard (OCDS) data is published and updated over time as two JSON document formats: “releases” and “records”.  This page exists to:

*   Outline the purpose of releases and records
*   Describe how to publish a change history using releases and records 
*   Show the components of an OCDS record
```
The only thing that can be truly called “OCDS data” is a JSON document that validates against the OCDS schema. The JSON documents that OCDS uses are called “releases” and “records.”

Within a contracting process, there are usually 5 stages associated with major events that mark the progress from one stage to another, like an award notice. Smaller events take place within a stage, like a deadline extension for bidding. In OCDS, all updates are published as immutable **releases**. Releases are JSON documents that are published each time there is an update in the process following the [release schema](https://standard.open-contracting.org/latest/en/schema/reference/). 

Each change is published as a new immutable release, rather than by updating an existing one. The collection of releases for a contracting process composes its change history. Each release contains an ocid to identify the contracting process it relates to. An ocid is composed of a prefix registered by the publisher, and a unique process identifier chosen by the publisher.

Tracking changes over time is important to users of contracting data because there can be many changes in the life of a contracting process. Understanding how and when certain attributes changed can help users to understand the process, identify inefficiencies, and spot red flags for corruption.

**Records** are JSON documents that act as an index of all releases for a single contracting process, following the [record schema](https://standard.open-contracting.org/latest/en/schema/records_reference/). While releases are never updated, records are updated each time there is a change, and there should be only one for each contracting process. A record is updated by adding a new release to this index.

Records and releases each contain several fields which can be used in different sections. OCDS’ schema sets out the fields that ought to be included in each section (where applicable), aiming to reuse simple structures to represent information. For example, a release may contain information about items being procured. OCDS’ schema sets out standard building blocks for items across releases, including the name of the item, a description, each item’s value, and the currency used.

Some schema fields refer to [codelists](https://standard.open-contracting.org/latest/en/schema/codelists/), to limit and standardize the possible values of the fields, in order to promote data interoperability.

When you publish data, you are encouraged to:

*   Ensure all documents referenced in OCDS releases are available online;
*   Publish each release and record at its own persistent URL;
*   Produce bulk packages of releases and records for users to download;
*   Publish versions of the data for users to access in CSV for Excel formats

```{eval-rst}
.. note::

   .. markdown::

To learn more, go to the next page in the primer: How can I implement OCDS? You can also review the further resources below to go deeper into the subjects introduced on this page.

[OCDS Schema Release Reference](https://standard.open-contracting.org/latest/en/schema/reference/)
[OCDS Schema Record Reference](https://standard.open-contracting.org/latest/en/schema/records_reference/)
[Using Open Contracting Data](https://www.open-contracting.org/data/data-use/#tools)
```

[Button: previous page]					   		     [Button: next page]
