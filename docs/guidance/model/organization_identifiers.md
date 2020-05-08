# Organization identifiers

Normally, publishers collect *legal identifiers* from the organizations that are part of the contracting process.  [Organization identifiers](../../schema/identifiers/#organization-ids) can be provided in OCDS by identifying the **organization registers or lists** used in the source data, choosing an appropiate **organization register prefix** for each one, and identifying the organizational ID for each registry or list and organization in the data.

It is strongly recommended to use an organization register prefix from [org-id.guide](http://org-id.guide), or to [propose a new entry](http://docs.org-id.guide/en/latest/contribute/#proposing-a-new-entry) for the organization register used if an appropiate entry does not exists. The instructions in the [org-id meta-data guide](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code) can be used to build a meaningful organization register prefix.

Publishers should consider if/when to include [local lists](../../schema/identifiers/#choosing-an-identifier).  Local lists may not be registered in [org-id.guide](http://org-id.guide), provided that the organization list is described in a [publication policy document](../publication_policy/).

## Worked example

The Government of UK uses identifiers from the UK Companies House to uniquely identify suppliers. The UK Companies House has an entry in [org-id.guide](http://org-id.guide/list/GB-COH), which specifies the "GB-COH" code for the registry. IBM has been assigned the company number ‘04336774’ by the Companies House.  The globally unique organization identifier for IBM can then be expressed as in the `identifier` section in the sample below:

```eval_rst
.. jsoninclude:: ../examples/organization-identifiers.json
    :jsonpointer: /releases/0/parties/1
    :expand: identifier, additionalIdentifiers
```

The publisher also collects two extra identifiers, which are disclosed in the `additionalIdentifiers` block. The first one is the VAT identification number for suppliers. Note that the VAT registry is not present in [org-id.guide](http://org-id.guide/), but the publisher followed the instructions in the [org-id meta-data guide](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code) to build the "GB-VAT" code used in the `scheme` field: the two-letter country prefix ("GB") plus a short abbreviation for the registry ("VAT").

The last identifier in the `additionalIdentifiers` array belongs to an internal supplier list used in Contracts Finder, the platform used in England to publish opportunities and contract information. The publisher built the "X-GB-CF" code for the list, and the "X-" prefix indicates that the code represents a local list.