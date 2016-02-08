# What to publish

Increasing the transparency, efficiency and effectiveness of public contracting is a process of constant improvement. 

OCDS sets out three levels for disclosure (basic, intermediate and advanced), alongside a 5* framework for the technical approach to data publication for publishers to self-assess themselves against. 


![Levels](../../../assets/levels_en.png)


This supports step-by-step improvement of open contracting data and document disclosure on the web.

## Publication levels: data

The basic, intermediate and advanced levels provide guidance on the specific kinds of data governments should be able to publish.

### Basic
The **basic** level captures data that should already be available in most contracting data systems, and that provides users with an overview of contracting processes.

Basic level data includes: 

* buyer name and address; 
* tender identifiers, titles, descriptions, status, procurement method, period, item descriptions and quantities,
* documents associated with the tender; 
* award identifiers, titles, descriptions, dates, values;
* selected supplier names and addresses; 
* contract identifiers, titles, status, period, values, item descriptions and quantities. 

At a basic level, the publication of contract documents and implementation information (milestones, documents and spending transactions) is also recommended. 

### Intermediate

The **intermediate** level may require publishers to take extra steps to provide identifiers that join up data between systems, and that enable users to see changes in contracting processes over time.

In addition to basic fields, intermediate publication involves providing: 

* organisation identifiers for buyers and suppliers; 
* detailed classification of line items in tender, award and contracts; 
* planning information including budget details and associated documents; 
* tender award criteria, anticipated values and submission information;
* tender enquiry periods details;
* details of the number of organisations submitting tenders and a list of their names; 
* contract documents;
* the data of contract signature;
* information and dates for contract implementation milestones;
* documents related to implementation of the contract.

At an intermediate level, publishing documents related to awards, and identifying information on each organisation submitting a tender, is also recommended

### Advanced
The **advanced level** incorporates fields which are important to connect open contracting data with other data sources, and with the real-world impacts of contracting. Publishing this data may require planning for additional data collection and management. 

In addition to basic and intermediate fields, advanced publication involves providing:

* structured information on project milestones at the tender stage;
* regularly updated milestone information during contract implementation;
* detailed unit, quantity and cost information for line items at tender, award and contract stages;
* identifiers for each tendering organisation;
* information on spending transactions to suppliers during contract implementation;

At an advanced level the use of URIs alongside identifiers, to provide links to other datasets, is also recommended.

### Summary

The table below lists each of the fields in OCDS along with a check mark for whether this is Required (X) or Recommended (-) at basic, intermediate or advanced level. 

<iframe src="https://docs.google.com/spreadsheets/d/1EhyC2pbG6Qxly9vMsZhk0tD8xV2mV4c6KeWkJKi5TMQ/pubhtml?gid=1312410321&single=true" width="100%", height="500"></iframe>


## Publication levels: documents

The following list details the documents the priority documents that publishers should provide at different levels of publication. This list is non-exhaustive, and publishers should make other relevant documents available also.

<iframe src="https://docs.google.com/spreadsheets/d/1i2XagfbBcwzQ5Zasz94fAfdeMwWImiJtfcZelveywr4/pubhtml?gid=172990428&amp;single=true&amp;widget=true&amp;headers=false" width="100%", height="500"></iframe>


## How to publish - 5 ☆ approach

The open data movement has established good practices for publishing data on the web. 

Alongside the the basic, intermediate, advanced model, we have mapped OCDS against Tim Berners-Lee’s [Five Stars of Linked Open Data](http://www.w3.org/DesignIssues/LinkedData.html) approach and have set out how publishers can achieve 3 ☆ data and higher.

Each level increase makes data more accessible, re-usable and valuable. 

### ☆ Upload basic open contracting information to the web

Take information on contracting processes in whatever format it is currently available, and make sure it is available to citizens on the Web.

An example of publication at this level would involve uploading all the documents relating to a contract process to an agency website. Good practice would involve using common naming and filing conventions, so users can easily find all the documents related to a specific tender or contract. 

#### Stepping up

Providing documents offers an initial level of transparency, but users have to dig through them to find the key information they need. That’s why providing machine-readable data that can be more easily searched and filtered is important. 


### ☆ ☆ Provide machine-readable data about contracts

Provide machine-readable datasets that contain key information recommended in the Open Contracting Data Standard.

An example of publication at this level would involve providing a downloadable CSV file of contract information extracted from an existing database seeking to use, or map to, field names and data structures recommended by OCDS wherever possible.

The documentation on [flat CSV file serialization](../../../implementation/serialization/#csv) of the standard, and the [OCDS mapper](https://github.com/open-contracting/mapper), may be useful for those seeking to publish at this level.

#### Stepping up
Providing structured data will allow users to perform basic analysis, but until a common standard is used, it will be more difficult to join up contracting information across datasets and to analyze patterns across organizations or sectors. From structured data, the next step is to map this to the OCDS standard.


### ☆ ☆ ☆ Provide structured data using open standards

Using the Open Contracting Data Standard model to publish initiation, award, contract and implementation information for each contracting process.

OCDS provides guidance on the fields to include, and how to structure them using [a JSON schema](../../../schema/reference/) so that third-parties can re-use your data effectively. 

Fully compliant OCDS publication involves providing a release of data for every event or change that occurs in the life of a contracting process (e.g. when a tender is issued, an award made, and a contract signed), and then combining these into a summary record. This is important to enable tracking of change over time. However, there are different paths to take in moving towards this, and technical assistance from the community can be sought to identify the best approach.

An example of good quality publication at this level might involve regularly generated releases and records published in bulk files for download and also made available through query interfaces and APIs. 

#### Stepping up

Publishing data at custom download locations, or through custom query interfaces, requires users to manually discover and access data. 

Applying best practices for publishing on the web will allow automatic discovery of information, making contracting information more searchable for humans, easier to track and follow at a per-contract level, and more accessible for powerful big-data analysis that can make connections across many open contracting datasets. 


### ☆ ☆ ☆ ☆ Use best practices for data on the web

Make each **release** and **record** describing a contracting process accessible at its own persistent URI (web address).

Provide feeds that detail recently changed information, and that allow users to search for specific kinds of tenders, awards or contracts (for example, by the classification of goods and services being procured). 

Use [established protocols](../../hosting#discovery-and-apis) to support discovery of your data, and to provide atom feeds of recently updated data. At this level, publishers may also expose data through an API, following community established conventions for API operation.

The use of these protocols, and following API conventions, will allow aggregators and other analysts to integrate this open contracting data in minutes and hours or work, rather than days, weeks and months. 

In the future OCDS may also have an RDF serialization to enable linked data publication at this level.

#### Stepping up
Contracting data may contain many cross-references to other important datasets - from government budgets, to company registers and registers of public interest. If 4 or 5 ☆ data is published for any of these, then OCDS can be used to make links between these datasets. 

This will allow users to follow the links to discover more about the context of the contracting processes they are exploring, and will allow big-data analysis linking in these different datasets. For example, following links to a company register to discover whether a company awarded a contract has been dissolved, or following links to budget and spending information. 


### ☆ ☆ ☆ ☆ ☆ Make links to other datasets

OCDS provides spaces to give URIs to identify key dataset elements. By drawing on data published on the web by other agencies, and maintaining integration between your systems, you can provide links to these other data points within your OCDS data.

This level builds upon 4 ☆ publication, and helps to build a joined up web of data.

An example of publication at this level would involve including organization URIs to point to company registers, budget URIs to point to budget lines, and spending URIs to point to spending information (i.e. using web links to identify things, with those web links returning data on the things identified.).

For simplicity, the OCDS does not yet include URI fields at all points of the standard, but these can be added as extensions in collaboration with 5 ☆ linked data publishers. 

#### Stepping up
Whatever level you are at - publishing data is only part of the process. It is important to also [engage with users](http://www.opendataimpacts.net/engagement/) and to think about how to build your open data back into your organizational processes, closing the feedback loop.
