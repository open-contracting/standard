# Data files, APIs and discovery

Different users have different needs when it comes to accessing OCDS data. 

[Data on the Web Best Practice #15](https://www.w3.org/TR/dwbp/#dataFormats) suggests that "Data should be available in multiple data formats" in order to increases the number of different users, tools and applications that can process the data.

Which formats are most important will depend on the priority use cases for each OCDS implementation, but you should consider:

* **Bulk downloads** - packaging together multiple releases or multiple records in one or more files for users to download and import into local tools.
* **Individual release and record downloads** - providing a URI at which each release or record can be obtained. This is crucial for 4 ☆ data publication.
* **CSV and Spreadsheet serializations** - providing multiple releases or compiled records for download, enabling users to work with data directly in spreadsheet software or other tools. 
* **API access** - enabling interactive access to your data. OCDS does not currently provide a standard for constructing APIs, but [potential approaches can be discussed with the community here](https://github.com/open-contracting/standard/issues/290).

## Bulk downloads

The release and record data package containers (in JSON and CSV) offer a way to provide **bulk access** to a collection of contracting process release and records. 

However, very large files can be difficult for users to download and process. The following section provides suggested good practices which will assist users in accessing data. These are not requirements of the standard, but are based on experiences of maximizing the number of users able to work with datasets with their existing hardware and software.

### File size limits

When generating data packages for bulk download, apply the following limits:

* Unzipped OCDS data packages should not exceed 1Gb each;
* Zipped OCDS data packages should not exceed 10 Mb each;
* A single OCDS data package should contain a maximum of 250,000 awards or contracts; 

When a file is likely to exceed one of these limits, release or records should be split across multiple files. Dynamically generated bulk downloads do not have to apply these limits, though publishers should consider ways to advise users when a query is likely to generate a very large file. 

### Segmenting files

When the suggested limits require publication of multiple files, publishers should consider ways to split data across available files. 

For releases, publishers may choose to:

1. Segment by **releaseDate** - placing all the releases from a given day, month or year in the same file;
1. Segment by **contracting process identifier** - placing all the releases related to a given set of contract process identifiers together in the same data package;

For records, publishers should segment either based on the first **releaseDate** associated with a contracting process, or by **contracting process identifier.**

Following these approaches will avoid release and records 'jumping' between files when the bulk files are updated. 

### Compression

OCDS data packages may be compressed in order to save on disk space and bandwidth. 

If compressing data packages, publishers *should* use the zip file format.

### Serving files

Publishers should ensure that the web server providing access to bulk files correctly reports the [HTTP Last-Modified](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.29) header so that consuming applications only need to download updated files.

## Individual releases and records

To achieve [4 ☆](levels.md) OCDS publication requires each release and record to be accessible at a permanent URI. This may be achieved by:

(a) Archiving a single-release release package for each release to a web accessible file system as it is created, and then regularly merging these releases to compile individual record files in the same file system. One approach may be to have a folder for each ```ocid``` and to place the releases and record related to that process into that folder. 

(b) Providing access to releases and records through an API.

Note that the second approach will require the API to maintain a full revision history of each contracting process, so that releases from each stage of a contracting process can be provided. 

Publishers should consider how to [ensure URIs can remain stable](https://www.w3.org/Provider/Style/URI.html), even across a change of systems.

## Flattened serializations

The [serialization](../../serialization/) page provides details of how to generate 'flat' versions of OCDS data for use in spreadsheet software.

The same principles discussed for bulk files above should be applied to CSV or Excel downloads of data.


## Discovery and APIs

There are many thousands of organizations who should be able to publish Open Contracting data. As a result, maintaining a central registry of all published data is impractical. Instead, OCDS proposes a common pattern for the discovery of Open Contracting data releases and records.

For the discovery of bulk datasets, and the location of any data feeds, we propose use of a data.json file.

For the discovery of individual releases and records, we propose use atom feeds.

There is a [community discussion here](https://github.com/open-contracting/standard/issues/290) on whether OCDS should include a proposed API standard in future iterations.

### Dataset and feed discovery

Publishers should provide a data.json document describing the location of all of the bulk OCDS files available for download. 

This should follow the structure proposed by the [US Project Open Data](https://project-open-data.github.io/schema/) with:

* Each record containing a distribution block with at least one accessURL pointing to OCDS data.
* Each record containing 'open-contracting-data', and either 'open-contracting-release' or 'open-contracting-record' in the keyword array.
* accessLevel set appropriately

In addition, the data.json document may contain one or more records with the keyword 'open-contracting-feed' and either 'open-contracting-release' or 'open-contracting-record' and pointing via an accessURL in their distribution block to an atom feed document.

### Feeds

Publishers exposing individual records and releases, of regularly updated data packages in small sets, should provide one or more [atom feeds](http://en.wikipedia.org/wiki/Atom_%28standard%29) that index these, and provide an easy mechanism for users to discover recently published or updated release and records.

The link to the release or record should be provided via a ```<link>``` tag, and the updated date of the entry should reflect the updated date of that release or record. The ```<id>``` should reflect the release id for release, or the ocid for records.
    
The release.tag should be contained within an ```<category>``` element of the feed. 

Feeds requiring pagination should follow the approach set out in [RFC 5005](https://tools.ietf.org/html/rfc5005#section-3).

### Well Known

Future implementations of OCDS will explore use of the <a href="http://tools.ietf.org/html/rfc5785">/.well-known/</a> protocol to declare a location for storing a data.json file. 

At present, such files can be hosted anywhere, and consuming applications pointed towards them manually. 

The data.json structure has been chosen to allow organizations following this approach to include tagged 'open-contracting-data' within their existing data discovery mechanisms, and given the availability of a plugin for the widely used CKAN which will also support exposure of data.json files. 

## Linking data

For 5 ☆ publication of OCDS data, publishers should seek to use URIs in their datasets, linking to other machine-readable data sources at an entity-by-entity level.
