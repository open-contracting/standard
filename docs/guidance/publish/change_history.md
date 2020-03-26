# Change history

The following example shows how to publish the full history of a contracting process using releases and records. Each subsection refers to a stage or event in the contracting process lifetime.

Refer to the [change history](../../getting_started/change_history) guidance for an introduction to the concepts involved.

### Planning

In order to prepare the market for the tender for cycle lane improvements which is planned for later in the year, the London Borough of Barnet publishes a 'notice of planned procurement' (also known as 'prior information notice' or 'future opportunity notice').

The notice is represented in OCDS as a release with the 'planning' tag and data on the planned procurement, such as the estimated date the tender will be issued, is provided in the `tender` section with `.status` set to 'planned'. The `releases` list in the record for the contracting process is updated to include the ‘planning’ release, the only one that exists for the process at the moment. The compiled and versioned releases inside the record contain the latest information, which should be very similar to the 'planning' release. Compare the planning release and the record using the box below.


```eval_rst

.. jsoninclude:: ../../examples/planning.json
   :jsonpointer: /releases
   :expand: planning, tag, tender
   :title: release

```

```eval_rst

.. jsoninclude:: ../../examples/records/planning.json
   :jsonpointer: /records
   :expand: compiledRelease, planning, tender
   :title: record

```

### Tender

The London Borough of Barnet is ready to invite bids for the contract, so they issue the tender via an 'notice of intended procurement' (also known as 'contract notice' or 'opportunity notice').

In OCDS, the notice is represented as a new release, using the 'tender' tag and providing details in the 'tender' section.

No changes are made to the already published planning release, however the `tender` section of the new tender release is updated with the actual date the tender was issued, along with additional information about the deadline for bid submission, the items being procured, links to copies of tender documents and the estimated tender value.

The tender release is added to the `releases` list in the record for the contracting process and the compiled release is updated to reflect the latest values for the new and updated fields in the 'tender' release. Note that the bid submission dates have been updated in the compiled release, and the versioned release now contains a list of changes for each field.


```eval_rst

.. jsoninclude:: ../../examples/tender.json
   :jsonpointer: /releases
   :expand: tender, tag, documents
   :title: release

```

```eval_rst

.. jsoninclude:: ../../examples/records/tender.json
   :jsonpointer: /records
   :expand: compiledRelease, tender, documents
   :title: record

```

### Tender Update

The enquiry period has ended, and a few questions from potential suppliers have been received. The procuring entity issues a document with the responses to the enquiries received from bidders.

In OCDS, a new release is published using the 'tenderUpdate' tag.

No changes are made to the existing planning and tender releases, however in the new release a link to the enquiry responses is added to `tender.documents`.

The `hasEnquiries` field is set to true.

The publisher has decided to include all unchanged fields and values for the previous immutable release in the new one.

The record for the contracting process now has three immutable releases, and updated compiled and versioned releases. Note that the compiled release has included the enquiries document in the tender section, and the field hasEnquiries has more than one entry in the versioned release.

```eval_rst

.. jsoninclude:: ../../examples/tenderUpdate.json
   :jsonpointer: /releases
   :expand: tender, tag, documents
   :title: release

```

```eval_rst

.. jsoninclude:: ../../examples/records/tenderUpdate.json
   :jsonpointer: /records
   :expand: compiledRelease, tender, documents
   :title: record

```

### Award

The procuring entity makes the decision to award the contract to Balfour Beatty and issues an award notice. 

The award notice is represented as a new OCDS release with the details of the award provided in the `award` section and using the 'award' tag. An entry is added to the `parties` array to provide information about the supplier and the full tender block is included as well with the `.status` field set to 'complete'. No changes are made to the existing planning, tender and tenderUpdate releases.

The record for the contracting process has been updated to include the latest release, and the compiled and versioned releases have been updated accordingly. The compiled release has an award block and the supplier in parties, and the status of the tender has been updated to 'complete' as well. The versioned release also reflects the change in the status field.

```eval_rst

.. jsoninclude:: ../../examples/award.json
   :jsonpointer: /releases
   :expand: parties, tender, awards, value, suppliers, contractPeriod
   :title: release

```

```eval_rst

.. jsoninclude:: ../../examples/records/award.json
   :jsonpointer: /records
   :expand: compiledRelease, parties, tender, awards, value, suppliers, contractPeriod
   :title: record

```

### Contract

After the standstill period has passed and no complaints have been issued against the award of the contract, the procuring entity and the supplier sign the contract. A new OCDS release is published using the 'contract' tag with the `contracts` section populated.

The record now has an additional release, and the compiled and versioned releases now include the contract section with no other changes.


```eval_rst

.. jsoninclude:: ../../examples/contract.json
   :jsonpointer: /releases
   :expand: contracts, value, period
   :title: release

```

```eval_rst

.. jsoninclude:: ../../examples/records/contract.json
   :jsonpointer: /records
   :expand: compiledRelease, contracts, value, period
   :title: record

```


### Implementation

The supplier has started the construction work, and the procuring entity makes the first payment against the contract using their finance system, which shares a common contract identifier with the contract register. 

An OCDS release is published from the finance system using the 'implementation' tag, with details of the payment provided in the `contracts.implementation.transactions` section.

Since the previous releases from the contract register share a common `ocid` with the release from the finance system, it’s possible to update the OCDS record for the contracting process with the new information from the finance system.

<div class="example hint" markdown=1>

<p class="first admonition-title">Combining data from different systems</p>

Refer to the guidance on system architecture for more information on how OCDS can be used to combine data from different systems.

</div>

The new release from the finance system is added to the releases list in the OCDS record and both the compiled and versioned releases are updated to include the new transaction.


```eval_rst

.. jsoninclude:: ../../examples/implementation.json
   :jsonpointer: /releases
   :expand: contracts, implementation, transactions
   :title: release

```

```eval_rst

.. jsoninclude:: ../../examples/records/implementation.json
   :jsonpointer: /records
   :expand: compiledRelease, contracts, implementation, transactions
   :title: record

```

### Contract Amendment

Due to unforeseen complications with subsistence in the area of the works, the procuring entity and the supplier agree to a contract extension to cover the additional time and cost required to complete the works. The contract register is updated with the new contract value and period and a modification notice is issued, this is represented in OCDS as a new release with the 'contractAmendment' tag.

Refer to the amendments worked example for more information on how contract amendments are modelled in OCDS.

The record for the contracting process is updated with an entry in the releases list for the new contract amendment release. The compiled release reflects the new values, and the versioned release shows new entries for the contract’s value and end date.


```eval_rst

.. jsoninclude:: ../../examples/contractAmendment.json
   :jsonpointer: /releases
   :expand: contracts, amendments
   :title: release

```

```eval_rst

.. jsoninclude:: ../../examples/records/contractAmendment.json
   :jsonpointer: /records
   :expand: compiledRelease, contracts, amendments
   :title: record

```
