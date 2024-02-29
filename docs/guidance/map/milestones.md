```{workedexample} Milestones
:tags: milestone,planning,tender,contract,implementation
```

# Milestones

Milestones can be included within the planning, tender, contract and contract implementation sections. 

## Planning

The planning milestones block is used for two types of milestones:
 * Key events in the planning process, for example, the preparation of an environmental impact assessment, the approval to proceed with a project, or the date of a public consultation. 
 * Anticipated milestones during the contract implementation stage, for example, the date by which goods delivery of the goods is required.

If during the planning process you have information about tender process milestones, then you ought to
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

The nature of a milestone is indicated by the [milestone type codelist](../../schema/codelists.md#milestone-type), for example, a milestone representing a draft bid submission deadline would use the 'procurement' code, whilst a milestone representing the date by which goods are to be provided would use the 'delivery' code. 

At the point of contract signature, a comparison between `tender/milestones` and `contract/implementation/milestones` with a `milestone/type` of 'delivery' or 'reporting' should reveal how the negotiated contract differs from what was set out at tender time.

The `dueDate`, `dateMet`, `dateModified` and [`status`](../../schema/codelists.md#milestone-status) fields are used to track the lifecycle of the milestone.

To represent a planned payment, add a `Milestone`, set its `.type` to 'payment' and set its `.value` to the payment's value. Once the milestone is met, add a [Transaction](../../schema/reference.md#transaction) to `contracts/implementation/transactions`. For implementation milestones, the transaction can refer back to the milestone using the [transaction-related milestones extension](https://extensions.open-contracting.org/en/extensions/transaction_milestones/master/).

## Worked examples

The following worked examples show how milestones are modelled.

### Planning milestones

A buyer publishes information about a new planning process, including the date the budget is expected to be approved.

Because the approval relates to a planning process, it is modelled as a milestone in `planning.milestones` with `.type` set to 'preProcurement'. `.dueDate` is set to the expected date of the approval and `.status` is set to 'scheduled' because the approval has not yet occurred.

```{jsoninclude} ../../examples/milestones/planning_milestones.json
:jsonpointer: /releases/0
:expand: planning, milestones
```

### Delivery milestones

This worked example shows how delivery milestones are modelled.

#### Implementation release

A buyer publishes the expected completion date of a construction project.

Because the completion date relates to contract delivery, it is modelled as a milestone in `contracts.implementation.milestones` with `.type` set to 'delivery'. `.dueDate` is set to the expected completion date and `.status` is set to 'scheduled' because the project is not yet complete.

The publisher defines their own value for the milestone's `.code` so that they can filter and compare completion dates across different contracts.

```{jsoninclude} ../../examples/milestones/delivery_milestones.json
:jsonpointer: /releases/0
:expand: tag, contracts, implementation, milestones
```

#### Implementation update release

The buyer publishes the actual completion date of the construction project.

The milestone's `.dateMet` is set to the actual completion date, `.status` is set to 'met' and `.dateModified` is set to the date the milestone was updated.

Users can compare the milestone's `.dueDate` and `.dateMet` to determine whether the project was completed on time.

```{jsoninclude} ../../examples/milestones/delivery_milestones.json
:jsonpointer: /releases/1
:expand: tag, contracts, implementation, milestones
```

### Payment milestones

This example shows how payment milestones are modelled.

#### Implementation release

A buyer publishes the expected date and value of the payment for the completion of a construction project.

```{jsoninclude} ../../examples/milestones/payment_milestones.json
:jsonpointer: /releases/0
:expand: tag, contracts, implementation, milestones
```

#### Implementation update release

The buyer publishes the actual date and value of the payment for completion of the project.

The milestone is updated to reflect that the payment has been made: it's `.status` is set to `.met` and the `.dateMet` and `.dateModified` fields are populated. A transaction is added to `contracts.implementation.transactions` with the actual date and value of the payment. The [transaction-related milestones extension](https://extensions.open-contracting.org/en/extensions/transaction_milestones/master/) is used to link the transaction to the milestone.

Users can compare the milestone's `.dueDate` and `.value` to the transaction's `.date` and `.value` to determine whether the payment was made on time and for the expected amount.

```{jsoninclude} ../../examples/milestones/payment_milestones.json
:jsonpointer: /releases/1
:expand: tag, contracts, implementation, milestones, transactions
```
