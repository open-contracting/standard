# Data files and APIs

```{tip}
Did you arrive at this page looking to [download OCDS data](https://data.open-contracting.org)? Check out the [OCP Data Registry](https://data.open-contracting.org).
```

Different users have different needs when it comes to accessing OCDS data. A common need is to automate the download of all the OCDS data, in some form.

The W3C [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/#MultipleFormats) describe ways to increase the number of users, tools and applications that can access and make effective use of a given dataset.

With respect to your OCDS publication, which best practices are most important will depend on the particular needs of your users, but you are encouraged to consider:

* **[Bulk downloads](#bulk-downloads)** - packaging together multiple releases or multiple records in one or more files for users to download and import into local tools. ([Best Practice 17](https://www.w3.org/TR/dwbp/#BulkAccess))
* **[Individual release and records](#individual-releases-and-records)** - providing a URL at which each release or record can be accessed ([Best Practice 10](https://www.w3.org/TR/dwbp/#identifiersWithinDatasets)).
* **[API access](#api-access)** - enabling interactive access to your data. ([Best Practice 23](https://www.w3.org/TR/dwbp/#useanAPI))
* **[CSV and spreadsheet serializations](#csv-and-spreadsheet-serializations)** - providing multiple releases or compiled records for download, enabling users to work with data directly in spreadsheet software or other tools. ([Best Practice 14](https://www.w3.org/TR/dwbp/#MultipleFormats))

To meet the [basic criteria for data quality](../publish/quality.md#basic-criteria), it ought to be possible for a user to automate the download of all the data, either using an HTML page listing bulk download URLs, or using only machine-readable data as input.

## Bulk downloads

The [release package](../../schema/release_package) and [record package](../../schema/record_package) can provide **bulk access** to releases and records, respectively.

However, very large files can be difficult for users to download and process. The following section suggests good practices to assist users in accessing data. These are not requirements of the standard, but are based on experiences of maximizing the number of users able to work with datasets with their existing hardware and software.

### File size limits

When generating packages for bulk download, apply the following limits:

* Unzipped OCDS packages ought to not exceed 1 Gb each.
* Zipped OCDS packages ought to not exceed 10 Mb each.
* A single OCDS package ought to contain a maximum of 250,000 awards or contracts.

When a file is likely to exceed one of these limits, release or records ought to be split across multiple files. Dynamically generated bulk downloads do not have to apply these limits, though publishers ought to consider ways to advise users when a query is likely to generate a very large file.

### Segmenting files

When the suggested limits entail publication of multiple files, publishers ought to consider ways to split data across available files.

For releases, publishers can:

* Segment by **release date** - placing all the releases from a given day, month or year in the same file.
* Segment by **open contracting process identifier** - placing all the releases related to a given set of process identifiers together in the same package.

For records, publishers can segment by the first **release date** associated with a contracting (or planning) process, or by **open contracting process identifier.**

Following these approaches will avoid releases and records 'jumping' between files when the bulk files are updated.

### Compression

OCDS packages can be compressed in order to save on disk space and bandwidth.

When compressing packages, use ZIP or GZIP, as these are commonly available, often without additional software. Avoid RAR, which requires additional software.

### Serving files

The web server providing access to bulk files ought to report the [HTTP Last-Modified](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.29) header correctly, so that consuming applications only need to download updated files.

Also, publishers ought to ensure that the data export is completed successfully, i.e. that no files were truncated.

## Individual releases and records

Each release and record can be made accessible at a permanent URL. This can be achieved by:

* Archiving a ‘single-release’ release package for each release to a web accessible file system as it is created, and then regularly merging these releases into records in the same file system. One approach might be to have a directory for each ocid and to put the releases and the record related to that process in that directory.
* Providing access to each release and the merged records via an API.

Publishers ought to consider how to [ensure that URLs remain stable](https://www.w3.org/Provider/Style/URI.html), even across a change of systems.

## API access

API design is a deep topic. As such, the following guidance is not intended to be comprehensive or prescriptive. Wherever possible, publishers ought to carry out their own user research.

### Discoverability

Ensure that the API endpoints and documentation are discoverable. For example, add a link to the footer of your procurement portal, and list the API endpoints in your open data portal.

### Documentation

Provide API documentation, with at least the lists of endpoints, methods and parameters. Many publishers use [Swagger](https://swagger.io) to document their APIs.

### Access control and rate limiting

Avoid adding access controls (like user registration or API keys), in order to maximize the ease of access to the publication.

If access controls are necessary, do not use access tokens that need to be refreshed regularly. For example, every two hours is too frequent.

If the API implements rate limits (throttling):

* Document the rate limits in the API documentation ([example](https://developer.twitter.com/en/docs/twitter-api/rate-limits)).
* When a user exceeds a rate limit, return a [HTTP 429 “Too Many Requests” response status code,](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) and set the [Retry-After](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) HTTP header to indicate how long to wait before making a new request.

### Completeness

Ensure that all the OCDS data can be accessed via the API. For example, if the data source is an Elasticsearch index, either implement pagination using the [search_after](https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html#search-after) parameter, or ensure that [index.max_result_window](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html#index-max-result-window) is large enough to return all results.

### Endpoints

Your design choices in this area ought to be informed by user research. That said, you can consider providing:

* A release package endpoint with [pagination](#pagination), for retrieving multiple releases without providing a specific OCID and release ID
* A record package endpoint with pagination, for retrieving multiple records without providing a specific OCID
* A release endpoint, for retrieving an individual release by OCID and release ID
* A record endpoint, for retrieving an individual record by OCID

For package endpoints, you can also provide filtering and ordering options. In particular, consider date filters and/or a reverse chronological order option, so that users can retrieve only new or updated data.

If you choose to provide endpoints for retrieving individual records and/or releases but **not** endpoints for paginating through records and/or releases, then you need to provide a machine-readable list of OCIDs and/or release IDs. Otherwise, it will not be possible to automate the download of all the data, which is a [basic criterion for data quality](../publish/quality.md#basic-criteria).

### Response format

* Put the release, record or package at the top-level of the JSON data. For example, do not embed it under a results array.
* Use a JSON library instead of implementing JSON serialization yourself. This also guarantees that the encoding is UTF-8.
* Remove NULL characters (\u0000) from the JSON response. These characters cannot be imported by users into some SQL databases.
* If results cannot be returned, use an appropriate HTTP error code (400-599); do not return a JSON object with an error message and a 200 HTTP status code. That said, if a search request returns no results, it is appropriate to use a 200 HTTP status code, with an empty result set.

### Pagination

To support pagination, the top-level `links` object in release packages and record packages has two fields:

* `next`: A URL to the next sequential package
* `prev`: A URL to the previous sequential package

Ensure that the API's performance does not degrade on deep pages. For example, if the data source is a SQL database, use the [seek method](https://developer.wordpress.com/2014/02/14/an-efficient-alternative-to-paging-with-sql-offsets/) (also known as keyset pagination) rather than an [OFFSET clause](https://www.postgresql.org/docs/current/queries-limit.html).

When using the **seek method**, you can use _either_ of these query string parameters to construct the `next` and/or `prev` URLs:

* `cursor=CURSOR`, to return a page of results that are positioned after the cursor, in sequential order. The cursor might be a row ID or similar.
* `since=TIMESTAMP`, to return a page of results that are modified after the `since` timestamp, in chronological order.

When using the **offset method**, you can use _either_ of these query string parameters to construct the `next` and/or `prev` URLs:

* `offset=NUMBER`, to return a page of results that are positioned after the `offset` number, in sequential order. Use `offset=0` for the first offset.
* `page=NUMBER`, to return a page of results that are positioned at the `page` number, in sequential order. Use `page=1` for the first page, not `page=0`.

In either case:

* Use `limit=NUMBER`, to limit the number of results returned on each page.
* Include the total number of results across all pages.

In addition to performance reasons, the seek method is preferred to the offset method when results are ordered in reverse chronology, because:

* A given page won't return the same results over time. `page=1` will return different results today, next week, and next year.
* Users can receive duplicate results while paginating. For example, if a new release is published to page 1 while users are paginating, then the result at the bottom of each page will be moved to the top of the following page.
* It is harder for users to synchronize with the API. With the seek method, users can retrieve new results by submitting the timestamp or ID of their last request. With `page`, users need to determine which results are new or old.

### Monitoring

Set up error monitoring, so that if a request causes an HTTP 500 Internal Server Error, you can investigate.

## CSV and spreadsheet serializations

The [serialization](serialization) page provides details of how to generate 'flat' versions of OCDS data for use in spreadsheet software.

The same principles discussed for bulk files above ought to be applied to CSV or Excel downloads of data.
