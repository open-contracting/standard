# Personal Identifiers

To identify the parties involved in a procurement process, OCDS strongly recommends the use of a **legal identifier** 
registered in [org-id.guide](http://org-id.guide/).

But if you don't have that information but your system collects information about personal identification of suppliers 
instead, OCDS recommends to follow the same approach used in the 
[BODS](http://standard.openownership.org/en/schema-beta-2/schema/guidance/identifiers.html?#shared-identifiers) standard:

> *"the scheme should have the pattern {JURISDICTION}-{TYPE} where JURISDICTION is an ISO 3-digit country code and TYPE
> is one of PASSPORT, TAXID or IDCARD"*

This approach can be follow only if the laws in your jurisdiction allows you to publish this kind of personal information
and no other identification is available.

## Worked example

In the example below:

* Colombia needs to publish information about a tenderer that doesn't have a legal identifier
* Colombia has the IDCARD for that tenderer and the laws there allows the publication of IDCARDS. 
* The ISO 3-digit country code for Colombia is *COL*
* Colombia then publishes the IDCARD for the tenderer with the code `COL-IDCARD` used as `identifier.scheme`.
* The IDCARD number is used as `identifier.id`


```eval_rst

.. jsoninclude:: ../examples/personal-identifier.json
   :jsonpointer: 
   :expand: releases, parties, identifier
   :title: personal-identifiers

```

