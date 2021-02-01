# Purchase orders

Purchase orders that are made against contracts with a definite quantity or value of items ought to not be disclosed in the `contracts` section of OCDS, due to the risk of double counting items on the purchase order and the contract it relates to.

## Example: Double counting contracts and purchase orders

The UK's Department for Transport awards a £1.2m, 12-month contract to KPMG to provide the Project Management Office function for a project to construct a new highway bypass. The contract specifies that payment will be made quarterly in arrears in four equal amounts. The contract is represented in the `contracts` section of OCDS as follows:

```{eval-rst}
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../examples/purchase_orders/parent_contract.csv
```

Calculating the sum of the contract value in the above example gives the correct result of £1.2m.

The Department for Transport issues a purchase order on the final day of each quarter of the contract term, each for £300k.

If purchase orders were also disclosed in the `contracts` section of OCDS, by the end of the contract term, the `contracts` section of OCDS would be populated as follows:

```{eval-rst}
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../examples/purchase_orders/contracts_pos.csv
```

Calculating the sum of the contract value in the above example gives an incorrect result of £2.4m - double the actual value of the contract.

```{eval-rst}
.. admonition:: Note
    :class: note

    .. markdown::

      The approach for modelling purchase orders in OCDS is under discussion ([GitHub issue](https://github.com/open-contracting/standard/issues/897))

```
