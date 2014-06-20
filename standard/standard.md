<br />
<div class="panel panel-warning">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-comment"></span>Open for consultation</h4>
     </div>
     <div class="panel-body"><p>This version is open for consultation until July 15th. Visit <a hef="http://open-contracting.github.io">http://open-contracting.github.io</a> for more background information.</p>
     </div>
</div>

[TOC]

##About this document
This document sets out a proposed conceptual model for the [Open Contracting Data Standard](http://open-contracting.github.io), and poses a series of questions for consultation. 

It *does not* provide a field-level specification of the standard, or how the data may be represented in specific file formats. That will be provided through the beta release of the standard in Q3 2014, developed based on responses to this document. 

##Background and context

### Motivation
Countries signing up to the [Open Contracting Global Principles](http://www.open-contracting.org/global_principles) commit to share "information related to the formation, award, execution, performance, and completion of public contracts" including data on all stages of contracting, from pre-bid to performance evaluations, and information on subcontracting arrangements. 

The Open Contracting Data Standard is being developed to allow much of this information to be shared as structured data: delivered in ways that enable the widest possible range of users to benefit from greater transparency of contracting arrangements and supporting greater participation, monitoring and oversight in contracting processes.

The Open Contracting Data Standard is a core product of the [Open Contracting Partnership](http://www.open-contracting.org/). 
Version 1.0 of the standard is being developed for the OCP by the [World Wide Web Foundation](http://www.webfoundation.org) and [Aptivate](http://www.aptivate.org), through a project supported by 
The [Omidyar Network](http://www.omidyar.com/) and the [World Bank](http://www.worldbank.org).

The development process is also a process of action-research into creating accessible and effective open data standards, and exploring opportunities for [Joined Up Data](http://devinit.org/report/joined-data-building-blocks-common-standards/). 

### Development process
This first release from the development of an Open Contracting Data Standard presents a high-level overview of a proposed data model.

Following a technical scoping exercise we have adopted a development process based on:

- specifying a single format-independent conceptual model;
- developing this into a data model, identifying common vocabularies and taxonomies to use in defining fields, and creating new fields where required;
- specifying how this data model should be represented in key formats such as CSV, JSON, XML and RDF, respecting the particular idioms most familiar in these formats.
- identifying the tools that are necessary for standard to thrive such as aggregation and visualization.

This document contributes to the first of these steps, offering a conceptual model for publishing Open Contracting Data and outlining the components that are captured within that model. The next phase of work will identify and create vocabularies covering key field definitions and will present a full data model. The final phase of this development process will recommend approaches to serialise this model and vocabulary using different formats. In parallel, work is taking place to develop a governance model for the future development of the standard. 

### Sources
The development of the alpha data model has been based on:

* **Assessing data currently supplied through contract portals** - in order to understand the data that governments currently hold and publish, and how it is structured. To carry out this analysis we created the [Contracting Data Comparison tool](http://ocds.open-contracting.org/opendatacomparison/), and [Contracting Data Map](http://ocds.open-contracting.org/opendatacomparison/datamap/) which explores the fields of data available from a wide range of different government contracting data portals around the world. 
* **Exploring demand for data on contracting** - to identify the ways in which different users think about contracting data, and how they want to use it. This work is ongoing, and only initial use cases are factored into this conceptual model. In the next iteration of the conceptual model and field level information, further emphasis will be placed on use cases. 

This initial iteration of the conceptual model is focussed on procurement processes. Future iterations will look at contracts in the land and extractives sector, and we anticipate this will lead to further developments in the terminology used. 

We offer this draft data model as the basis for a discussion. Following feedback over June and July 2014 we will revise or confirm the conceptual model, and will work towards providing more detailed field-level information by the third quarter of 2014.

##Conceptual Model

### The contracting process 

The contracting process is the sequence of events related to the lifespan of a contract, beginning with planning and culminating in contract closure. 

![Visual of opencontrating process](https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/contracting%20process.png)

`*` Formation, when dealing with basic procurement processes, will often be referred to as Tendering & Award.

For descriptions of the phases see the "Definitions" tab at the top.

In this version of the standard, you will not see planning included. 
Please see "[A note on planning](#a-note-on-planning)" for a full explanation.
This is because the standard, at this point, has been drafted primarily 
on the basis of a deep search into the existing data, where we did not find planning data.
The standard will evolve on the basis of use cases and demand for contracting data also,
so we welcome detailed use cases regarding planning data to help us build out this area of the standard.

### Conceptual Model
We propose an Open Contracting Data Standard consisting of two parts:

- A **contracting record** - is used to summarize all the key
  features of the a unique contracting process, bringing together information from 
  all phases of the contracting process into one record. It is updated as 
  new information becomes available to accurately reflect the current state of the 
  contract processes. The contracting record should provide an 
  at-a-glance view of key information and can then be used to access more detailed information from the releases.

- A set of **contracting releases** - specific releases of information, 
  such as tender notices, award notices, or details of a contract. 
  The revision history of releases should be kept, and releases will often 
  have a number of attached documents. The contracting releases provide 
  in-depth information about a particular aspect of the contracting process, 
  and should be published in a timely fashion.  

The information in contracting **releases** is used to build a contracting 
**record** - each contracting release must, therefore, be tied to a unique 
**open contracting identifier**. See later section on identifying a unique 
contracting process.

![Visual of publishing process](https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/releases%20and%20record.png)

The Contracting Record above shows the core components of our data model.

-   Buyer
    -   The buyer is the department, agency or entity who is paying for
        the goods /services in the contract. The buyer may be distinct
        from a procuring agency or awarding body - an independent entity
        that runs the procurement process (tender and award) - this
        allows for pooling of resources as well as enhancing
        impartiality).
-   Supplier
    -   The supplier is the entity, or entities, providing the goods or services in
        the contract. It could be an individual, a private organization,
        or another public body.
-   Items - Goods / services / works
    -   Details, ideally at the line item level, of the goods,
        services or works being procured. This should include a standardized code (detailing 
        the items category e.g. construction or agricultural goods)
        & description as well as any supporting information or documents, such as technical specifications. This category will be expanded later
        as we move to support other types of contract beyond procurement.
-   Formation
    -   In the case of standard procurement, this the information about the tender process. It may include:
        opening dates, closing dates, consultation information, the type
        of bidding process (open process, selective tendering, limited
        tendering or sole source), award criteria (lowest cost, best
        proposal, appropriate quality), as well as links to supporting
        documentation, a tender ID, and a link to the tender notice. It may
        also include information such as the number of bids and bidders who
        participated in the process.
    -   This category will also include other types of formation such as
        negotiation of Public Private Partnerships, extractives and land contracts. We will be focusing on these 
        other types of contracting after building out all the fields for standard procurement.
-   Award
    -   This is information about the Contract Award e.g. the award date, and the
        awarded value. This is distinct from the contract information which reflects the
        actual contract document which is finalized and signed after an award. In the case
        of framework contracts, where multiple contracts are issued in a contracting process, the
        award would contain the details of the framework award.
-   Contract
    -   Information about the contract document(s) itself.
        Including award signature date, start & end date, 
        links to the award & contract documents, and termination information. 
        It would also capture details of contract amendments (change of value, deliverables
        alterations, no-cost extensions)
-   Performance
    -   In performance we store details related to the contract implementation
        including details of payments made, evaluation, audit and performance reports.

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         <ul>
             <li>Does the proposed conceptual model make sense for the ways you want to publish or use open contracting data?</li>
             <li>Which do you need most: a summary contracting record, or detailed releases of information at each stage of the contracting process?</li>
             <li>Do these components cover all the relevant information you want to publish or access about contracting?</li>
             <li>Are we missing key elements in our description of what each component will contain?</li>
             <li>How does the proposed approach of having the contracting record represent the latest stage of contracting (i.e. overwriting earlier data) affect how you might publish or use open contracting data?</li>
         </ul>     
     </div>
</div>

### Defining a unique contracting process
For the data standard, defining a unique contracting process is critical for getting useful, comparable, clean data. But, there are cases 
where what the unique process is not obvious. For example, a framework contract has only one tender and award but many contracts associated with that award.

We define a unique contracting process as that with a unique tendering / competitive phase.

**Example 1**

<div class="pull-left"><img alt="Multiple processes" src="https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/tender_notice_with_multiple_journeys.png"></div>

This Tender notice has a single ID and six line items. However, to secure each item suppliers must enter a seperate bid and the competition is handled seperately for each item leading to 6 contracts. Because the competitive process is unique for each 6 items there are 6 contracting processes here, in spite of the single Tender Notice ID.

<div class="clearfix"></div>

**Example 2**
<div class="pull-left"><img alt="Single process" src="https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/one_journey_multiple_contracts.png"></div>

This snippet from a [tender notice](https://buyandsell.gc.ca/procurement-data/tender-notice/PW-14-00635129) offers an unspecified number of contracts for the successful supplier(s). The details note that there is a limit of $25k per contract, anything higher than that must be rebid competitively. All of the $25k or less contracts that are awarded under the award that will result from this tender are part of a single contracting process, because of the single bidding process.

<div class="clearfix"></div>

### Add on information
In addition to the core components, there will be cases where
publishers, or users, need to augment the core data with their
own information. The standard will provide a mechanism for Add-On
information. This will include additional fields in core components as
well as Add On components (e.g. new kinds of **contracting release**).

The publishing and re-use of add-ons will be encouraged to try and
reduce duplication and facilitate reuse of tools. The use of Add-Ons
will be subject to the following restrictions[^2]:

-   It must not use terms from outside this specification's terms where
    this specification's terms would suffice

-   It may use terms from outside this specification's terms where this
    specification's terms are insufficient.

[^2]:
    The use of add-on conditions were adapted from the
    The Popolo Project - [http://popoloproject.com/specs/\#conformance](http://popoloproject.com/specs/#conformance)

### A note on framework contracts
Many public procurements take place under framework agreements, or standing arrangements. These help facilitate routine purchasing. Suppliers are pre-approved to provide a list of goods or services. In
this case, there are typically multiple contracts under a given award. In the case of a framework contract an award notice would define the framework
and this information would be stored in the contracting record under Award. Then the multiple contracts that are issued under the contract will
hold the seperately issued contracts under this framework award.

### Linking to documents
There are often many documents associated with a contracting process including tender specifications, contract documents, performance reports etc. The standard will
provide a way to link to these documents. We are considering how to handle documents in the contracting record. We
 may have a simplified contracting record that indicates that documents are available and a full contracting record that provides links to all
the available documents. As we flesh out the different serializations over July and August this will be defined. Document links will always 
be available through the release that declared them.

### A note on planning
In this version of the standard, you will not see planning included. 
This is because the standard, at this point, has been drafted primarily 
on the basis of a deep search into the existing data, where we did not find planning data.
The standard will evolve on the basis of use cases and demand for contracting data also,
so we welcome detailed use cases regarding planning data to help us build out this area of the standard.

##The contracting record 
The contracting record is a master document that collects together a summary of key information about a contracting process. 

Each contracting record represents a single contracting process and should be uniquely identifiable.

The contracting record will be possible to serialize in a flat/table form with as little information loss as possible. 

The contracting record will contains the latest version of the information for each of the core components, as well as information about 
the publishing source, the last updated information, and crucially, links to all releases associated with this contracting process.

The contracting record will reflect the latest state of the contracting process. 
For example, if a tender is issued for Widget A with a minimum value of $10 
and maximum of $20, at the tender stage the 'Amounts:minimum' would be $10, 
and 'Amounts:maximum' would be $20. If during consulation the range is 
determined to be unrealistic and a tender ammendment is issued changing the 
range of acceptable tenders to $20 - $30 then the contracting record would be 
updated to an 'Amounts:minimum' of $20 and 'Amounts:maximum' of $30. 
To see the history of these amounts would require looking at the individual 
contracting releases or tracking changes to the contracting record. 

## Contracting releases
The contracting record is formed and updated through releases. Releases are
snapshots of information which may be the first time information has been 
released or they may be revisions or amendments. Examples of release types are:

* Tender notice (declaring formation information)
* Tender notice amendment (an amendment to the formation information - perhaps
  after a clarification or consultation period)
* Award notice
* Award notice amendment
* Contract signature (with details of the signed contract)
* Contract amendment
* Reports release (containing an implementation report)
* Spending release (containing spending data or a reference to spending data)
* Termination notice

### Release tracking 
Ideally, each release will refer to the unique open contracting process id, 
and the contracting record will be updated with a link to each
notice and amendment, thereby providing a two-way data link.

In the event that the publisher is not maintaining a contract record,
the ID of the first notice will serve as the unique identifier moving
forward the contracting process. Subsequent notices and amendments may
have their own unique identifiers (e.g. an award notice identifier) but
they must all contain a reference to the unique identifier.

Each release, or a group of releases, will contain publisher
information, and each release will contain a release number and date
from that publisher. The idea is to accommodate the modularization of
publishing such that along the contracting process, different bodies
could publish different sets of releases. For example, one publisher
for tenders and awards, and a separate publisher for contracts
releases. In addition, third-party publishers may wish to augment the
contracting data with their own releases such as an Add On containing
geo-coding information.


<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         In future research we will be investigating different ways that amendments and updates to releases might be represented.
         <ul>
             <li>What approaches to representing and publishing amendments to releases could be adopted?</li>
         </ul>     
     </div>
</div>


## Use Cases 
This draft is based primarily on research of existing published datasets as well as preliminary work on use cases for data demand. In particular, we are seeking to support the following demands on the data:

-   publishers release download-able data documenting tender opportunities, contract
    awards, contracts and contract amendments as part of transparency
    obligations

-   publishers release feeds of tender notices for individual suppliers
    and third-party data providers to stay up-to-date on contracting
    opportunities

-   publishers release feeds or downloads of award notices as part of trade-agreement and/or transparency obligations

-   users of data want to be able to compare costs of goods / services in one area compared to another

-   users want to be able to see joined-up information in one place that brings together the contracting process
    
<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         <ul>
             <li>In your opinion, does the proposed conceptual model work for these use cases?</li>
             <li>Are there other important use cases we should be considering? </li>
             <li>Are there use cases you can envisage where the proposed conceptual model does not work well? </li>
         </ul>     
     </div>
</div>

##Next steps
Over June 2014 we will be validating the conceptual model proposed in this document of a Contracing Process, Contracting Records and Contracting Releases. 
You are invited to add your comments directly to the online copy of this document at [http://ocds.open-contracting.org/standard/](http://ocds.open-contracting.org/standard/), 
or to join discussions on [the project mailing list](https://groups.google.com/a/webfoundation.org/forum/#!forum/public-ocds). 

Over July and August 2014 we will be fleshing out in more detail the data fields that belong to each of the core components, and will develop a full data model. The proposed model will be validated against a range of use cases developed through demand side research. 

This data model will be format-agnostic. That is, it will be a generic model rather than a specific serialization in JSON, XML or CSV. 

Following the development and validation of the model, we will outline a number of approaches to serialize this data in different priority formats. 

Throughout this process we will be seeking to re-use existing data structures from prior standards. 

## Schema re-use 
This document is intended as a non-technical introduction to the
standard, and as a such does not include an ontology (the formal data
representation of the standard). However, its worth noting here that we
will be reusing existing specifications wherever appropriate. In
particular, we already know that Buyer and Supplier are types of
Organization, that will have People and Addresses. There are already
well-known schemas for Organizations, People and Addresses and so we
will re-use this existing standard work where possible.

There is an [existing standardisation effort](http://community.openspending.org/research/standard/) 
for Budget and Spending data under development through the Open Spending project. In line with the principles of Joined Up 
Data we will explore ways to connect data in the Open Contracting Data Standard with data in the proposed Open Spending and 
Open Budget data standards. 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h4>
     </div>
     <div class="panel-body">
         <ul>
             <li>Are there other standards we should looking to 'join up' to in order to supply tracing the full contracting process, beyond those aspects that will be captured in the Open Contracting Data Standard?</li>
         </ul>     
     </div>
</div>


##Credits
The Open Contracting Data Standard project is a collaboration of the [Open Contracting Partnership](http://www.open-contracting.org/home-v1) and the [World Wide Web Foundation (Web Foundation)](http://www.webfoundation.org), supported by a grant from [Omidyar Network](http://www.omidyar.com/) and the [World Bank](http://www.worldbank.org), with [Aptivate](http://www.aptivate.org) as the lead technical partner to the project. The development of this draft has been led by Sarah Bird ([Aptivate](http://www.aptivate.org)), with contributions from Tim Davies (Web Foundation) and Ana Brandusescu. 

Coordinators of the research leading towards this standard include: Michael Roberts, Lindsey Marchessault, Marcela Rozo and Steven Davenport. 
