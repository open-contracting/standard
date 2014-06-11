This version is open for consultation until July 10th. Visit [http://open-contracting.github.io](http://open-contracting.github.io) for more background information.

<div class="panel panel-primary">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Share your comments</h3>
     </div>
     <div class="panel-body">
         The online version of this document is open for comment. You can share your comments in three ways:
         <ul>
             <li><strong>Inline comments on the document</strong> - select the <span class="glyphicon glyphicon glyphicon-comment"></span> icon at the top of the page for details of how to add in-line comments on the document. Once authenticated you can highlight any text on the page and add your own shared annotations, or respond to those left by others.</li>
             <li><strong><a href="https://github.com/open-contracting/standard/issues">Issue tracker</a></strong> - you can add issues to the <a href="https://github.com/open-contracting/standard/issues">standard's GitHub issue tracker</a>.</li>
        </ul>
        Throughout this document there are specific questions for consultation included, but you are not limited to responding to these questions: we welcome all input you can offer. 
         
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

The development of the standard is being undertaken by the World Wide Web Foundation and Aptivate, supported by The Omidyar Network and the World Bank, and working in partnership with the Open Contracting Partnership. The development process is also a process of action-research into creating accessible and effective open data standards, and exploring opportunities for [Joined Up Data](http://devinit.org/report/joined-data-building-blocks-common-standards/). 

### Development process
This first release from the development of an Open Contracting Data Standard presents a high-level overview of a proposed data model.

Following a technical scoping exercise we have adopted a development process based on:

- specifying a single format-independent conceptual model;
- developing this into a data model, identifying common vocabularies and taxonomies to use in defining fields, and creating new fields where required;
- specifying how this data model should be represented in key formats such as CSV, JSON, XML and RDF, respecting the particular idioms most familiar in these formats.

This document contributes to the first of these steps, offering a conceptual model for publishing Open Contracting Data and outlining the components that are captured within that model. The next phase of work will identify and create vocabularies covering key field definitions and will present a full data model. The final phase of this development process will recommend approaches to serialise this model and vocabulary using different formats. In parallel, work is taking place to develop a governance model for the future development of the standard. 

### Sources
The development of the alpha data model has been based on:

* **Assessing data currently supplied through contract portals** - in order to understand the data that governments currently hold and publish, and how it is structured.
* **Exploring demand for data on contracting** - to identify the ways in which different users think about contracting data, and how they want to useit.

We offer this draft data model as the basis for a discussion. Following feedback over June and July 2014 we will revise or confirm the conceptual model, and will work towards providing more detailed field-level information by the third quarter of 2014.

### Vocabulary

The world of procurement and contacting has many specialist terms. However, the precise way that these terms are used can vary from sector to sector, and country to country. Below we define how we are using a number of key terms. 

-   **Contracting** - the entire process of public contracting including the
    planning, formation, award, execution, performance, completion, and
    evaluation of a contract. Contracting includes procurement and and may include
    acquisition. Other terms that may be used for this process are
    public procurement, public tendering. 

-   **Contract** - the specific document that is finally signed between the buyer and supplier.

-   **Tender** - the process on inviting suppliers to compete for a
    contract. Common terms for this include: Request for quotation
    (RFQ), invitation to bid (ITB)

-   **Award** - the process of selecting the supplier who will be awarded a
    contract for the items being tendered.
    
-   **Termination** - the ending of a contract, either because the contracted activity is complete, or because of some other reason (e.g. breach of contract terms).

-   **Release** - the publication of information about any aspect of contracting. Often in the form of a notice, but also including other supplementary releases of information. 

-   **Notice** - a document providing information about a specific stage of the contracting process. For example, a tender notice or an award notice. 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>Is this proposed use of vocabulary clear and robust?</li>
             <li>Are there any third-party sources we should draw upon for clear definitions of these and other terms?</li>
         </ul>     
     </div>
</div>


##Conceptual Model

### The contracting journey 
![Contracting Journey](https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/contracting_journey.png)

There are many different stages involved in contracting: from the 
decision that some goods or services are required, through to deciding
how they will be bought (procurement processes), assessing bids, 
awarding a contract, negotiating and signing a contract, performing the
contract and exchanging money and reviewing whether the contract has been met. 
We use the term 'Contracting Journey' to describe an overarching container for all these stages.

#### Defining a unique contracting journey
There are cases where what the unique journey is not obvious. For example, a framework contract has only one tender and award but many contracts associated with that award.

We define a unique contracting journey as that with a unique tendering / competitive phase.

**Example 1**

<div class="pull-left"><img alt="Multiple journeys" src="https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/tender_notice_with_multiple_journeys.png"></div>

This Tender notice has a single ID and six line items. However, to secure each item vendors must enter a seperate bid and the competition is handled seperately for each item leading to 6 contracts. Because the competitive process is unique for each 6 items there are 6 contracting journeys here, in spite of the single Tender Notice ID.

<div class="clearfix"></div>

**Example 2**
<div class="pull-left"><img alt="Single journey" src="https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/one_journey_multiple_contracts.png"></div>

This snippet from a [tender notice](https://buyandsell.gc.ca/procurement-data/tender-notice/PW-14-00635129) offers an unspecified number of contracts for the successful supplier(s). The details note that there is a limit of $25k per contract, anything higher than that must be rebid competitively. All of the $25k or less contracts that are awarded under the award that will result from this tender are part of a single contracting journey, because of the single bidding process.

<div class="clearfix"></div>

### Scope of the standard
In this first draft, and for the planned beta in Q3 2014, we propose a focus on the four phases:

* Tender
* Award
* Contract
* Termination[^2]

We have excluded the planning and spending elements of the contracting journey from this draft standard for the following reasons:

-   We want to implement a readily adoptable standard and so, for a
    first version, we want to focus our efforts where we can add the most value.

-   The tender, award, and contract phases of contracting have
    consistent data (often drawn from the same systems inside a publisher) and share much terminology. By contrast, planning, budgeting and spending data is often held in different systems, and may not be stored in ways that link it to a contracting journey. 
    
-   There is an [existing standardisation effort](http://community.openspending.org/research/standard/) for Budget and Spending data under development through the Open Spending project. In line with the principles of Joined Up Data we will explore ways to connect data in the Open Contracting Data Standard with data in the proposed Open Spending and Open Budget data standards. 
   

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>Is this the right scope for the version 1.0 standard?</li>
             <li>Are there other standards we should looking to 'join up' to in order to supply tracing the full contracting journey, beyond those aspects that will be captured in the Open Contracting Data Standard?</li>
         </ul>     
     </div>
</div>

### Conceptual Model
We propose an Open Contracting Data Standard consisting of two parts:

- A **contracting record** - a core summary record used to describe key features of a complete 'contracting journey' - updated as new information becomes available to accurately reflect the state of tender, award or contract processes. The contracting record should provide an at-a-glance view of key information used in locating and analysing current, past or future contracting activities.

- A set of **contracting releases** - specific releases of information, such as tender notices, award notices, or details of a contract. The revision history of releases should be kept, and releases will often have a number of attached documents. The contracting releases provide in-depth information about a particular aspect of the contracting process, and should be published in a timely fashion.  

The information in contracting **releases** is used to build a contracting **record** - each contracting release must, therefore, be tied to a unique **open contracting identifier**. 

![Visual of publishing process](https://raw.githubusercontent.com/open-contracting/standard/master/standard/assets/releases%20and%20record.png)

The following sections are a high-level description of the open-contracting concepts, record and releases. The beta standard (due Q3 2014) will provide field-level definitions. 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>Does the proposed conceptual model make sense for the ways you want to publish or use open contracting data?</li>
             <li>Which do you need most: a summary contracting record, or detailed releases of information at each stage of the contracting journey?</li>
         </ul>     
     </div>
</div>


##Core components
The Data Standard will provide core components with which to publish data. These split into features, process, and add-ons.

### Contracting features
First, there is data that describes the **key features** of a proposed or enacted contract:

-   Goods / services
    -   Details, ideally at the line item level, of the goods and
        services being procured. This should include a standardized code (detailing 
        the items category e.g. construction or agricultural goods)
        & description as well as any supporting information.
-   Amount
    -   Details of the value of the goods / services being procured. At
        the tender phase, this may include a budget for the procurement
        or a minimum & maximum value for potential bids. At the award
        phase, this would include the awarded amount, ideally on a
        per-item basis. At the contract phase, this would include any
        contract amendments to alter the contract value, and the total
        and final value of the contract.
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

### Contracting process
Secondly, there is data that describes the **process** of contracting:

-   Tender
    -   This the information about the tender process. It may include:
        opening dates, closing dates, consultation information, the type
        of bidding process (open process, selective tendering, limited
        tendering or sole source), award criteria (lowest cost, best
        proposal, appropriate quality), as well as links to supporting
        documentation, a tender ID, and a link to the tender notice.

-   Award
    -   The information about the award process. Along with supplier and
        the awarded value, the award information would include a link to
        the award notice with an award date. It may also include
        information such as the number of bids, and number of bidders in
        the process.

-   Contract
    -   Information about the contract and the process through to
        completion. Including links to the contract documents, details
        of contract amendments (change of value, deliverables
        alterations, no-cost extensions), reports on deliverables and
        the status of the contract (active, completed, terminated).
    -   Note that Termination information (details of why the contract
        ended, final costs paid, final deliverables, and evaluation information.)
        is included under contract within our data model although it is a seperate
        phase in the contracting journey.

### Add on information
Thirdly, in addition to the core components, there will be cases where
publishers, or users, need to augment the core data with their
own information. The standard will provide a mechanism for Add-On
information. This will include additional fields in core components as
well as Add On components (e.g. new kinds of **contracting release**).

The publishing and re-use of add-ons will be encouraged to try and
reduce duplication and facilitate reuse of tools. The use of Add-Ons
will be subject to the following restrictions[^1]:

-   It must not use terms from outside this specification's terms where
    this specification's terms would suffice

-   It may use terms from outside this specification's terms where this
    specification's terms are insufficient.

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>Do these components cover all the relevant information you want to publish or access about contracting?</li>
             <li>Are we missing key elements in our description of what each component will contain?</li>
         </ul>     
     </div>
</div>


##The contracting record 
The contracting record is a master document that collects together a summary of key information about a contracting process. 

Each contracting record represents a single **contracting journey** and should have a unique **open contracting identifier**.

The contracting record should be possible to serialize in a flat (tabular) form with as little information loss as possible. 

The contracting record will contains the latest version of the information for each of the core components, including, when available details of:

* A unique open contracting identifier
* Meta-data about the publisher providing information
* Last-updated information
* The buyer
* The supplier
* Goods and services 
* Amounts 
* The tender process
* The award process
* The contracting process
* Links to the contracting releases for this contracting journey
* Links to other supporting documents

The contracting record will reflect the latest state of the contracting process. For example, if a tender is issued for Widget A with a minimum value of $10 and maximum of $20, at the tender stage the 'Amounts:minimum' would be $10, and 'Amounts:maximum' would be $20. If during consulation the range is determined to be unrealistic and a tender ammendment is issued changing the range of acceptable tenders to $20 - $30 then the contracting record would be updated to an 'Amounts:minimum' of $20 and 'Amounts:maximum' of $30. To see the history of these amounts would require looking at the individual contracting releases or tracking changes to the contracting record. 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>What are the most important fields you need in a summary contracting record?</li>
             <li>How does the proposed approach of having the contracting record represent the latest stage of contracting (i.e. overwriting earlier data) affect how you might publish or use open contracting data?</li>
         </ul>     
     </div>
</div>

### A note on framework contracts
Many public procurements take place under framework agreements, or standing arrangements. These help facilitate routine purchasing. Suppliers are pre-approved to provide a list of goods or services. In
this case, there are typically multiple contracts under a given award. The contracting record will need to allow for repeating sections of information where its necessary to represent the information.

##Contracting releases: notices and amendments 
The contracting record is formed and updated through releases, which
are either notices and amendments. There are three types of notice:

-   Tender notice
-   Award notice
-   Contract notice

A notice signifies the commencement of a new phase of the contracting
process. After a new phase has been commenced, amendments may be issued
to updated the information. Once a new phase commences, amendments
should not be made to the previous phase.

Not all notices are necessary for a complete contracting record. If an
entity was only publishing award notice data, it could still publish an
almost complete contracting record as the award contains a description
of the goods, the value, the buyer, seller, and could contain tender process 
information also. We would encourage further disclosure, but lack
of disclosure on one part of the contracting process does not preclude a
contracting record being created.

### Release tracking 
Ideally, each notice and amendment will refer to the parent contracting
record, and the contracting record will be updated with a link to each
notice and amendment, thereby providing a two-way data link.

In the event that the publisher is not maintaining a contract record,
the ID of the first notice will serve as the unique identifier moving
forward the contracting process. Subsequent notices and amendments may
have their own unique identifiers (e.g. an award notice identifier) but
they must all contain a reference to the unique identifier.

Each release, or a group of releases, will contain publisher
information, and each release will contain a release number and date
from that publisher. The idea is to accommodate the modularization of
publishing such that along the contracting journey, different bodies
could publish different sets of releases. For example, one publisher
for tenders and awards, and a separate publisher for contracts
releases. In addition, third-party publishers may wish to augment the
contracting data with their own releases such as an Add On containing
geo-coding information.


<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
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

-   users want to be able to see joined-up information in one place that brings together the contracting journey
    
<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
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
Over June 2014 we will be validating the conceptual model proposed in this document of a Contracing Journey, Contracting Records and Contracting Releases. You are invited to add your comments directly to the online copy of this document at [http://ocds.aptivate.org/standard/](http://ocds.aptivate.org/standard/), or to join discussions on [the project technical e-mail list](http://open-contracting.github.io/pages/community.html). 

Over July and August 2014 we will be fleshing out in more detail the data fields that belong to each of the core components, and will develop a full data model. The proposed model will be validated against a range of use cases developed through demand side research. 

This data model will be format-agnostic. That is, it will be a generic model rather than a specific serialization in JSON, XML or CSV. 

Following the development and validation of the model, we will outline a number of approaches to serialize this data in different priority formats. 

Throughout this process we will be seeking to re-use existing data structures from prior standards. 

### Schema re-use 
This document is intended as a non-technical introduction to the
standard, and as a such does not include an ontology (the formal data
representation of the standard). However, its worth noting here that we
will be reusing existing specifications wherever appropriate. In
particular, we already know that Buyer and Supplier are types of
Organization, that will have People and Addresses. There are already
well-known schemas for Organizations, People and Addresses and so we
will re-use this existing standard work where possible.

##Footnotes
[^1]:
    The use of add-on conditions were adapted from the
    The Popolo Project - [http://popoloproject.com/specs/\#conformance](http://popoloproject.com/specs/#conformance)
   
[^2]: It is worth noting that, from our supply side assessment, there is currently only limited existing data available on the termination and evaluation of contracts.

##Credits
The Open Contracting Data Standard project is a collaboration of the [Open Contracting Partnership](http://www.open-contracting.org/home-v1) and the [World Wide Web Foundation (Web Foundation)](http://www.webfoundation.org), supported by a grant from [Omidyar Network](http://www.omidyar.com/) and the [World Bank](http://www.worldbank.org), with [Aptivate](http://www.aptivate.org) as the lead technical partner to the project. The development of this draft has been led by Sarah Bird ([Aptivate](http://www.aptivate.org)), with contributions from Tim Davies (Web Foundation) and Ana Brandusescu. 

Coordinators of the research leading towards this standard include: Michael Roberts, Lindsey Marchessault, Marcela Rozo and Steven Davenport. 