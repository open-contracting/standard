[TOC]

# Publication guidance

<span class="lead">The Open Contracting Data Standard is designed to support step-by-step improvements in how contracting data is published on the web. In this section you will find core principles of good publishing practices, alongside tools to help you plan the effective publication of your data.</span> 


We have set out a 5* approach to progressively improving the publication of Open Contracting Data on the web. In this section we consider a number of publishing good practices and patterns.

### Publication policy

See [https://github.com/open-contracting/standard/issues/133](https://github.com/open-contracting/standard/issues/133) 

### Licensing



**ToDo**

"description": "A link to the license that applies to the data in this datapackage. [Open Definition Conformant](http://opendefinition.org/licenses/) licenses are strongly recommended. The canonical URI of the license should be used. Documents linked from this file may be under other license conditions. ",

### Release URIs

See [https://github.com/open-contracting/standard/issues/31](https://github.com/open-contracting/standard/issues/31) 

**File segmentation**

The release and record data package containers (in JSON and CSV) offer a way to provide **bulk access** to a collection of contracting process release and records. However, very large files can be difficult for users to download and process.

The following section provides suggested good practices which will assist users in accessing data. These are not requirements of the standard, but are based on experiences of maximising the number of users able to work with datasets with their existing hardware and software. 

#### Limits

When generating data packages for bulk download, apply the following limits:

* Unzipped OCDS data packages should not exceed 1Gb each;

* Zipped OCDS data packages should not exceed 10 Mb each;

* A single OCDS data package should contain a maximim of 250,000 awards or contracts; 

When a file is likely to exceed one of these limits, release or records should be split across multiple files. Dynamically generated bulk downloads do not have to apply these limits, though publishers should consider ways to advise users when a query is likely to generate a very large file. 

Segmenting files

When the suggested limits require publication of multiple files, publishers should consider ways to split data across available files. 

For releases, publishers may choose to:

1. Segment by **releaseDate - **placing all the releases from a given day, month or year in the same file;

2. Segment by **contracting process identifier **- placing all the releases related to a given set of contract process identifiers together in the same data package;

For records, publishers should segment either based on the first **releaseDate** associated with a contracting process, or by **contracting process identifier.**

Following these approaches will avoid release and records moving between files. 

Compression

OCDS data packages may be compressed in order to save on diskspace and bandwidth. 

If compressing data packages, publishers *should* use the zip file format. 

#### Serving files

Publishers should ensure that the web server providing access to bulk files correctly reports the [HTTP Last-Modified](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.29) header so that consuming applications only need to download updated files.

## Providing flat-file exports

## Supporting discovery

<span class="well">This section is in early draft form, and is subject to revision based on [feedback and discussion here](https://github.com/open-contracting/standard/issues/75). </span>

<span class="lead">There are many thousands of organisations who should be able to publish Open Contracting data. As a result, maintaining a central registry of all published data is impractical. Instead, OCDS proposes a common pattern for the discovery of Open Contracting data releases and records</span>

For the discovery of bulk datasets, and the location of any data feeds, we propose use of a data.json file.

For the discovery of individual releases and records, we propose use atom feeds.

### Dataset and feed discovery

Publishers should provide a data.json document describing the location of all of the bulk OCDS files available for download. 

This should follow the structure proposed by the [US Project Open Data](https://project-open-data.github.io/schema/) with:

* Each record containing a distribution block with at least one accessURL pointing to OCDS data.
* Each record containing 'open-contracting-data', and either 'open-contracting-release' or 'open-contracting-record' in the keyword array.
* accessLevel set appropriately

In addition, the data.json document may contain one or more records with the keyword 'open-contracting-feed' and either 'open-contracting-release' or 'open-contracting-record' and pointing via an accessURL in their distribution block to an atom feed document.

### Feeds

Publishers exposing individual records and releases, of regularly updated data packages in small sets, should provide one or more [atom feeds](http://en.wikipedia.org/wiki/Atom_%28standard%29) that index these, and provide an easy mechanism for users to discover recently published or updated release and records.

The link to the release or record should be provided via a <link> tag, and the updated date of the entry should reflect the updated date of that release or record. The <id> should reflect the release id for release, or the ocid for records.
    
The releaseTag should be contained within a <category> element of the feed. 

Feeds requiring pagination should follow the approach set out in [RFC 5005](https://tools.ietf.org/html/rfc5005#section-3).

### Well Known

Future implementations of OCDS will explore use of the <a href="http://tools.ietf.org/html/rfc5785">/.well-known/</a> protocol to declare a location for storing a data.json file. 

At present, such files can be hosted anywhere, and consuming applications pointed towards them manually. 

The data.json structure has been chosen to allow organisations following this approach to include tagged 'open-contracting-data' within their existing data discovery mechanisms, and given the availability of a plugin for the widely used CKAN which will also support exposure of data.json files. 


~~~~

#### Questions (Not part of documentation)

##### Data.json
Should we be using [JSON-LD DCAT instead](https://github.com/project-open-data/project-open-data.github.io/issues/23#issuecomment-17978611)? I opted for data.json as there are tools around to generate it, clear docs and schema, and assuming a JSON-LD context might be possible in future? 

Would also give instant adoption from Socrata, and US Government Agencies, plus a CKAN Extension is available which can output this, all leading to reasonable chance of data discovery. 


##### Atom category
Should we define a scheme for the atom category used to provide the releaseTag

Should we also define how to respond to querystrings against the atom (as per GData specification). E.g. allowing that feed.xml?category=contractAmendment should only return contract amendment tagged content. Or entry.updated-min=2014-10-31T00:00:00Z should only get releases updated after that date. 





ToDo: Turn into proper documentation:

Data providers need to be able to:

* Declare where their records files are found;
* Declare where their release files are found;

Publishing approaches will differ between:
 - Bulk file (dcat) or data.json 
 - Feed (atom)


tag: release
tag: record

Register the location of your data.json | feed.xml


### Permanence 