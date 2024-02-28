```{workedexample} Updates and amendments
:tags: amendment,tender,contract
```

# Updates and amendments

Information about a contracting (or planning) process will often change over time.

Each time information changes, a new OCDS release ought to be published. The new release can contain information that was previously published, in addition to the new information.

There are three kinds of changes:

* **New information**. For example, when information about the award of a contract is first released.
* **Updates to existing information**. For example, to correct errors in earlier releases, or to make minor adjustments to titles, descriptions or date.
* **Amendments**. For example, when the value or duration of a contract is changed. The term amendment often has a specific legal meaning for a publisher. Certain changes to a tender, award or contract might only be allowed as part of an amendment.

The nature of a change can be made explicit using:

* **The release tag** (`tag`). For example, for a release with a new contract, use 'contract'. For an update to the contract, use 'contractUpdate', and for an amendment to the contract, use 'contractAmendment'.

* **The amendments** building block. This can contain an array of amendment explanations, and clearly identify the releases that contain before and after values.

## Worked examples

### Example 1: Tender updates and amendments

This example illustrates how updates and amendments are modelled in OCDS.

#### Tender release

A buyer publishes a tender for the purchase of office supplies.

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0/releases/0
:expand: tender, tag
:title: Tender
```

#### Tender update release

The buyer adds a main procurement category to the tender. The new information is not a formal amendment to the tender so the publisher uses the 'tenderUpdate' tag and omits the `tender.amendments` field. The publisher chooses to repeat fields whose values are unchanged from the previous release. Such fields can be omitted when a publication provides access to historic releases.

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0/releases/1
:expand: tender, tag
:title: TenderUpdate
```

#### Tender amendment release

The buyer increases the estimated value of the tender. This change is a formal amendment to the tender so the publisher uses the 'tenderAmendment' tag and populates the `tender.amendments` field. Note that `tender.amendments` does not include the changed values. Rather, the `tender.value.amount` field itself is updated. 

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0/releases/2
:expand: tender, tag, amendments
:title: TenderAmendment
```

#### Record

`releases` contains the above releases, `compiledRelease` contains the latest value of each field and, `versionedRelease` contains a history of changes to each field. The `releaseID` and `amendsReleaseID` fields in the `amendments` array of the compiled release can be looked up in `releases` and `versionedRelease` to identify what changed.

```{jsoninclude} ../../examples/amendments/tender.json
:jsonpointer: /records/0
:expand: compiledRelease, versionedRelease, value, amount
:title: FullRecord
```

```{hint}
It is encouraged to [download](../../examples/amendments/tender.json) the record example and use the [Data Review Tool](https://review.standard.open-contracting.org/) to explore the changes in the contracting process.
```

### Example 2: Contract amendment

This example shows an update to the value and scope of a contract.

#### Contract

A contract signature notice is published for the purchase of domestic appliances. The publisher builds a release and uses the 'contract' `tag`.

See the JSON release below.

```{jsoninclude} ../../examples/amendments/contract.json
:jsonpointer: /records/0/releases/0
:expand: tag, contracts, items
:title: Contract
```

#### Contract Amendment

A few days after the contract release, its scope is increased to include the purchase of one additional appliance. A new 'contractAmendment' release is built, where a single item is added in the `contracts/items` block and the value of the contract is increased. A `amendments` block is included to explain the rationale of the changes.

See the example release below.

```{jsoninclude} ../../examples/amendments/contract.json
:jsonpointer: /records/0/releases/1
:expand: tag, contracts, items, amendments
:title: ContractAmendment
```

Note that amendments can cover more than values or duration. Also, note that the publisher chose to not repeat the contract items, but add a new one with a new ID value.

In certain scenarios there might not be a valid `amendsReleaseID` and so it can be omitted, e.g. when historical data is being published in a single release.

#### Record

An example record for the whole process is shown below. Consider downloading the [record example](../../examples/amendments/contract.json) and use the [Data Review Tool](https://review.standard.open-contracting.org/) to explore the changes in the contracting process.

Note that the `compiledRelease` contains all the items, included the latest one added in the contract amendment.

```{jsoninclude} ../../examples/amendments/contract.json
:jsonpointer:
:expand: records, releases
:title: Record
```

### Example 3: Amendments in a Easy Releases scenario

The [Easy releases guidance](../build/easy_releases) explains how to publish releases without storing or publishing a full change history. Depending on the source system, it might still be possible to publish a history of amendments when using this model.

Where the source system stores a history of contract amendments, either as separate notices or as properties of the original contract signature notice, contract amendments can be published as separate releases in OCDS. For example, Australia's AusTender platform [stores contract amendments as separate notices, related to the original contract signature notice](https://www.tenders.gov.au/Cn/Show/03a3c53e-b3bd-eac1-558a-4c659e44a516).

The table below shows an example of a contract signature notices table from a procurement system, with an original contract in the first row and an amendment of the same contract in the second. The amendment increases the value of the original contract and changes the contract period.

```{csv-table-no-translate}
:header-rows: 1
:file: ../../examples/amendments/contract_notice.csv
```

This can be modelled as the separate releases in OCDS as shown below. The original `contract` release includes all the fields from the first entry in the contract signature notices table. A `contractAmendment` release is built for each contract amendment identified in the table (by verifying that the `amendmentId` column in the contract signature notices table is not empty).

```{jsoninclude} ../../examples/amendments/easy_releases.json
:jsonpointer: /records/0/releases/1
:expand: tag, contracts
:title: Contract
```

```{jsoninclude} ../../examples/amendments/easy_releases.json
:jsonpointer: /records/0/releases/2
:expand: tag, contracts, amendments
:title: ContractAmendment
```

Note that the mapping of the fields remains the same for the contract amendments, except for the `description` column. When a row in the contract signature notices table is identified as an original contract, the description is included in the `contracts/description` field, and when the row represents a contract amendment, it is mapped to the `contracts/amendments/description` field. This aligns with the use of the `description` column, because for contract amendments it is used to include an explanation of the change.

The advantage of this approach, in contrast with the Easy releases proposal, is that the users have access to the details of each amendment instead of the latest values only without any additional effort of their end.

As in the previous examples, you can download a [record](../../examples/amendments/easy_releases.json) file for the example and use the [Data Review Tool](https://review.standard.open-contracting.org/) to explore the changes in the contracting process.
