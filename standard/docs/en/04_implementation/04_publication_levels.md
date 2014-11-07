[TOC]

# Progressive Publication

<span class="lead">Increasing the transparency, efficiency and effectiveness of public contracting is a process of constant improvement. Governments, platform providers and other organizations can all make progressive step-by-step changes to their practice to achieve the highest possible levels of open contracting data publication on the web.</span>

<span class="lead">This section sets out a series of steps towards improving the content, and the technical openness, of contracting data.</lead>

## Content - what to include

The table below shows the different categories of data that publishers should seek to collect, manage and publish as part of an open contracting process. These are divided into three levels:

* **Basic** - these items are commonly held by organisations and provide a basic overview of a contracting process
* **Intermediate** - these items are important to providing joined-up open contracting data, letting users key features of a contracting process over time. They may require publishers to connect up data in their internal systems.
* **Advanced** - these items are important to connecting open contracting data with other data sources (e.g. budget), and with real-world impacts (locations, milestones etc.). They may require some publishers to collect and manage additional data. 

The detailed fields that can be used to represent each of these items are described in the ODCS schema, but the table below can be used for policy-level planning. 

<iframe src="https://docs.google.com/spreadsheets/d/12W3C3lHY2FW2MRuCGm-kV53bk03TGhXB_z223Rg8xUg/pubhtml?gid=428233391&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="500"></iframe>


## How to publish

The open data movement has established good practices for publishing data on the web. Building on Tim Berners-Lee’s [Five Stars of Linked Open Data](http://www.w3.org/DesignIssues/LinkedData.html) approach, we have set out a model that encourages publishers to strive for 3 ☆ and higher data publication. 

Each level increase makes data more accessible, re-usable and valuable. 

### ☆ Upload basic open contracting information to the web

<span class="lead">Take information on contracting processes in whatever format it is currently available, and make sure it is available to citizens on the Web.</span>

An example of publication at this level would involve uploading all the documents relating to a contract process to an agency website. Good practice would involve using common naming and filing conventions, so users can easily find all the documents related to a specific tender or contract. 

#### Stepping up

Providing documents offers an initial level of transparency, but users have to dig through them to find the key information they need. That’s why providing machine-readable data that can be more easily searched and filtered is important. 


### ☆ ☆ Provide machine-readable data about contracts

<span class="lead">Provide machine-readable datasets that contain key information recommended in the Open Contracting Data Standard.</span>

An example of publication at this level would involve providing a downloadable CSV file of contract information extracted from an existing database, but not necessarily using all the field names and data structures recommended by OCDS.

The documentation on flat file serialization of the standard may be useful for those seeking to publish at this level.

#### Stepping up
Providing structured data will allow users to perform basic analysis, but until a common standard is used, it will be more difficult to join up contracting information across datasets and to analyse patterns across organisations or sectors. From structured data, the next step is to map this to the OCDS standard.


### ☆ ☆ ☆ Provide structured data using open standards

<span class="lead">Using the Open Contracting Data Standard model to publish initiation, award, contract and implementation information for each contracting process.</span>

OCDS provides guidance on the fields to include, and how to structure them so that third-parties can re-use your data effectively. 

Fully compliant OCDS publication involves providing a release of data for every event or change that occurs in the life of a contracting process (e.g. when a tender is issued, an award made, and a contract signed), and then combining these into a summary record. This is important to enable tracking of change over time. However, there are different paths to take in moving towards this, and technical assistance from the community can be sought to identify the best approach.

An example of good quality publication at this level might involve regularly generated releases and records published in bulk files for download and also be made available through query interfaces and APIs. 

#### Stepping up
Using data at custom download locations, or through custom query interfaces, requires users to still manually discover and access data. 

Applying best practices for publishing on the web will allow automatic discovery of information, making contracting information more searchable for humans, easier to track and follow at a per-contract level, and more accessible for powerful big-data analysis that can make connections across many open contracting datasets. 


### ☆ ☆ ☆ ☆ Use best practices for data on the web

Make each **release** and **record** describing a contracting process accessible at it’s own persistent URI (web address).

Provide feeds that detail recently changed information, and that allow users to search for specific kinds of tenders, awards or contracts (for example, by the category of goods and services being procured). 

Use the /.well-known/ protocol to let machines discover your data. 

An example of publishing at this level might involve being able to look up URLs such as /oc/contractProcess/1234 to return a record in JSON format, and that record then detailing a list of releases, each with their own URIs such as /oc/release/1234-1 and /oc/release/1234-2 which detail the different moments in the life of the contracting process. Users interested in the contract could regularly check /oc/contractProcess/1234 to discover updates, or could use a search service at /oc/search/?initiation.item.classification=CPV:03451100-7 to lookup a feed of all the tenders for ‘Bedding Plants’. 

The /.well-known/ file will allow aggregators and other analysts to integrate this open contracting data in minutes and hours or work, rather than days, weeks and months. 

In future OCDS may also have an RDF serialization to enable linked data publication at this level.

#### Stepping up
Contracting data may contain many cross-references to other important datasets - from government budgets, to company registers and registers of public interest. If 4 or 5 ☆ data is published for any of these, then OCDS can be used to make links between these datasets. 

This will allow users to follow the links to discover more about the context of the contracting processes they are exploring, and will allow big-data analysis linking in these different datasets. For example, following links to a company register to discover whether a company awarded a contract has been disolved, or following links to budget and spending information. 


### ☆ ☆ ☆ ☆ ☆ Make links to other datasets

<span class="lead">OCDS provides spaces to give URIs to identify key dataset elements. By drawing on data published on the web by other agencies, and maintaining integration between your systems, you can provide links to these other data points within your OCDS data. </span>

This level builds upon 4 ☆ publication, and helps to build a joined up web of data.

An example of publication at this level would involve including organisation URIs to point to company registers, budget URIs to point to budget lines, and spending URIs to point to spending information.

For simplicity, the OCDS does not yet include URI fields at all points of the standard, but these can be added as extensions in collaboration with 5 ☆ linked data publishers. 

#### Stepping up
Whatever level you are at - publishing data is only part of the process. It is important to also [engage with users](http://www.opendataimpacts.net/engagement/) and to think about how to build your open data back into your organisational processes, closing the feedback loop.

## Examples

As use of the OCDS specification develops we will compile examples to show publication at each of these levels.