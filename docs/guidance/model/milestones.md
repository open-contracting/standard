# Milestones

Milestones can be included within the planning, tender, contract and contract implementation sections. 

* The planning milestones block is used for two types of milestones:
  * Key events in the planning stage, for example, the preparation of an environmental impact assessment, the approval to proceed with a project, or the date of a public consultation. 
 * Anticipated milestones during the contract implementation stage, for example, the date by which goods delivery of the goods is required.

* The tender milestones block is used to describe two types of milestone:
  * Key dates in the tender and award stages which are not covered by other fields, for example, the date by which procuring entity will respond to enquiries.
  * Anticipated milestones during the contract implementation stage, for example, the date by which goods need to be delivered.

* The contract milestones block is used for events related to the signing of the contract, for example, the date of commercial close in a PPP contract.

* The contract implementation milestones block is used for any events related to the delivery of the contract, for example, the agreed date by which goods will be delivered.

The nature of the milestone is indicated by the [milestone type codelist](../../../schema/codelists#milestone-type), for example, to distinguish between milestones in the planning section which relate to events in the pre-procurement phase and milestones in the planning section which relate to contract implementation.

The `dueDate`, `dateMet`, `dateModified` and [`status`](../../../schema/codelists/#milestone-status) fields are used to track the lifecycle of the milestone.

## Worked examples

The following worked examples show how to use milestones in different scenarios.

### Planning and tender milestones

The planning milestone block should be used only to disclose information about the planning process, such as the 
budget approval, key studies etc. If during the planning stage you have information about tender process milestones, then you
should populated the tender/milestones block instead.

The example below includes two OCDS releases:

* A planning release with details of a planned procurement, including the date the budget plan is expected to be ready and the date the tender notice is expected to be issued.
* A tender release with the actual date the tender notice was issued.

In the planning release:

* The date the budget plan is expected to be ready is represented using a milestone in `planning/milestones` with `.type` is set to 'preProcurement' because the milestone relates to the planning stage of the contracting process. `.dueDate` is set to the date and `.status` is set to 'scheduled'.
* The date the tender notice is expected to be issued is represented using a milestone in `tender/milestones` because it relates to the tender stage of the contracting process. `.dueDate` is set to the date and `.status` is set to scheduled.

In the tender release:

* The `.dateMet` field in the tender notice milestone is updated with the actual date the notice was issued and `.status` is set to 'met'.
To explore differences between the planned and actual date of the tender milestone, users can then compare the values of `tender/milestones/dueDate` and `tender/milestones/dateMet` in a single (compiled) release.

```eval_rst

.. jsoninclude:: ../../examples/milestones/planning-tender-milestones.json
   :jsonpointer: 
   :expand: releases, planning, milestones, tender, milestones
   :title: planning

.. jsoninclude:: ../../examples/milestones/planning-tender-milestones-2.json
   :jsonpointer: 
   :expand: releases, planning, milestones, tender, milestones
   :title: tender

```

### Contract implementation milestones

#### 1. Project data

This worked example shows how to use milestones to model the planned and actual start and finish dates for a construction project.

The example below includes 3 OCDS releases from a contracting process for the construction of a cycle lane:

* An award release which includes the scheduled start and end dates for the project.
* An implementation update release with the actual start date of the project
* An implementation update release with the actual end date of the project

In the award release:

* The scheduled start and end dates for the project are represented using milestones in `contracts/implementation/milestones` with `.type` set to 'delivery' because they related to the delivery of the contract. The dates are provided in `.dueDate` and `.status` is set to 'scheduled'.
* The publisher has defined their own values for the `.code` field so they can filter and compare start and end date milestones across different contracts.

The first implementation update is published after the project starts but before it completes:

* In the project commencement milestone, `.dateMet` is set to the actual start date and `.status` is set to 'met'. `.dateModified` is set to the date the milestone was updated.
* In the project completion milestone, `.status` is set to 'notMet' since the project is not yet complete and `.dateModified` is set to the date the milestone was updated.

Users can compare the project commencement milestone's `.dueDate` and `.dateMet` fields to determine if the project started on time. Users can also compare the project completion milestone's `.dueDate` and `.dateModified` fields to determine whether the `.status` has been updated since the scheduled completion date.

The second implementation update is published after the project completes:

* In the project completion milestone, `.dateMet` is set to the actual completion date for the project and `.status` is set to 'met'.

```eval_rst

.. jsoninclude:: ../../examples/milestones/implementation-milestones-1.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation

```

```eval_rst

.. jsoninclude:: ../../examples/milestones/implementation-milestones-2.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation-update-1

```

```eval_rst

.. jsoninclude:: ../../examples/milestones/implementation-milestones-3.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation-update-2

```

#### 2. Delivery and financing data

This example shows how milestones can be used to keep track of delivery and financing (payment) data in a contracting process.

The procuring entity in the example, the Ministry of Border and Tribal Affairs,
is managing the procurement for the mantainance of a high school building.
Milestones have been set for the delivery and payment of goods and services
related to the project. In the first release shown below, contract information
is released along its implementation milestones.

Once the first milestone has been reached ("Finish the exterior and interior walls"), a new release is created with  the related milestone `status` set to 'met' and the relevant dates added to the `dateMet` and `dateModified` fields.

In a second update, the construction company has received payment for the work done so far, and the milestone for the wall restoration with type 'financing' is updated in a new release. 
A new `transaction` is also disclosed, with the amount paid to the company.

```eval_rst

.. jsoninclude:: ../../examples/milestones/af-implementation-milestones-1.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation

```

```eval_rst

.. jsoninclude:: ../../examples/milestones/af-implementation-milestones-2.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation-update-1

```

```eval_rst

.. jsoninclude:: ../../examples/milestones/af-implementation-milestones-3.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones, transactions
   :title: implementation-update-2

```

Notes:

* Contract implementation milestones should be kept updated as things progress with the relevant date added to the `dateModified` field.
* At the point of contract signature, a comparison between `tender/milestones` and `contract/implementation/milestones` 
with a `milestone/type` of 'delivery' or 'reporting' should reveal how the negotiated contract differs from what was set out at tender time.
