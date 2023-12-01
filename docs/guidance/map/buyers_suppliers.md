```{workedexample} Buyers and suppliers
:tags: parties,tender,award
```

# Buyers and suppliers

## Definitions

In order to understand the modelling examples, it’s important to first clarify the definitions of some key concepts.

### Buyer

OCDS defines the buyer as:

```{field-description} ../../../build/current_lang/release-schema.json /properties/buyer
```

In OCDS, the **buyer** is modelled as relating to the contracting (or planning) process as a whole and each process has only a single `buyer` field, i.e. all awards and contracts resulting from the contracting process share the same buyer.

That said, many organizations can be assigned the 'buyer' role in the `parties` section, making it possible to represent contracting (or planning) processes with a 'lead' buyer and other buyers.

### Suppliers

OCDS defines a supplier as:

```{code-description} ../../../build/current_lang/codelists/partyRole.csv supplier
```

**Suppliers** are modelled as relating to awards in OCDS and there can be multiple suppliers per award, i.e. all contracts relating to the same award share the same suppliers.

## Consortia suppliers

When multiple potential suppliers put together a single bid, and are awarded as a group, this is known as a consortium.

In some countries, these suppliers only create a legal entity after the award, to sign the contract; or, they decide on a prime contractor, with the others being subcontractors.

In such cases, the `Award` object in OCDS can have multiple suppliers associated with it, one for each member of the consortium.

### Example: Consortia suppliers

Siemens and Microsoft bid as a consortium for a contract to develop a new medical imaging device for the Department of Health and Social Care.

The contract is awarded to the consortium; however, the legal entity for the consortium is not created until after the contract award.

Both Siemens and Microsoft are listed as suppliers on the contract award in OCDS, with `id`s constructed according to [`Organization.id`](../../schema/reference.md#release-schema.json,/definitions/Organization,id).

```json
{
  "awards": [
    {
      "id": "DHSC-2019-A18074",
      "title": "Medical imaging device development",
      "suppliers": [
        {
          "name": "SIEMENS PUBLIC LIMITED COMPANY",
          "id": "GB-COH-727817"
        },
        {
          "name": "MICROSOFT LIMITED",
          "id":"GB-COH-1624297"
        }
      ]
    }
  ]
}
```
