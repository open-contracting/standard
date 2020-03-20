# Build

This phase is about creating a new IT system, or updating an existing IT system, to [implement your mapping](map) and publish OCDS data.

As you complete this phase, you can:

* Fill in the *Publication architecture* sub-section of your [Publication Plan](map).

## Register an OCID prefix

The [identifiers](../../schema/identifiers) reference page describes the contracting process identifier (`ocid`) and how ocid prefixes are used to ensure `ocid`s are globally unique.

To publish OCDS data, you need to register an ocid prefix. Simply email <data@open-contracting.org> with your organization's name.

```eval_rst
.. note::

   .. markdown::

      All registered OCID prefixes are accessible as a [web page](https://docs.google.com/spreadsheets/d/1Am3gq0B77xN034-8hDjhb45wOuq-8qW6kGOdp40rN4M/pubhtml?gid=506986894&single=true&widget=true) or [CSV file](https://docs.google.com/spreadsheets/d/1Am3gq0B77xN034-8hDjhb45wOuq-8qW6kGOdp40rN4M/pub?gid=506986894&single=true&output=csv).
```

## Determine your system architecture

There are many ways to extract data from data sources, combine it, map it to OCDS, and publish it. [*Getting your data together*](https://www.open-contracting.org/2016/06/30/getting-data-together-routes-towards-ocds-api/) presents four options for connecting systems.

## Build your data pipeline

Having determined your system architecture, it's time to implement it. This is one of the longest steps of implementing OCDS. Depending on your [Technical Assessment](map) and system architecture, you might be able to reuse some of these OCDS tools:

```eval_rst
.. note::

   .. markdown::

      If you have any issues using OCDS tools, [contact the OCDS Helpdesk](../../support/index).
```

<div class="spaced" markdown=1>

* If you are creating (or upgrading) an **electronic government procurement (e-GP) system** or open contracting data portal, refer to our [Guide to Defining OCDS Functional Requirements for e-GP Systems](https://www.open-contracting.org/resources/guide-defining-open-contracting-data-standard-functional-requirements-electronic-government-procurement-systems/).
* If your source data is in **CSV/Excel files**, you can rename the columns to match the JSON paths in OCDS (for example, `buyer/name`) and then [transform the CSV/Excel files to OCDS JSON](https://www.open-contracting.org/2016/08/08/open-contracting-data-structure-spreadsheets/) by using [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/), a command-line tool. Or, you can transform Excel files by using the [Open Contracting Explorer](http://www.developmentgateway.org/expertise/contracting), which also includes a web interface and web API for users to access and explore the OCDS data, authored by Development Gateway.
* If your source data is in **SQL tables**, you can use this tool to [extract data from SQL tables and transform it to OCDS](https://gitlab.com/dncp-opendata/opendata-etl), authored by Paraguay's Dirección Nacional de Contrataciones Públicas (DNCP). To use this tool, you write SQL queries to extract data from SQL tables, setting the columns for the query results to match the JSON paths in OCDS (for example, `buyer/name`). The query results are saved to CSV files, which are transformed to OCDS JSON using [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/usage-ocds/). (*Documentation is in Spanish.*)
* To **make OCDS data available via an API**, you can use the [previous tool](https://gitlab.com/dncp-opendata/opendata-etl) to load OCDS data into [ElasticSearch](https://www.elastic.co/), and then use [another tool](https://gitlab.com/dncp-opendata/opendata-api-v3) to make it available via an API, authored by Paraguay's Dirección Nacional de Contrataciones Públicas (DNCP).
* If you intend to **publish [record packages](../../schema/record_package)**, [OCDS Merge](https://ocds-merge.readthedocs.io/en/latest/) is the best software library for creating OCDS [records](../../getting_started/releases_and_records). If you use the [Python](https://www.python.org/) programming language, you can use it directly. If not, you can use its [test cases](https://ocds-merge.readthedocs.io/en/latest/#test-cases) to test your implementation of the [merge routine](../../schema/merging), and you can read its [commented code](https://github.com/open-contracting/ocds-merge) as inspiration for your implementation.
* If you have [release packages](../../schema/release_package) and want to have [record packages](../../schema/record_package), if you have data that follows an older version of OCDS, or if you otherwise need to **transform your OCDS data**, you can use [OCDS Kit](https://ocdskit.readthedocs.io/) as a command-line tool or [Python](https://www.python.org/) library.
* If you are **authoring data from scratch**, you can use this tool to [enter data](https://github.com/INAImexico/Contrataciones_abiertas_v2), which also includes a web interface for users to access and explore the OCDS data, authored by Mexico's Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales (INAI). (*Manuals are in Spanish.*)

</div>

```eval_rst
.. note::

   .. markdown::

      If you want to use OCDS Kit or Flatten Tool, but don't have access to the command line or can't install new software on your computer, you can use [OCDS Toucan](https://toucan.open-contracting.org), which gives access to these tools through a web browser.
```

Re-using tools isn't always easy. [Tool Re-Use in Open Contracting: A Primer](https://www.open-contracting.org/resources/tool-re-use-in-open-contracting-a-primer/) is a step-by-step guide to help you determine what you need, evaluate which tool is the right fit, and evaluate whether the right conditions are in place for successful re-use of a tool.

New tools are continually being authored for publishing OCDS data. Please refer to our [Tools Directory](https://www.open-contracting.org/resources/open-contracting-tools-directory/) for a complete list.

[Next phase: Publish](publish)
