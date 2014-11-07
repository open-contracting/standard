[TOC]


# Further information

<a name="unique"></a>
## Defining a unique contracting process

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

## Add-ons

In addition to the core components, there will be cases where publishers, or users, need to augment the core data with their own information. The standard will provide a mechanism for Add-On information. This will include additional fields in core components as well as Add On components (e.g. new kinds of **contracting release**).

The publishing and re-use of add-ons will be encouraged to try and reduce duplication and facilitate reuse of tools. The use of Add-Ons will be subject to the following restrictions [^1]

* It must not use terms from outside this specification's terms where this specification's terms would suffice

* It may use terms from outside this specification's terms where this specification's terms are insufficient.

We have identified that a location add-on will be a priority for future development, but as no publishers are currently providing location data, we were not able to develop this during the iterations towards the beta standard.

[^1]:
    The use of add-on conditions were adapted from the
    The Popolo Project - [http://popoloproject.com/specs/\#conformance](http://popoloproject.com/specs/#conformance)

## A note on framework contracts

Many public procurements take place under framework agreements. These help facilitate routine purchasing. Suppliers are pre-approved to provide a list of goods or services. Under a framework agreement, there are typically multiple contracts that are all authorized by a single award. In the data standard, an award notice release would define the framework and this information would be stored in the contracting record under Award details. Then there will be multiple contract signature releases and each one would create a new Contract section in the contracting record. This provides a way to aggregate all the information on the contracts given under a single framework agreement.

Alternative names for framework agreements: Dynamic Purchasing System (EU), Standing Offers and Supply Arrangements (buyandsell.gc.ca)

## Validator

A prototype validator is available at [http://ocds.open-contracting.org/validator/](http://ocds.open-contracting.org/validator/) which can be used to check draft documents against the schema.

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

This draft is based primarily on research of existing published datasets. At the same time, the project has begun to explore priority use cases for open contracting data through workshops, webinars, a mailing list, and bilateral discussions with more than 200 stakeholders. The purpose of demand-side research is to capture the real needs and circumstances of the publishers and users of public contracting data. We wanted to understand who wants to use contracting information, what information do they need, how do they  want to use the information, and why? 

A [questionnaire](https://docs.google.com/a/webfoundation.org/document/d/1GmOwGpvTgkPNiq1rzw1s1oj5TbE3G0KLowIaLSA19a4) was created and shared with our online community, and with specific stakeholders representing different user profiles (including government publishers, policymakers, procuring entities, auditors, donors, journalists, auditors, data aggregators, contractors, contract monitors, service delivery monitors, anti-corruption monitors, researchers, and transparency activists).

In our consultations four primary use cases emerged. These users are interested to use open contracting data in order to:

* Achieve value for money for the procuring entity;
* Enable the private sector to compete for public contracts;
* Monitor service delivery for effectiveness; and
* Detect corruption and fraud in public contracting.

Each of the use cases we created includes a user profile, their objectives, and their contracting information needs. This document was posted [here](https://docs.google.com/document/d/1zdgqSf-LUFVxO6Y_7v1cQf7l0vx35-p502jAI49JRmQ/edit?usp=sharing) for public comment.

Drawing on these summaries we then identified 141 specific user requirements and 145 related technical requirements for the open contracting data standard. You can find a list of all the requirements we identified [here](https://docs.google.com/a/webfoundation.org/spreadsheets/d/1m_Kr7I5XqM7PFcz75ZNmcdFCzLaike_IsEmAh5eN-WE). 

For the most recent release of the standard we have worked through over 50 of 
the requirements identified, and have found that 30 are already handled by fields in the draft standard. For the remaining requirements, a number have resulted in [issues](https://github.com/open-contracting/standard/issues)
 for future cycles of development logged on the standards GitHub pages, and others highlight some of the tools that may need to be created alongside the standard, such as aggregators and analysis tools.

These use cases not only demonstrate what can and could be done with open contracting data, but will also shape the development of the Open Contracting Data Standard as we move towards defining the field-level specification.

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

Over the coming months (September - November 2014) we are working towards a version 1.0 standard which can be implemented, with future changes taking place through an open consultative process.

To get there:

* We are inviting general feedback on the data model and fields in this beta release through the [public mailing list](http://groups.google.com/a/webfoundation.org/group/public-ocds/) and/or by commenting on the document directly (see instructions at the top of this page);

* We are establishing working groups around the private sector, civil society, and publishers to provide additional input;  

* We will be exploring further user demands and building these into the standard by:
	* Completing an assessment of user requirements and how these can be met either directly in the standard, or in accompanying tools and services;
	* Building up a list of issues to be addressed in the next iteration of the standard as we move towards version 1.0 later in the year - and prioritising these in consultation with key potential users of open contracting data; and
	* Using the GitHub issue tracker to identify which requirements can be met over the short-term, and which will need further development beyond the version 1.0 release.

* We will conduct field missions to the first two pilot countries in October 2014 to: 
	* Explore how the standard may be adapted to other contracting use cases outside public procurement including extractives and land;
	* Meet and/or host workshops with civil society and government to better understand demand use-cases; and
	* Compare the draft data standard with country-specific procurement datasets including the possibility of piloting the data standard.


## Acknowledgements

The Open Contracting Data Standard is a core product of the [Open Contracting Partnership (OCP)](http://www.open-contracting.org/). Version 1.0 of the standard is being developed for the OCP by the [World Wide Web Foundation](http://www.webfoundation.org), through a project supported by The [Omidyar Network](http://www.omidyar.com/) and the [World Bank](http://www.worldbank.org)".

This document contains significant contributions from Sarah Bird ([Aptivate](http://www.aptivate.org)), Ana Brandusescu and Tim Davies (World Wide Web Foundation). Other contributors include: Jose M. Alonso (World Wide Web Foundation), Steven Davenport (World Bank), Lindsey Marchessault, Michael Roberts (World Wide Web Foundation), and Marcela Rozo (World Bank).
