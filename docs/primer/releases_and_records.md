# How is OCDS data published?

```{admonition} Objectives
:class: note

Open Contracting Data Standard (OCDS) data is published and updated over time using two types of JSON data: “releases” and “records.” This page will:

* Outline the purpose of releases and records
* Describe how to publish a change history using releases and records
* Show the components of an OCDS record
```

```{ifconfig} language != 'es'
<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/OeDCLMWlY_U" title="Introducing releases and records" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```
```{ifconfig} language == 'es'
<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/wFf5KAv3LMs" title="Presentación de entregas y registros" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```

The only thing that can be truly called “OCDS data” is JSON data that validates against the OCDS schema. There are two schemas for OCDS data: “releases” and “records.”

OCDS publishers are encouraged to use releases and records to publish data in near real-time and to provide a change history. Tracking change over time is important to users of contracting data because there can be many changes in the lifetime of a contracting process. Knowing how and when certain attributes have changed can help users to understand the process, identify inefficiencies, and spot red flags for corruption.

A **release** is JSON data that is published each time there is a change to a contracting (or planning) process. Releases follow the OCDS [release schema](../schema/reference) and contain an OCID to identify the contracting (or planning) process they relate to.

Releases are immutable, which means they cannot be changed once published. There can be many releases per contracting (or planning) process and the collection of releases for a process constitutes its change history.

A **record** is JSON data that acts as an index of all releases for a single contracting (or planning) process. While releases are never updated, records are updated each time there is a change to a process by adding a new release to this index. Records follow the OCDS [record schema](../schema/records_reference) and, in addition to the release index, can also contain:

* A **compiled release,** which follows the same structure as a release and provides the latest value of each field. The compiled release makes it easy for users to get the latest version of the data about a contracting (or planning) process.
* A **versioned release,** which contains a history of changes for each field and allows users to see how a particular field has changed over time.

Each time a new release is published it is added to the index, the compiled release is updated with the latest values, and the versioned release is updated with any new changes.

![A contracting (or planning) process is described by many releases, which are aggregated into a single record](../_static/png/change_history_process_record.png)

Records and releases each contain several fields which can be used in different sections. The OCDS schema sets out the fields that ought to be included in each section (where applicable), aiming to reuse simple structures to represent information. For example, a release may contain information about items being procured. OCDS' schema sets out standard building blocks for items across releases, including the name of the item, a description, each item's value, and the currency used.

When you publish OCDS releases and records, you are encouraged to:

* Publish each release and record at its own persistent URL
* Produce bulk packages of releases and records for users to download

```{note}
**To learn more,** go to the next page in the Primer: [How can I implement the OCDS?](next) You can also review the further resources below to go deeper into the subjects introduced on this page.

* [OCP Learning: Publishing OCDS Data](https://www.open-contracting.org/learn/publish/)
* [Video Learning Guide to the OCDS](https://www.youtube.com/playlist?list=PL7sSifLpWd8hLOVrNMiwNApXAsOr06E1Q)
* [OCDS Schema Release Reference](../schema/reference)
* [OCDS Schema Record Reference](../schema/records_reference)
```
