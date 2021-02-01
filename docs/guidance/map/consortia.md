# Consortia suppliers

When multiple suppliers put together a single bid, and are awarded as a group, this is known as a consortium.

In some countries, these suppliers only create a legal entity after the award, to sign the contract; or, they decide on a prime contractor, with the others being subcontractors.

In such cases, the `Award` object in OCDS can have multiple suppliers associated with it, one for each member of the consortium.

## Example: Consortia suppliers

Siemens and Microsoft bid as a consortium for a contract to develop a new medical imaging device for the Department of Health and Social Care.

The contract is awarded to the consortium; however, the legal entity for the consortium is not created until after the contract award.

Both Siemens and Microsoft are listed as suppliers on the contract award in OCDS, with the respective legal entity identifiers for each organization:

```{eval-rst}
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../examples/consortia_simple.csv
```
