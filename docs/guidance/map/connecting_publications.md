```{workedexample} Connecting releases from different publications
:tags: release
```

# Connecting releases from different publications

Different OCDS publications can contain releases describing the same contracting process. In OCDS, each contracting or planning process is assigned a globally unique identifier, the ocid. Ideally, releases describing the same contracting or planning process in different publications would reuse the same ocid so that users can merge releases.

This page explains the problems that can occur when reusing ocids across publications, describes how to connect releases from different publications without reusing ocids, and describes the scenarios in which it is possible to reuse ocids across different publications.

The examples on this page are based on Scotland's Public Contracts Scotland (PCS) publication and the UK's Find a Tender Service (FTS) publication, both of which include releases about the same contracting processes, covering the same stages of the contracting processes and with many fields in common.

## Problems with reusing ocids across publications

Unless publications have disjoint fields or use consistent mappings, reusing the same OCIDs across publications can result in unpredictable and nonsensical results when releases are merged to create a compiled release. For example, unless publications use an identical approach to assigning local identifiers to objects in arrays, then awards, contracts and other objects in arrays will overwrite and/or duplicate each other in nonsensical ways.

### Example: Reusing ocids across Public Contracts Scotland and Find a Tender Service

The PCS and FTS have many overlapping fields, but implement slightly different OCDS mappings. Therefore, if FTS were to reuse the ocids minted by PCS, merging the releases to create a compiled release would result in nonsensical data

For example, the `.id` of the buyer in the `.parties` array is inconsistent between the publications so a merged release would result in duplicate buyers:

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

## How to connect releases from different publications without reusing ocids

If publications have overlapping fields and/or inconsistent mappings, then you ought to use the `links` field to connect releases from different publications. If, like FTS, a publication includes releases that represent the same notices as another publication, the derivative publication should use the 'canonical' links relation type to refer to releases in the canonical publication. If a publication includes releases that relate to later stages of the contracting process, but cannot reuse ocids, then the publication ought to use the 'prev' link relation type to refer to the previous releases in a different publication.

Building on the PCS and FTS example, PCS is the canonical publication because procurement officials enter procurement notice data into PCS, which publishes OCDS releases. For contracting processes over a threshold value, PCS sends the notice data to FTS, which also publishes OCDS releases. Therefore, the FTS publication mints a new ocid using its own ocid prefix and links back to the release from PCS using the 'canonical' link relation type:

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

### When to reuse ocids across publications

There are two scenarios in which reusing ocids across publications is encouraged: publications with distinct coverage of OCDS fields and  publications with consistent OCDS mappings.

### Publications with distinct coverage

If two publications cover disjoint sets of OCDS fields, with the exception of the release-level required fields (`ocid`, `id`, `date` and `tag`),then they ought to use the same ocid so that users can merge releases.

Building on the PCS and FTS example above, if PCS were to publish only the `parties` array and `tender` object and FTS were to publish only the `awards` array, then it would be possible for FTS to reuse the ocids minted by PCS:

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

However, this scenario is unlikely to occur since a publication that includes the `awards` array ought to also include details of the suppliers in the `parties` array. In which case, in order to avoid the risk of clashing identifiers, the publications would need to coordinate their approaches to assigning local identifiers to objects in the `parties` array.

### Publications with consistent OCDS mappings

If two publications use consistent OCDS mappings, in particular the approach to assigning local identifiers to objects in arrays, then they ought to use the same ocid so that users can merge releases.

Building on the PCS and FTS example above, if both publications used a consistent OCDS mapping, not only could FTS add an organization object that represents the supplier to the `parties` array without the risk of clashing identifiers, but it could add fields like `.contactPoint` to the organization object published by PCS that represents the buyer:

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
