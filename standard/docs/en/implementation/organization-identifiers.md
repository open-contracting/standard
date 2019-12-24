# Organization identifiers

Publishers usually collect **legal identifiers** from the organizations that are part of the contracting process.
**Organization identifiers** are provided in OCDS by identifying the **organization lists** used in the source
data, choosing an appropiate **organization register prefix** for each list, and identifying the organizational
ID for each list and organization in the data.

It is strongly recommended to take an organization register prefix from [org-id.guide](http://org-id.guide), or to 
[propose a new entry](http://docs.org-id.guide/en/latest/contribute/#proposing-a-new-entry) for the 
organization register used if an appropiate entry does not exists. The instructions in the 
[Meta-data guide](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code) can be used to build a meaningful
organization register prefix.

## Worked example

An example publisher uses identifiers from the UK Companies House for suppliers, which has the GB-COH prefix in [org-id.guide](http://org-id.guide). 
AnyCorp Ltd. has been assigned the company number ‘1234567844’ by Companies House. 
The globally unique organization identifier for AnyCorp Ltd. can then be expressed in the `identifier` section in the sample
below:

```eval_rst
.. jsoninclude:: ../examples/organization-identifiers.json
    :jsonpointer: /releases/0/parties/1
    :expand: identifier
```

Note that it is possible to use more than one organization register, in which case any additional identifiers can be included
in the `additionalIdentifiers` section.

Publishers should consider if/when to include [local identifiers](../schema/identifiers#choosing-an-identifier).
Local identifiers may not be registered in [org-id.guide](http://org-id.guide), provided that the organization list is described in a
publication policies document.
