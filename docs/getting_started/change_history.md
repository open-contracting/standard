# Change History

Tracking change over time is important for users of contracting data. For example, frequent changes or amendments can signal possible corruption (red flags), or opportunities for improvement in the management of public contracts.

Publishers are encouraged to publish changes to the contracting process in real time, whenever possible. OCDS supports real-time publication with the releases and records model, which describes how to publish updates to a contracting process and maintain a history of changes.

## The Releases and Records model

Releases and records are the JSON document formats supported by OCDS. These formats are not independent (records require the use of releases), but they can be seen as alternative publication formats. Publishers should decide whether to use releases, records or both to better support their goals.

Consider the timeline of a contracting process. While OCDS identifies five possible stages in the timeline (planning, tender, award, contract, implementation) there can be multiple events during each stage. The image below shows a slice of the timeline in a contracting process.

![Contracting Process](../_static/png/changehistory_process.png)

There are major events that indicate progress from one stage to another, like the publication of an award notice, and there are smaller events that  take place within a stage, like extending the deadline for bid submission. In OCDS, all changes are disclosed using **releases**. Releases are JSON documents, published each time there is any update to the contracting process.

![Contracting Process with releases](../_static/png/changehistory_process2.png)

Releases are **immutable**, therefore each change should be documented in a **new** release, rather than by updating an existing one. The history of a contracting process, then, is represented by the collection of all releases published for the process.

**Records** are JSON documents that act as an index of all releases for a single contracting process. While releases should never be updated, records should be updated each time there is a change to add a new release to the index. There should be a single record for each contracting process at all times.

![Contracting Process with releases and a record](../_static/png/changehistory_process_record.png)

Records may also contain:

* A *compiled release*, which uses the same structure as an OCDS release and represents the latest state of each field.

* A *versioned release*, that contains a history of changes for each individual field.

These structures are designed to help users easily access both the current state of the whole contracting process and a detailed history of changes for individual fields.

In accounting terms, releases are analogous to individual transactions in an account, whilst a record represents both the ledger of all transactions for the account (the releases list) and the closing balance for the account (the compiled release).

In software development terms, releases are analogous to individual Git commits on a branch, whilst a record represents both the commit history for the branch (the releases list) and HEAD for the branch (the compiled release). 


### Releases

Releases follow the OCDS Release schema, which gives them flexibility to publish small portions of data along with a few required fields. The box below shows an example.

```eval_rst
.. jsoninclude:: ../examples/tender.json
   :jsonpointer: /releases
   :expand: 
   :title: release
```

See the [Release reference](../schema/reference/) for more details on the fields available.

#### Identifiers

Each release needs to contain an ocid to identify the contracting process it relates to, and a release identifier unique in the scope of that contracting process. A release id can be built in several ways, and a publisher can use any generation strategy as long as the ids don’t clash within a contracting process.

The Easy releases section introduces two strategies that can be used in any scenario. 

#### Packaging

When published, releases should be always wrapped in a release package to provide context to the data. The uri package field should contain an URI to an online copy of the same release. In a complete OCDS implementation, each release would be published at its own persistent URL, and kept online permanently.

See the [Release Package schema](../schema/release_package/) for details.

#### Tags

Each release also needs to provide one or more tags. Tags provide information about the event the release relates to.

For example:

* When a invitation to tender is published the ‘tender’ tag should be used and the `tender` section populated with the relevant details, however the release may also contain information in the `planning` section about the budget for the procurement.

* When an award is made the ‘award’ tag should be used and the `award` section populated with the relevant details, however the `tender` section may also be updated with the list of tenderers that submitted a bid.

The [Release tag codelist](../schema/codelists/#release-tag) contains the list of all tags provided by OCDS. Note that it is valid to use more than one tag in the same release. For example, a tenderUpdate and an award tags could be used together in a release that provides award information and also updates the number of tenderers.

#### Repeating previous information

Releases can include new information only, or can repeat unchanged data from previous releases along with new or updated data. Both alternatives are equally valid and publishers can choose how much unchanged data to include in their releases while being careful of always including required fields. Releases with repeating information may be more appropriate for datasets with fewer releases per contracting processes. Repeating previous information can impact on the final size of the dataset.

<div class="example hint" markdown=1>

<p class="first admonition-title">Example</p>

The following example presents releases from a contracting process with minimal changes on each update. The first release presents tender data. The second introduces a new document in the tender section with the tenderUpdate tag. Note that all not-required tender fields are omitted, even the tender notice present in the previous release. The third release presents award data, and the complete tender section is omitted.
 
 ```eval_rst
.. jsoninclude:: ../examples/minimal_updates/tender.json
   :jsonpointer: /releases/0
   :expand: tender
```
 
```eval_rst
.. jsoninclude:: ../examples/minimal_updates/tenderUpdate.json
   :jsonpointer: /releases/0
   :expand: tender
```
 
```eval_rst
.. jsoninclude:: ../examples/minimal_updates/award.json
   :jsonpointer: /releases/0
   :expand: award
```

</div>

### Records

A record should follow the structure defined in the [Records Reference](../schema/records_reference). Below is a full example.

```eval_rst
.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer: /records/0
   :expand: 
```

#### Compiled and Versioned Releases

A **compiled release** follows the release structure and contains the latest value for all fields that have been filled in the releases of a contracting process. The example above shows how a compiled release looks like. It is strongly recommended to include a compiled release when producing records.

A **versioned release** follows a structure similar to the release, but in place of each field an object is provided, containing a history of changes to the field.

The following animation shows how the record for a contracting process should be updated as releases are published over time.

![Record updates](../_static/change_history_animation.gif)

Each time a new release is available:

* The new release is added to the releases list, either embedding it or by adding a link to it.
* Both the compiled and versioned releases are updated with the new information from the release. Whether release repeat unchanged information from previous releases doesn't affect the resulting compiled and versioned releases.

<div class="example hint" markdown=1>

<p class="first admonition-title">Hint</p>

Although publishing compiled releases is not mandatory, it helps to make OCDS data more accessible to users that don’t require a detailed change history. 

Consider how to calculate the **total value of active tenders** using compiled releases:

```eval_rst
.. csv-table-no-translate::
    :header-rows: 1
    :file: ../examples/compiledreleases_compiled.csv
```

Compare that to how to calculate the **total value of active tenders** using releases:

```eval_rst
.. csv-table-no-translate::
    :header-rows: 1
    :file: ../examples/compiledreleases_releases.csv
```

Working with individual releases, we need to check whether an active tender has later been cancelled before including it in our results.

Whilst it’s easier to answer this simple question using the compiled releases, a full change history is required to answer other types of question, such as checking how many times a tender value was amended.

</div>

#### Embedding or linking Releases

Records contain the history of a contracting process as a group of releases. Releases can be embedded in the record, or a list of URLs to the releases can be provided inside it.

See the [Record reference](../schema/records_reference/) for more details.

#### Packaging

When publishing, records should be always published wrapped in a Record Package , with a URI leading to a copy of the package and record.
