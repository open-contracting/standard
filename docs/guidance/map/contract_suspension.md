# Contract suspension

A contract can be suspended after it is signed. A suspended contract is still legally in force, but work has been suspended. For example, a contract might be suspended in the following scenarios:

* the buyer suspends a contract because the supplier fails to perform.
* the supplier suspends a contract because the buyer fails to pay.
* either party suspends a contract due to force majeure.

In OCDS, the `contracts.status` field describes the status of a contract, using codes from the [contract status codelist](https://standard.open-contracting.org/latest/en/schema/codelists/#contract-status). The `contracts.statusDetails` field can be used to provide additional details on the status of a contract.

To disclose that a contract is suspended, set the contract's `.status` to 'active' and use its `.statusDetails` field to record that the contract is suspended.

If you collect other details about contract suspension, such as the rationale for the suspension or the period of the suspension, you can publish the details in an unstructured way in the `.statusDetails` field.

```{note}
If you want to publish structured data about contract suspension, you can contribute to the [Github issue](https://github.com/open-contracting/standard/issues/758) on suspended contracts.
```

## Example: Suspended contracts in Afghanistan

In the following example, a contract in the [Afghanistan Government Electronic and Open Procurement System](https://ageops.net) is suspended.

```{jsoninclude} ../../examples/suspendedcontract.json
:jsonpointer:
:expand: releases, contracts
:title: Suspended Contract
```
