# Build

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/NSiIIH2-GJM" title="Getting your data ready to publish" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This phase is about creating a new IT system, or updating an existing IT system, to implement your [mapping](map) and publish OCDS data.

Alternatively, if you don't have the capacity to create or update an IT system, you can consider reusing an existing [data collection tool](build/data_collection_tools). If you're reusing an existing tool, this phase is about customizing that tool to meet your needs and working out how to combine and publish your data. The [Data Support Team](../support/index) can help you to consider options for collecting, combining and publishing data.

```{toctree}
:hidden:

build/data_collection_tools
```

As you complete this phase, you can:

* Fill in the *Technical options for implementing OCDS* sub-section of your [Technical Assessment Template](map.md#identify-your-data-sources).

## Register an OCID prefix

In OCDS, the contracting process identifier (`ocid`) uniquely identifies a contracting process. As a publisher, you will assign a unique `ocid` to each contracting process.

To ensure that your `ocid`s do not conflict with those of another publisher, you need to register an ocid prefix.

**Action**: Email [data@open-contracting.org](mailto:data@open-contracting.org) to request an OCID prefix. Provide the name of the publishing organization and the email address of a contact person at this organization.

**Resource**: To learn more about the `ocid` and its prefixes, refer to the [identifiers](../../schema/identifiers) reference.

```{note}
All registered OCID prefixes are accessible as a [web page](https://docs.google.com/spreadsheets/d/1E5ZVhc8VhGOakCq4GegvkyFYT974QQb-sSjvOfaxH7s/pubhtml?gid=506986894&single=true&widget=true) or [CSV file](https://docs.google.com/spreadsheets/d/e/2PACX-1vQP8EwbUhsfxN7Fx7vX3mTA6Y8CXyGi04bHUepdcfxvM6VRVP9f5BWAYEG6MPbnJjWJp-La81DgG8wx/pub?gid=506986894&single=true&output=csv).
```

## Determine your system architecture

There are many ways to extract data from data sources, combine it, map it to OCDS, and publish it. The [system architectures](build/system_architectures) guidance page describes some possible approaches.

Your choice of architecture can determine how frequently your data is updated, whether you can publish a change history and the access methods available to your users. **Remember to check that your chosen architecture meets the needs you identified in the design stage.**

```{toctree}
:hidden:

build/system_architectures
build/change_history
build/easy_releases
build/merging
```

**Resource:** [Technical case studies: OCDS implementation insights report](https://www.open-contracting.org/resources/technical-case-studies-ocds-implementation-insights/) provides insights into the technical choices made in OCDS implementations in Paraguay, Zambia, Colombia, Moldova and Argentina's Road Agency Vialidad.

### Decide how to combine spreadsheet data

If you aren't creating or updating an IT system, but are instead collecting data from different individuals, departments or agencies using spreadsheets, then this step is about working out how to combine your data into a single file for publication. Combining your data makes it easier for users to analyze the whole dataset.

If you plan to publish your data infrequently, you only have a small number of spreadsheets and your spreadsheets have identical headers, then simply copy-pasting the data into a single file for publication may be the easiest method.

Otherwise, you can consider the following methods:

* If you're comfortable using a command-line interface, you can use CSV Kit's [`in2csv` command](https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html) to convert each sheet of a spreadsheet into a CSV file, and then use the [`csvstack` command](https://csvkit.readthedocs.io/en/latest/scripts/csvstack.html) to combine sets of CSV files with identical headers into single CSV files.
* If you're comfortable writing Visual Basic for Applications (VBA) or Google Apps Script code, you can write a macro for Microsoft Excel or Google Sheets to combine your data into a single file.
* If you're comfortable using spreadsheet formulae, you can use Google Sheet's [IMPORTRANGE](https://support.google.com/docs/answer/3093340?hl=en) or [QUERY](https://support.google.com/docs/answer/3093343?hl=en) functions to import data from multiple spreadsheets to a single sheet.
* If you aren't comfortable with the above methods, you can consider using a spreadsheet add-on for combining data from multiple sheets.

## Establish your publication formats and access methods

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/njw7H4UKPsY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

OCDS data can be published in different formats and accessed using different methods.

It is best practice to provide data in multiple formats, so that as many users as possible can use the data without first having to transform it to their preferred format. In OCDS terms, this means [publishing both structured JSON data and tabular CSV or spreadsheet data](build/serialization).

Where resources allow, it is also best practice to provide multiple access methods for your data, so that both humans and machines can access it easily. In OCDS terms, this means [providing both bulk downloads and an API](build/hosting). The [OCDS pagination extension](https://extensions.open-contracting.org/en/extensions/pagination/master/) describes how to paginate OCDS data via an API.

**Remember to check that your chosen publication formats and access methods meet the needs you identified at the design stage.**

**Tool:** [Flatten-tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/) can be used to convert OCDS data between JSON and CSV/spreadsheet formats.

```{toctree}
:hidden:

build/serialization
build/hosting
```

## Build your data pipeline

Having determined your system architecture, it's time to implement it. This is one of the longest steps of implementing OCDS.

Whether your current infrastructure is low tech or high tech, we have tools and resources to help you publish OCDS. Depending on your [data sources](map.md#identify-your-data-sources) and system architecture, you might be able to reuse some of these OCDS tools:

```{note}
If you have any issues using OCDS tools, contact the [Data Support Team](../../support/index).
```

* If you are creating (or upgrading) an **electronic government procurement (e-GP) system** or open contracting data portal, refer to our [Guide to Defining OCDS Functional Requirements for e-GP Systems](https://www.open-contracting.org/resources/guide-defining-open-contracting-data-standard-functional-requirements-electronic-government-procurement-systems/).
* If your source data is in **CSV/Excel files**, you can rename the columns to match the JSON paths in OCDS (for example, `buyer/name`) and then [transform the CSV/Excel files to OCDS JSON](https://www.open-contracting.org/2016/08/08/open-contracting-data-structure-spreadsheets/) by using [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/), a command-line tool.
* If your source data is in **Excel files**, you can alternately transform Excel files to OCDS JSON by using the [Open Contracting Explorer](https://developmentgateway.org/expertise/open-contracting-procurement/), which includes a web interface and web API for users to access and explore the OCDS data. (This tool is authored by Development Gateway.)
* If your source data is in **SQL tables**, you can use [Kavure'i](https://gitlab.com/dncp-opendata/opendata-etl/-/blob/master/README_en.md) to transform it to OCDS. To use it, you write SQL queries to extract data from SQL tables, setting the columns for the query results to match the JSON paths in OCDS (for example, `buyer/name`). The query results are saved to CSV files, which are transformed to OCDS JSON using [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/). (Kavure'i is authored by Paraguay's Dirección Nacional de Contrataciones Públicas (DNCP).)
* To **make OCDS data available via an API**, you can use another component of [Kavure'i](https://gitlab.com/dncp-opendata/opendata-etl/-/blob/master/README_en.md) to load OCDS data into [ElasticSearch](https://www.elastic.co/), and then use [Pitogüé](https://gitlab.com/dncp-opendata/opendata-api-v3/blob/master/README_en.md) to make it available via an API. (Both tools are authored by Paraguay's Dirección Nacional de Contrataciones Públicas (DNCP).)
* If you intend to **publish [record packages](../../schema/record_package)**, [OCDS Merge](https://ocds-merge.readthedocs.io/en/latest/) is the best software library for creating OCDS [records](../../primer/releases_and_records). If you use the [Python](https://www.python.org/) programming language, you can use it directly. If not, you can use its [test cases](https://ocds-merge.readthedocs.io/en/latest/#test-cases) to test your implementation of the [merge routine](../../schema/merging), and you can read its [commented code](https://github.com/open-contracting/ocds-merge) as inspiration for your implementation.
* If you have [release packages](../../schema/release_package) and want to have [record packages](../../schema/record_package), if you have data that follows an older version of OCDS, or if you otherwise need to transform your OCDS data, you can use [OCDS Kit](https://ocdskit.readthedocs.io/en/latest/) as a command-line tool or [Python](https://www.python.org/) library.

If you aren't creating or updating an IT system, but are instead reusing an existing [data collection tool](build/data_collection_tools), you can customize it:

* The [data collection spreadsheet](https://www.open-contracting.org/resources/data-collection-spreadsheet/) includes instructions describing how to add fields and how to add and reformat sheets.
* The [data collection form](https://www.open-contracting.org/resources/ocds-data-collection-form/) includes instructions describing how to add fields and how to customize descriptions and guidance.

Contact the [Data Support Team](../support/index) for guidance on customizing a tool to meet your needs.

**Resource:** [Using tabular versions of OCDS to generate JSON data](https://www.open-contracting.org/2020/03/06/using-tabular-versions-of-ocds-to-generate-json-data/) details the approach used in Paraguay.

**Resource:** To learn about how to create a spreadsheet input template for OCDS, check out our blog series on prototyping OCDS data using spreadsheets ([Part 1](https://www.open-contracting.org/2020/04/24/prototyping-ocds-data-using-spreadsheets/), [Part 2](https://www.open-contracting.org/2020/05/11/prototyping-ocds-data-using-spreadsheets-part-ii/), [Part 3](https://www.open-contracting.org/2020/05/28/prototyping-ocds-data-using-spreadsheets-part-iii/)).

```{note}
Re-using tools isn't always easy. [Tool Re-Use in Open Contracting: A Primer](https://www.open-contracting.org/resources/tool-re-use-in-open-contracting-a-primer/) is a step-by-step guide to help you determine what you need, evaluate which tool is the right fit, and evaluate whether the right conditions are in place for successful reuse of a tool.
```

## Build your extensions

If your [mapping](map) identified data elements which don't map to OCDS or an existing extension, you ought to develop your own extensions. Documenting your additional fields using extensions makes important information about the structure, format and meaning of your data available to users.

**Action:** Read the guidance on [developing new extensions](map/extensions.md#developing-new-extensions), which includes links to useful tools and resources.

**Action:** Request assistance from the [Data Support Team](../../support/index) to model your extensions.

**Action:** Share your extensions with the OCDS community on [GitHub](https://github.com/open-contracting/standard/issues).

**Resource:** [Webinar: Creating OCDS Extensions](https://youtu.be/1uTik92PWfo) ([presentation](https://docs.google.com/presentation/d/16poTfulCN1oYctfWnMJ9YDRrX1GJMi1MuOmFlOJMC5w/edit))

## Keep users in mind as you build

As covered in the [Design](design) phase, different users will need information in different ways. Some will need bulk downloads, some will need APIs, some will need CSVs, most will need change history published on a timely basis with individual releases and records.

**Resource:** [Guidance on bulk downloads, APIs, individual releases and records, and flattened serializations](build/hosting)

**Resource:** [Guidance on JSON and CSV serialization, including packaging files with metadata](build/serialization)

## Check your data

Throughout the build phase you ought to regularly use the [OCDS Data Review Tool](https://standard.open-contracting.org/review/) to check the structure and format of your data. This ensures that your data is compatible with OCDS tools and is comparable with other OCDS data.

OCDS data needs to be published as part of a release package or a record package. You can use [OCDS Kit](https://pypi.org/project/ocdskit/) to reformat your data before submitting it to the review tool, but any data you publish needs to be correctly packaged.

The Data Review Tool reports any structural issues with your data. It checks whether your data makes sense and displays a preview of your data, so that you can check whether the information is appearing in the correct place within the schema.

You ought to use real data for testing, wherever possible. Using fictional data can lead to false positives and missed errors in your data pipeline: for example, if your test data includes incoherent values for the award date and the contract signature date, it won't be possible to identify issues with how these fields are mapped in your OCDS data.

If your data source doesn't contain any data yet, because you are developing a new system to collect and publish data, for example, then you ought to work with stakeholders to collect enough real data to populate all the data elements for at least one contracting process.

If you can't collect enough real data for testing, then you ought to create realistic and coherent test data:

* use real entities, products, and services
* use plausible dates and values
* avoid using placeholder values
* avoid setting multiple data elements to the same value.

**Action:** Upload some data to the [OCDS Data Review Tool](https://standard.open-contracting.org/review/).

**Action:** Request feedback on your draft data from the [Data Support Team](../../support/index).

**Tool:** The [jOCDS Validator](https://developmentgateway.org/blog/your-data-ocds-compliant-introducing-jocds-validator) can be used for bulk checking of the structure and format of OCDS data

**Resource:** [How to check your OCDS data validates](https://www.open-contracting.org/2018/05/09/check-ocds-data-validates/)

[Next phase: Publish](publish)
