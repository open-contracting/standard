<br />
<br />

[TOC]

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

The basic principle of of merging is very simple, the latest data overwrites
previous data.  For example:

<pre>
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
            "method": [
                {
                    "value": "Selective",
                    "releaseDate": "2014-01-01",
                    "releaseTag": "tenderNotice",
                    "releaseID": "1"
                },
                {
                    "value": "Open",
                    "releaseDate": "2014-01-02",
                    "releaseTag": "tenderNotice",
                    "releaseID": "2"
                }
            ]
        }
    }
}
</pre>

Merging gets more complicated when trying to merge arrays / lists of data.

We adopt two approaches to merging arrays:
- overwrite (the same treatment as the fields above)
- overwriteByKey (overwrite looks for a uniqueID when making the merge)

For most array fields, overwrite is used. 

OverwriteByKey is used on only two arrays:

- Awards 
- Contracts

First, we will discuss, basic overwrite. In this strategy a list of objects
must **always be given in the same order** in each release. Whilst this 
may be a problem for data quality, the alternative, as used in awards and contracts
is that every object requires a unique value, which is also practically challenging.

Basic, overwrite works as follows, where the value of Item 2 changes:

<pre>
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
</pre>

If only the changed item was provided in the second release, when the entire 
array is updated, only the second item would be available in
the merged record, as follows.

<pre>
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
</pre>

We have made two exceptions to this type of merging with the overwriteByKey on
awards and contract. Over the course of a large or framework contracting process
many awards and contracts are made, it is useful to be able to just release 
information about one award or contract at a time rather than having to 
include all information about all awards and contracts previously made each
time. The items in the array are first matched on the unique identifier, awardID 
and contractID respectively, and then the standard overwrite takes place. This
means that awardID and contractID cannot change.

A simplified example is given below (with incomplete data) to illustrate the pattern:

<pre>
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
</pre>

## Implementing merging
To merge releases into records, we use the jsonmerge library with its 
add-ons to json schema that specify a mergeStrategy on each field.

A customized version of the jsonmerge library is available at [https://github.com/open-contracting/jsonmerge](https://github.com/open-contracting/jsonmerge) using the ocds branch (set as default).

An example of merging releases into a record can be seen in this ipython notebook:
[http://nbviewer.ipython.org/github/open-contracting/sample-data/blob/master/buyandsell/processing/Demonstrate%20merging%20a%20release.ipynb](http://nbviewer.ipython.org/github/open-contracting/sample-data/blob/master/buyandsell/processing/Demonstrate%20merging%20a%20release.ipynb)

The compiledRelease is built using the mergeStrategies that are in the normal Release Schema.

To build a versionedRelease, we use the mergeStrategies specified in the Versioned Release Schema.

Data in the compiledRelease, should validate against the regular Release Schema. Data in a versionedRelease needs to be validated against a seperate schema, which will be published soon (and can be generated
using the jsonmerge library).
