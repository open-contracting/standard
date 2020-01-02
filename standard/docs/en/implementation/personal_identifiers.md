# Personal Identifiers

To identify the parties involved in a procurement process, OCDS strongly recommends the use of a **legal identifier** 
registered in [org-id.guide](http://org-id.guide/).

But if you dont have that information but your system collects information about personal identification of suppliers instead
and the laws in your jurisdiction allows you to publish it, OCDS recommends to follow the same approach used in the 
[BODS](http://standard.openownership.org/en/schema-beta-2/schema/guidance/identifiers.html?#shared-identifiers) standard
to identify them and setting the `identifier.scheme` field:

> the scheme should have the pattern {JURISDICTION}-{TYPE} where JURISDICTION is an ISO 3-digit country code and TYPE
> is one of PASSPORT, TAXID or IDCARD

## Worked example

In the example below:

* Colombia publishes the IDCARD for a tenderer, so the code `COL-IDCARD` is used as `identifier.scheme`.
* The IDCARD number is used as `identifier.id`


```eval_rst

.. jsoninclude:: ../examples/personal-identifier.json
   :jsonpointer: 
   :expand: releases, parties
   :title: personal-identifiers

```

