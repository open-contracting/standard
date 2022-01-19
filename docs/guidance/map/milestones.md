```{workedexample} Milestones
:tags: milestone,planning,tender,contract,implementation
```
# Milestones

Milestones can be included within the planning, tender, contract and contract implementation sections. 

## Planning

The planning milestones block is used for two types of milestones:
 * Key events in the planning process, for example, the preparation of an environmental impact assessment, the approval to proceed with a project, or the date of a public consultation. 
 * Anticipated milestones during the contract implementation stage, for example, the date by which goods delivery of the goods is required.

If during the planning process you have information about tender process milestones, then you
populate the tender milestones block instead.

## Tender

The tender milestones block is used to describe two types of milestone:
  * Key dates in the tender and award stages which are not covered by other fields, for example, the date by which procuring entity will respond to enquiries.
  * Anticipated milestones during the contract implementation stage, for example, the date by which goods need to be delivered.

## Contract

The contract milestones block is used to describe:
  * Events related to the signing of the contract, for example, the date of commercial close in a PPP contract.
 
## Contract Implementation

The contract implementation milestones block is used to describe:
  * Any events related to the delivery of the contract, for example, the agreed date by which goods will be delivered.

The nature of the milestone is indicated by the [milestone type codelist](../../schema/codelists.md#milestone-type), for example, to distinguish between milestones in the planning section which relate to events in the pre-procurement phase and those which relate to contract implementation.

At the point of contract signature, a comparison between `tender/milestones` and `contract/implementation/milestones` with a `milestone/type` of 'delivery' or 'reporting' should reveal how the negotiated contract differs from what was set out at tender time.

The `dueDate`, `dateMet`, `dateModified` and [`status`](../../schema/codelists.md#milestone-status) fields are used to track the lifecycle of the milestone.

To represent a planned payment, add a `Milestone`, set its `.type` to 'payment' and set its `.value` to the payment's value. Once the milestone is met, add a [Transaction](../../schema/reference.md#transaction) to `contracts/implementation/transactions`. For implementation milestones, the transaction can refer back to the milestone using the [transaction-related milestones extension](https://extensions.open-contracting.org/en/extensions/transaction_milestones/master/).

## Worked examples

The following worked examples show how to use milestones in different scenarios.

### Planning milestones

The example below includes a planning release with details of a planned procurement, including the date the budget plan is expected to be ready.

The date the budget plan is expected to be ready is represented using a milestone in `planning/milestones` with `.type` is set to 'preProcurement' because the milestone relates to the planning process. `.dueDate` is set to the date and `.status` is set to 'scheduled'.

```{jsoninclude} ../../examples/milestones/planning-tender-milestones.json
:jsonpointer:
:expand: releases, planning, milestones
:title: planning
```

### Contract implementation milestones

The following worked examples show how to use milestones in contract implementation releases

#### Project data

This worked example shows how to use milestones to model the planned and actual start and finish dates for a construction project.

The example below includes three OCDS releases:

* An implementation release which includes the scheduled start and end dates for the project.
* An implementation update release with the actual start date of the project
* An implementation update release with the actual end date of the project

In the award release:

* The scheduled start and end dates for the project are represented using milestones in `contracts/implementation/milestones` with `.type` set to 'delivery' because they relate to the delivery of the contract. The dates are provided in `.dueDate` and `.status` is set to 'scheduled'.
* The publisher has defined their own values for the `.code` field so they can filter and compare start and end date milestones across different contracts.

In the first implementation update release, which is published after the project starts but before it completes:
* In the project commencement milestone, `.dateMet` is set to the actual start date and `.status` is set to 'met'. `.dateModified` is set to the date the milestone was updated.
* In the project completion milestone, `.status` is set to 'notMet' since the project is not yet complete and `.dateModified` is set to the date the milestone was updated.

Users can compare the project commencement milestone's `.dueDate` and `.dateMet` fields to determine if the project started on time. Users can also compare the project completion milestone's `.dueDate` and `.dateModified` fields to determine whether the `.status` has been updated since the scheduled completion date.

In the second implementation update release, which is published after the project completes:
* In the project completion milestone, `.dateMet` is set to the actual completion date for the project and `.status` is set to 'met'.

```{jsoninclude} ../../examples/milestones/implementation-milestones-1.json
:jsonpointer:
:expand: releases, contracts, implementation, milestones
:title: implementation
```

```{jsoninclude} ../../examples/milestones/implementation-milestones-2.json
:jsonpointer:
:expand: releases, contracts, implementation, milestones
:title: implementation-update-1
```

```{jsoninclude} ../../examples/milestones/implementation-milestones-3.json
:jsonpointer:
:expand: releases, contracts, implementation, milestones
:title: implementation-update-2
```

#### Delivery and payment data

This example shows how milestones can be used to keep track of delivery and payment data in a contracting process.

The example below includes three OCDS releases:

* An implementation release with contract information including scheduled implementation milestones and planned payments.
* An implementation update release with the actual date the milestone was reached.
* An implementation update release with payment information

In the implementation release:

* Milestones have been set for the delivery and payment of goods and services related to the project. Contract information is released along with the implementation milestones.

In the first implementation update release:

* The milestone ("Finish the exterior and interior walls") has been met, so the `status` field is set to 'met' and the relevant dates are added to the `dateMet` and `dateModified` fields.

In the second implementation update release:

* The construction company has received payment for the work done so far, so the milestone for the wall restoration with type 'payment' is updated. A new `transaction` is disclosed, with the amount paid to the company. The [transaction-related milestones extension](https://extensions.open-contracting.org/en/extensions/transaction_milestones/master/) is used to link the transaction to the milestone.

```{jsoninclude} ../../examples/milestones/af-implementation-milestones-1.json
:jsonpointer:
:expand: releases, contracts, implementation, milestones
:title: implementation
```

```{jsoninclude} ../../examples/milestones/af-implementation-milestones-2.json
:jsonpointer:
:expand: releases, contracts, implementation, milestones
:title: implementation-update-1
```

```{jsoninclude} ../../examples/milestones/af-implementation-milestones-3.json
:jsonpointer:
:expand: releases, contracts, implementation, milestones, transactions
:title: implementation-update-2
```
