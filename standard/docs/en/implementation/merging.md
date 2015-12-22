

# Merging

<span class="lead">To create a full record from a series of OCDS releases related to an contracting process the releases should be merged. This section details the creation of records.</span>

## Record recap

The basic format of a record is simple. There are three components:

- Releases: A list of all the releases in the record. Either provided as a list of links to
  identify the release, or the releases themselves can be embedded.
- Compiled Release: A compiled release, this is the same format as a release but contains the
  most up-to-date information compiled from all the releases.
- Versioned Release: For each field in the release, the versioned release contains the history
  of all the changes to that field over all the releases.

For full information on records and releases see the [key concepts](../../key_concepts/components/) and [schema reference](../../schema/reference).

## Merging

If a publisher provides releases and a record containing a list of the releases, then third party software should be able to create compiled and versioned releases. Publishers may or may not want to run this software themselves and provide the full record for download.

The following sections describe how merging works should individual parties wish to implement merging or a merging library.

### Requirements

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

Other lists with ```.id``` properties do not need to be republished in full, but publishers should note the [guidance on emptying fields and values](../../schema/reference#emptying-fields-and-values).

### Merge Strategies

The purpose of merging releases is to create (a) a snapshot record of the current state of a contracting process; (b) a versioned history of the process. 

Different sections of the data structure need to be handled differently as releases are merged. For some lists, a new release should overwrite the previous list in fully. For example, if a later release updates the list of suppliers against an award, this new list in full should be taken as the latest authoritative information. For other lists, such as a list of contracts, a release may add a new contract to the list without needing to repeat all the previous contracts, or may amend a single award without repeating all the other awards. 

This leads to a set of mergeStrategies which are included in the full schema.

The OCDS merging has been based on the open source [jsonmerge library](https://github.com/avian2/jsonmerge), but can be implemented in other software as required. 

Within the OCDS release schema, each field has a mergeStrategy property. This strategy describes how to merge that and child fields.

We inhert the existing merge strategies from [jsonmerge](https://github.com/avian2/jsonmerge#merge-strategies) and add a number of specific strategies for OCDS, which are currently only available in the [OCDS fork of jsonmerge](https://github.com/open-contracting/jsonmerge) and which are described below.

#### ocdsVersion merge strategy

Most fields have the mergeStrategy ocdsVersion. The ocdsVersion strategy has two
modes of operation:

- when making a compiled record, the field is overridden with the latest value
- when making a versioned record, the field history is documented.

Here is a simple example:

<div class="tabbable">
    <ul class="nav nav-tabs">
        <li class="active"><a href="#ar1" data-toggle="tab">release 1</a></li>
        <li><a href="#ar2" data-toggle="tab">release 2</a></li>
        <li><a href="#amerged" data-toggle="tab">merged</a></li>
    </ul>
    <div class="tab-content">
        
        <div class="tab-pane active" id="ar1">
            <div class="include-json" data-src="standard/example/merge_r1.json"></div>
        </div>
        <div class="tab-pane" id="ar2">
            <div class="include-json" data-src="standard/example/merge_r2.json"></div>
        </div>
        <div class="tab-pane" id="amerged">
            <div class="include-json" data-src="standard/example/merge_r1_r2.json"></div>
        </div>
    </div>
</div>
<p>Note that the compiledRelease not has 'procurementMethod' of 'open', reflecting the most recent value of this fields.</p>
<p>As you can see in the versionedRelease, the field procurementMethod has changed from a value documenting the latest correct value, to a list of objects which document the value for each release in which it changed.</p>
<p>(Other record fields are omitted for easy presentation.)</p>

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

An example of this strategy in action is shown below:

<div class="tabbable">
<ul class="nav nav-tabs">
  <li class="active"><a href="#lr1" data-toggle="tab">release 1</a></li>
  <li><a href="#lr2" data-toggle="tab">release 2</a></li>
  <li><a href="#lmerged" data-toggle="tab">merged</a></li>
</ul>
<div class="tab-content">
    
<div class="tab-pane active" id="lr1">
<div class="include-json" data-src="standard/example/li_merge_r1.json"></div>
</div>
<div class="tab-pane" id="lr2">
<div class="include-json" data-src="standard/example/li_merge_r2.json"></div>
</div>
<div class="tab-pane" id="lmerged">
<div class="include-json" data-src="standard/example/li_merge_r1_r2.json"></div>
</div>
</div>
</div>


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

To remove an entry it would have to have it's field values set to null, as per the [guidance on emptying fields and values](../../schema/reference#emptying-fields-and-values).

<div class="tabbable">
<ul class="nav nav-tabs">
  <li class="active"><a href="#r1" data-toggle="tab">release 1</a></li>
  <li><a href="#r2" data-toggle="tab">release 2</a></li>
  <li><a href="#merged" data-toggle="tab">merged</a></li>
</ul>
<div class="tab-content">
    
<div class="tab-pane active" id="r1">
<div class="include-json" data-src="standard/example/ar_merge_r1.json"></div>
</div>
<div class="tab-pane" id="r2">
<div class="include-json" data-src="standard/example/ar_merge_r2.json"></div>
</div>
<div class="tab-pane" id="merged">
<div class="include-json" data-src="standard/example/ar_merge_r1_r2.json"></div>
</div>
</div>
</div>


#### ocdsOmit merge strategy

There are a number of fields marked with the strategy ocdsOmit.

This strategy returns nothing on merge, because to update the field wouldn't make sense.

For example, the field for `tag` should not be updated to the latest version, 
it should be updated to `compiled` for it to make sense.

### Implementing merging

To merge releases into records, we use the jsonmerge library with its add-ons to json schema that specify a mergeStrategy on each field.

A customized version of the jsonmerge library is available at [https://github.com/open-contracting/jsonmerge](https://github.com/open-contracting/jsonmerge) using the ocds branch (set as default) as a
reference implementation. As of 2014-11-08 it has not been rigorously tested against all our mergeStrategies.

An example of merging releases into a record can be seen [in this ipython notebook](http://nbviewer.ipython.org/github/open-contracting/sample-data/blob/1__0__0/buyandsell/processing/Demonstrate%20merging%20a%20release.ipynb)

To make a compiled release with jsonmerge replace mergeStrategy ocdsVersion with overwrite or objectMerge (the default jsonmerge strategies).

There is a util that makes a validation schema for a versioned release based on the merge strategies. This schema is stored as versioned-release-validation-schema.json.
