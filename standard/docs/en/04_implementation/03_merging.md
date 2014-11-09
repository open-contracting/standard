[TOC]

## Record recap

The basic format of a record is simple. There are three components:

- Releaes: A list of all the releases in the record. Either provided as a list of links to
  identify the release, or the releases themselves can be embedded.
- Compiled Release: A compiled release, this is the same format as a release but contains the
  most up-to-date information compiled from all the releases.
- Versioned Release: For each field in the release, the versioned release contains the history
  of all the changes to that field over all the releases.

For full information on records and releases see: [http://ocds.stage.aptivate.org/standard/r/master/en/key_concepts/releases_and_records/](http://ocds.stage.aptivate.org/standard/r/master/en/key_concepts/releases_and_records/)


## Merging

If a publisher provides releases and a record containing a list of the releases, then third party software 
should be able to create compiled and versioned releases. Publishers may or 
may not want to run this software themselves and provide the full record.

The following sections describe how merging works should invididual parties 
wish to implement merging or a merging library.

### Things to be careful of when publishing to enable merging:

The following all require unique identifiers (at least unique to the ocid):

- awards
- contracts
- items
- documents
- transactions
- milestones

The following lists of things must be re-published in full for each release:

- Award.suppliers
- Organization.additionalIdentifiers
- Item.additionalClassifications
- Amendment.changes

### Merge Strategies

The OCDS merging is based on the open source jsonmerge library https://github.com/avian2/jsonmerge.

But the principles could be re-implemented if desired.

Within the OCDS release schema, each field has a mergeStrategy property.

This documents how to merge fields. In the basic jsonmerge library there are some
basic strategies - consult the jsonmerge documentation.

#### ocdsVersion merge strategy

Most fields have the mergeStrategy ocdsVersion. The ocdsVersion strategy has two
modes of operation:

- when making a compiled record, the field is overridden with the latest value
- when making a versioned record, the field history is documented.

Here is a simple example.

<pre>
release_1 = {
    "ocid": "A",
    "id": "1",
    "date": "2014-01-01",
    "tag": "tender",
    "tender": {
        "id": "A",
        "procurementMethod": "Selective"
    } 
}
release_2 = {
    "ocid": "A",
    "id": "2",
    "date": "2014-01-02",
    "tag": "tender",
    "tender": {
        "id": "A",
        "procurementMethod": "Open" // This second release updates the procurmentMethod
    } 
}
record = {
    //...
    // Other record fields omitted
    //....
    "compiledRelease": {
        "ocid": "A",
        "id": "compiled",
        "date": "2014-01-03", 
        "tag": "compiled",
        "tender": {
            "id": "A",
            "procurementMethod": "Open" // This is the latest value for the compiledRelease
        } 
    },
    "versionedRelease": {
        "ocid": "A",
        "tender": {
            "id": "A",
            "procurementMethod": [
                {
                    "value": "Selective",
                    "releaseDate": "2014-01-01",
                    "releaseTag": "tender",
                    "releaseID": "1"
                },
                {
                    "value": "Open",
                    "releaseDate": "2014-01-02",
                    "releaseTag": "tender",
                    "releaseID": "2"
                }
            ]
        }
    }
}
</pre>

As you can see in the versionedRelease, the field procurementMethod has changed from a value 
documenting the latest correct value, to a list of objects which document the value for each release 
in which it changed.

#### Merging lists

Merging gets more complicated when trying to merge arrays / lists of data.

We adopt two approaches to merging arrays:
- ocdsVersion (the same treatment as the fields above)
- arrayMergeById (overwrite looks for a uniqueID when making the merge)

#### Merging lists - arrayMergeById

The arrayMergeById applies to the following lists of objects within the release:

- awards
- contracts
- items
- documents
- transactions
- milestones

Each of these objects has a required id field on it. When the merge is being performed, the
item with the corresponding id is looked up for the before and after versions of the release and the
fields are then matched accordingly.

<pre>
release_1 = {
    "ocid": "A",
    "id": "1",
    "date": "2014-01-01",
    "tag": "tender",
    "tender": {
        "items": [
            {
                "id": "1",
                "description": "Item 1",
                "quantity": 1
            },
            {
                "id": "2",
                "description": "Item 2",
                "quantity": 1
            }
        ]
    }
}

release_2 = {
    "ocid": "A",
    "id": "2",
    "date": "2014-01-02",
    "tag": "tender",
    "tender": {
        "items": [
            {
                "id": "1",
                "description": "Item 1",
                "quantity": 2 // The quantity for item 1 has been updated
            },
            {
                "id": "3",
                "description": "Item 3", // Item 3 has been added
                "quantity": 1
            }
        ]
    }
}

record_snippet = {
    "compiledRelease": {
        "ocid": "A",
        "tag": "compiled",
        "tender": {
            "items": [
                {
                    "id": "1",
                    "description": "Item 1",
                    "quantity": 2
                },
                {
                    "id": "2",
                    "description": "Item 2",
                    "quantity": 1
                },
                {
                    "id": "3",
                    "description": "Item 3",
                    "quantity": 1
                }
            ]
        }
    },
    "versionedRelease": {
        "ocid": "A",
        "tag": "compiled",
        "tender": {
            "items": [
                {
                    "id": "1",
                    "description": [
                        {
                            "value": "Item 1",
                            "releaseDate": "2014-01-01",
                            "releaseTag": "tender",
                            "releaseID": "1"
                        }
                    ]
                    "quantity": [
                        {
                            "value": 1,
                            "releaseDate": "2014-01-01",
                            "releaseTag": "tender",
                            "releaseID": "1"
                        },
                        {
                            "value": 2,
                            "releaseDate": "2014-01-02",
                            "releaseTag": "tender",
                            "releaseID": "2"
                        }
                    ]
                },
                {
                    "id": "2",
                    "description": [
                        {
                            "value": "Item 2",
                            "releaseDate": "2014-01-01",
                            "releaseTag": "tender",
                            "releaseID": "1"
                        }
                    ],
                    "quantity": [
                        {
                            "value": 1,
                            "releaseDate": "2014-01-01",
                            "releaseTag": "tender",
                            "releaseID": "1"
                        },
                    ]
                },
                {
                    "id": "3",
                    "description": [
                        {
                            "value": "Item 3",
                            "releaseDate": "2014-01-02",
                            "releaseTag": "tender",
                            "releaseID": "2"
                        }
                    ],
                    "quantity": [
                        {
                            "value": 1,
                            "releaseDate": "2014-01-02",
                            "releaseTag": "tender",
                            "releaseID": "2"
                        },
                    ]
                }
            ]
        }
    }
}
</pre>


#### Merging lists - ocdsVersion

The ocdsVersion strategy applies to the following lists:

-  Award.suppliers
-  Organization.additionalIdentifiers
-  Item.additionalClassifications
-  Amendment.changes

In this instance the entire list is treated as one single value and any change to any field will
result in the whole list being updated and documented as changed.

To keep the versioning as clean as possible, the list of objects should 
**always be given in the same order** in each release, so as not to mistakenly
mark a change when actually only order has shifted.

This merging strategy has the advantage of not requiring unique identifiers on
every object, but has the downside of requiring every release to publish the 
whole block of data, not just an incremental change.

<pre>
release_1 = {
    "ocid": "A",
    "id": "1",
    "date": "2014-01-01",
    "tag": "award",
    "awards": [
        {
            "id": 1,
            "suppliers": [
                {
                    "name": "Supplier 1",
                    "address": {
                        "countryName": "Canada"
                    }
                },
                {
                    "name": "Supplier 2",
                    "address": {
                        "countryName": "Canada"
                    }
                }
            ]
        }
    ]
}

release_2 = {
    "ocid": "A",
    "id": "2",
    "date": "2014-01-02",
    "tag": "award",
    "awards": [
        {
            "id": 1,
            "suppliers": [
                {
                    "name": "Supplier 1",
                    "address": {
                        "countryName": "Canada"
                    }
                },
                {
                    "name": "Supplier 2",
                    "address": {
                        "countryName": "United Kingdom"
                    }
                }
            ]
        }
    ]
}

record_snippet = {
    "compiledRelease": {
        "ocid": "A",
        "tag": "compiled",
        "awards": [
            {
                "id": 1,
                "suppliers": [
                    {
                        "name": "Supplier 1",
                        "address": {
                            "countryName": "Canada"
                        }
                    },
                    {
                        "name": "Supplier 2",
                        "address": {
                            "countryName": "United Kingdom"
                        }
                    }
                ]
            }
        ]
    },
    "versionedRelease": {
        "ocid": "A",
        "tag": "compiled",
        "awards": [
            {
                "id": 1,
                "suppliers": [
                    {
                        "value": [ // Note the entire list is the value (as opposed to individual fields)
                            {
                                "name": "Supplier 1",
                                "address": {
                                    "countryName": "Canada"
                                }
                            },
                            {
                                "name": "Supplier 2",
                                "address": {
                                    "countryName": "Canada"
                                }
                            }
                        ],
                        "releaseDate": "2014-01-01",
                        "releaseTag": "award",
                        "releaseID": "1"
                    },
                    {
                        "value": [
                            {
                                "name": "Supplier 1",
                                "address": {
                                    "countryName": "Canada"
                                }
                            },
                            {
                                "name": "Supplier 2",
                                "address": {
                                    "countryName": "United Kingdom"
                                }
                            }
                        ],
                        "releaseDate": "2014-01-02",
                        "releaseTag": "award",
                        "releaseID": "2"
                    }
                ]
            }
        ]
    },
}
</pre>

#### Merge strategies ocdsOmit

There are a number of fields marked with the strategy ocdsOmit.

This strategy returns nothing on merge, because to update the field wouldn't make sense.

For example, the field for `tag` should not be updated to the latest version, 
it should be updated to `compiled` for it to make sense.

### Implementing merging

To merge releases into records, we use the jsonmerge library with its 
add-ons to json schema that specify a mergeStrategy on each field.

A customized version of the jsonmerge library is available at [https://github.com/open-contracting/jsonmerge](https://github.com/open-contracting/jsonmerge) using the ocds branch (set as default) as a
reference implementation. As of 2014-11-08 it has not been rigorously tested against all our mergeStrategies.

An example of merging releases into a record can be seen in this ipython notebook:
[http://nbviewer.ipython.org/github/open-contracting/sample-data/blob/master/buyandsell/processing/Demonstrate%20merging%20a%20release.ipynb](http://nbviewer.ipython.org/github/open-contracting/sample-data/blob/master/buyandsell/processing/Demonstrate%20merging%20a%20release.ipynb)

To make a compiled release with jsonmerge replace mergeStrategy ocdsVersion with overwrite or objectMerge (the default jsonmerge strategies).

There is a util that makes a validation schema for a versioned release based on the merge strategies. This schema is stored as versioned-release-validation-schema.json.
