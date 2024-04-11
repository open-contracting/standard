```{workedexample} Change history
:tags: release,record
```

# Change history

The following example shows how to publish data about a contracting process. Publish a release for each event in the process and update the record each time you publish a release.

Each subsection refers to a stage or event in the contracting process lifetime.

```{note}
For an introduction to the concept of a change history, see the [releases and records](../../primer/releases_and_records) primer.
```

```{note}
For guidance on how to set the `id` field on each release, see the [easy releases](easy_releases) worked example.
```

## Tender

The London Borough of Barnet publishes a tender for cycle lane improvements. They issue the tender via a *notice of intended procurement*.

The publisher creates a release to represent this notice. The release uses the 'tender' tag and provides the details in the `tender` section.

The publisher also creates a record for the new contracting process. The releases list includes the new and only release so far. The compiled and versioned releases are also created for the record. Since there is only one release, the compiled release is nearly identical to this release. Compare the release and the record using the box below.

```{jsoninclude} ../../examples/change_history/tender.json
:jsonpointer: /releases
:expand: tender, tag, documents
:title: release
```

```{jsoninclude} ../../examples/change_history/records/tender.json
:jsonpointer: /records
:expand: compiledRelease, tender, documents
:title: record
```

## Tender Update

The enquiry period has ended, and a few questions from potential suppliers have been received. The procuring entity issues a document with the responses to the enquiries received from bidders.

The publisher creates a new OCDS release with the 'tenderUpdate' tag.

The previous release is not changed. In the new release, the publisher adds a link to the new document in the `tender.documents` section. The `tender.hasEnquiries` field is also set to true. The publisher has decided to keep unchanged fields from the previous releases in the new one.

The record now has two immutable releases, and updated compiled and versioned releases. The compiled release now includes the enquiries document in the tender section. The versioned release has a new entry for the `tender.hasEnquiries` field.

```{jsoninclude} ../../examples/change_history/tenderUpdate.json
:jsonpointer: /releases
:expand: tender, tag, documents
:title: release
```

```{jsoninclude} ../../examples/change_history/records/tenderUpdate.json
:jsonpointer: /records
:expand: compiledRelease, tender, documents
:title: record
```

## Award

The procuring entity makes the decision to award the contract to Balfour Beatty. They issue an award notice. 

The publisher creates a new OCDS release for the award. The record has the relevant information in the award section and uses the 'award' tag. 

The `parties` array has a new entry with the supplier's information. The complete `tender` section is repeated, and its `finalStatus` field is set to 'complete'. Previous releases remain unchanged.

The publisher adds the new release to the record. They also update the compiled and versioned releases. The compiled release reflects the changes to the `tender`, `awards` and `parties` sections. The versioned release now sets the `tender.finalStatus` field.

```{jsoninclude} ../../examples/change_history/award.json
:jsonpointer: /releases
:expand: parties, tender, awards, value, suppliers, contractPeriod
:title: release
```

```{jsoninclude} ../../examples/change_history/records/award.json
:jsonpointer: /records
:expand: compiledRelease, parties, tender, awards, value, suppliers, contractPeriod
:title: record
```

## Contract

By law, the procuring entity has to wait for complaints for a given period of time before signing a contract. Once the period ends with no complaints, the contract with the supplier is signed.

The publisher creates a new OCDS release using the 'contract' tag. They include all the relevant information in the `contracts` section.

The record gets updated to include the new release. The compiled and versioned releases now set the `contracts` section. There are no updates to other sections.

```{jsoninclude} ../../examples/change_history/contract.json
:jsonpointer: /releases
:expand: contracts, value, period
:title: release
```

```{jsoninclude} ../../examples/change_history/records/contract.json
:jsonpointer: /records
:expand: compiledRelease, contracts, value, period
:title: record
```

## Implementation

The supplier starts the construction work. After a while, the buyer makes the first payment to the supplier. The publisher creates a release to document this update in the process.

So far, the council used a single procurement system to manage the process. The procurement system published the previous OCDS releases.

The council now uses a separate financial system to manage payments. The financial system publishes the new OCDS release.

The procurement system and the financial system share a common identifier for contracting processes. This means that the two systems can publish releases using the same `ocid`.

The new release uses the 'implementation' tag. The `contracts.implementation.transactions` section includes the details of the payment.

Because the new release uses the same `ocid`, it is possible to update the record with the information.

```{admonition} Combining data from different systems
:class: hint

OCDS can be used to combine data from different systems. For more information refer to the guidance on system architectures.
```

The publisher adds the new release from the finance system to the releases list in the OCDS record. The compiled and versioned releases now set the transaction.

```{jsoninclude} ../../examples/change_history/implementation.json
:jsonpointer: /releases
:expand: contracts, implementation, transactions
:title: release
```

```{jsoninclude} ../../examples/change_history/records/implementation.json
:jsonpointer: /records
:expand: compiledRelease, contracts, implementation, transactions
:title: record
```

## Contract Amendment

Unexpected complications causes delays in the construction work. Because of them the procuring entity and the supplier agree to a contract extension. This will cover the extra time and cost needed to complete the works. 

The publisher updates their procurement system with the new contract value and period. They issue a modification notice through the system. They also create a new OCDS with the 'contractAmendment' tag to represent the notice.

```{note}
Contract amendments in OCDS involves more modelling considerations. See the [amendments example](../map/amendments).
```

The publisher updates the record for the contracting process with the new release. The compiled release has the new values. The versioned release has new entries for the contract's value and end date.

```{jsoninclude} ../../examples/change_history/contractAmendment.json
:jsonpointer: /releases
:expand: contracts, amendments
:title: release
```

```{jsoninclude} ../../examples/change_history/records/contractAmendment.json
:jsonpointer: /records
:expand: compiledRelease, contracts, amendments
:title: record
```
