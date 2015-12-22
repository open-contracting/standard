

# Publication patterns

<span class="lead">The following section sets out a number of publication patterns that will increase the usability of data for users.</span>

## Basic

### Licensing

Publishing data under an open licenses is an important part of open contracting. Without this, restrictions on re-use may prevent many of the important [use cases](../../standard/use_cases) for open contracting information being realised.

A license statement sets out the permission that users have to access, use and re-use the data. This can take the form of a [Public Domain Dedication or Certification](http://creativecommons.org/publicdomain/) which transfers a dataset into the public domain, or re-asserts that there are no existing copyrights or database rights inherent in the dataset (which is the case for government datasets in some jurisdictions), or the application of a license which sets out the terms under which a dataset may be re-used.

We recommend the use of either a public domain dedication/certification, or an attribution only license.

* Public domain dedication – asserting no copyright, database rights, or contractual rights over the open contracting data. Examples include [Creative Commons’ public domain tools](http://creativecommons.org/publicdomain/). These licenses are useful for publishers who manage their own works or have the necessary rights to apply a public domain license to another person’s work. In addition, although attribution cannot be "enforced" under such licenses, we recommend that you actively acknowledge and give attribution to all sources, such as the data providers or any data aggregators. Public domain approaches are preferred for Open Contracting Datasets.
* Attribution-only open licenses – licenses that allow for use and reuse, with the only restriction being that attribution (credit) be given. A examples includes the [Creative Commons Attribution licenses 4.0](http://creativecommons.org/licenses/by/4.0/)

When using custom licenses, publishers are encouraged to check that they are [compliant with the Open Definition](http://opendefinition.org/licenses/).

In structured data file you can embed a link to the license in the ```license``` field of the release or record package. In individual CSV files or other models of publishing, it may not be possible to embed the license information. In these cases (and in the structured data case also) publishers should ensure that a clear statement is provided alongside files where they are provided for download linking to, and explaining, the license terms they are under. Particular attention should be paid to ensuring license information on any data catalogues where open contracting data is listed are accurate. 

### Publication policy

Publishing Open Contracting data involves making a number of choices about what data and documents to include and how to classify and categorise different items. To allow users to understand the choices that a publisher has made, a publisher should provide a public web page or document that details the decisions they have made concerning the issues listed below.

This document should also contain information about future plans for changes to the data and who to contact with enquiries about the data.

Publication policy pages should include information about:

* Who is responsible for providing this data - including appropriate contact details and locations of where to offer feedback.
* How the data is generated, and how often - for example, a brief summary describing the systems the data is generated from, how often the source data is updated, and any processes that operate between the source data and the published open contracting data and documents.
* Any exclusions from the data - such as information which is not disclosed for reasons of privacy and security. This may describe the fields which are excluded for a selection of records, and/or the policy applied to decide if any information should be withheld from a public OCDS release. 
* Any custom code lists used - or custom codes added to existing codelists. 
* Future development plans - brief notes on the future plans of the publisher to improve their data.

Publishers may also wish to apply for, and include the results of, an [Open Data Certificate](https://certificates.theodi.org/), on their publication policy pages. 

### Flat CSV file options

The [serialization section](../../key_concepts/serialization/#flat-csv-formats) provides information on publishing data as flat CSV files.

* * * *

## Intermediate

### Release and record URIs

To achieve [3 and 4 ☆](../publication_levels) ODCS publication, publishers should provide data in files following the full OCDS schema, and either with releases and records provided in bulk (3 ☆), or with each release at it's own unique URI (4 ☆). 

<!--ToDo: Work up examples of this in future-->

### Provide full records

A basic OCDS record can list the releases related to a given contracting process. However, a full record will provide a compiled release, showing the current state of the contracting process.  

### User-friendly publication

The release and record data package containers (in JSON and CSV) offer a way to provide **bulk access** to a collection of contracting process release and records. However, very large files can be difficult for users to download and process. The following section provides suggested good practices which will assist users in accessing data. These are not requirements of the standard, but are based on experiences of maximising the number of users able to work with datasets with their existing hardware and software.

#### File size limits

When generating data packages for bulk download, apply the following limits:

* Unzipped OCDS data packages should not exceed 1Gb each;
* Zipped OCDS data packages should not exceed 10 Mb each;
* A single OCDS data package should contain a maximim of 250,000 awards or contracts; 

When a file is likely to exceed one of these limits, release or records should be split across multiple files. Dynamically generated bulk downloads do not have to apply these limits, though publishers should consider ways to advise users when a query is likely to generate a very large file. 

#### Segmenting files

When the suggested limits require publication of multiple files, publishers should consider ways to split data across available files. 

For releases, publishers may choose to:

1. Segment by **releaseDate - **placing all the releases from a given day, month or year in the same file;
1. Segment by **contracting process identifier **- placing all the releases related to a given set of contract process identifiers together in the same data package;

For records, publishers should segment either based on the first **releaseDate** associated with a contracting process, or by **contracting process identifier.**

Following these approaches will avoid release and records moving between files. 

#### Compression

OCDS data packages may be compressed in order to save on diskspace and bandwidth. 

If compressing data packages, publishers *should* use the zip file format.

#### Serving files

Publishers should ensure that the web server providing access to bulk files correctly reports the [HTTP Last-Modified](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.29) header so that consuming applications only need to download updated files.


## Advanced

### Supporting discovery

There are many thousands of organisations who should be able to publish Open Contracting data. As a result, maintaining a central registry of all published data is impractical. Instead, OCDS proposes a common pattern for the discovery of Open Contracting data releases and records.

For the discovery of bulk datasets, and the location of any data feeds, we propose use of a data.json file.

For the discovery of individual releases and records, we propose use atom feeds.

#### Dataset and feed discovery

Publishers should provide a data.json document describing the location of all of the bulk OCDS files available for download. 

This should follow the structure proposed by the [US Project Open Data](https://project-open-data.github.io/schema/) with:

* Each record containing a distribution block with at least one accessURL pointing to OCDS data.
* Each record containing 'open-contracting-data', and either 'open-contracting-release' or 'open-contracting-record' in the keyword array.
* accessLevel set appropriately

In addition, the data.json document may contain one or more records with the keyword 'open-contracting-feed' and either 'open-contracting-release' or 'open-contracting-record' and pointing via an accessURL in their distribution block to an atom feed document.

#### Feeds

Publishers exposing individual records and releases, of regularly updated data packages in small sets, should provide one or more [atom feeds](http://en.wikipedia.org/wiki/Atom_%28standard%29) that index these, and provide an easy mechanism for users to discover recently published or updated release and records.

The link to the release or record should be provided via a <link> tag, and the updated date of the entry should reflect the updated date of that release or record. The <id> should reflect the release id for release, or the ocid for records.
    
The release.tag should be contained within a <category> element of the feed. 

Feeds requiring pagination should follow the approach set out in [RFC 5005](https://tools.ietf.org/html/rfc5005#section-3).

#### Well Known

Future implementations of OCDS will explore use of the <a href="http://tools.ietf.org/html/rfc5785">/.well-known/</a> protocol to declare a location for storing a data.json file. 

At present, such files can be hosted anywhere, and consuming applications pointed towards them manually. 

The data.json structure has been chosen to allow organisations following this approach to include tagged 'open-contracting-data' within their existing data discovery mechanisms, and given the availability of a plugin for the widely used CKAN which will also support exposure of data.json files. 

### Linking data

For 5 ☆ publication of OCDS data, publishers should seek to use URIs in their datasets, linking to other machine-readable data sources at an entity-by-entity level.
