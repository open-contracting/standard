# Identifiers

Consistent identifiers are essential to help join up open contracting data.

* The Open Contracting ID (OCID) is a globally unique identifier used to join up data on all stages of a contracting process;
* Organisation identifiers are important to know who is involved in each contract;
* Release, tender, award and contract identifiers are important to help cross-reference information.


## Types of identifiers 

In OCDS there are two kinds of identifiers: globally unique and local. 

### Globally unique identifiers

Across the whole universe of OCDS publishers these identifiers should refer to one specific contracting process or organisation. 

We create globally unique contracting process identifiers by adding a prefix to the internal identifiers held by publishers. 

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

Two government publishers (Town A and Town B) number their contracting processes from 0 upwards. 

Town A publishes information on a contracting process to build a new road. Internally they know this as contract 0005.

Town B publishes information on a contracting process to buy textbooks for a school. Internally they also know this as contract 0005. 

When they publish their OCDS data, each government adds a unique prefix onto their internal identifiers.

Now Town A's contracting process has the ```ocid``` of 'ocds-fh349f-0005' and Town B's contracting process has the ```ocid``` of 'ocds-twb234-0005'. 

There is now no chance of these getting mixed up in a system which imports data from both towns.

And, if an independent civil society contract monitoring group want to publish a report about implementation of Town A's road project, or Town B's text-book procurement, they have distinct identifiers they can use in their own data to refer to these.

</div>

You can read more about the OCDS approach to identify organisations below. 

### Local identifiers

Not all the identifiers in OCDS need to be globally unique. Most only need to be unique amongst their 'sibling' records.

* A release ID must be unique within any release package it appears in;
* A tender, award and contract ID must be unique within the contracting process it appears in;
* An item, milestone or document ID must be unique within the array it is part of.

Local identifiers must be used consistently. For example, if an award is given the ID '22' in one release, then the same award must have the same ID (22) in any subsequent releases which contain it. 

## Contracting Process Identifier (OCID)
<img src="../../../assets/green_compilation.svg.png" width="150" align="right"/>

An Open Contracting ID (OCID) is a **globally unique identifier** for a contracting process. Every OCDS release has an ```ocid```.

It can be used to join up information published at different times, and in different places. 

Setting the ```ocid``` is usually a simple two step process:

1. Identify the best **internal identifier** recorded against the contracting processes being disclosed;
2. Register an ```ocid``` prefix to prepend to this internal identifier.

In some cases, you may need to consider changes to existing systems to ensure that different systems handling information about your contracting processes have a common internal identifier to draw upon. 

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

In Mexico City, each time a tender or direct contract award process is initiated, the department responsible assigns an identifier. 

These are made up of an identifier for the department responsible for the procurement, a tender number, and the year. 

For example:

> OM-DGRMSG-004-13

This internal identifier can be exchanged with, and recorded in, any other systems which process information about this contracting process. For example, systems for reporting or recording spending transactions to suppliers.

Mexico City then registered a prefix with the OCDS helpdesk. They have been given the prefix ‘ocds-87sd3t’ which can be added to their unique process identifiers to give a globally unique ```ocid```. E.g.

> ocds-87sd3t-OM-DGRMSG-004-13

</div>

The OCDS prefix itself is made up of two parts: a prefix agency identifier (currently only 'ocds' is used), and a random six-character alphanumeric string generated for each publisher of data. 

The OCID is case sensitive.

### Registered prefixes
See the [registration pages](../implementation/registration.md) for details of how to obtain your OCID prefix. 

Prefix are randomly generated lowercase alpha-numberic strings. A prefix is assigned to each organisation that holds the existing internal identifier for a Contracting Processes. 

Currently, only the Open Contracting Partnership issues valid prefixes. In future, other organisations may be able to issue prefixes, each with their own prefix agency identifiers.

You can find a [list of registered prefixes here along with a registration form for creating new prefixes](../implementation/registration.md). 

The registered prefixes are dumb identifiers. They are not intended to carry any semantics, and their sole purpose is to turn internal identifiers into globally unique identifiers which can be cross-referenced between systems. 

### Publisher namespace

Earlier versions of this documentation imposed a stricter pattern on how internal identifiers should be combined with the ocid prefix, including a requirement for local namespaces. This requirement has been relaxed in practice and should be considered deprecated. 

However, publishers are encouraged to consider whether there are any risks of clashes in local identifiers (e.g. the possibility that two parts of the publishing body might use the same identifier for different contracting processes) and to plan to mitigate this when establishing their own patterns to generate their ```ocid```




## Organisation IDs
<img src="../../../assets/green_organisation.svg.png" width="150" align="right"/>

Reliably identifying the legal entities involved in a contracting process is vital for transparency and accountability, and for carrying out analysis to improve procurement and contract management.

Publishers should seek to collect and record the **legal identifier** from an official register of any organisations involved in a contracting process (including procuring organisations, bidders and suppliers), and should include this in their OCDS files.

There are two parts to expressing an **organisation identifier** in open contracting data. 

1. An **organization register prefix** identifying a **register** in which the organisation is identified
2. The **existing organizational ID** provided in that public register

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

The **organisation register prefix** for UK Companies House is GB-COH. The organisation **Development Initiatives** has been assigned the company number ‘06368740’ by Companies House. The globally unique organisation identifier for Development Initiatives can then expressed as follows:


```eval_rst

.. jsoninclude:: ../standard/example/organization.json
   :jsonpointer: 
   :expand: 

```

</div>

In OCDS, the organization register prefix is included in the ```scheme``` field of an identifier block, with the existing organization id placed in the ```id``` field. If there is a recognized public URI that uniquely identifies this organization (for example, drawn from [Open Corporates](https://opencorporates.com/)) this can also be given in the ```uri``` field. 

### Choosing an identifier

The **organisation register prefix** is used to refer to a register from which the organisation identifier is drawn. There are a range of different kinds of **organisation list**:

* **Primary registers** - such as national or state company registrars. An identifier issued by these bodies has a specific legal meaning. There is a one to one equivalence between the identifier and a legal entity of a particular form in a given jurisdiction. The identifier is created at the same time that the organisation is formally constituted, and changes to the status of the organisation are recorded against this identifier in an official register. **Identifiers from a primary register are strongly preferred in OCDS.**

* **Secondary registers** - which record a particular property of an organisation, such as being registered for VAT, or registered as an employer. An organisations identifier in such a registry might change without the organisation itself changing in nature. For example, in some jurisdictions, an organisation may de-register from VAT, and then re-register, gaining a new number in the process; or different branches of the same legal entity might register for different VAT numbers. 

* **Third-party databases** - which compile a list of organisations, and sometimes their sub-units, on an on-demand basis. These databases do not confer any legal status or special properties on the organisations, but may record a mapping between their own identifiers and other primary or secondary register identifiers for the organisation. A common examples of a third-party database is the proprietary Dun&Bradstreet number. The OCDS organisational identifier scheme will recognise identifiers from third-party databases, but strongly prefers those drawn from non-propietary databases, which allow users to lookup identifier information. 

* **Local lists** - Some publishers do not map their data to external identifiers, maintaining instead a local list of suppliers. In these cases, the publisher may use their internal identifiers, and should adopt their own **organisation list prefix** starting with X- to use. Where possible, the publisher should also provide their local list on the web, with as much additional data about each supplier as possible, in order to maximise the chance of data users matching their local list to some more authoritative register. 

Local lists may commonly need to be used for identifying public bodies, as in many countries there is no official list of public agencies. 

At present, the OCDS standard defers to the organisation list prefixes provided by the [IATI Organisation Registration Agency codelist](http://iatistandard.org/codelists/OrganisationRegistrationAgency/) which cover a wide range of organization types. If you require codes to be added to this list, please contact the [Open Contracting Data Standard helpdesk](../support/index.md) and they will work to achieve this.


## Release ID

The release ID must be unique within the contracting process it is part of, **and** within any given data package it is part of. 

> Within any release or record package **and** for any given ocid, there should be no two release IDs that refer to different releases.

### Tender, Award and Contract

The tender, award and contract IDs must be unique within the contracting process it is part of. 

> For any given ocid, there should be no two tender, award or contract IDs that refer to different tender, award or contract sections respectively.

Contracts should always cross-reference a related award (using the awardID property), as key information such as suppliers may be contained in the related award. There may be multiple contracts referring to a single award, as in the case of a framework contract where multiple contract are issued against a single award.

## Items, Documents and Milestones

An item, document or milestone ID must be unique within a given array of items, and must be used consistently across all the releases in a contracting process. 

The same id may be re-used in another array of items within the same release, and no cross-reference between these identifiers is implied. 

The use of an identifier means that subsequent releases can update prior identified items, documents or milestones, without needing to republish all the items, documents or milestones.

For example:

* A release may contain tender.items (Items tendered for) and award.items
* tender.items may contain three items, with identifiers of: [1, 2, 3]
* award.items may contain two items, with identifiers of: [3, 4]
* A second release is issued in which award.items contains six items: [3, 4, 5]

In this situation, note that:

* There is no implied relationship between the tender.item with id 3 and the award.item with id 3: these could be entirely different items
* There is a relationship between the award.items with id 3 and 4 in the first release, and with award.id of 3 and 4 in the second release. The second release should be interpreted as updating items 3 and 4, and adding a new item, 5. 
