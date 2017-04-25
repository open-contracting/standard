Contract Suppliers
==================

## Meta-data

To use this extension, include it's URL in the ```extension``` array of your release or record package. 

```json
{
    "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_contract_suppliers_extension/master/extension.json"],
    "releases":[]
}
```

This extension is maintained at [https://github.com/open-contracting/ocds_contract_suppliers_extension](https://github.com/open-contracting/ocds_contract_suppliers_extension)

## Documentation

OCDS is designed around a contracting model in which:

* One or more awards are made naming the selected suppliers;
* One contract is signed for each award made, refering back to the related award;

For this reason, the core ```contract``` block does not include information on ```suppliers```. These can be located by looking at the related ```award``` using the ```awardID``` cross-reference.

However, there are some contracting processes in which a single award to multiple suppliers, results in multiple contracts, each to a single supplier. In these instances, it is important to specify suppliers at the contract level. 

The Contract suppliers extension introduces a ```contract/suppliers``` array for this purpose. 

## Schema

```eval_rst
.. extensiontable::
   :extension: contract_suppliers
```
