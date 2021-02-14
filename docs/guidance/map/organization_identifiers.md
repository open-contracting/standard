# Organization identifiers

Normally, publishers collect *legal identifiers* from the organizations that are part of the contracting process. [Organization identifiers](../../../schema/identifiers/#organization-ids) can be provided in OCDS by identifying the **organization registers** used in the source data, choosing an appropiate **organization register prefix** for each one, and identifying the organizational ID for each registry or list and organization in the data.

Use [org-id.guide](http://org-id.guide/) to find the code for the register your identifiers are drawn from. If no code exists for the register, contact the [OCDS Helpdesk](../../support/index) to register an organization list.

If a publisher chooses not to register an organization list with org-id.guide, the publisher ought to describe the organization list in a [publication policy](../../publish/#finalize-your-publication-policy), and needs to ensure that its prefix doesn't collide with a list code in org-id.guide.

## Worked example

The Government of UK uses identifiers from the UK Companies House to uniquely identify suppliers. The UK Companies House has an entry in [org-id.guide](http://org-id.guide/list/GB-COH), which specifies the "GB-COH" code for the registry. IBM has been assigned the company number ‘04336774’ by the Companies House.  The globally unique organization identifier for IBM can then be expressed as in the `identifier` section in the sample below:

```{eval-rst}
.. jsoninclude:: ../../examples/organization-identifiers.json
    :jsonpointer: /releases/0/parties/1
    :expand: identifier, additionalIdentifiers
```

The publisher also collects two extra identifiers, which are disclosed in the `additionalIdentifiers` block. The first one is the VAT identification number for suppliers. Note that the VAT registry is not present in org-id.guide, but the publisher followed the instructions in the [org-id meta-data guide](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code) to build the "GB-VAT" code used in the `scheme` field: the two-letter country prefix ("GB") plus a short abbreviation for the registry ("VAT"). The publisher checked that it does not conflict with any list code in org-id.guide.
