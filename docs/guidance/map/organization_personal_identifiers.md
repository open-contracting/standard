# Personal Identifiers

Suppliers and tenderers can be organizations or individuals (natural persons). Such individuals are often referred to as "sole traders" or "self-employed individuals".

Details of natural persons can be disclosed using the `parties` section in OCDS only if:

* The natural person is a tenderer or supplier; and
* The laws in your jurisdiction permit the publication of such details

Subject to the above, you can disclose identifiers for natural persons using the `Identifier` building block.

There are two components to an identifier in OCDS:

* a code indicating the list or register from which the identifier is drawn (the `scheme`); and
* the identifier itself (the `id`).

Follow the [guidance](http://standard.openownership.org/en/0.2.0/schema/guidance/identifiers.html#shared-identifiers) from the Beneficial Ownership Data Standard to construct a `scheme` value for the personal identifier:

> the scheme should have the pattern {JURISDICTION}-{TYPE} where JURISDICTION is an uppercase ISO 3166-1 alpha-3 country code and TYPE is one of PASSPORT, TAXID or IDCARD

## Worked example

In the example below:

* A self-employed individual submits a bid for a tender in Colombia
* The individual is listed in the `parties` section with 'tenderer' in `.roles`
* The individual's ID card number is published in `.identifier.id`
* `.identifier.scheme` is constructed from the ISO 3166-1 alpha-3 country code for Colombia ('COL') and the type of the identifier ('IDCARD')


```{eval-rst}
.. jsoninclude:: ../../examples/organization-personal-identifier.json
   :jsonpointer:
   :expand: releases, parties, identifier
   :title: personal-identifiers
```
