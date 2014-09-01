## Merging

To turn releases into a record, they must be merged into a single record.

The basic format of a record is simple. There are three component:

- A list of all the releases in the record. This can be with linked data to
  identify the release, or embedding the release themselves.
- A compiled release, this is the same format as a release but contains the
  most up-to-date information compiled from all the releases.
- A versioned release, this contains the information about the compiled field.
  For each field in the release, the versioned release contains a list of objects
  describing where the data came from and previous values of a field.

The basic principle of of merging is very simple, the latest data overrides
previous data.  For example:

<code>
release_1 = {
    "releaseDate": "2014-01-01",
    "releaseID": "1",
    "releaseTag": "tenderNotice",
    "ocid": "A",
    "formation": {
        "tenderId": "A",
        "method": "Selective"
    } 
}
release_2 = {
    "releaseDate": "2014-01-02",
    "releaseID": "2",
    "releaseTag": "tenderNotice",
    "ocid": "A",
    "formation": {
        "tenderId": "A",
        "method": "Open"
    } 
}
record = {
    // Other required fields omitted for clarity
    "compiledRelease": {
        "ocid": "A",
        "releaseID": "2",   // Has no meaning, but kept for validation
        "releaseDate": "2014-01-02",    // Has no meaning but kept for validation
        "releaseTag": "compiled",
        "formation": {
            "tenderId": "A",
            "method": "Open"
        } 
    },
    "versionedRelease": {
        "ocid": "A",
        "formation": {
            "tenderId": "A",
            "totalValue": [
                {
                    "valueFromRelease": "Selective",
                    "date": "2014-01-01",
                    "releaseTag": "tenderNotice",
                    "releaseID": "1"
                },
                {
                    "valueFromRelease": "Open",
                    "date": "2014-01-02",
                    "releaseTag": "tenderNotice",
                    "releaseID": "2"
                }
            ]
        }
    }
}
</code>

Merging gets more complicated when trying to merge arrays / lists of data.

We adopt two approaches to merging arrays:
- override (the same treatment as the fields above)
- overrideByKey (override looks for a uniqueID when making the merge)

For most array fields, override is used. 

OverrideByKey is used on only two arrays:

- Awards 
- Contracts

First, we will discuss, basic override. In this strategy a list of objects
must **always be given in the same order** in each release. Whilst this 
may be a problem for data quality, the alternative, as used in awards and contracts
is that every object requires a unique value, which is also practically challenging.

Basic, override works as follows, where the value of Item 2 changes:

<code>
release_1_snippet = {
    "formation": {
        "itemsToBeProcured": [
            {
                "description": "Item 1",
                "quantity": 1,
                "valuePerUnit": {
                    "amount": 100,
                    "currency": "GBP"
                }
            },
            {
                "description": "Item 2",
                "quantity": 1,
                "valuePerUnit": {
                    "amount": 200,
                    "currency": "GBP"
                }
            }
        ]
    }
}

release_2_snippet = {
    "formation": {
        "itemsToBeProcured": [
            {
                "description": "Item 1",
                "quantity": 1,
                "valuePerUnit": {
                    "amount": 100,
                    "currency": "GBP"
                }
            },
            {
                "description": "Item 2",
                "quantity": 1,
                "valuePerUnit": {
                    "amount": 150, // Value changed
                    "currency": "GBP"
                }
            }
        ]
    }
}

record_snipped = {
    "compiledRelease": {
        "ocid": "A",
        "releaseTag": "compiled",
        "formation": {
            "itemsToBeProcured": [
                {
                    "description": "Item 1",
                    "quantity": 1,
                    "valuePerUnit": {
                        "amount": 100,
                        "currency": "GBP"
                    }
                },
                {
                    "description": "Item 2",
                    "quantity": 1,
                    "valuePerUnit": {
                        "amount": 150, // Value changed
                        "currency": "GBP"
                    }
                }
            ]
        }
}
</code>

If only the changed item was provided in the second release, when the entire 
array is updated, only the second item would be available in
the merged record, as follows.

<code>
release_1_snippet = {
    "formation": {
        "itemsToBeProcured": [
            {
                "description": "Item 1",
                "quantity": 1,
                "valuePerUnit": {
                    "amount": 100,
                    "currency": "GBP"
                }
            },
            {
                "description": "Item 2",
                "quantity": 1,
                "valuePerUnit": {
                    "amount": 200,
                    "currency": "GBP"
                }
            }
        ]
    }
}

release_2_snippet = {
    "formation": {
        "itemsToBeProcured": [
            {
                "description": "Item 2",
                "quantity": 1,
                "valuePerUnit": {
                    "amount": 150, // Value changed
                    "currency": "GBP"
                }
            }
        ]
    }
}

record_snippet = {
    "compiledRelease": {
        "ocid": "A",
        "releaseTag": "compiled",
        "formation": {
            "itemsToBeProcured": [
                {
                    "description": "Item 2",
                    "quantity": 1,
                    "valuePerUnit": {
                        "amount": 150, // Value changed
                        "currency": "GBP"
                    }
                }
            ]
        }
}
</code>

We have made two exceptions to this type of merging with the overrideByKey on
awards and contract. Over the course of a large or framework contracting process
many awards and contracts are made, it is useful to be able to just release 
information about one award or contract at a time rather than having to 
include all information about all awards and contracts previously made each
time. The items in the array are first matched on the unique identifier, awardID 
and contractID respectively, and then the standard override takes place. This
means that awardID and contractID cannot change.

A simplified example is given below (with incomplete data) to illustrate the pattern:

<code>
release_1 = {
    "awards": [
        {
            "awardID": "ABC",
            "awardValue": 100
        }
    ]
}
release_2 = {
    "awards": [
        {
            "awardID": "DEF",
            "awardValue": 100
        }
    ]
}
release_3 = {
    "awards": [
        {
            "awardID": "DEF",  
            "awardValue": 150 // Updating information from release_2
        }
    ]
}

record_snippet = {
    "compiledRelease": {
        "awards": [
            {
                "awardID": "ABC",
                "awardValue": 100
            },
            {
                "awardID": "DEF",
                "awardValue": 150
            }
        ]
    }
}
</code>
