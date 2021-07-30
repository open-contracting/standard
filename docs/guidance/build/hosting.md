# Data files and APIs

Different users have different needs when it comes to accessing OCDS data. It also needs to be possible to automate the download of all the OCDS data, in some form.

[Data on the Web Best Practices](https://www.w3.org/TR/dwbp/#MultipleFormats) suggests that "Data should be available in multiple data formats" in order to increases the number of different users, tools and applications that can process the data.

Which formats are most important will depend on the priority use cases for each OCDS implementation, but you are encouraged to consider:

* **Bulk downloads** - packaging together multiple releases or multiple records in one or more files for users to download and import into local tools.
* **Individual release and record downloads** - providing a URI at which each release or record can be obtained.
* **CSV and spreadsheet serializations** - providing multiple releases or compiled records for download, enabling users to work with data directly in spreadsheet software or other tools. 
* **API access** - enabling interactive access to your data.

## Bulk downloads

The release package and record package can provide **bulk access** to releases and records, respectively.

However, very large files can be difficult for users to download and process. The following section provides suggested good practices which will assist users in accessing data. These are not requirements of the standard, but are based on experiences of maximizing the number of users able to work with datasets with their existing hardware and software.

### File size limits

When generating packages for bulk download, apply the following limits:

* Unzipped OCDS packages ought to not exceed 1Gb each;
* Zipped OCDS packages ought to not exceed 10 Mb each;
* A single OCDS package ought to contain a maximum of 250,000 awards or contracts; 

When a file is likely to exceed one of these limits, release or records ought to be split across multiple files. Dynamically generated bulk downloads do not have to apply these limits, though publishers ought to consider ways to advise users when a query is likely to generate a very large file. 

### Segmenting files

When the suggested limits entail publication of multiple files, publishers ought to consider ways to split data across available files. 

For releases, publishers can:

1. Segment by **release date** - placing all the releases from a given day, month or year in the same file;
1. Segment by **open contracting process identifier** - placing all the releases related to a given set of process identifiers together in the same package;

For records, publishers can segment by the first **release date** associated with a contracting process, or by **open contracting process identifier.**

Following these approaches will avoid release and records 'jumping' between files when the bulk files are updated. 

### Compression

OCDS packages can be compressed in order to save on disk space and bandwidth. 

If compressing packages, publishers ought to use the ZIP file format.

### Serving files

The web server providing access to bulk files ought to correctly report the [HTTP Last-Modified](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.29) header so that consuming applications only need to download updated files.

## Individual releases and records

Each release and record can be made accessible at a permanent URI. This can be achieved by:

(a) Archiving a single-release release package for each release to a web accessible file system as it is created, and then regularly merging these releases to compile individual record files in the same file system. One approach might be to have a folder for each `ocid` and to place the releases and record related to that process into that folder. 

(b) Providing access to releases and records through an API.

Note that the second approach needs the API to maintain a full revision history of each contracting process, so that releases from each stage of a contracting process can be provided. 

Publishers ought to consider how to [ensure URIs can remain stable](https://www.w3.org/Provider/Style/URI.html), even across a change of systems.

## Flattened serializations

The [serialization](serialization) page provides details of how to generate 'flat' versions of OCDS data for use in spreadsheet software.

The same principles discussed for bulk files above ought to be applied to CSV or Excel downloads of data.
