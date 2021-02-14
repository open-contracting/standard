# Amendments

Information about a contracting process will often change over time.

Each time information changes, a new OCDS release ought to be published.

There are three kinds of changes:

* **New information**. For example, when information about the award of a contract is first released.
* **Updates to existing information**. For example, to correct errors in earlier releases, or to make minor adjustments to titles, descriptions or date.
* **Amendments**. For example, when the value or duration of a contract is changed. The term amendment often has a specific legal meaning for a publisher. Certain changes to a tender, award or contract might only be allowed as part of an amendment.

The nature of a change can be made explicit using:

* **The release tag** (`tag`). For example, for a release with a new contract, use 'contract'. For an update to the contract, use 'contractUpdate', and for an amendment to the contract, use 'contractAmendment'.

* **The amendments** building block. This can contain an array of amendment explanations, and clearly identify the releases that contain before and after values.

## Worked examples

### Example 1: Tender updates and amendments

This example goes through updates during the **tender** stage in a contracting process.

#### Tender

A publisher issues a tender for a "Data merge tool". A new release with the `tag` 'tender' is built, see the JSON example below.

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-tender-example.json
   :jsonpointer: /records/0/releases/0
   :expand: tender, tag
   :title: Tender

```

#### Tender Update

Weeks later, the publisher expands the `description` of the tender to provide more details about the tool being procured. A new release with the `tag` 'tenderUpdate' is built. The publisher does not consider this to be a formal 'amendment' to the tender, so does not publish any amendment information. See the JSON release below.

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-tender-example.json
   :jsonpointer: /records/0/releases/1
   :expand: tender, tag
   :title: TenderUpdate

```

#### Tender Amendment

A few days later, the publisher increases the value of the tender and extends the deadline for bid submissions. These changes are considered as an 'amendment' by the publisher (depending on jurisdiction, certain changes can need to be disclosed as amendments), and so the new release has the `tag` 'tenderAmendment' and an `amendments` block under `tender`. The release reflects the updated value (USD 2000 instead of USD 1000) and the updated closing date for bid submissions (`2012-02-20` instead of `2012-02-15`). See the JSON example below.

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-tender-example.json
   :jsonpointer: /records/0/releases/2
   :expand: tender, tag, amendments
   :title: TenderAmendment

```

#### Record

A full record is provided below, with all the releases for the process and a `compiledRelease` and `versionedRelease`. The `versionedRelease` block reflects all the changes made in the tender.

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-tender-example.json
   :jsonpointer:
   :expand: records, releases
   :title: FullRecord

```

<div class="example hint" markdown=1>

<p class="first admonition-title">Hint</p>

It is encouraged to <a href="../../../_static/json/amendments/amendments-tender-example.json" target="_blank">download</a> the record example and use the [Data Review Tool](https://standard.open-contracting.org/review) to explore the changes in the contracting process.

</div>

Note in this example that:

* **The amendments block does not contain data on what was changed**. Changes are recorded by updating the fields of the `tender` block a new release.

* **The publisher chooses in the 'tenderAmendment' release to repeat a fragment of the original 'tender' release**. This is not necessary when a full archive of releases is made accessible, but a publisher might want to provide the latest data available in each release.

* **In the record**, the `releaseID` and `amendsReleaseID` fields from the `amendments` array can be used to look up information in the `versionedRelease` object or `releases` array, to see where changes are explained by an amendment `rationale`.

### Example 2: Contract amendment

This example shows an update to the value and scope of a contract.

#### Contract

A contract notice is published for the purchase of domestic appliances. The publisher builds a release and uses the 'contract' `tag`.

See the JSON release below.

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-contract-example.json
   :jsonpointer: /records/0/releases/0
   :expand: tag, contracts, items
   :title: Contract

```

#### Contract Amendment

A few days after the contract release, its scope is increased to include the purchase of one additional appliance. A new 'contractAmendment' release is built, where a single item is added in the `contracts/items` block and the value of the contract is increased. A `amendments` block is included to explain the rationale of the changes.

See the example release below.

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-contract-example.json
   :jsonpointer: /records/0/releases/1
   :expand: tag, contracts, items, amendments
   :title: ContractAmendment

```

Note that amendments can cover more than values or duration. Also, note that the publisher chose to not repeat the contract items, but add a new one with a new ID value.

In certain scenarios there might not be a valid `amendsReleaseID` and so it can be omitted, e.g. when historical data is being published in a single release.

#### Record

An example record for the whole process is shown below. Consider downloading the <a href="../../../_static/json/amendments/amendments-contract-example.json" target="_blank">record example</a> and use the [Data Review Tool](https://standard.open-contracting.org/review) to explore the changes in the contracting process.

Note that the `compiledRelease` contains all the items, included the latest one added in the contract amendment.

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-contract-example.json
   :jsonpointer:
   :expand: records, releases
   :title: Record

```

### Example 3: Amendments in a Easy Releases scenario

The [Easy releases guidance](../build/easy_releases) explains how to publish releases without storing or publishing a full change history. Depending on the source system, it might still be possible to publish a history of amendments when using this model.

Where the source system stores a history of contract amendments, either as separate notices or as properties of the original contract notice, contract amendments can be published as separate releases in OCDS. For example, Australia's AusTender platform [stores contract amendments as separate notices, related to the original contract notice](https://www.tenders.gov.au/Cn/Show/03a3c53e-b3bd-eac1-558a-4c659e44a516).

The table below shows an example of a contract notices table from a procurement system, with an original contract in the first row and an amendment of the same contract in the second. The amendment increases the value of the original contract and changes the contract period.

```{eval-rst}
.. csv-table-no-translate::
   :file: ../../examples/amendments-contract-notice.csv
   :header-rows: 1
```

This can be modelled as the separate releases in OCDS as shown below. The original `contract` release includes all the fields from the first entry in the contract notices table. A `contractAmendment` release is built for each contract amendment identified in the table (by verifying that the `amendmentId` column in the contract notices table is not empty).

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-easy-releases-example.json
   :jsonpointer: /records/0/releases/1
   :expand: tag, contracts
   :title: Contract

```

```{eval-rst}

.. jsoninclude:: ../../_static/json/amendments/amendments-easy-releases-example.json
   :jsonpointer: /records/0/releases/2
   :expand: tag, contracts, amendments
   :title: ContractAmendment
```

Note that the mapping of the fields remains the same for the contract amendments, except for the `description` column. When a row in the contract notices table is identified as an original contract, the description is included in the `contracts/description` field, and when the row represents a contract amendment, it is mapped to the `contracts/amendments/description` field. This aligns with the use of the `description` column, because for contract amendments it is used to include an explanation of the change.

The advantage of this approach, in contrast with the Easy releases proposal, is that the users have access to the details of each amendment instead of the latest values only without any additional effort of their end.

As in the previous examples, you can download a <a href="../../../_static/json/amendments/amendments-easy-releases-example.json" target="_blank">record</a> file for the example and use the [Data Review Tool](https://standard.open-contracting.org/review) to explore the changes in the contracting process.
