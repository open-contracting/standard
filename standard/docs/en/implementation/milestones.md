# Milestones

Milestones can be included within the planning, tender, contract and contract implementation blocks. 

* The planning milestone block may describe anticipated milestones during the planning stage, such as the preparation 
of key studies. Usually using the 'preProcurement' milestone type code.

* The tender milestone block should be used to describe anticipated milestones during the proposed delivery 
of a contract, as well as key dates from the process of tendering and awarding the contract.

* The contract milestone block should be used for events related to the signing of the contract documents.

* The contract implementation milestones block should be used for any event related to delivery of the contract.

The nature of the milestone is indicated by the milestone type code list.

The lifecycle of the milestone should be modeled with the fields: `dueDate`, `dateMet`, `dateModified` and `status`.

## Worked example

In the example below:

* A contract is awarded to a user committee with milestones for project commencement and project completion.
* The project starts later than expected. The project commencement milestone is updated with actual start date and the project completion milestone is set to `notMet`.
* The project is completed earlier than expected. The project completion milestone is updated with the actual completion date.

```eval_rst

.. jsoninclude:: ../examples/implementation-milestones-1.json
   :jsonpointer: 
   :expand: contracts, implementation, milestones
   :title: milestones-1

```

```eval_rst

.. jsoninclude:: ../examples/implementation-milestones-2.json
   :jsonpointer: 
   :expand: contracts, implementation, milestones
   :title: milestones-2

```

```eval_rst

.. jsoninclude:: ../examples/implementation-milestones-3.json
   :jsonpointer: 
   :expand: contracts, implementation, milestones
   :title: milestones-3

```
