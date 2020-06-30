# Build

This phase is about creating a new IT system, or updating an existing IT system, to implement your [mapping](map) and publish OCDS data.

As you complete this phase, you can:

* Fill in the *Publication architecture* sub-section of your [Publication Plan](https://www.open-contracting.org/resources/ocds-publication-plan-template/).

## Register an OCID prefix

The [identifiers](../../schema/identifiers) reference page describes the contracting process identifier (`ocid`) and how ocid prefixes are used to ensure `ocid`s are globally unique.

To publish OCDS data, you need to register an ocid prefix.

**Action**: Email <data@open-contracting.org> with your organization's name and request an OCID prefix.

```eval_rst
.. note::

   .. markdown::

      All registered OCID prefixes are accessible as a [web page](https://docs.google.com/spreadsheets/d/1Am3gq0B77xN034-8hDjhb45wOuq-8qW6kGOdp40rN4M/pubhtml?gid=506986894&single=true&widget=true) or [CSV file](https://docs.google.com/spreadsheets/d/1Am3gq0B77xN034-8hDjhb45wOuq-8qW6kGOdp40rN4M/pub?gid=506986894&single=true&output=csv).
```

## Determine your system architecture

There are many ways to extract data from data sources, combine it, map it to OCDS, and publish it. The [system architectures](build/system_architectures) guidance page describes some possible approaches.

Your choice of architecture can determine how frequently your data is updated, whether you can publish a change history and the access methods available to your users. **Remember to check that your chosen architecture meets the needs you identified in the design stage.**

```eval_rst
.. toctree::
   :hidden:

   build/system_architectures
   build/change_history
   build/easy_releases
```

## Establish your publication formats and access methods

OCDS data can be published in different formats and accessed using different methods.

It is best practice to provide data in multiple formats, so that as many users as possible can use the data without first having to transform it to their preferred format. In OCDS terms, this means [publishing both structured JSON data and tabular CSV or spreadsheet data](build/serialization).

Where resources allow, it is also best practice to provide multiple access methods for your data, so that both humans and machines can access it easily. In OCDS terms, this means [providing both bulk downloads and an API](build/hosting). The [OCDS pagination extension](https://github.com/open-contracting-extensions/ocds_pagination_extension) describes how to paginate OCDS data via an API.

**Remember to check that your chosen publication formats and access methods meet the needs you identified at the design stage.**

**Tool:** [Flatten-tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/) can be used to convert OCDS data between JSON and CSV/spreadsheet formats.

```eval_rst
.. toctree::
   :hidden:

   build/serialization
   build/hosting
```

## Build your data pipeline

Having determined your system architecture, it's time to implement it. This is one of the longest steps of implementing OCDS. Depending on your [data sources](../map/#identify-your-data-sources) and system architecture, you might be able to reuse some of these OCDS tools:

```eval_rst
.. note::

   .. markdown::

      If you have any issues using OCDS tools, contact the [OCDS Helpdesk](../../support/index).
```

<div class="spaced" markdown=1>

* If you are creating (or upgrading) an **electronic government procurement (e-GP) system** or open contracting data portal, refer to our [Guide to Defining OCDS Functional Requirements for e-GP Systems](https://www.open-contracting.org/resources/guide-defining-open-contracting-data-standard-functional-requirements-electronic-government-procurement-systems/).
* If your source data is in **CSV/Excel files**, you can rename the columns to match the JSON paths in OCDS (for example, `buyer/name`) and then [transform the CSV/Excel files to OCDS JSON](https://www.open-contracting.org/2016/08/08/open-contracting-data-structure-spreadsheets/) by using [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/), a command-line tool.
* If your source data is in **Excel files**, you can alternately transform Excel files to OCDS JSON by using the [Open Contracting Explorer](http://www.developmentgateway.org/expertise/contracting), which includes a web interface and web API for users to access and explore the OCDS data. (This tool is authored by Development Gateway.)
* If your source data is in **SQL tables**, you can use [Kavure'i](https://gitlab.com/dncp-opendata/opendata-etl/-/blob/master/README_en.md) to transform it to OCDS. To use it, you write SQL queries to extract data from SQL tables, setting the columns for the query results to match the JSON paths in OCDS (for example, `buyer/name`). The query results are saved to CSV files, which are transformed to OCDS JSON using [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/). (Kavure'i is authored by Paraguay's Dirección Nacional de Contrataciones Públicas (DNCP).)
* To **make OCDS data available via an API**, you can use another component of [Kavure'i](https://gitlab.com/dncp-opendata/opendata-etl/-/blob/master/README_en.md) to load OCDS data into [ElasticSearch](https://www.elastic.co/), and then use [Pitogüé](https://gitlab.com/dncp-opendata/opendata-api-v3/blob/master/README_en.md) to make it available via an API. (Both tools are authored by Paraguay's Dirección Nacional de Contrataciones Públicas (DNCP).)
* If you intend to **publish [record packages](../../schema/record_package)**, [OCDS Merge](https://ocds-merge.readthedocs.io/en/latest/) is the best software library for creating OCDS [records](../../getting_started/releases_and_records). If you use the [Python](https://www.python.org/) programming language, you can use it directly. If not, you can use its [test cases](https://ocds-merge.readthedocs.io/en/latest/#test-cases) to test your implementation of the [merge routine](../../schema/merging), and you can read its [commented code](https://github.com/open-contracting/ocds-merge) as inspiration for your implementation.
* If you have [release packages](../../schema/release_package) and want to have [record packages](../../schema/record_package), if you have data that follows an older version of OCDS, or if you otherwise need to transform your OCDS data, you can use [OCDS Kit](https://ocdskit.readthedocs.io/) as a command-line tool or [Python](https://www.python.org/) library.
* If you are **authoring data from scratch**, you can use this tool to [enter data](https://github.com/INAImexico/Contrataciones_abiertas_v2), which also includes a web interface for users to access and explore the OCDS data. (This tool is authored by Mexico's Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales (INAI).) (*Manuals are in Spanish.*)
* If you want to **collect data using a spreadsheet or without an internet connection**, you can develop a [spreadsheet input template](https://www.open-contracting.org/resources/simple-ocds-spreadsheet-template/).

</div>

**Resource:** [Using tabular versions of JSON to generate JSON data](https://www.open-contracting.org/2020/03/06/using-tabular-versions-of-ocds-to-generate-json-data/) details the approach used in Paraguay.

**Resource:** To learn about how to create a spreadsheet input template for OCDS, check out our blog series on prototyping OCDS data using spreadsheets ([part I](https://www.open-contracting.org/2020/04/24/prototyping-ocds-data-using-spreadsheets/),[part II](https://www.open-contracting.org/2020/05/11/prototyping-ocds-data-using-spreadsheets-part-ii/)).

```eval_rst
.. note::

   .. markdown::

      If you want to use OCDS Kit or Flatten Tool, but don't have access to the command line or can't install new software on your computer, you can use [OCDS Toucan](https://toucan.open-contracting.org/), which gives access to these tools through a web browser.

      Re-using tools isn't always easy. [Tool Re-Use in Open Contracting: A Primer](https://www.open-contracting.org/resources/tool-re-use-in-open-contracting-a-primer/) is a step-by-step guide to help you determine what you need, evaluate which tool is the right fit, and evaluate whether the right conditions are in place for successful re-use of a tool.

      New tools are continually being authored for publishing OCDS data. Please refer to our [Tools Directory](https://www.open-contracting.org/resources/open-contracting-tools-directory/) for a complete list.
```

## Build your extensions

If your [mapping](map) identified data elements which don't map to OCDS or an existing extension, you ought to develop your own extensions. Documenting your additional fields using extensions makes important information about the structure, format and meaning of your data available to users.

**Action:** Read the guidance on [developing new extensions](../map/extensions/#developing-new-extensions), which includes links to useful tools and resources.

**Action:** Request support from the [OCDS Helpdesk](../../support/index) to model your extensions.

**Action:** Share your extensions with the OCDS community on [Github](https://github.com/open-contracting/standard/issues).

## Keep users in mind as you build

As covered in the [Design](design) phase, different users will need information in different ways. Some will need bulk downloads, some will need APIs, some will need CSVs, most will need change history published on a timely basis with individual releases and records.

**Resource:** [Guidance on bulk downloads, APIs, individual releases and records, and flattened serializations](hosting/#data-files-and-apis)

**Resource:** [Guidance on JSON and CSV serialization, including packaging files with metadata](build/serialization)

## Check your data

Throughout the build phase you ought to regularly use the [OCDS Data Review Tool](http://standard.open-contracting.org/review/) to check the structure and format of your data.

OCDS data needs to be published as part of a release package or a record package. You can use [OCDSKit](https://pypi.org/project/ocdskit/) to reformat your data before submitting it to the review tool, but any data you publish needs to be correctly packaged.

The Data Review Tool reports any structural issues with your data. It checks whether your data makes sense and uses [OCDS Show](https://open-contracting.github.io/ocds-show/) to display a preview of your data, so that you can check whether the information is appearing in the correct place within the schema. You can also use [OCDS Show](https://open-contracting.github.io/ocds-show/) directly.

**Action:** Upload some data to the [OCDS Data Review Tool](http://standard.open-contracting.org/review/).

**Action:** Request feedback on your draft data from the [OCDS Helpdesk](../../support/index).

**Tool:** The [jOCDS Validator](http://www.developmentgateway.org/blog/your-data-ocds-compliant-introducing-jocds-validator) can be used for bulk checking of the structure and format of OCDS data

**Tool:** [OCDS Show](https://open-contracting.github.io/ocds-show/)

**Resource:** [How to check your OCDS data validates](https://www.open-contracting.org/2018/05/09/check-ocds-data-validates/)

[Next phase: Publish](publish)
