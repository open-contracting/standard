[TOC]

# Serializations

<span class="lead">The Open Contracting Data Standard provides a **structured data model** for capturing in-depth information about all stages of the contracting process.</span>

<span class="lead">The current canonical version of this data model is provided by a **[JSON Schema](../../schema/release)** which describes field names, field definitions and structures for the data. The compliance of data with the Open Contracting Data Standard will be assessed against this schema.</span>

However, there are many use cases where publishers and users will want to work with data serialized in other formats. For this reason, the current version of OCDS supports a number of **secondary serializations** which are based on the canonical schema.

## JSON

JSON stands for Javascript Object Notation, and is a format widely used for the exchange of data on the web. The JSON schema language provides validation tools for working with JSON data.

### Generating JSON
Most programming languages provide tools for output data as JSON. 

The [OCDS Mapper](https://github.com/open-contracting/mapper) tool can convert from flat files to structured OCDS data based on a mapping template. 

[A range of tools](http://json-schema.org/implementations.html) are available for working with [JSON-Schema](http://json-schema.org/), including validation and form generation tools. 

### Consuming JSON
Most programming languages provide tools for reading JSON.

A number of [JSON native databases](http://en.wikipedia.org/wiki/NoSQL) are available for working directly with large collections of JSON documents, and command line tools such as [jq](http://stedolan.github.io/jq/) support advanced query and data retrieval with JSON files.

There are also a range of generic tools which can convert JSON into flat structures, including:

* [JSON -> CSV](http://konklone.io/json/) - online tool for converting small documents.
* [Open Refine](http://openrefine.org/) - desktop tool that can handle large documents, and supports advanced data manipulation.

## Flat formats

JSON is based on a tree structure, with data elements nested inside one another. However, many people are more familiar working with tabular data, made up of columns and rows. There is no easy way to represent structured data in a single table. However, we propose two models for publishers to adopt. 

* **Simplified single table** - for cases where there are no one-to-many relationships in the data (e.g. each tender has only one award and contract, and each has only one line-item).
* **Multi-table** - where more advanced structures are required, but where it is desirable to be able to work with data in spreadsheet-style layouts

In each case, fields are identified by the path to their JSON equivalent. For example:

<div class="include-json" data-src="standard/example/serialization-flat.json"></div>

would be rendered in a flat format as:

<div class="include-csv" data-src="standard/example/serialization-flat.csv" data-table-class="table table-striped schema-table"></div>

A set of prototype tools for generating flat OCDS templates are [available on GitHub](https://github.com/open-contracting/flattening-ocds).

### Simplified single table 

In cases where there are no one-to-many relationships within a release, a release can be represented in a single tabular row and stored as CSV. 

Such cases are likely to be rare. Flat data models based upon repeated lines to handle one-to-many relationships should be avoided. 

### Multi-table

In cases where there are one-to-many relationships within a release, it will be necessary to split the data into multiple tables. A set of tables can be presented as tabs in a spreadsheet, providing a familiar tool for data entry and analysis, or can be contained within a [data package](http://dataprotocols.org/data-packages/). 

By including identifiers in the sub-tables that point to the ocid, releaseID and the id of the parent entity of the sub-table item, it is possible to:

* Use [database joins](http://en.wikipedia.org/wiki/Join_%28SQL%29) or spreadsheet Vlookup ([Excel](http://office.microsoft.com/en-gb/excel-help/vlookup-HP005209335.aspx), [Google Docs](https://support.google.com/docs/answer/3093318?hl=en), [Open Office](https://wiki.openoffice.org/wiki/Documentation/How_Tos/Calc:_VLOOKUP_function)) to analyse the data;

* Re-construct a structured data tree (e.g. in JSON) from the tabular data;

The JSON re-uses common definitions regularly (e.g. for items, classifications, organizations etc.) and applications following the multi-table approach should generally seek to collect together items of each type in their own table, rather than creating different tables for each kind of item, organization and so-on.

A worked example of a multi-table template is shown below.

NOTE: This example is based on an earlier version of the schema, and does not show all sub-tables. It should be understood as illustrative only.



<div class="tabbable">
<ul class="nav nav-tabs">
  <li class="active"><a href="#release" data-toggle="tab">release</a></li>
  <li><a href="#award" data-toggle="tab">award</a></li>
  <li><a href="#contract" data-toggle="tab">contract</a></li>
  <li><a href="#item" data-toggle="tab">item</a></li>
  <li><a href="#organization" data-toggle="tab">organization</a></li>
  <li><a href="#milestone" data-toggle="tab">milestone</a></li>
  <li><a href="#attachment" data-toggle="tab">attachment</a></li>  
</ul>
<div class="tab-content">
    
<div class="tab-pane active" id="release">
    
<div class="include-csv" data-src="standard/example/flat/release.csv" data-table-class="table table-striped schema-table"></div>

</div>
<div class="tab-pane" id="award">

<div class="include-csv" data-src="standard/example/flat/award.csv" data-table-class="table table-striped schema-table"></div>

</div>
<div class="tab-pane" id="contract">
<div class="include-csv" data-src="standard/example/flat/contract.csv" data-table-class="table table-striped schema-table"></div>
</div>
<div class="tab-pane" id="item">
<div class="include-csv" data-src="standard/example/flat/item.csv" data-table-class="table table-striped schema-table"></div>
</div>
<div class="tab-pane" id="organization">
<div class="include-csv" data-src="standard/example/flat/organization.csv" data-table-class="table table-striped schema-table"></div>
</div>
<div class="tab-pane" id="milestone">
<div class="include-csv" data-src="standard/example/flat/milestone.csv" data-table-class="table table-striped schema-table"></div>
</div>
<div class="tab-pane" id="attachment">
<div class="include-csv" data-src="standard/example/flat/attachment.csv" data-table-class="table table-striped schema-table"></div>
</div>
</div>
</div>


### Data packages

Whatever serialisation is used for Open Contracting Data, a single file may contain one or more release and records.

The release and record data package schemas describe the key meta-data that must be supplied for any file providing Open Contracting Data. This includes the publishedDate, publisher, uri for accessing the file, and the licensing details for the file.