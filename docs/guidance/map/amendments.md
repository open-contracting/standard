```{workedexample} Updates and amendments
:tags: amendment,tender,contract
```

# Updates and amendments

Information about a contracting (or planning) process often changes over time.

Each time information changes, a new OCDS release ought to be published. The new release can repeat information that was previously published, in addition to new and changed information.

There are three types of change:

* **New information**. For example, when information about the award of a contract is first released.
* **Updates to existing information**. For example, to correct errors in earlier releases, or to make minor adjustments to titles, descriptions or dates.
* **Amendments**. For example, when the value or duration of a contract is changed. The term amendment often has a specific legal meaning for a publisher. Certain changes to a tender, award or contract might only be permitted as part of an amendment.

The nature of a change can be made explicit using:

* **The release tag** field (`tag`), which is used to identify the type of change. For example, 'contract' identifies information about a new contract, 'contractUpdate' identifies an update to existing information about a contract, and 'contractAmendment' identifies a formal amendment to a contract.

* **The amendments** fields (`tender.amendments` and `contract.amendments`), which are used to list amendments along with their rationales and references to the releases that contain before and after values.

## Worked examples

### Example 1: Tender updates and amendments

This example illustrates how new information, updates and amendments are modelled in OCDS when publishing a change history using releases and records.

#### Tender release

A buyer publishes an opportunity for the purchase of office supplies.

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0/releases/0
:expand: tender, tag
:title: Tender
```

#### Tender update release

The buyer now indicates the opportunity's main procurement category. The new information is not a formal amendment so the publisher uses the 'tenderUpdate' tag and omits the `tender.amendments` field.

The publisher chooses to repeat fields whose values are unchanged from the previous release. Such fields can be omitted when a publication provides access to historic releases.

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0/releases/1
:expand: tender, tag
:title: TenderUpdate
```

#### Tender amendment release

The buyer increases the estimated value of the opportunity. This change is a formal amendment so the publisher uses the 'tenderAmendment' tag and populates the `tender.amendments` field.

Note that `tender.amendments` does not include the changed values. Rather, the `tender.value.amount` field itself is updated. 

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0/releases/2
:expand: tender, tag, amendments
:title: TenderAmendment
```

#### Record

`releases` contains the above releases, `compiledRelease` contains the latest value of each field, and `versionedRelease` contains a history of changes to each field.

The `releaseID` and `amendsReleaseID` fields in the `amendments` array of the compiled release can be looked up in `releases` and `versionedRelease` to identify what changed.

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0
:expand: compiledRelease, versionedRelease, value, amount
:title: FullRecord
```

```{hint}
[Download](../../examples/amendments/tender.json) the record example and use the [Data Review Tool](https://review.standard.open-contracting.org/) to explore the changes in the contracting process.
```

```{admonition} Contract updates and amendments
Contract updates and amendments are modelled in the same way: the 'contract', 'contractUpdate' and 'contractAmendment' release tags distinguish the type of change and amendments are listed in the `contract.amendments` field.
```

### Example 2: Amendments without a change history

If you cannot publish a full change history as described in [change history options](../build/change_history_options.md), you might still be able to publish the details of amendments using [individual releases](../build/individual_releases.md).

Where the source system stores a history of amendments, a separate release can be published for each amendment, in addition to the release that represents the tender or contract that is amended.

A procurement system stores tenders and amendments in the same table. `tender_id` is a unique identifier for each contracting process and `amendment_id` is a unique identifier for each amendment. `last_modified` stores the date and time of the last modification to the row.

A buyer publishes an opportunity and subsequently amends its value.

```{csv-table-no-translate}
:header-rows: 1
:file: ../../examples/amendments/no_change_history.csv
```

Each row is modelled as a separate OCDS release. The first row is represented as a tender release. `id` is [set to the last modified date](../build/individual_releases.md#last-modified-date) of the tender.

```{jsoninclude} ../../examples/amendments/no_change_history.json
:jsonpointer: /releases/0
:expand: tag, tender
```

The second row is represented as a tender amendment release. `id` is again set to the last modified date of the amendment.

```{jsoninclude} ../../examples/amendments/no_change_history.json
:jsonpointer: /releases/1
:expand: tag, tender, amendments
```
