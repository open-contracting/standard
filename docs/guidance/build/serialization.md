# Serialization

The Open Contracting Data Standard provides a **structured data model** for capturing in-depth information about all stages of the contracting process.

The current canonical version of this data model is provided by a **[JSON Schema](../../schema/release)** which describes field names, field definitions and structures for the data. The compliance of data with the Open Contracting Data Standard will be assessed against this schema.

However, there are many use cases where publishers and users will want to work with data serialized in other formats. For this reason, the current version of OCDS supports a number of **secondary serializations** which are based on the canonical schema. These are not currently official components of the standard, but are designed to support publishers in providing accessible data to a range of different users.

## JSON 

JSON stands for JavaScript Object Notation, and is a format widely used for the exchange of data on the web. The JSON schema language provides validation tools for working with JSON data.

OCDS data needs to follow the I-JSON (Internet JSON) specification in [RFC7493](https://tools.ietf.org/html/rfc7493), according to which JSON text needs to be encoded using [UTF-8](https://en.wikipedia.org/wiki/UTF-8), and which introduces a number of requirements for numbers, objects and dates.

### Generating JSON

Most programming languages provide tools for output data as JSON. 

[A range of tools](http://json-schema.org/implementations.html) are available for working with [JSON-Schema](http://json-schema.org/), including validation and form generation tools. 

### Consuming JSON

Most programming languages provide tools for reading JSON.

A number of [JSON native databases](http://en.wikipedia.org/wiki/NoSQL) are available for working directly with large collections of JSON documents, and command line tools such as [jq](http://stedolan.github.io/jq/) support advanced query and data retrieval with JSON files.

There are also a range of generic tools which can convert JSON into flat CSV structures, including:

* [JSON -> CSV](http://konklone.io/json/) - online tool for converting small documents.
* [Open Refine](http://openrefine.org/) - desktop tool that can handle large documents, and supports advanced data manipulation.

## CSV 

JSON is based on a tree structure, with data elements nested inside one another. However, many people are more familiar working with tabular data, made up of columns and rows. There is no easy way to represent structured data in a single table. However, we propose two models for publishers to adopt. 

* **Simplified single table** - for cases where there are no one-to-many relationships in the data (e.g. each tender has only one award and contract, and each has only one line-item).
* **Multi-table** - where more advanced structures are needed, but where it is desirable to be able to work with data in spreadsheet-style layouts

In each case, fields are identified in CSV headers by their [JSON Pointer](http://tools.ietf.org/html/rfc6901). For example:

**JSON**

```{eval-rst}
.. jsoninclude:: ../../examples/serialization-flat.json
   :jsonpointer: 
   :expand: releases, tender, items

```

**CSV**

```{eval-rst}
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../examples/serialization-flat.csv
   
```

[Beta open source tooling](http://flatten-tool.readthedocs.io/en/latest/usage-ocds/) exists for generating flat CSV OCDS templates, and converting in both directions between JSON spreadsheets following these templates. The OCDS Data Review Tool incorporates this tooling and will offer to convert files uploaded to it.

### Simplified single table 

It is possible to represent a full release in a single flat CSV row by using full JSON pointers for each field as the headings. 

This approach is generally only appropriate for data without one-to-many relationships (for example, only one item per tender, and one award and contract for each tender process).

It is, however, theoretically possible to represent a full release in a single flat CSV row by using full JSON pointers for each field as the headings. For arrays, this involves adding the array index to the path, such as `tender/item/0/id` and `tender/item/1/id` as separate columns to represent each of the items. 

For example, to represent a tender release with two items, the CSV file would include:

```{eval-rst}
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../examples/serialization-flat-two-items.csv
   
```

The JSON equivalent of this would be:

```{eval-rst}
.. jsoninclude:: ../../examples/serialization-flat-two-items.json
   :jsonpointer: 
   :expand: releases, tender, items

```

Whilst this allows complex data to be expressed in flat CSV, users will need to rebuild the structure in order to analyze the data.

Instead, data with a one-to-many relationship can be represented using a multi-table serialization. 

```{eval-rst}
.. admonition:: CSV encoding
   :class: note

   OCDS CSV files ought to be encoded in either UTF-8 or Windows-1252.

```

### Multi-table

The multi-table serialization separates  objects with many to one relationships (i.e. arrays) into their own tables. 

Multiple tables can be packaged together as the tabs of an Excel spreadsheet, or in a collection of CSV files.  

An example multi-table template can be found [in the sample data repository](https://github.com/open-contracting/sample-data/tree/main/flat-template).

For further information on multi-table serializations please see the [flatten tool documentation](http://flatten-tool.readthedocs.io/en/latest/).

## Packaging files with metadata

Whatever serialization is used for Open Contracting Data, a single file can contain one or more release and records.

The release package and record package schemas describe the key metadata that ought to be supplied for any file providing Open Contracting Data. This includes the `publishedDate`, `publisher`, `uri` for accessing the file, and the licensing details for the file.
