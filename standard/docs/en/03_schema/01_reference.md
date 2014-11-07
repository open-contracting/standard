[TOC]

# Schema Reference

<span class="lead">The [Release Schema](../release) provides a detailed specification of the fields and data structures to use when publishing data, with supplementary schemas showing how to combine release and records. This reference section works step-by-step through additional supporting information to assist publishers and users of the data.</span>

(Note: If any conflicts are found between this text, and the text within the schema, the schema takes precedence)

## Release structure

The majority of OCDS data is held within a structured [release](../release). Releases must be published within a release package. Releases are made up of a number of blocks of data, including:

* tender
* award
* contract
* performance

A release can only contain one set of tender information (as we define a unique [contracting process](../../definitions#contracting-process) by the initiation stage), but may contain multiple instances of awards, contracts and performance information.

Releases are given a [tag](#release-tag) to indicate what stage of a contracting process they represent, but there are no formal restrictions on when information about a stage of the contracting process may be provided. For example, a publisher announcing the signing of a contract with a 'contract' tagged release, may also include information in the award and tender blocks in order to provide a comprehensive picture of the contracting process to date which led to that contract being signed. 

### Package Metadata

A release package, modelled on the [Data Package](http://dataprotocols.org/data-packages/) protocol, provides meta-data about release(s) it contains. 

<div class="include-csv" data-src="standard/docs/field_definitions/release-package.csv" data-table-class="table table-striped schema-table"></div>

* The uri should unique identify this release package. Publishers should provide a [dereferenceable HTTP URI](http://en.wikipedia.org/wiki/Dereferenceable_Uniform_Resource_Identifier) wherever possible and should host the data package at this URI, enabling users to look-up and verify the contents of a release package from its original source. 

* The [publishedDate](#date) on which this package was published. If a package is automatically generated and re-published on a regular basis, this date should reflect the date of the last change to the contents of the package. 

* The publisher should be identified using an Organisation block. See the [Organization/Entity](#entity) guidance for details.

* See the [licensing guidance](../../implementation/publication_patterns#licensing) for more details on selecting and publishing license information. 

* See the [publication policy](../../implementation/publication_patterns#publication-policy) guidance for more details.

### Top level fields

#### OCID

Providing each [contracting process](../../definitions#contracting-process) with a unique identifier is essential to enable data about contracts to be linked up across different releases.

Open Contracting IDs are composed of a prefix assigned to each publisher, and a local identifier drawn from their internal systems that can be used to tie together tenders, awards, contracts and other key data points from a specific contracting process.

See the [Open Contracting Identifier guidance](../../identifiers#ocid) for details of how to construct an OCID. 

#### Release date

The release [date](#date) should reflect the point in time at which the information in this release was disclosed. 

A release package may contain release with different release dates.

#### formationType (ToDo: check - should this be initiationType?)

Contracts may be formed under a number of different processes. 

Values must be drawn from the [formationType codelist](../codelists#formationType)

Currently, only 'tender' is supported. 

#### Tag (ToDo: Check Title)

The release tag is used to identify the nature of the release being made. 

This can be used by consuming applications to filter releases, or may in future be used for advanced validation.

A release which updates or amends previous data must always use the appropriate update or amendment release tag. 

Values must be drawn from the [releaseTag codelist](../codelists#releaseTag).

#### Language

See the section on [multi-language support](#multi-language-support) for details.

#### Buyer

Published using an [organization](#entity) block.

### Tender

The tender section includes details of the announcement that a organization intends to source some particular goods or services, and to establish one or more contract(s) for these.

It may contain details of a forthcoming process to receive and evaluate proposals to supply these goods and services, and may also be used to record details of how a completed tender process, including details of bids received. 

#### Tender ID

#### Procuring Entity

#### Attachments

#### Items

#### Value

#### Procurement Method

#### Selection Criteria

#### Selection Details

#### Submission Method

#### Submission Details

#### Tender Period

#### Clarification Period

#### Clarifications

#### Award Period

#### Bidders

ToDo: Check if numberOfBidders and numberOfBids included



### Award



### Contract


### Implementation



## Record structure

Whereas there can be multiple releases concerning a given contracting process, there is a single **contracting record** for each OCID, providing a summary of all the available data about this particular contracting process.

Releases MUST contain:

* An [OCID](../../key_concepts/identifiers#ocid)
* An array of **releases** related to this contracting process - either by providing a URL for where these releases can be found, or embedding a full copy of the release

Release SHOULD contain:

* **compiledRelease** - the latest version of all open contracting process fields, represented using the release schema. For example, if a contractSignature release has been issued with with a contractValue of $100, and then a contractAmendment release has been issued with a contractValue updated to $200, the compiledRelease would have contract/contractValue of $200.

and

* **versionedRelease** - containing the history of the data in the compiledRecord, with all known past values of any field and the release that information came from.

Records should be embedded within a record package.  

### Package meta-data

<div class="include-csv" data-src="standard/docs/field_definitions/record-package.csv" data-table-class="table table-striped schema-table"></div>

See the guidance on [package meta-data](#package-metadata) above. In addition, a record package includes:

* ```packages``` - which should provide links to all the release packages used to compile this record. 
* ```records``` - see below.

### Records

Each record package contains an array of one or more records, consisting of the following sections:

* Releases (required)
* Compiled Release (optional)
* Versioning Release (optional)

#### Releases

The releases that go to make up a contracting process can be provided in two ways:

* URLs for each release
* Embedded copies of the release

If providing and array of URLs, it should be possible for a consuming application to look up each URL, retrieve a release package, and locate the release inside it. 

In order to locate the specific release inside a release package the releaseID of the release should be appended to the package URL using a fragment identifier.

For example:

* http://ocds.open-contracting.org/demos/releases/12345.json#ocds-a2ef3d01-1594121/1 to refer to the release with a release.id of ocds-a2ef3d01-1594121/1 

ToDo: Construct these as real examples.

#### Compiled Release

The compiled release is latest version of all the data about this contracting process, and has the same schema as a release.

The process for creating a compiled release is described in the guidance on [merging](../../implementation/merging). 

A compiled release provides a snapshot of the current state of a contracting process. 

#### Versioned Release

A versioned release contains the history of all the data in the compiled release, including which fields have changed, when they were changed, and the release that updated them.

Providing this versioned information is valuable for many use cases relating to contract monitoring. 

Publishers may chose to provide a copy of the record with, and without, this information, as for large contracting processes it can add substantially to file sizes.

Third parties should also be able to use the information in the releases list to fetch source data, compile and verify their own version history for a contract.


## Multi-language support (ToVerify)

Many publishers need to be able to share key data in multiple languages. All free-text title and description fields in the Open Contracting Data Standard can be given in one or more languages.

Language variations are included by a copy of multi-lingual fields, suffixed with a language code.

E.g. ```title``` and ```title_es```

In order to allow users to identify the language used in non-suffixed fields, OCDS release and records should declare the default language in the ```language``` field. 

In order to allow users to identify all the other languages in a file, the language codes for any other included languages should be given in the ```languagesIncluded``` array. (ToDo: CHECK PROPERTY NAME)

Languages should be identified using language tags taken from [BCP47](http://tools.ietf.org/html/bcp47). The specification allows BCP47 values in order to accommodate variations in dialect where this is important. However, publishers **should** use the two letter [ISO-639-1 two-digit language tags](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) in the vast majority of circumstances, and should not assume that the users are able to distinguish between sub-tag variations (for example, OCDS publishers should strongly prefer 'en' over 'en_US' or 'en_GB'). 

To include a language variation of a field, the field name should be suffixed with _ and the appropriate language tag. For example: ```title_es``` for Spanish.

### Example

A contract is for ‘Software consultancy services’ may be published in a release with the default language sent to ‘en’ (the ISO-639-1 code for English). The following examples give the description of an item as English, French and Spanish.

<div class="tabbable">
<ul class="nav nav-tabs">
  <li class="active"><a href="#json" data-toggle="tab">json</a></li>
  <li><a href="#csv" data-toggle="tab">csv</a></li>
</ul>

<div class="tab-content">
<div class="tab-pane active" id="json">
<div class="include-json" data-src="standard/example/language.json"></div>
</div>
<div class="tab-pane" id="csv">
<div class="include-csv" data-src="standard/example/language.csv" data-table-class="table table-striped"></div>
</div>
</div>
</div>

The JSON Schema makes use of the JSON Scheme 0.4 [‘Pattern Properties](http://spacetelescope.github.io/understanding-json-schema/reference/object.html#pattern-properties)’ definition to allow validation of multi-language fields. 


## Field reference


### Classification

ToDo:


### Organization

ToDo: Update once organisation contact details confirmed.

### Attachment

### Date

OCDS makes use of [ISO8601](http://en.wikipedia.org/wiki/ISO_8601) date-times, following [RFC3339 §5.6](http://tools.ietf.org/html/rfc3339#section-5.6).

A time and timezone/offset MUST always be provided in a date-time.

The following are valid date-times:

* '2014-10-21T09:30:00Z' - 9:30 am on the 21st October 2014, UTC
* '2014-11-18T18:00:00-06:00' - 6pm on 18th November 2014 CST (Central Standard Time)

The following are not valid:

* '2014-10-21' - Missing time portion
* '2014-10-21T18:00' - missing seconds in time portion.
* '2014-11-18T18:00:00' - Missing timezone/offset portion
* '11/18/2014 18:00' - Not following the pattern at all!

Accurately including the time and timezone offsets is particular important for tender deadlines and other dates which may have legal significance, and where users of the data may be from different timezones. The character Z on the end of a date-time indicates the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) (or Zero offset) timezone, whereas other timezones are indicated by their value '+/-hh:mm' UTC on the end of the date-time value. 

In the event that the system from which data is drawn only includes dates, and does not include time information, publishers should consider sensible defaults for each field. For example, the startDate time of a clarification period may be set to '00:00:00Z' to indicate that clarifications can be requested from any time on the date stated, with the endDate time set to 23:23:59Z to indicate that clarifications can be sent up until the end of the endDate given. Alternatively, if clarification requests are only accepted in standard office hours, these values might be 09:00:00Z and 17:00:00Z respectively. 

In the event that a date field is not bound to a specific time at all, publishers should choose a default time value of '23:23:59' and either 'Z' (for UTC) or the timezone of the publisher, indicating that the time refers to the end of the given date. 

### Item

<div class="include-csv" data-src="standard/docs/field_definitions/release-item.csv" data-table-class="table table-striped schema-table"></div>


### Milestone

ToDo: Review once updated

<div class="include-csv" data-src="standard/docs/field_definitions/release-milestone.csv" data-table-class="table table-striped schema-table"></div>

### Value

<div class="include-csv" data-src="standard/docs/field_definitions/release-value.csv" data-table-class="table table-striped schema-table"></div>

### Location

The addition of location information is handled through an extension to the specification, with an integral location element considered for future versions of the specification.