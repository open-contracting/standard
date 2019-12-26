# Amendments

Information about a contracting process will often change over time.

Each time information changes, a new OCDS release ought to be published. 

There are three kinds of changes:

* **New information**. For example, when information about the award of a contract is first released.
* **Updates to existing information**. For example, to correct errors in earlier releases, or to make minor adjustments to titles, descriptions or date. 
* **Amendments**. For example, when the value or duration of a contract is changed. The term amendment often has a specific legal meaning for a publisher. Certain changes to a tender, award or contract might only be allowed as part of an amendment. 

The nature of a change can be made explicit using:

* **The release tag** (`tag`). For example, for a release with a new contract, use 'contract'. For an update to the award, use 'contractUpdate', and for an amendment to the contract, use 'contractAmendment'. 

* **The amendments** building block. This can contain an array of amendment explanations, and clearly identify the releases that contain before and after values. 

## Worked examples

Each example includes sample JSON files located at the bottom of the page. Use the combobox at the end of the page to display the files for each example and step.

### Example 1: Tender

This example goes through updates during the **tender** stage in a contracting process.

1. A tender is issued for a "Data merge tool" in a release with the `tag` 'tender'. 
2. Information is updated in a new release with the `tag` 'tenderUpdate' to provide an expanded description of the item. The publisher did not consider this to be a formal 'amendment' to the tender, so did not publish any amendment information.
3. Then there is a new update, where the value of the tender increases and the deadline for bid submissions is extended. This is considered as an 'amendment' by the publisher (depending of jurisdiction, both changes require an official approval), and so the new release has the `tag` 'tenderAmendment' and an `amendments` block under `tender`. The release reflects the updated value (USD 2000 instead of USD 1000) and the updated closing date for bid submissions (`2012-02-20` instead of `2012-02-15`).

Note in this example that:

* **The amendments block does not contain amended values (as in previous versions of OCDS)**. Values are updated in the same fields and using a new release. 

* **The publisher chooses in the tenderAmendment release to repeat a fragment of the original 'tender' release**. This is not necessary when a full archive of releases is made accessible, but can be a convenient way of publishers making structured information on the before and after values of a field more accessible to users. 

* **In the merged record**, the information in the `amendments` array can be used to lookup information in the `versionedRelease` section, to see where changes are explained by an amendment `rationale`. 

### Example 2: Contract

This example shows an update in the value and scope of a contract.

1. A contract notice is published for the purchase of domestic appliances. The release uses the 'contract' `tag`.
2. The scope of the contract is increased to include the purchase of one additional appliance. A single item is added in the `contracts/items` block and the value of the contract is increased.

Note that amendments can cover more than values or duration. In the amendment release, the publisher chose to not repeat the contract items, but add a new one with a new ID value.

In certain scenarios there may not be a valid `amendsReleaseID` and so it can be omitted, e.g. when historical data is being published in a single release.

```eval_rst

.. jsoninclude:: ../examples/merging/merge-tender-1.json
   :jsonpointer: 
   :expand: releases, tender, tag
   :title: Example1_1-Tender

```

```eval_rst

.. jsoninclude:: ../examples/merging/merge-tender-2.json
   :jsonpointer: 
   :expand: releases, tender, tag
   :title: Example1_2-TenderUpdate

```

```eval_rst

.. jsoninclude:: ../examples/merging/merge-tender-3.json
   :jsonpointer: 
   :expand: releases, tender, tag, amendments
   :title: Example1_3-TenderAmendment

```

```eval_rst

.. jsoninclude:: ../examples/merging/versioned-tender.json
   :jsonpointer: 
   :expand: records, compiledRelease, tender, tag, versionedRelease, tender, value, amount, releaseTag, amendments
   :title: Example1_MergedRecord

```

```eval_rst

.. jsoninclude:: ../examples/merging/merge-contract-1.json
   :jsonpointer: 
   :expand: releases, tag, contracts, items
   :title: Example2_1-Contract

```

```eval_rst

.. jsoninclude:: ../examples/merging/merge-contract-2.json
   :jsonpointer: 
   :expand: releases, tag, contracts, items, amendments
   :title: Example2_2-ContractAmendment

```

```eval_rst

.. jsoninclude:: ../examples/merging/versioned-contract.json
   :jsonpointer: 
   :expand: records, compiledRelease, versionedRelease
   :title: Example2_MergedRelease

```

