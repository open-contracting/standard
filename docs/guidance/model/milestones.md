# Milestones

Milestones can be included within the planning, tender, contract and contract implementation sections. 

* The planning milestone block may describe anticipated milestones during the planning stage, such as the preparation 
of key studies. Usually using the 'preProcurement' milestone type code.

* The tender milestone block should be used to describe anticipated milestones during the proposed delivery 
of a contract, as well as key dates from the process of tendering and awarding the contract.

* The contract milestone block should be used for events related to the signing of the contract documents.

* The contract implementation milestone block should be used for any event related to delivery of the contract.

The nature of the milestone is indicated by the [milestone type codelist](../../../schema/codelists#milestone-type).

The lifecycle of the milestone should be modeled with the fields: `dueDate`, `dateMet`, `dateModified` and [status](../../../schema/codelists/#milestone-status).

## Worked examples

The following worked examples will show how to fill the milestone block depending on its nature.

### Planning and tender milestones

The planning milestone block should be used only to disclose information about the planning process, such as the 
budget approval, key studies etc. If during the planning stage you have information about tender process milestones, then you
should populated the tender/milestones block instead.

In the example below:

* The process starts at the planning stage, and the information about when the budget plan is estimated to be ready 
is available. We create a planning release including a `preProcurement` milestone type with the estimated date set 
in the `dueDate` field and `scheduled` status. The publisher also knows when the tender notice is estimated to take place. 
This information is part of the **tender** process. A `preProcurement` milestone type with a `dueDate` is created 
at the `tender/milestones` block. The tender must have the `planned` status.
* The process goes forward and enters the tender stage. We publish a tender release 
with `tender/status` = `active`, the actual dates for milestones in `tender/milestones/dateMet` and `met` status.


```eval_rst

.. jsoninclude:: ../../examples/planning-tender-milestones.json
   :jsonpointer: 
   :expand: releases, planning, milestones, tender, milestones
   :title: planning

.. jsoninclude:: ../../examples/planning-tender-milestones-2.json
   :jsonpointer: 
   :expand: releases, planning, milestones, tender, milestones
   :title: tender

```

### Contract implementation milestones

#### 1. Project data

This worked example shows how milestones for project commencement and project completion should be updated in OCDS.

The example includes three updates to a single contracting process (ocds-213czf-000-00001):

* A contract is awarded to a user committee with milestones for project commencement and project completion.
* The project starts later than expected. The project commencement milestone is updated with the actual start date and the project completion milestone `status` is set to `notMet`.
* The project is completed earlier than expected. The project completion milestone is updated with the actual completion date.

The OCDS releases for each update are shown below. 

```eval_rst

.. jsoninclude:: ../../examples/implementation-milestones-1.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation

```

```eval_rst

.. jsoninclude:: ../../examples/implementation-milestones-2.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation-update-1

```

```eval_rst

.. jsoninclude:: ../../examples/implementation-milestones-3.json
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

Once the first milestone has been reached ("Finish the exterior and interior walls"), a new release is created with the related
milestone marked as "met" in the scheduled date.

In a second update, the construction company has received payment for the work done so far, and the milestone related to the
payment for the walls restoration is updated in a new release. A new transaction is also disclosed, with the amount paid to the 
company.

```eval_rst

.. jsoninclude:: ../../examples/af-implementation-milestones-1.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation

```

```eval_rst

.. jsoninclude:: ../../examples/af-implementation-milestones-2.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones
   :title: implementation-update-1

```

```eval_rst

.. jsoninclude:: ../../examples/af-implementation-milestones-3.json
   :jsonpointer: 
   :expand: releases, contracts, implementation, milestones, transactions
   :title: implementation-update-2

```

Notes:

* Contract implementation milestones should be kept updated as things progress.
* At the point of contract signature, a comparison between `tender/milestones` and `contract/implementation/milestones` 
with a `milestone/type` of `delivery` or `reporting` should reveal how the negotiated contract differs from what was set out at tender time.
