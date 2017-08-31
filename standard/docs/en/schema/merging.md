# Merging 

In OCDS, merging involves combining individual [releases](../getting_started/releases_and_records.md) of data during a contracting process into a [record](../getting_started/releases_and_records.md) which provides an overview of the current state of that process. Including a versioned release as part of the merged record provides structured information on the history of the process: showing when updates were made, or values were changed. 

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

A publisher provides a tender release on 1st January, with a planned contract value of $1000.

On 5th February, the publisher provides an amended tender release updating the planned contract value to $2000.

After assessing bids, it is decided to award the contract in two lots.

On 1st March, the publisher provides an award release, announcing Company A has been awarded a contract for $750.

On 3rd March, the publisher provides an separate award release, announcing that company B has been awarded a contract for $750

These independent releases each provide real-time information about what is happening in the contracting process. The record will combine them together. Using the same schema and structure as the releases, the main body of the record will contain a tender with contract value of $1500, and details of both awards.

If the record is complete with versioning information, then the versioning section will reveal that the planned contract value changed from $1000 to $1500 on 31st January.

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-tender-1.json
   :jsonpointer: /releases
   :expand: releases, tender, tag
   :title: tender

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-tender-3.json
   :jsonpointer: /releases
   :expand: releases, tender, tag
   :title: tenderAmendment

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-award-1.json
   :jsonpointer: /releases
   :expand: releases, award
   :title: awardOne

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-award-2.json
   :jsonpointer: /releases
   :expand: releases, award
   :title: awardTwo

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merged.json
   :jsonpointer: 
   :expand: records, compiledRelease, tender, award, tag
   :title: record

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/versioned.json
   :jsonpointer: 
   :expand: records,versionedRelease, tender, award, tag
   :title: versioned

```

</div>

## Merging rules

Order all the releases that share an ```ocid``` by their release ```date```. Starting from the oldest release (old), compare it with the next oldest release (new), and apply the following rules.

### Objects

In the compiled record, merge **new** into **old** by:

* Overwriting all key that exist in both **old** and **new** with the values from **new**
* Add any key value pairs that exist in **new**, but not in **old**
* Remove any key that have their value explicitly set to ```null``` in **new**
* Retain any keys from **old** that are not mentioned in **new**

If the value of key value pair is a list of strings, the entire list should be treated as a single value. When the list contains objects, the list merge rules below should be used.

### Lists

There are two merge patterns for lists of objects. Identifier merge, and whole list merge. 

#### Identifier merge

When a list contains objects with their own ```id``` field, then:

* Check for an object in **old** with the same ```id``` as an object in **new**, and, if so, follow the object merge rules as above
* If there is no object in **new** with the same ```id``` as an object in **old**, keep the object from **old** in the list
* If there is an object in **new** with an ```id``` not found in **old** then add the object to the list

Note: to remove information from an old list entry its values must be explicitly set to null. 

#### Whole list merge

Where the objects contain no top level ```id``` values, or the schema specifies the ```"wholeListMerge": true``` for the array in question, then merging should take place by treating the entire list of objects as a single value. 

I.e. if the list exists in **new**, the entire list in **new** will overwrite the list in **old**. 

### Omit when merged

A few properties in the schema are marked with ```"omitWhenMerged": true```. These properties should be dropped from the merged record - as they only make sense in the context of a single release. 

### Reference implementation

A reference implementation of the merge routine in python [is available on GitHub](https://github.com/open-contracting/ocds-merge). 


## Versioned data

There are some situations in which it is important to be able to see how data about a contracting process has changed over time. For example, to identify how contract values have altered, or milestones moved through stages of implementation. 

The [versioned release validation schema](../../../../versioned-release-validation-schema.json) provides a model for representing this data.

In a versioned release, instead of over-writing past values when combining multiple releases, each field (with the exception of the ```id``` property of objects within an array) becomes an array of objects, indicating the:

* The date, id and tag of the releases where a field-value pair was first encountered;
* The value of the field-value pair at that point;

As a result, the history of any field can be easily read from the data structure.

The property ```"versionId":true``` is used to explicitly declare the cases where an ```id``` field **should** be versioned (i.e. within an object that is not within an array). 

### Example

```eval_rst

.. jsoninclude:: docs/en/examples/merging/versioned.json
   :jsonpointer: /records/0/versionedRelease/tender/value
   :expand: value, amount
   :title: versioned_extract
   
```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/versioned.json
   :jsonpointer: 
   :expand: 
   :title: full_versioned_file
   
```

