# Amendments

Information about a contracting process will often change over time.

Each time information changes, a new OCDS release should be published. 

There are three kinds of changes:

* **New information**. For example, when information about the award of a contract is first released.
* **Updates to existing information**. For example, to correct errors in earlier releases, or to make minor adjustments to titles, descriptions or date. 
* **Amendments**. For example, when the value or duration of a contract is changed. The term amendment often has a specific legal meaning for a publisher. Certain changes to a tender, award or contract may only be allowed as part of an amendment. 

The nature of a change can be made explicit using:

* **The release tag** (`tag`). For example, for a release with a new contract, use 'contract'. For an update to the award, use 'contractUpdate', and for an amendment to the contract, use 'contractAmendment'. 

* **The amendments** building block. This can contain an array of amendment explanations, and clearly identify the releases that contain before and after values. 

## Worked example

In the example below:

* A tender is issued for a "Data merge tool" in a release with the `tag` 'tender'. 
* This is updated in a release with the `tag` 'tenderUpdate' to provide an expanded description of the item. The publisher did not consider this to be a formal 'amendment' to the tender, so did not publish any amendment information.
* The tender is then formally amended, with an increased value. This is published in a release with the `tag` 'tenderAmendment', and an `amendments` block under `tender`.


```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-tender-1.json
   :jsonpointer: 
   :expand: releases, tender, tag
   :title: tender

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-tender-2.json
   :jsonpointer: 
   :expand: releases, tender, tag
   :title: tenderUpdate

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-tender-3.json
   :jsonpointer: 
   :expand: releases, tender, tag, amendments
   :title: tenderAmendment

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/versioned.json
   :jsonpointer: 
   :expand: records, compiledRelease, tender, tag, versionedRelease, tender, value, amount, releaseTag, amendments
   :title: versionedRecord

```


Note in this example that:

* **The publisher chooses in the tenderAmendment release to repeat a fragment of the original 'tender' release**, so that the before and after values of the tender can be accessed in the single file. This is not required when a full archive of releases is made accessible, but can be a convenient way of publishers making structured information on the before and after values of a field more accessible to users. 

* **In the merged record**, the information in the `amendments` array can be used to lookup information in the `versionedRelease` section, to see where changes are explained by an amendment `rationale`. 



