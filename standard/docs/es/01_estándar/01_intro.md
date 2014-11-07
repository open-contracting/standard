<br /><a id="above"></a>

<div class="panel panel-warning">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-comment"></span>Open for consultation</h4>
     </div>
     <div class="panel-body"><p>This version is open for consultation until September 30th. Visit <a href="http://standard.open-contracting.org">http://standard.open-contracting.org</a> for more background information.</p>
     </div>
</div>


[TOC]

## Purpose


Limita el número de artículos que se mostrará

This is the beta release of the Open Contracting Data Standard. This release provides:

* A description of the overall Open Contracting Data Standard Model
* A JSON Schema for open contracting **releases** and **records** 
* Details of suggested implementation.

This beta offers early adopters the chance to test the overall data model for the standard, and to provide feedback on the coverage and definition of fields provided by the standard.

Both structural and field changes should be anticipated between the beta and initial release version.

## Background 

Countries signing up to the Open Contracting Global Principles commit to share "information related to the formation, performance, and completion of public contracts" including data on all stages of contracting, including subcontracting arrangements.

The Open Contracting Data Standard is being developed to allow as much of this information as possible to be shared as structured data in addition to documents. The objective of the OCDS is to enable the widest possible range of stakeholders to use contracting data and documents to achieve value for money for the government, a competitive playing field for the private sector, and high quality goods, works, and services for citizens.

The development of the Data Model Draft has been based on:

* **Assessing data currently supplied through contract portals** - in order to understand the data that governments currently hold and publish, and how it is structured. To carry out this analysis we created the [Contracting Data Comparison tool](http://ocds.open-contracting.org/opendatacomparison/), and [Contracting Data Map](http://ocds.open-contracting.org/opendatacomparison/datamap/) which explores the fields of data available from a wide range of different government contracting data portals around the world.



* **Exploring demand for data on contracting** - to identify the ways in which different users think about contracting data, and how they want to use it. This work is ongoing, and initial use cases are factored into this conceptual model and will continue to shape future iterations.



* **A Review of existing schemas: **There are already well-known schemas for Organizations, People and Addresses, and related purposes. This project will build upon existing standards efforts where appropriate. 

The Open Contracting Data Standard is a core product of the Open Contracting Partnership. Version 1.0 of the standard is being developed for the OCP by the World Wide Web Foundation and World Bank, through a project supported by The Omidyar Network and the World Bank.

More detailed information about the development process is available [below](#development-process).

## Conceptual Model

### The contracting process

The contracting process is the sequence of stages related to the lifespan of a contract, beginning with planning and culminating in contract closure.

![Contracting Process](https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/contracting%20process.png)

<p>* Formation, when dealing with basic procurement processes, will often be referred to as Tendering & Award.</p>

For descriptions of the phases see the "Definitions" tab [above](#above).

Each Open Contracting Process should be given a unique **Open Contracting ID** (ocid). We define an Open Contracting Process as having a single unique tendering / competitive phase, but with the possibility of this resulting in multiple awards and contracts. See defining a unique contracting process [below](#unique) for more details. 

### Contracting releases and record

Information about an Open Contracting Process may accumulate over time. As a result, the Open Contracting Data Standard provides for two kinds of data:

* **Contracting releases** - each release provides information pertaining to a particular stage in the contracting process -- such as tender notices, award notices, or details of a finalized contract. These releases may equate to formal legal notices as part of a procurement process, or may be new releases of information. They can have attached documents. Release may also include amendments. Once published a release should not be changed, and new information should be shared through new releases with relevant amendments. 

* **Contracting record.** - A contracting record provides a snapshot of all the key elements of a unique contracting process, including its planning, formation, performance and completion. It is updated as new information becomes available through contracting releases to accurately reflect the current state of the contract processes. The contracting record should provide an at-a-glance view of key information and can then be used to access more detailed information from the releases. A full contracting record can contain detailed revision information for fields. Contracting records may be published in full, or may contain a pointer to releases, allowing third-parties to assemble and verify a record of the whole contracting process.

Both **contracting releases** and **contracting records** should be provided within data packages, containing meta-data about the publisher, publication data and licensing information. 

Publishers can package a number of releases and records together in the same file, or can publish one release / record per-file.

### Data model and serialisations

For the beta of the Open Contracting Data Standard we have developed a [JSON Schema](http://json-schema.org/) rendering of a data model, whilst at the same time paying attention to ensure this model can be easily serialised in other formats. We have proposed an approach to map this data model into [flat file CSV and DataPackage formats](https://github.com/open-contracting/standard/issues/32). 

We have carried out initial work to identify [JSON-LD mapping](http://www.w3.org/TR/json-ld/) but this is [not currently a development priority for version 1.0](https://github.com/open-contracting/standard/issues/40). 
