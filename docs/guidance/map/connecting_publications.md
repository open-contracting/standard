```{workedexample} Connecting releases from different publications
:tags: release
```

# Connecting releases from different publications

Different OCDS publications can contain releases describing the same contracting (or planning) process. In OCDS, each contracting or planning process is assigned a globally unique identifier, the [OCID](../../schema/identifiers.md#open-contracting-process-identifier-ocid). Ideally, releases describing the same contracting or planning process in different publications would reuse the same OCID so that users can [merge releases](../../schema/merging.md).

This page describes the problems that can occur when reusing OCIDs across publications, how to connect releases from different publications without reusing OCIDs, and how to reuse OCIDs across publications.

The examples on this page are based on Scotland's Public Contracts Scotland (PCS) publication and the UK's Find a Tender Service (FTS) publication, both of which include releases about the same contracting (or planning) processes, covering the same contracting (or planning) process stages and having many fields in common.

## Problems with reusing OCIDs across publications

Unless publications have disjoint coverage of OCDS fields or implement consistent mappings, reusing the OCIDs across publications can result in unpredictable and nonsensical results when releases are merged to create a compiled release. For example, unless publications use an identical approach to assigning [local identifiers](../../schema/identifiers.md#local-identifiers) to objects in arrays, then awards, contracts and other objects in arrays can overwrite and/or duplicate each other in nonsensical ways.

### Example: Reusing OCIDs across Public Contracts Scotland and Find a Tender Service

The PCS and FTS publications have many overlapping fields, but implement slightly different mappings. Therefore, if FTS were to reuse the OCIDs assigned by PCS, merging releases would result in nonsensical data

For example, the publications implement inconsistent mappings for the `.id` of the buyer in the `.parties` array so merging releases would result in duplicate buyers:

`````{tab-set}
````{tab-item}  PCS release
```json
{
  "id": "rls-1-JAN468109",
  "ocid": "ocds-r6ebe6-0000710562",
  "date": "2023-01-09T00:00:00Z",
  "tag": [
    "planning"
  ],
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ]
}
```
````
````{tab-item}  FTS release
```json
{
  "id": "000521-2023",
  "ocid": "ocds-r6ebe6-0000710562",
  "date": "2023-01-09T12:26:29Z",
  "tag": [
    "planning"
  ],  
  "parties": [
    {
      "id": "GB-FTS-2273",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ]
}
```
````
````{tab-item}  Compiled release
```json
{
  "ocid": "ocds-r6ebe6-0000710562",
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    },
    {
      "id": "GB-FTS-2273",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ]
}
```
````
`````

## How to connect releases from different publications without reusing OCIDs

If publications have overlapping fields and inconsistent mappings, then you ought to use [links](../../schema/reference.md#link) to connect releases across the publications. If, like FTS, a publication's releases are derived from another publication's data, the derivative publication ought to use the 'canonical' [link relation type](../../schema/codelists.md#link-relation-type) to refer to the releases in the authoritative publication. If a publication's releases follow another publication's releases, the subsequent publication ought to use the 'prev' link relation type to refer to the earlier releases.

Building on the PCS and FTS example, the publishers agreed that PCS is the canonical publication. Therefore, when re-publishing releases from PCS, FTS mints a new OCID using its own [OCID prefix](../../schema/identifiers.md#registered-prefixes) and links back to the PCS release using the 'canonical' link relation type:

`````{tab-set}
````{tab-item}  PCS release
```json
{
  "id": "rls-1-JAN468109",
  "ocid": "ocds-r6ebe6-0000710562",
  "date": "2023-01-09T00:00:00Z",
  "tag": [
    "planning"
  ],
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ]
}
```
````
````{tab-item}  FTS release
```json
{
  "id": "000521-2023",
  "ocid": "ocds-h6vhtk-0395de",
  "date": "2023-01-09T12:26:29Z",
  "tag": [
    "planning"
  ],  
  "parties": [
    {
      "id": "GB-FTS-2273",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ],
  "links": [
    {
      "href": "https://api.publiccontractsscotland.gov.uk/v1/Notice?id=ocds-r6ebe6-0000710562",
      "rel": "canonical"
    }
  ]
}
```
````
`````

## How to reuse OCIDs across publications

There are two scenarios in which reusing OCIDs across publications might be possible: publications with distinct coverage of OCDS fields and publications that implement consistent OCDS mappings.

### Publications with distinct coverage

```{note}
This scenario is unlikely to occur since most publications are likely to include some common fields, for example, the `parties` array. In which case, in order to avoid the risk of clashing identifiers, publishers would need to implement consistent OCDS mappings. For more information, see [publications with consistent OCDS mappings](#publications-with-consistent-ocds-mappings).
```

If two publications cover disjoint sets of OCDS fields, with the exception of the release-level required fields (`ocid`, `id`, `date` and `tag`), then the publications can reuse OCIDs so that users can merge releases.

Building on the PCS and FTS example above, if PCS were to publish only the `parties` array and `tender` object and FTS were to publish only the `awards` array, then it would be possible for FTS to reuse the OCIDs assigned by PCS:

`````{tab-set}
````{tab-item}  PCS release
```json
{
  "id": "rls-1-JAN468109",
  "ocid": "ocds-r6ebe6-0000710562",
  "date": "2023-01-09T00:00:00Z",
  "tag": [
    "tender"
  ],
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ], 
  "tender": {
    "title": "New build housing and land acquisition (Fife Wide)",
    "mainProcurementCategory": "works",
    "value": {
      "amount": 100000000,
      "currency": "GBP"
    }
  }
}
```
````
````{tab-item}  FTS release
```json
{
  "id": "000521-2023",
  "ocid": "ocds-r6ebe6-0000710562",
  "date": "2023-01-09T12:26:29Z",
  "tag": [
    "award"
  ],  
  "awards": [
    {
      "id": "1",
      "title": "New build housing and land acquisition (Fife Wide)",
      "value": {
        "amount": 75000000,
        "currency": "GBP"
      }
    }
  ]
}
```
````
````{tab-item}  Compiled release
```json
{
  "ocid": "ocds-r6ebe6-0000710562",
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ],
  "tender": {
    "title": "New build housing and land acquisition (Fife Wide)",
    "mainProcurementCategory": "works",
    "value": {
      "amount": 100000000,
      "currency": "GBP"
    }
  },
  "awards": [
    {
      "id": "1",
      "title": "New build housing and land acquisition (Fife Wide)",
      "value": {
        "amount": 75000000,
        "currency": "GBP"
      }
    }
  ]
}
```
````
`````

### Publications with consistent OCDS mappings

If two publications implement consistent OCDS mappings, in particular the approach to assigning local identifiers to objects in arrays, then the publications can reuse OCIDs so that users can merge releases.

As in the distinct coverage example, the publishers would need to agree on and implement the governance and technical aspects of minting and sharing OCIDs. They would also need to:

* agree on a single deterministic mapping of shared fields;
* consistently implement the mappings;
* agree on how the systems will be integrated. For example: whether a given system's data takes precedence over another's, the order of precedence, the direction in which the data flows, etc; and
* implement the agreed integrations.

Given these governance and technical challenges, this scenario is unlikely to occur.

Building on the PCS and FTS example above, if both publications implemented consistent OCDS mappings, FTS could publish an organization object that represents the supplier in the `parties` array without the risk of clashing identifiers. FTS could also add fields like `.contactPoint` to the buyer organization object published by PCS:

`````{tab-set}
````{tab-item}  PCS release
```json
{
  "id": "rls-1-JAN468109",
  "ocid": "ocds-r6ebe6-0000710562",
  "date": "2023-01-09T00:00:00Z",
  "tag": [
    "tender"
  ],
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ]
    }
  ], 
  "tender": {
    "title": "New build housing and land acquisition (Fife Wide)",
    "mainProcurementCategory": "works",
    "value": {
      "amount": 100000000,
      "currency": "GBP"
    }
  }
}
```
````
````{tab-item}  FTS release
```json
{
  "id": "000521-2023",
  "ocid": "ocds-r6ebe6-0000710562",
  "date": "2023-01-09T12:26:29Z",
  "tag": [
    "award"
  ],  
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ],
      "contactPoint": {
        "email": "dawn.watson@fife.gov.uk",
        "name": "Dawn Watson",
        "telephone": "+44 3451550000"
      }
    },
    {
      "id": "org-2",
      "name": "Skanska AB",
      "roles": [
        "supplier"
      ]
    }   
  ],
  "awards": [
    {
      "id": "1",
      "title": "New build housing and land acquisition (Fife Wide)",
      "value": {
        "amount": 75000000,
        "currency": "GBP"
      },
      "suppliers": [
        {
          "id": "org-2",
          "name": "Skanska AB"
        } 
      ]
    }
  ]
}
```
````
````{tab-item}  Compiled release
```json
{
  "ocid": "ocds-r6ebe6-0000710562",
  "parties": [
    {
      "id": "org-1",
      "identifier": {
        "legalName": "Fife Council"
      },
      "name": "Fife Council",
      "roles": [
        "buyer"
      ],
      "contactPoint": {
        "email": "dawn.watson@fife.gov.uk",
        "name": "Dawn Watson",
        "telephone": "+44 3451550000"
      }
    },
    {
      "id": "org-2",
      "name": "Skanska AB",
      "roles": [
        "supplier"
      ]
    }   
  ],
  "tender": {
    "title": "New build housing and land acquisition (Fife Wide)",
    "mainProcurementCategory": "works",
    "value": {
      "amount": 100000000,
      "currency": "GBP"
    }
  },
  "awards": [
    {
      "id": "1",
      "title": "New build housing and land acquisition (Fife Wide)",
      "value": {
        "amount": 75000000,
        "currency": "GBP"
      },
      "suppliers": [
        {
          "id": "org-2",
          "name": "Skanska AB"
        } 
      ]
    }
  ]
}
```
````
`````
