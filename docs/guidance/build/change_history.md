# Change history

The following example shows how to publish data about a contracting process. Publish a release for each event in the process and update the record each time you publish a release.

Each subsection refers to a stage or event in the contracting process lifetime.

Refer to the [releases and records](../../getting_started/releases_and_records) guidance for an introduction to the concepts involved.

## Planning

The London Borough of Barnet plans to publish a tender for cycle lane improvements later in the year. To prepare the market they publish a *notice of planned procurement*. This is also known as *prior information notice*, or *future opportunity notice*.

The publisher creates an OCDS release to represent this notice. The release uses the 'planning' tag and includes data about the planned procurement. The `tender` section holds the estimated values and publication date. The tender status is 'planned'.

The publisher also creates an OCDS record for the new contracting process. The releases list includes the new and only release so far. The compiled and versioned releases are also created for the record. Since there is only one release, the compiled version is expected look very much like this release. Compare the planning release and the record using the box below.


```{eval-rst}

.. jsoninclude:: ../../examples/planning.json
   :jsonpointer: /releases
   :expand: planning, tag, tender
   :title: release

```

```{eval-rst}

.. jsoninclude:: ../../examples/records/planning.json
   :jsonpointer: /records
   :expand: compiledRelease, planning, tender
   :title: record

```

## Tender

The London Borough of Barnet is ready to invite bids for the contract. They issue the tender via an *notice of intended procurement*. This is also known as *contract notice* or *opportunity notice*.

The publisher creates a new release to represent this notice. The release uses the 'tender' tag and provides the details in the `tender` section.

There are no changes to the planning release published before. But the new release has the updated information about the tender. This includes the actual publication date, and the following new information:

* The deadline for bid submission

* The items to buy

* Links to copies of tender documents

* The estimated tender value

The publisher adds the new release to the record, in the releases list. Also they update the compiled and versioned releases with the new information. Note that the bid submission date has changed in the compiled release. Also, note that the versioned release has a list of changes for each field that has been updated.


```{eval-rst}

.. jsoninclude:: ../../examples/tender.json
   :jsonpointer: /releases
   :expand: tender, tag, documents
   :title: release

```

```{eval-rst}

.. jsoninclude:: ../../examples/records/tender.json
   :jsonpointer: /records
   :expand: compiledRelease, tender, documents
   :title: record

```

## Tender Update

The enquiry period has ended, and a few questions from potential suppliers have been received. The procuring entity issues a document with the responses to the enquiries received from bidders.

The publisher creates a new OCDS release with the 'tenderUpdate' tag.

The previous releases of planning and tender are not changed. In the new release, the publisher adds a link to the new document in the `tender.documents` section. The `tender.hasEnquiries` field is also set to true. The publisher has decided to keep unchanged fields from the previous releases in the new one.

The record now has three immutable releases, and updated compiled and versioned releases. Note that the compiled release includes the enquiries document in the tender section. Also, the field `tender.hasEnquiries` has more than one entry in the versioned release.

```{eval-rst}

.. jsoninclude:: ../../examples/tenderUpdate.json
   :jsonpointer: /releases
   :expand: tender, tag, documents
   :title: release

```

```{eval-rst}

.. jsoninclude:: ../../examples/records/tenderUpdate.json
   :jsonpointer: /records
   :expand: compiledRelease, tender, documents
   :title: record

```

## Award

The procuring entity makes the decision to award the contract to Balfour Beatty. They issue an award notice. 

The publisher creates a new OCDS release for the award. The record has the relevant information in the award section and uses the 'award' tag. 

The `parties` array has a new entry with the supplier's information. The complete `tender` section is repeated, with the `status` field set to 'complete'. Previous releases remain unchanged.

The publisher adds the new release to the record. They also update the compiled and versioned releases. The compiled release reflects the changes to the `awards`, `tender` and `parties` sections. The versioned release includes a new change for the `tender.status` field.

```{eval-rst}

.. jsoninclude:: ../../examples/award.json
   :jsonpointer: /releases
   :expand: parties, tender, awards, value, suppliers, contractPeriod
   :title: release

```

```{eval-rst}

.. jsoninclude:: ../../examples/records/award.json
   :jsonpointer: /records
   :expand: compiledRelease, parties, tender, awards, value, suppliers, contractPeriod
   :title: record

```

## Contract

By law, the procuring entity has to wait for complaints for a given period of time before signing a contract. Once the period ends with no complaints, the contract with the supplier is signed.

The publisher creates a new OCDS release using the 'contract' tag. They include all the relevant information in the `contracts` section.

The record gets updated to include the new release. The compiled and versioned release now have the new `contract` section. There are no updates to other sections.


```{eval-rst}

.. jsoninclude:: ../../examples/contract.json
   :jsonpointer: /releases
   :expand: contracts, value, period
   :title: release

```

```{eval-rst}

.. jsoninclude:: ../../examples/records/contract.json
   :jsonpointer: /records
   :expand: compiledRelease, contracts, value, period
   :title: record

```


## Implementation

The supplier starts the construction work. After a while, the procuring entity makes the first payment to the supplier. The publisher creates a release to document this update in the process.

So far, the council used a single procurement system to manage the process. The procurement system published the previous OCDS releases.

The council now uses a separate financial system to manage payments. The financial system publishes the new OCDS release.

The procurement system and the financial system share a common contracting process identifier. This means that the two systems can publish releases using the same `ocid`.

The new release uses the 'implementation' tag. The `contracts.implementation.transactions` section includes the details of the payment.

Because the new release uses the same `ocid`, it is possible to update the record with the information.

<div class="example hint" markdown=1>

<p class="first admonition-title">Combining data from different systems</p>

OCDS can be used to combine data from different systems. For more information refer to the guidance on system architectures.

</div>

The publisher adds the new release from the finance system to the releases list in the OCDS record. The compiled and versioned releases get updated to include the new transaction.


```{eval-rst}

.. jsoninclude:: ../../examples/implementation.json
   :jsonpointer: /releases
   :expand: contracts, implementation, transactions
   :title: release

```

```{eval-rst}

.. jsoninclude:: ../../examples/records/implementation.json
   :jsonpointer: /records
   :expand: compiledRelease, contracts, implementation, transactions
   :title: record

```

## Contract Amendment

Unexpected complications causes delays in the construction work. Because of them the procuring entity and the supplier agree to a contract extension. This will cover the extra time and cost needed to complete the works. 

The publisher updates their procurement system with the new contract value and period. They issue a modification notice through the system. They also create a new OCDS with the 'contractAmendment' tag to represent the notice.

Note that contract amendments in OCDS involves more modelling considerations. Refer to the amendments worked example for guidance on the topic.

The publisher updates the record for the contracting process with the new release. The compiled release has the new values. The versioned release shows new entries for the contract’s value and end date.


```{eval-rst}

.. jsoninclude:: ../../examples/contractAmendment.json
   :jsonpointer: /releases
   :expand: contracts, amendments
   :title: release

```

```{eval-rst}

.. jsoninclude:: ../../examples/records/contractAmendment.json
   :jsonpointer: /records
   :expand: compiledRelease, contracts, amendments
   :title: record

```
