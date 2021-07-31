# Buyers and suppliers

## Definitions

In order to understand the modelling examples, it’s important to first clarify the definitions of some key concepts.

### Buyer

OCDS defines the buyer as:

```{field-description} ../../../build/current_lang/release-schema.json /properties/buyer
```

```{note}
Elsewhere in the OCDS schema the buyer is described as:

> *The entity managing the procurement. This may be different from the buyer who pays for, **or uses**, the items being procured.*

There is a proposal to align this description with the above definition.
```

In OCDS, the **buyer** is modelled as relating to the contracting process as a whole and each contracting process has only a single `buyer` field, i.e. all awards and contracts resulting from the contracting process share the same buyer.

That said, many organizations can be assigned the 'buyer' role in the `parties` section, making it possible to represent contracting processes with a 'lead' buyer and other buyers.

### Suppliers

OCDS defines a supplier as:

```{code-description} ../../../build/current_lang/codelists/partyRole.csv supplier
```

**Suppliers** are modelled as relating to awards in OCDS and there can be multiple suppliers per award, i.e. all contracts relating to the same award share the same suppliers.

## Consortia suppliers

When multiple suppliers put together a single bid, and are awarded as a group, this is known as a consortium.

In some countries, these suppliers only create a legal entity after the award, to sign the contract; or, they decide on a prime contractor, with the others being subcontractors.

In such cases, the `Award` object in OCDS can have multiple suppliers associated with it, one for each member of the consortium.

### Example: Consortia suppliers

Siemens and Microsoft bid as a consortium for a contract to develop a new medical imaging device for the Department of Health and Social Care.

The contract is awarded to the consortium; however, the legal entity for the consortium is not created until after the contract award.

Both Siemens and Microsoft are listed as suppliers on the contract award in OCDS, with the respective legal entity identifiers for each organization:

```{csv-table-no-translate}
:header-rows: 1
:widths: auto
:file: ../../examples/consortia_simple.csv
```
