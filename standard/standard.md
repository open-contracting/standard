<br /><a id="above"></a>

<div class="panel panel-warning">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-comment"></span>Open for consultation</h4>
     </div>
     <div class="panel-body"><p>This version is open for consultation until September 30th. Visit <a hef="http://standard.open-contracting.org">http://standard.open-contracting.org</a> for more background information.</p>
     </div>
</div>


[TOC]

## Purpose

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

## Releases

A full schema for releases can be accessed from the 'Release Schema' tab above. Click each section to expand that component of the schema. 

A release should contain the following elements:

### Planning
<script src="/standard/static/docson/widget.js" data-schema="/standard/r/master/release-schema.json$/definitions/planning"></script>

## The contracting record

The contracting record would contain the latest version of the information for each of the core components, as well as information about the publishing source, the last updated information, and crucially, links to all releases associated with this contracting process.

The core components of the Contracting Record and our data model are:

* Buyer

    * The buyer is the department, agency or entity who is paying for the goods /services in the contract. The buyer may be distinct from a procuring agency or awarding body - an independent entity that runs the procurement process (tender and award) - this allows for pooling of resources as well as enhancing impartiality).

* Supplier

    * The supplier is the entity, or entities, providing the goods or services in the contract. It could be an individual, a private organization, or another public body.

* Items - Goods / services / works

    * Details, ideally at the line item level, of the goods, services or works being procured. This should include a standardized code (detailing the items category e.g. construction or agricultural goods) & description as well as any supporting information or documents, such as technical specifications. This category will be expanded later as we move to support other types of contract beyond procurement.

* Planning

    * Before a tender notice is issued, the public entity will identify its procurement needs, such as: what the entity intends to procure, the justification for the procurement, the likelihood of the procurement, the cost estimates, and any anticipated milestones. This category contains information specific to planning for this specific contracting process. 

* Formation process

    * In the case of standard procurement, this the information about the tender process. It may include: opening dates, closing dates, consultation information, the type of bidding process (open process, selective tendering, limited tendering or sole source), award criteria (lowest cost, best proposal, appropriate quality), as well as links to supporting documentation, a tender ID, and a link to the tender notice. It may also include information such as the number of bids and bidders who participated in the process.

* Award details

    * This is information about the Contract Award e.g. the award date, and the awarded value. This is distinct from the contract information which reflects the actual contract document which is finalized and signed after an award. In the case of framework contracts, where multiple contracts are issued in a contracting process, the award would contain the details of the framework award.

* Contract

    * Information about the contract document(s) itself. Including award signature date, start & end date, links to the award & contract documents, and termination information. It would also capture details of contract amendments (change of value, deliverables alterations, no-cost extensions)

* Performance

    * In performance we store details related to the contract implementation including details of payments made, evaluation, audit and performance reports.

The contracting record will reflect the latest state of the contracting process. For example, if a tender is issued for Widget A with a minimum value of $10 and maximum of $20, at the tender stage the 'Amounts:minimum' would be $10, and 'Amounts:maximum' would be $20. If during consultation the range is determined to be unrealistic and a tender amendment is issued changing the range of acceptable tenders to $20 - $30 then the contracting record would be updated to an 'Amounts:minimum' of $20 and 'Amounts:maximum' of $30. To see the history of these amounts would require looking at the individual contracting releases or tracking changes to the contracting record.

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         <ul>
             <li>Does the proposed conceptual model make sense for the ways you want to publish or use open contracting data?</li>
             <li>Which do you need most: a summary contracting record, or detailed releases of information at each stage of the contracting process?</li>
             <li>Do these components cover all the relevant categories of information you want to publish or access about contracting?</li>
             <li>Are we missing key elements in our description of what each component will contain?</li>
             <li>How does the proposed approach of having the contracting record represent the latest stage of contracting (i.e. overwriting earlier data) affect how you might publish or use open contracting data?</li>
         </ul>     
     </div>
</div>

## Contracting releases

The contracting record is formed and updated through releases. Releases are snapshots of information which may be the first time information has been released or they may be revisions or amendments. 

### Release tracking

Ideally, each release will refer to the unique open contracting process ID, and the contracting record will be updated with a link to each notice and amendment, thereby providing a two-way data link.

In the event that the publisher is not maintaining a contract record, the ID of the first notice will serve as the unique identifier moving forward the contracting process. Subsequent notices and amendments may have their own unique identifiers (e.g. an award notice identifier) but they must all contain a reference to the unique identifier.

Each release, or a group of releases, will contain publisher information, and each release will contain a release number and date from that publisher. The idea is to accommodate the modularization of publishing such that along the contracting process, different bodies could publish different sets of releases. For example, one publisher for tenders and awards, and a separate publisher for contracts releases. In addition, third-party publishers may wish to augment the contracting data with their own releases such as an Add On containing geo-coding information.

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         <p>In future research we will be investigating different ways that amendments and updates to releases might be represented.</p>
         <ul>
             <li>What are options / approaches, from a technical / data structure point of view to represent and publish amendments or revisions to releases? And what are the strengths and weaknesses?</li>
         </ul>     
     </div>
</div>

<a name="unique"></a>
### Defining a unique contracting process

For the data standard, defining a unique contracting process is critical for getting useful, comparable, clean data. But, there are cases where what the unique process is not obvious. For example, a framework contract has only one tender and award but many contracts associated with that award.

We define a unique contracting process as that with a unique tendering / competitive phase.

**Example 1**
<div class="pull-left"><img alt="Multiple processes" src="https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/tender_notice_with_multiple_processes.png"></div>

This Tender notice has a single ID and six line items. However, to secure each item suppliers must enter a separate bid and the competition is handled separately for each item leading to 6 contracts. Because the competitive process is unique for each 6 items there are 6 contracting processes here, in spite of the single Tender Notice ID.

<div class="clearfix"></div>

**Example 2**

<div class="pull-left"><img alt="Single process" src="https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/one_process_multiple_contracts.png"></div>

This snippet from a [tender notice](https://buyandsell.gc.ca/procurement-data/tender-notice/PW-14-00635129) offers an unspecified number of contracts for the successful supplier(s). The details note that there is a limit of $25k per contract, anything higher than that must be rebid competitively. All of the $25k or less contracts that are awarded under the award that will result from this tender are part of a single contracting process, because of the single bidding process.

<div class="clearfix"></div>

### Add on information

In addition to the core components, there will be cases where publishers, or users, need to augment the core data with their own information. The standard will provide a mechanism for Add-On information. This will include additional fields in core components as well as Add On components (e.g. new kinds of **contracting release**).

The publishing and re-use of add-ons will be encouraged to try and reduce duplication and facilitate reuse of tools. The use of Add-Ons will be subject to the following restrictions [^1]

* It must not use terms from outside this specification's terms where this specification's terms would suffice

* It may use terms from outside this specification's terms where this specification's terms are insufficient.

[^1]:
    The use of add-on conditions were adapted from the
    The Popolo Project - [http://popoloproject.com/specs/\#conformance](http://popoloproject.com/specs/#conformance)

### A note on framework contracts

Many public procurements take place under framework agreements. These help facilitate routine purchasing. Suppliers are pre-approved to provide a list of goods or services. Under a framework agreement, there are typically multiple contracts that are all authorized by a single award. In the data standard, an award notice release would define the framework and this information would be stored in the contracting record under Award details. Then there will be multiple contract signature releases and each one would create a new Contract section in the contracting record. This provides a way to aggregate all the information on the contracts given under a single framework agreement.

Alternative names for framework agreements: Dynamic Purchasing System (EU), Standing Offers and Supply Arrangements (buyandsell.gc.ca)

### Linking to documents

There are often many documents associated with a contracting process including tender specifications, contract documents, performance reports etc. The standard will provide a way to link to these documents. We are considering how to handle documents in the contracting record. We may have a simplified contracting record that indicates that documents are available and a full contracting record that provides links to all the available documents. As we flesh out the different serializations over July and August this will be defined. Document links will always be available through the release that declared them.

## Development process

The development of the Data Model has been based on:

### 1) Supply-side research

The supply-side research is focused on comparing contract data (37 datasets with over 175 

downloadable assets from 27 publishers, from across the world). 26 publishers are from 15 countries that were selected as priority countries due to their current activity in open government and the Open Government Partnership (OGP) Action Plan. The effort sought to understand:

* which elements of the contracting process are captured in currently published data;

* which fields are commonly found across different datasets;

* how do different datasets represent and model the contracting process; and

* how far are there common identifiers that can be used to link datasets.

To answer the above questions a Contracting Data Comparison tool was created with a team of volunteer developers to provide a platform for curating meta-data about public contracting datasets from the priority countries.

The effort focused on capturing the metadata of contract data available. As it develops, the intention is for the Contracting Data Comparison tool to allow for wider public participation and thus create an ever more detailed picture of the landscape of contracting data availability and focus.

### 2) Demand-side use-cases

This draft is based primarily on research of existing published datasets. At the same time, the project has begun to explore priority use cases for open contracting data through workshops, webinars, a mailing list, and bilateral discussions with more than 200 stakeholders. The purpose of demand-side research is to capture the real needs and circumstances of the publishers and users of public contracting data.

In our consultations with government, civil society, donors, journalists, auditors, and the private sector, four primary use cases emerged. These users are interested to use open contracting data in order to:

* Achieve value for money for the procuring entity;

* Enable the private sector to compete for public contracts;

* Monitor service delivery for effectiveness; and

* Detect corruption and fraud in public contracting.

The draft use cases are being developed on an ongoing basis and can be found [here](https://docs.google.com/document/d/1zdgqSf-LUFVxO6Y_7v1cQf7l0vx35-p502jAI49JRmQ/edit?usp=sharing). These use cases not only demonstrate what can and could be done with open contracting data, but will also shape the development of the Open Contracting Data Standard as we move towards defining the field-level specification.

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         <ul>
             <li>In your opinion, does the proposed conceptual model work for these use cases?</li>
             <li>Are there other important use cases we should be considering?</li>
             <li>Are there use cases you can envisage where the proposed conceptual model does not work well?</li>
         </ul>     
     </div>
</div>

### 3) Research on related initiatives

There are existing standardization efforts for budget and spending data under development through the Open Spending Project. In line with the principles of [Joined Up Data](http://devinit.org/report/joined-data-building-blocks-common-standards/) this project will explore ways to connect data in the Open Contracting Data Standard with data in the proposed Open Spending and Open Budget Data Standards, among others.

In addition, the approach taken is informed by the development of other data standards. Research related to the Data Standard Architecture and Data Standard Governance will be released separately from the Data Model Draft.

## Next steps



## Acknowledgements

The Open Contracting Data Standard is a core product of the [Open Contracting Partnership (OCP)](http://www.open-contracting.org/). Version 1.0 of the standard is being developed for the OCP by the [World Wide Web Foundation](http://www.webfoundation.org), through a project supported by The [Omidyar Network](http://www.omidyar.com/) and the [World Bank](http://www.worldbank.org)".

This document contains significant contributions from Sarah Bird ([Aptivate](http://www.aptivate.org)), Ana Brandusescu and Tim Davies (World Wide Web Foundation). Other contributors include: Jose M. Alonso (World Wide Web Foundation), Steven Davenport (World Bank), Lindsey Marchessault, Michael Roberts (World Wide Web Foundation), and Marcela Rozo (World Bank).
