# Merging 

In OCDS, merging involves combining individual [releases](../getting_started/releases_and_records.md) of data during a contracting process into a [record](../getting_started/releases_and_records.md) which provides an at-a-glance view of the current state and history of that process. 

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

A publisher provides a tender release on 1st January, with a planned contract value of $1000.

On 31st January, the publisher provides an amended tender release updating the planned contract value to $1500.

After assessing bids, it is decided to award the contract in two lots.

On 1st March, the publisher provides an award release, announcing Company A have been awarded a contract for $750.

On 3rd March, the publisher provides an separate award release, announcing that company B have been awarded a contract for $750

These independent releases each provide real-time information about what is happening in the contracting process. The record will combine them together. Using the same schema and structure as the releases, the main body of the record will contain a tender with contract value of $1500, and details of both awards.

If the record is complete with versioning information, then the versioning section will reveal that the planned contract value changed from $1000 to $1500 on 31st January.

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-tender-1.json
   :jsonpointer: /releases
   :expand: releases, tender
   :title: Tender

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-tender-2.json
   :jsonpointer: /releases
   :expand: releases, tender
   :title: Tender_update

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-award-1.json
   :jsonpointer: /releases
   :expand: releases, award
   :title: Award_One

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merge-award-2.json
   :jsonpointer: /releases
   :expand: releases, award
   :title: Award_Two

```

```eval_rst

.. jsoninclude:: docs/en/examples/merging/merged.json
   :jsonpointer: 
   :expand: releases, tender, award
   :title: Merged

```

</div>

## Merging rules

The merging rules can be summarised as follows:

1. All releases with the same ```ocid``` should be compiled together, processed by order of the release date, and starting with the oldest first. Compare each pair or releases in turn following the rules below. 

2. For literal values, replace the older value with the newer value. You may remove fields which have been set to null. 

   <!--TODO - EXAMPLE-->

3. For an array of objects, merge the array by the id of each object EXCEPT as noted in 4.

   <!--TODO - EXAMPLE-->

4. For the following arrays, replace the entire array in the older release with the entire array from the newer release

   - ```award.suppliers```
   - ```organization.additionalIdentifiers```
   - ```item.additionalClassifications```
   - ```amendment.changes```

   Note that this means releases must republish these arrays in full.

5. When all releases are merged, remove the ```release.id``` and ```release.date``` from the resulting data structure, and add ```compiled``` to the list of ```release.tag``` values. 

A reference implementation of the merge routine in python [is available on GitHub](https://github.com/open-contracting/ocds-merge). 

## Requirements for merging

For merging to work effectively, all the releases to be merged must share a common ```ocid``` and a number of other criteria must be met.

The following all require unique identifiers (at least unique within that ocid):

- awards
- contracts
- items
- documents
- transactions
- milestones

The following arrays of items must be re-published in full for each release:

- Award.suppliers
- Organization.additionalIdentifiers
- Item.additionalClassifications
- Amendment.changes

Other lists with ```.id``` properties do not need to be republished in full, but publishers should note the [guidance on emptying fields and values](../../reference/#emptying-fields-and-values).


## Versioned data

There are some situations in which it is important to be able to see how data about a contracting process has changed over time. For example, to identify how contract values have altered, or milestones moved through stages of implementation. 

The versioned release schema provides a model for representing this data.

In a versioned release, instead of over-writing past values when combining multiple releases, each field becomes an array of objects, indicating the:

* The date, id and tag of the releases where a field-value pair was first encountered;
* The value of the field-value pair at that point;

As a result, the history of any field can be easily read from the data structure. 

### Example

```eval_rst

.. jsoninclude:: docs/en/examples/merging/versioned.json
   :jsonpointer: /records/0/versionedRelease/tender/value
   :expand: value, amount
   :title: Versioned_Example


```

## Merge strategies in the schema

Version 1.0 of the OCDS schema includes a series of ```mergeStrategy``` properties which were designed to indicate how releases should be compiled together. In initial implementation, we have found these can create some confusion, and so propose that future versions will omit all but the essential properties required to indicate the exceptions to the general rule in (4) above. 

This information is maintained here for reference.

### Merge strategy reference

The purpose of merging releases is to create (a) a snapshot record of the current state of a contracting process; (b) a versioned history of the process. 

Different sections of the data structure need to be handled differently as releases are merged. For some lists, a new release should overwrite the previous list in fully. For example, if a later release updates the list of suppliers against an award, this new list in full should be taken as the latest authoritative information. For other lists, such as a list of contracts, a release may add a new contract to the list without needing to repeat all the previous contracts, or may amend a single award without repeating all the other awards. 

This leads to a set of mergeStrategies which are included in the full schema.

The OCDS merging has been based on the open source [jsonmerge library](https://github.com/avian2/jsonmerge), but can be implemented in other software as required. 

Within the OCDS release schema, each field has a mergeStrategy property. This strategy describes how to merge that and child fields.

We inherit the existing merge strategies from [jsonmerge](https://github.com/avian2/jsonmerge#merge-strategies) and add a number of specific strategies for OCDS, which are currently only available in the [OCDS fork of jsonmerge](https://github.com/open-contracting/jsonmerge) and which are described below.

#### ocdsVersion merge strategy

Most fields have the mergeStrategy ocdsVersion. The ocdsVersion strategy has two
modes of operation:

- when making a compiled record, the field is overridden with the latest value
- when making a versioned record, the field history is documented.

#### ocdsVersion for lists

The ocdsVersion strategy also applies to the following lists:

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

#### arrayMergeById merge strategy

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

If a given entry is omitted (e.g. there is no information about a particular contract in a subsequent release), then the previous values carry forward. 

To remove an entry it would have to have it's field values set to null, as per the [guidance on emptying fields and values](../../reference/#emptying-fields-and-values).

#### ocdsOmit merge strategy

There are a number of fields marked with the strategy ocdsOmit.

This strategy returns nothing on merge, because to update the field wouldn't make sense.

For example, the field for `tag` should not be updated to the latest version, it should be updated to `compiled` for it to make sense.
