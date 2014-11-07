[TOC]

## Release data

A full schema for releases can be accessed from the 'Release Schema' tab above. Click each section to expand that component of the schema. 

A release should always contain:

* **ocid** - the Open Contracting Identifier for this Contracting Process. This should be globally unique. 
* **releaseID** - this should uniquely identify this release within the current 'package'. Generally these should be unique to a publisher, but are not required to be globally unique. 
* **releaseTag** - A tag that helps to identify the type of release being made. These may be used for advanced validation (i.e. certain kinds of release may in future require certain fields to be provided). The current list of tags is: planning, tenderNotice, awardNotice, contractSignature, contractAmendment, report, spending, terminationNotice
* **language** - An ISO 2-Digit Country code for the default language used in the document
* **buyer** - identifier and address details of the buying organisation (see below for the specification of an organisation)

A release can then contain elements within one or more of the following blocks: 

* planning
* formation
* awards
* contracts
* performance

The blocks are described in more detail below

### Planning
<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/planning"></script>

### Tender
<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/tender"></script>

### Awards
<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/award"></script>

### Contracts
<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/contract"></script>

### Performance
<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/performance"></script>

## Record data

There should be one record for each open contracting process. The record MUST contain:

* An **ocid** - An globally unique Open Contracting ID for this contracting process.
* An array of **releases** - either by providing URLs to each of the releases (so that a user can compile their own record), or embedding copies of each of the releases relating to this contracting process.

It SHOULD contain:

* **compiledRelease** - the latest version of all open contracting process fields, represented using the release schema. For example, if a contractSignature release has been issued with with a contractValue of $100, and then a contractAmendment release has been issued with a contractValue updated to $200, the compiledRelease would have contract/contractValue of $200. 

and

* **versionedRelease** - containing the history of the data in the compiledRecord, with all known past values of any field and the release that information came from. 

## Common data elements

The following data elements are used in a number of places throughout the standard.

### Values

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/value"></script>

### Periods

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/period"></script>

### Attachments

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/attachment"></script>


### Organization

Used for representing buyers, suppliers and bidders. We follow the IATI Organisation ID Standard for organisational identifiers.

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/organization"></script>

### Items

Used to itemsToBeProcured, itemsAwarded and itemsContracted

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/item"></script>
 
### Notices

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/notice"></script>
 
### Milestones

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/milestone"></script>

### Amendment information

<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/amendment"></script>

#### A note on amendments

When amending arrays (e.g. a list of itemsToBeProcured) then the amendment should contain *all* the items in the updated array, not just new items that are being added. 

# 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         <ul>
             <li>Does the proposed conceptual model make sense for the ways you want to publish or use open contracting data?</li>
             <li>Which do you need most: a summary contracting record, or detailed releases of information at each stage of the contracting process?</li>
             <li>Do these components cover all the relevant categories of information you want to publish or access about contracting?</li>
             <li>Are we missing key elements in our description of what each component will contain?</li>
             <li>How does the proposed approach of having the contracting record represent the latest stage of contracting (i.e. overwriting earlier data) affect how you might publish or use open contracting data?</li>
         </ul>     
     </div>
</div>
