Draft - May 2014

Preamble 
--------

Countries signing up to the [Open Contracting Global
Principles](http://www.open-contracting.org/global_principles) commit to
share "information related to the formation, award, execution,
performance, and completion of public contracts" including data on all
stages of contracting, from pre-tender to performance evaluations, and
information on subcontracting arrangements.

The Open Contracting Data Standard is being developed to enable this
information to be shared as structured data that enable the widest
possible range of users to benefit from it. The overall goal is
promoting greater transparency of contracting arrangements and
supporting greater participation, monitoring and oversight in
contracting processes.

Vocabulary 
----------

We have found that there are number of terms within open contracting
that have overlap & lead to confusion, so upfront we'd like to be
specific about a few terms that we use to try and enable clarity.

-   Contracting - the entire process of public contracts including the
    planning, formation, award, execution, performance, completion, and
    evaluation. Contracting includes procurement and and may include
    acquisition. Other terms that may be used for this process are
    public procurement, public tendering.

-   Tender - the process on inviting suppliers to compete for a
    contract. Common terms for this include: Request for quotation
    (RFQ), invitation to bid (ITB)

-   Award - the process of selecting the supplier who will be awarded a
    contract for the items being tendered.

-   Contract - the specific document that is finally signed between the
    buyer and supplier.

-   Notice - a document detailing specific information, usually about a
    specific process e.g. a tender notice or an award notice.

The contracting journey 
-----------------------

Planning -> Tender -> Award -> Contract -> Performance

There are many different stages involved in contracting: from the
decision that some goods or services are required, through to deciding
how they will be bought (procurement processes), assessing bids,
awarding a contract, negotiating and signing a contract, performing the
contract and exchanging money and reviewing whether the contract has
been met. We use the term 'Contracting Journey' to describe the
container for all these stages.

The proposed OCDS data model is based around the idea of an identifiable
Contracting Journey.

In this first draft, and for the planned for the first release in 2014,
we have chosen to focus on the central three phases:

Planning -> Tender -> Award -> Contract -> Performance

We have excluded the two ends of the contracting journey for the
following reasons:

-   We want to implement a readily adoptable standard and so, for a
    first version, we want to focus our efforts where we can add value.

-   The tender, award, and contract phases of contracting have
    consistent data and terminology and can be represented by unified
    vocabulary. Conversely, performance and planning data have a
    separate focus and vocabulary.

-   Performance data is typically transaction-wise data documenting
    individual transactions between, it is also known as spending data.
    It typically does have a link back to the contract that the
    transaction is related to. This information is definitely important
    to the goals of the Open Contracting Partnership. However, there are
    existing efforts in this area, in particular, the work of the [Open
    Spending
    project](http://community.openspending.org/research/standard/).
    We're keen not to duplicate efforts and to focus on how our standard
    can effectively link with existing work.

-   Planning data is associated with budgeting, and in the limited data
    we were able to find, there was no link or connection to data in the
    following processes, and we did not find any data from tender,
    award, or contract datasets that linked back to budgeting. In
    addition, the Open Spending project is building a new [data standard
    for budget and spending
    data](https://github.com/openspending/budget-data-package/), and
    again we don't want to duplicate efforts.

Use Cases 
---------

This draft is based primarily on research of existing published datasets
as well as preliminary work on use cases for data demand. In particular,
we are trying to support the following demands on the data:

-   publishers release download-able data documenting tenders, contract
    awards, contracts and contract amendments as part of transparency
    obligations

-   publishers release feeds of tender notices for individual suppliers
    and third-party data providers to stay up-to-date on contracting
    opportunities

-   publishers release feeds or downloads of award notices as part of
    transparency obligations

-   users of data want to be able to compare costs of goods / services
    in one area compared to another

-   users want to be able to see joined-up information in one place that
    brings together the contracting journey

Open Contracting Core Concepts 
------------------------------

Within open contracting data, we find a core set of concepts that
encapsulate the data along the contracting journey.

First, there's the data that describes the **basis** of the contract:

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

Next, there's the data that describes the **process** of contracting:

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

Open Contracting Add-On Concepts 
--------------------------------

In addition to the core concepts, there will be lots of cases where
publishers or users of the data need to augment the core data with their
own information. The standard will provide a mechanism for Add-On
information. This will include additional fields in core concepts as
well as Add On concepts.

The publishing and re-use of add-ons will be encouraged to try and
reduce duplication and facilitate reuse of tools. The use of Add-Ons
will be subject to the following restrictions[1](#footnote):

-   It must not use terms from outside this specification's terms where
    this specification's terms would suffice

-   It may use terms from outside this specification's terms where this
    specification's terms are insufficient.

Publishing Model 
----------------

Currently, for publishers, the norm is to publish contracting data as a
notice - a tender notice to publicize details of a new tender, or an
award notice to declare a contract award. In addition, sometimes
amendments are published of these notices.

There is generally a statutory obligation to publish these notices and
so any data standard must accommodate them. However, a tension exists
between releasing these snapshots of information and the desire to have
a complete & joined up record for a given contracting journey that is
comparable across other contracting journeys.

As such, the data standard will provide a number of possible modes of
data publishing, but to be compliant the data must be translatable
between these modes through the prescribed mechanisms.

In particular, the Open Contracting Data Standard provides for two
representations of the data:

-   The contracting record - an up-to-date entry that brings together
    data from across the contracting process

-   The contracting releases - a series of entries that are the
    published notices and amendments that occur along the contracting
    process. The releases update the contracting record.

![Visual of publishing process](https://raw.githubusercontent.com/open-contracting/standard/master/standard/revisions%20and%20record.png)

### The contracting record 

The contracting record is a master document that collects together the
complete set of information about a contracting process. Ideally it
lives at a URI that is assigned at the start of the contracting process.
Alternatively it can be assembled at any point in time, as needed.

The contracting record contains all the information in the core
concepts. In addition, it may contain links to supporting documents,
administrative links, and any add on pieces of information that the
publisher wishes or needs to publish as part of their procurement
process.

The contracting record should ideally be available compiled, on-line and
as a download-able set of records. However, at the minimum, the a
collection of links to the contracting releases should be available.

Many public procurements take place under framework agreements, or
standing arrangements. These help facilitate routine purchasing.
Suppliers are pre-approved to provide a list of goods or services. In
this case, there are typically multiple contracts under a given award.
The contract record will allow for repeating sections of information
where its necessary to represent the information. For example, the
contracting

### Contracting releases: notices and amendments 

The contracting record is formed and updated through releases, which
are either notices and amendments. There are four types of notice:

-   Tender notice

-   Award notice

-   Contract notice

-   Completion notice

A notice signifies the commencement of a new phase of the contracting
process. After a new phase has been commenced, amendments may be issued
to updated the information. Once a new phase commences, amendments
should not be made to the previous phase.

Not all notices are necessary for a complete contracting record. If an
entity was only publishing award notice data, it could still publish an
almost complete contracting record as the award contains a description
of the goods, the value, the buyer, seller, and could contain tender and
award information also. We would encourage further disclosure, but lack
of disclosure on one part of the contracting process does not preclude a
contracting record.

### Release tracking 

**This section requires research & consultation**

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
geo-coding information

Schema re-use 
-------------

This document is intended as a non-technical introduction to the
standard, and as a such does not include an ontology (the formal data
representation of the standard). However, its worth noting here that we
will be reusing existing specifications wherever appropriate. In
particular, we already know that Buyer and Supplier are types of
Organization, that will have People and Addresses. There are already
well-known schemas for Organizations, People and Addresses and so we
will re-use this existing standard work where possible.

[1](#footnote) The use of add-on conditions were adapted from the
The Popolo Project -
[http://popoloproject.com/specs/\#conformance](http://popoloproject.com/specs/#conformance)
