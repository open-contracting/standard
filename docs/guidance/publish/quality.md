# Assessing data quality

The Open Contracting Data Standard enables publication of detailed information about all stages of the public contracting process (and extensions can be used for additional information not covered by the core standard).

The limits of what can be published using the OCDS are usually defined by (1) absence of a legal mandate for publication and (2) challenges with data collection.

The OCDS was also designed to maximize the utility of contracting information for performing analysis on:

* Generating market opportunities for the private sector to fairly compete for public contracts 
* Achieving value for money for government
* Strengthening the transparency, accountability and integrity of public contracting
* Monitoring the effectiveness of service delivery
* Improving internal efficiency

However, the less information you publish, and the more incomplete the information, the less useful it will be for these objectives.

For example, if your stakeholders are interested to monitor the integrity of the public procurement system, or its competitiveness, you will need data about bidders to be published. If your stakeholders want to monitor late payments to contractors, you will need to publish information about the dates that invoices are received and paid.

We have prepared a [list of procurement indicators related to key use cases](http://bit.ly/UsingIt-indicators) that indicates which OCDS fields are needed for some of the most common goals.

Regulations or policies might need to be changed to enable publication of additional information to increase the scope and coverage of your OCDS publication.

In addition, you might have challenges collecting complete and accurate information. This challenge might have a variety of causes (poor compliance rates, lack of access to the internet, lack of incentives). If you are experiencing these challenges, OCP can help you think through approaches to improving the quality and completeness of the information you collect.

Finally, you might have challenges transforming that information into the OCDS format and publishing it in a manner that is accessible and user friendly. For this, you can reach out to our [Data Support Team](../../support/index).

Understanding all of the challenges above, we understand that increasing the transparency, efficiency and effectiveness of public contracting is a process of constant improvement. Therefore, we describe an iterative framework for assessing the quality and completeness of OCDS publications below.

## Basic criteria

All OCDS publications ought to meet the following criteria:

1. **Registered**: The data uses a [registered OCID prefix](../../schema/identifiers.md#contracting-process-identifier-ocid).
1. **Reviewable**: The [OCDS Data Review Tool](https://standard.open-contracting.org/review/) can report results for the data.
1. **Appropriate**: The data is in semantic accordance with OCDS. Additional fields and codes do not overlap semantically with standardized fields and codes.
1. **Relevant**: The data answers "who bought what from whom, for how much, when, and how" for at least one contracting process.
1. **Discoverable**: It is possible to discover the data by navigating a website whose homepage is indexed by popular web search engines.
1. **Representative**: The data describes all contracting processes within a relevant population. For example: all contracts for a public-private partnership; all above-threshold contracts since 2020 excluding those by state-owned enterprises, etc.
1. **Active**: The data contains a contracting process release with a top-level `date` value within the previous four calendar quarters.
1. **Retrievable**: It is possible for software to download the data in full, either by using an HTML page listing bulk download URLs, or by using machine-readable data as the only input.

The Data Support Team is happy to review draft and newly published OCDS data and can work with publishers with advice to meet the above criteria. A publication that does not meet this minimum threshold will not be listed as a publisher by OCP as part of [OCP’s regular reporting](https://www.open-contracting.org/why-open-contracting/learning/).

## Continuous improvement

From the minimum threshold above, we want to support publishers to continue to improve the quality and completeness of their publications across a variety of dimensions, including:

### Completeness

Improvement on the below indicators demonstrate that the published information is becoming more complete about the contracting processes within the publisher’s jurisdiction.

1. Increase the number of indicators covered (volume)
1. Increase the average number of fields covered per contracting process (density)
1. Increase the number of buyers covered ("who")
1. Increase the number of methods covered ("how")
1. Publish subsequent releases per OCID to show how the contracting process is progressing over time
1. Increase the temporal coverage into the past ("when")

### Timeliness

1. Publish multiple updates per contracting process
1. Decrease the delay between the information's creation and publication

### Accessibility

Improvements on the below indicators demonstrate that it is becoming easier for users to access the published information.

1. Publish a user guide or publication policy that describes the scope, at minimum
1. Publish API documentation that describes the endpoints and parameters, at minimum
1. Increase the number of access methods (API endpoints, bulk downloads)
1. Increase the number of data formats (JSON, Excel, CSV)
1. Facilitate indirect data use (e.g. search, dashboards, etc.)

### Retrievability and legal

1. Decrease the number of HTTP errors
1. Use a data license that conforms to the [Open Definition](https://opendefinition.org)

### Correctness

Improvement on the below indicators demonstrates that the concepts are being published more correctly, improving usability.

1. Decrease the number of types of structural errors
1. Decrease the average number of structural errors per contracting process
1. Decrease the number of [conformance](../../schema/conformance_and_extensions) issues
1. Decrease the number of types of quality warnings
1. Decrease the average number of quality warnings per contracting process

As publishers improve, the Data Support Team can work with them to identify how they can improve on the above criteria. OCP will note whether a publisher has improved in [OCP’s regular reporting](https://www.open-contracting.org/why-open-contracting/learning/).

## Advanced criteria

The most advanced OCDS publishers will demonstrate that they have achieved the below criteria:

**Completionist**  
_Indicates_: Whether the public can get data about all contracts that are disclosable according to local laws and regulations.  
_Measures_: The percentage of all contracting processes that are disclosed in OCDS data, by number and by value.

**Timely Publisher**  
_Indicates_: Whether the public can track the progress of a contracting process.  
_Measures_: Whether the OCDS publication is updated daily, including information from human-readable notices, that is published within an expected number of days of the notice.

**Thorough Publisher**  
_Indicates_: Whether the data contains details that are under-disclosed globally.  
_Measures_: Whether the publisher discloses the planning and implementation stages, and the transactions, milestones, planning values, call offs from framework agreements, bidders, bid values, items, locations fields; and whether they publish change history.

**Silo Breaker**  
_Indicates_: Whether the data supports linking to other datasets.  
_Measures_: The use of [org-id.guide](http://org-id.guide) organization identifiers, item classification schemes like CPV, and other linkages.

**OCDS Champion**  
_Indicates_: Whether OCDS data matches or exceeds the features of non-OCDS data.  
_Measures_: Any differences in field coverage, or access methods.

**User Champion**  
_Indicates_: Whether the publisher uses its own data and encourages data use by stakeholders.  
_Measures_: Whether the publisher calculates any key performance indicators or uses data for reporting purposes. Whether the publisher has designed user friendly APIs and dashboards or tools for non-technical users.

**Useful Publication**  
_Indicates_: Whether it is possible to answer the most fundamental questions of priority use cases (who buys what from who, when and for how much).  
_Measures_: Coverage of specific fields: tender value, tender period, tender title, buyer name, award value, award date, supplier name, contract period.

```{note}
The above described framework for assessing OCDS quality replaces the previous Basic/Intermediate/Advanced and Publication Star ☆ systems.
```
