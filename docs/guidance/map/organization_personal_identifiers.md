# Personal Identifiers

A procurement process has several parties involved, most of them are legal organizations. To identify them, OCDS recommends the use of a **legal identifier**. The data users should have information about about what this identifier is. The publisher should document the organization's identifier in [org-id.guide](http://org-id.guide/)

But sometimes, the party is not an organization, but a natural person, so it doesn't have a legal identifier. If the individual is a supplier and you have its personal identification you must declare it as it. OCDS recommends to follow the same approach used in the [BODS](http://standard.openownership.org/en/schema-beta-2/schema/guidance/identifiers.html?#shared-identifiers) standard:

> *"the scheme should have the pattern {JURISDICTION}-{TYPE} where JURISDICTION is an uppercase ISO 3166-1 alpha-3 country code and TYPE is one of PASSPORT, TAXID or IDCARD"*

You can follow this approach only if the laws in your jurisdiction allows the publication of personal information.

## Worked example

In the example below:

* Colombia needs to publish information about a tenderer that is a self-employed individual
* Colombia has the IDCARD for that tenderer. The laws there allow the publication of IDCARDs.
* The ISO 3166-1 alpha-3 country code for Colombia is *COL*
* Colombia publishes the IDCARD for the tenderer with `identifier.scheme` field set to `COL-IDCARD`.
* The `identifier.id` field is set to the IDCARD number.

```eval_rst

.. jsoninclude:: ../../examples/organization-personal-identifier.json
   :jsonpointer: 
   :expand: releases, parties, identifier
   :title: personal-identifiers

```

