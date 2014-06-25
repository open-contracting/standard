<br />
<div class="panel panel-warning">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-comment"></span>Open for consultation</h4>
     </div>
     <div class="panel-body"><p>This version is open for consultation until July 15th. Visit <a hef="http://ocds.open-contracting.org">http://ocds.open-contracting.org</a> for more background information.</p>
     </div>
</div>

[TOC]

## Open Contracting Data Standard

## Draft Data Model

## *Revision: 0.20 - June 24, 2014*

## Purpose

This is the first release of the Open Contracting Data Standard. In this release we would like to present our draft Data Model for Public Procurement. It presents a high-level overview of the structure of the Data Standard based on supply-side research and initial use-case feedback. This version of the Data Model has been designed for public procurement contracts. Our goal over the coming months is to adapt this model for public contracting in land and extractive industries.

The purpose of this release is to obtain feedback from the Open Contracting community on the draft Data Model before creating specific field names, reference lists, and file formats. 

There are three main discussion areas on which we hope to stimulate feedback and debate with this early release:

* What are the core components of a procurement standard?

* Can the needs of data producers and consumers be met with a system of various releases being compiled into a contracting record? 

* The need for and feasibility of a unique contracting identifier.

Throughout the document there are a series of questions to help guide the type of feedback we are seeking. We welcome general feedback.

Over the coming weeks we will continue to iteratively revise the Data Model Draft based on community feedback. One can follow revisions at [Open Contracting Data Standard](https://github.com/open-contracting/standard/commits/master/standard/standard.md). During the period over June and July 2014 the team will be revising the conceptual model as feedback is received. In addition, we will begin providing detailed field-level information for a formal release in the third quarter of 2014.

## Background

Countries signing up to the Open Contracting Global Principles commit to share "information related to the formation, performance, and completion of public contracts" including data on all stages of contracting, including subcontracting arrangements.

The Open Contracting Data Standard is being developed to allow as much of this information as possible to be shared as structured data in addition to documents. The objective of the OCDS is to enable the widest possible range of stakeholders to use contracting data and documents to achieve value for money for the government, a competitive playing field for the private sector, and high quality goods, works, and services for citizens.

The development of the Data Model Draft has been based on:

* **Assessing data currently supplied through contract portals** - in order to understand the data that governments currently hold and publish, and how it is structured. To carry out this analysis we created the [Contracting Data Comparison tool](http://ocds.open-contracting.org/opendatacomparison/), and [Contracting Data Map](http://ocds.open-contracting.org/opendatacomparison/datamap/) which explores the fields of data available from a wide range of different government contracting data portals around the world.

* **Exploring demand for data on contracting** - to identify the ways in which different users think about contracting data, and how they want to use it. This work is ongoing, and initial use cases are factored into this conceptual model and will continue to shape future iterations.

* **A Review of existing schemas: **There are already well-known schemas for Organizations, People and Addresses, and related purposes. This project will build upon existing standards efforts where appropriate. 

The Open Contracting Data Standard is a core product of the Open Contracting Partnership. Version 1.0 of the standard is being developed for the OCP by the World Wide Web Foundation and World Bank, through a project supported by The Omidyar Network and the World Bank.

More detailed information about the Development Process is available below. 

## Conceptual Model

### The contracting process

The contracting process is the sequence of stages related to the lifespan of a contract, beginning with planning and culminating in contract closure.

![Diagram 1](https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/image_0.png)

* Formation, when dealing with basic procurement processes, will often be referred to as Tendering & Award.

For descriptions of the phases see the "Vocabulary" section at the end.

### Conceptual Model

In most countries, public contracting information is scattered across multiple systems (and websites). Data released might be split across files by month or by some other segmentation. The siloed nature of contracting data suggests a simple standard may have substantial value to help link this information together to enhance its utility. Therefore, we propose a single specification containing all of the Open Contracting Data Standard fields grouped according to the components of the contracting record. Each contracting record would be uniquely identifiable, and serialized in a flat/table form. The fields within the record will be populated (or revised) through contracting releases. This is described below and in the diagram.

* A **contracting record** - is a summary of all the key elements of a unique contracting process, including its planning, formation, performance and completion. It is updated as new information becomes available in the form of contracting releases to accurately reflect the current state of the contract processes. The contracting record should provide an at-a-glance view of key information and can then be used to access more detailed information from the releases. In the image below, the blue boxes represent core components of the contracting record and will contain the "field-level" data. Descriptions of each of these components is below the diagram.

* A set of** releases** - of information pertaining to stages in the contracting process -- such as tender notices, award notices, or details of a finalized contract. The revision history of releases should be kept, and releases will often have a number of attached documents. The contracting releases may originate in different systems but can be compiled into the contracting record. The releases should be published in a timely fashion. 

The information in the contracting **releases** would be used to build a contracting **record. **For this to work, each contracting release must be tied to a unique **open contracting identifier**. Each of these components is discussed below. 

![image alt text](https://github.com/open-contracting/standard/blob/master/standard/assets/image_1.png)

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

#### **Consultation questions**

* Does the proposed conceptual model make sense for the ways you want to publish or use open contracting data?

* Which do you need most: a summary contracting record, or detailed releases of information at each stage of the contracting process?

* Do these components cover all the relevant categories of information you want to publish or access about contracting?

* How does the proposed approach of having the contracting record represent the latest stage of contracting (i.e. overwriting earlier data) affect how you might publish or use open contracting data?

* This model necessitates a unique contracting ID across the entire contracting process. What are the challenges around this?

## Contracting releases

The contracting record is formed and updated through releases. Releases are snapshots of information which may be the first time information has been released or they may be revisions or amendments. 

### Release tracking

Ideally, each release will refer to the unique open contracting process ID, and the contracting record will be updated with a link to each notice and amendment, thereby providing a two-way data link.

In the event that the publisher is not maintaining a contract record, the ID of the first notice will serve as the unique identifier moving forward the contracting process. Subsequent notices and amendments may have their own unique identifiers (e.g. an award notice identifier) but they must all contain a reference to the unique identifier.

Each release, or a group of releases, will contain publisher information, and each release will contain a release number and date from that publisher. The idea is to accommodate the modularization of publishing such that along the contracting process, different bodies could publish different sets of releases. For example, one publisher for tenders and awards, and a separate publisher for contracts releases. In addition, third-party publishers may wish to augment the contracting data with their own releases such as an Add On containing geo-coding information.

#### **Consultation questions**

In future research we will be investigating different ways that amendments and updates to releases might be represented.

* What are options / approaches, from a technical / data structure point of view to represent and publish amendments or revisions to releases? And what are the strengths and weaknesses?

### Defining a unique contracting process

For the data standard, defining a unique contracting process is critical for getting useful, comparable, clean data. But, there are cases where what the unique process is not obvious. For example, a framework contract has only one tender and award but many contracts associated with that award.

We define a unique contracting process as that with a unique tendering / competitive phase.

**Example 1**

![image alt text](https://github.com/open-contracting/standard/blob/master/standard/assets/image_2.png)

This Tender notice has a single ID and six line items. However, to secure each item suppliers must enter a separate bid and the competition is handled separately for each item leading to 6 contracts. Because the competitive process is unique for each 6 items there are 6 contracting processes here, in spite of the single Tender Notice ID.

**Example 2**

![image alt text](https://github.com/open-contracting/standard/blob/master/standard/assets/image_3.png)

This snippet from a [tender notice](https://buyandsell.gc.ca/procurement-data/tender-notice/PW-14-00635129) offers an unspecified number of contracts for the successful supplier(s). The details note that there is a limit of $25k per contract, anything higher than that must be rebid competitively. All of the $25k or less contracts that are awarded under the award that will result from this tender are part of a single contracting process, because of the single bidding process.

### Add on information

In addition to the core components, there will be cases where publishers, or users, need to augment the core data with their own information. The standard will provide a mechanism for Add-On information. This will include additional fields in core components as well as Add On components (e.g. new kinds of **contracting release**).

The publishing and re-use of add-ons will be encouraged to try and reduce duplication and facilitate reuse of tools. The use of Add-Ons will be subject to the following restrictions [1](http://ocds.open-contracting.org/standard/r/master/#fn:2):

* It must not use terms from outside this specification's terms where this specification's terms would suffice

* It may use terms from outside this specification's terms where this specification's terms are insufficient.

### A note on framework contracts

Many public procurements take place under framework agreements, or standing arrangements. These help facilitate routine purchasing. Suppliers are pre-approved to provide a list of goods or services. Under a framework agreement, there are typically multiple contracts that are all authorized by a single award. In the data standard, an award notice release would define the framework and this information would be stored in the contracting record under Award details. Then there will be multiple contract signature releases and each one would create a new Contract section in the contracting record. This provides a way to aggregate all the information on the contracts given under a single framework agreement.

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

The draft use cases are being developed on an ongoing basis and can be found [ here](https://docs.google.com/document/d/1zdgqSf-LUFVxO6Y_7v1cQf7l0vx35-p502jAI49JRmQ/edit?usp=sharing). These use cases not only demonstrate what can and could be done with open contracting data, but will also shape the development of the Open Contracting Data Standard as we move towards defining the field-level specification.

#### **Consultation questions**

* In your opinion, does the proposed conceptual model work for these use cases?

* Are there other important use cases we should be considering?

* Are there use cases you can envisage where the proposed conceptual model does not work well?

### 3) Research on related initiatives

There are existing standardization efforts for budget and spending data under development through the Open Spending Project. In line with the principles of [Joined Up Data](http://devinit.org/report/joined-data-building-blocks-common-standards/) this project will explore ways to connect data in the Open Contracting Data Standard with data in the proposed Open Spending and Open Budget Data Standards, among others.

In addition, the approach taken is informed by the development of other data standards. Research related to the Data Standard Architecture and Data Standard Governance will be released separately from the Data Model Draft.

## Next steps

Over June 2014 we will be validating the conceptual model proposed in this document of a Contracting Process, Contracting Records and Contracting Releases. You are invited to add your comments directly to the online copy of this document at [ http://ocds.open-contracting.org/standard/](http://ocds.open-contracting.org/standard/), or to join discussions on [the project mailing list](https://groups.google.com/a/webfoundation.org/forum/#%21forum/public-ocds).

Over July and August 2014 we will be fleshing out in more detail the data fields that belong to each of the core components, and will develop a full draft data standard. The proposed model will be validated against a range of use cases developed through demand side research.

The Data Standard itself will be format-agnostic. However following the development and validation of the Data Standard, we will outline a number of approaches to serialize this data in different priority formats such as JSON, XML, and CSV.

Throughout this process we will be seeking to re-use existing data structures from prior standards.

## Vocabulary

The world of procurement and contracting has many specialist terms. However, the precise way that these terms are used can vary from sector to sector, and country to country. Below we define how we are using a number of key terms.

* **Contract** - a legally enforceable agreement between two (or more) parties. Often times, contracts are thought of as a single document, the document that is signed by the parties. However, in many cases, a contract can be made up of multiple documents incorporated by reference containing additional terms, specifications, provisions, standard forms or other information (known as addendums, annexes, appendices, schedules, riders, etc.) A contract should also be understood to include any later agreements of the parties that change the terms of the contract (amendments). As a legal document, the law (statutes, regulations, case law) may also impose additional terms or conditions or otherwise affect a contract.

* **Open Contracting** - norms and practices for increased disclosure and participation in public contracting including tendering, performance and completion. It includes the variety of contract types, from more basic contracts for the procurement of goods, to complex contracts, joint venture agreements, licenses and production sharing agreements. Open contracting encompasses all public contracting, including contracts funded by combinations of public, private and donor sources.

* **Public Contracting Process** - the planning, formation, award, execution, performance, and completion of a contract to which a government entity is a party.

    * **Planning** - the process of deciding what to contract for, when and how. A procurement plan is a product of the planning process that indicates an procuring entities planned procurement activities over a period of time.

    * **Formation** - the activities undertaken in order to enter into a contract. Good public contracting practice favours open competitive bidding or tendering as a method to form contracts (the process of publicly inviting prospective contractors to submit bids for evaluation and selecting a winner or winners). However, contracts can be awarded in other ways, such as through non-competitive direct negotiation, prequalification of bidders, and other methodologies. The contract is then "awarded" to a selected contractor. Once the contractor has been selected and the terms of the contract have been agreed, the contract is signed (or executed) by the parties, and becomes active on an effective date.

    * **Performance** - the implementation of the contract in accordance with the obligations laid out therein. Often, contractors will enter into additional contracts with sub-contractors in order to implement the public contract.

    * **Completion** - the confirmation that all obligations (deliverables and payments) of the contract have been completed, or that the contract has been terminated for some other reason.

#### **Consultation questions**

* Is this proposed use of vocabulary clear and robust?

* Are there any third-party sources we should draw upon for clear definitions of these and other terms?

## Acknowledgements

The Open Contracting Data Standard is a core product of the [Open Contracting Partnership (OCP)](http://www.open-contracting.org/). Version 1.0 of the standard is being developed for the OCP by the [World Wide Web Foundation](http://www.webfoundation.org), through a project supported by The[ Omidyar Network](http://www.omidyar.com/) and the [World Bank](http://www.worldbank.org)".

This document contains significant contributions from Sarah Bird ([Aptivate](http://www.aptivate.org)), Ana Brandusescu and Tim Davies (World Wide Web Foundation). Other contributors include: Jose M. Alonso (World Wide Web Foundation), Steven Davenport (World Bank), Lindsey Marchessault, Michael Roberts (World Wide Web Foundation), and Marcela Rozo (World Bank).

* * *


1. The use of add-on conditions were adapted from the The Popolo Project -[ http://popoloproject.com/specs/#conformance](http://popoloproject.com/specs/#conformance) 


