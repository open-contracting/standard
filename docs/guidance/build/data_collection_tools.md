# Data collection tools

Where contracting data is managed using IT systems, implementing OCDS involves identifying how to extract, convert and publish that data.

Where contracting data is managed on paper or using unstructured electronic documents, implementing OCDS typically involves creating a bespoke IT system to collect data in a structured form.

If you need to collect structured data, but you don’t have the capacity to create an IT system, you can consider reusing an existing data collection tool. These tools offer fewer opportunities for customization than a bespoke IT system, but can provide a quick route to collecting and publishing data in OCDS format.

## Data collection form

The [data collection form](https://www.open-contracting.org/resources/ocds-data-collection-form/) is a web-based form for collecting OCDS data.

Data from the form is copied to a Google Sheet which structures and formats it to conform to OCDS.

Data entered using the form can be checked and converted using the [OCDS Data Review Tool](https://standard.open-contracting.org/review/) and published in either spreadsheet or JSON format.

Consider using the form if:

* You don’t have the capacity to develop or install a software tool
* Your users have access to reliable internet connections
* Your users are unfamiliar with spreadsheets
* Data entry will be done by many different users
* You want to minimize the work required to collate data
* You don’t need to update the data about a contracting process after it is first entered

The form includes a subset of fields from the **tender** and **buyer** sections of OCDS. The OCDS Helpdesk can help you extend and adapt the form to suit your needs.

Read more about using and customizing the form in the [resource guide](https://www.open-contracting.org/resources/ocds-data-collection-form/). The OCDS helpdesk can also provide guidance on using the form to collect data and help you to analyze the data that you collect.

## Data collection spreadsheet

The [data collection spreadsheet](https://www.open-contracting.org/resources/data-collection-spreadsheet/) is available in Google Sheets and for offline use in Microsoft Excel.

Data is entered directly into the template, which is structured and formatted to conform to OCDS.

Data entered the template can be checked and converted using the [OCDS Data Review Tool](https://standard.open-contracting.org/review/) and published in either spreadsheet or JSON format.

Consider using the spreadsheet template to collect data if:

* You don’t have the capacity to develop or install a software tool
* You need to collect data without access to an internet connection
* Your users are familiar with using spreadsheets
* Data entry will be done by a small number of users
* You have the capacity to collate data entered in multiple spreadsheets
* You need to make multiple updates over the life of a contracting process

The template includes a subset of fields from the **planning**, **tender**, **award**, **contract** and **implementation** sections of OCDS.

The spreadsheet includes instructions describing how to enter data and how to customize the spreadsheet to suit your needs. Read more about developing data collection spreadsheets in our blog series on [prototyping OCDS data using spreadsheets](https://www.open-contracting.org/2020/04/24/prototyping-ocds-data-using-spreadsheets/).

The OCDS Helpdesk can:

* Provide guidance on using the template to collect data
* Help you to extend or adapt the template to meet your requirements
* Help you to analyze the data that you collect

## OpenContractR

[OpenContractR](https://github.com/patxiworks/opencontractr) is a WordPress plugin for collecting and publishing OCDS data.

The plugin adds an interface for entering data, a contracts search function, visualizations and an OCDS format JSON API.

OpenContractR can be added to a new or existing WordPress site. There are many WordPress hosting providers to choose from if you do not already use WordPress.

Consider using OpenContractR if:

* You already have a WordPress website, or you have the capacity to set one up
* Your users have access to reliable internet connections
* Data entry will be done by many different users
* You want to minimize the work required to collate data
* You want users to be able to edit or update already entered data
* You want an online search interface for your data

Read more about OpenContractR in its [introduction](https://drive.google.com/file/d/18WHnQcnA6oESZtcZgS4rgaBLjd8BKvbM/view). If you’re interested in using OpenContractR please get in touch with the OCDS Helpdesk.

## Contrataciones Abiertas tool

[Contrataciones Abiertas](https://github.com/INAImexico/Contrataciones_abiertas_v2) is a tool developed by the Mexican government and it is made up of two main modules:

* Information capture module
* Visualization module

The objective of the tool is to enable the monitoring of contracting processes by using and producing OCDS data.

Consider using Contrataciones Abiertas if:

* You have the resources and technical capacity to [set up the tool](https://github.com/INAImexico/Contrataciones_abiertas_v2/raw/master/Manual%20de%20instalaci%C3%B3n.docx)
* Data entry will be done by different users
* You want to validate your data before publication
* You want to minimize the work required to collate and publish data
* You want a [dashboard and visualizations](https://www.open-contracting.org/2020/06/12/mexicos-inai-launches-new-open-source-tool-to-upload-and-visualize-open-contracting-data/) of your data
* Spanish is your (and your users') main language

The tool is open source and is [documented in Spanish](https://github.com/INAImexico/Contrataciones_abiertas_v2). You can also find an introduction to the tool in [our blog](https://www.open-contracting.org/2020/06/12/mexicos-inai-launches-new-open-source-tool-to-upload-and-visualize-open-contracting-data/).

## What next?

However you choose to collect and structure your data, you should publish it online using an [open license](../../publish/#license-your-data) so that others can make use of it.

Consider how you will make it easy for users to discover the data you have published. For example, by publishing it on an existing procurement portal, on your organization’s website, or an open data portal.

If you collected your data using the data collection form or spreadsheet, the easiest option is to simply collate the data into a single spreadsheet for publication.

If you collected your data using another tool, the tool may already provide options to publish data via bulk files or an API.
