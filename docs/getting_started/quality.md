# Assessing data quality

The Open Contracting Data Standard enables publication of detailed information about all stages of the public contracting process (and extensions can be used for additional information not covered by the core standard).

The limits of what can be published using the OCDS are usually defined by (1) absence of a legal mandate for publication and (2) challenges with data collection.

The OCDS was also designed to maximize the utility of contracting information for:

* Value for money analysis
* Fairness and ease of doing business
* Deterring corruption and monitoring the integrity of the procurement system
* Boosting the efficiency and effectiveness of public contracts.

However, the less information you publish, and the more incomplete the information, the less useful it will be for these objectives.

For example, if your stakeholders are interested to monitor the integrity of the public procurement system, or its competitiveness, you will need data about bidders to be published. If your stakeholders want to monitor late payments to contractors, you will need to publish information about the dates that invoices are received and paid.

We have prepared a [Usability spreadsheet](https://docs.google.com/spreadsheets/d/1nG7e52E1CXOXoUjz6pimW4Z7er9u3DJSs98QKdJJioE/edit#gid=110864222) that indicates which OCDS fields are needed for some of the most common goals.

Regulations or policies might need to be changed to enable publication of additional information to increase the scope and coverage of your OCDS publication.

In addition, you might have challenges collecting complete and accurate information. This challenge might have a variety of causes (poor compliance rates, lack of access to the internet, lack of incentives). If you are experiencing these challenges, OCP can help you think through approaches to improving the quality and completeness of the information you collect.

Finally, you might have challenges transforming that information into the OCDS format and publishing it in a manner that is accessible and user friendly. For this, you can reach out to our [OCDS Helpdesk](../support/index) for support.

Understanding all of the challenges above, we understand that increasing the transparency, efficiency and effectiveness of public contracting is a process of constant improvement. Therefore, we describe an iterative framework for assessing the quality and completeness of OCDS publications below.

## Basic criteria

All OCDS publications ought to meet the following criteria:

1. **Registered**: The data uses a [registered OCID prefix](../../schema/identifiers/#contracting-process-identifier-ocid).
1. **Discoverable**: It is possible to discover the data by navigating a website whose homepage is indexed by popular web search engines.
1. **Retrievable**: It is possible to automate the download of all the data, either using an HTML page listing bulk download URLs, or using only machine-readable data as input.
1. **Reviewable**: The [OCDS Data Review Tool](https://standard.open-contracting.org/review/) is able to report results on the data.
1. **Appropriate**: Concepts are published in semantic accordance with the rules of the OCDS (or registered extensions) rather than using a non-OCDS field or code.
1. **Active**: For each publisher, there is an OCDS release with a top-level `date` field value within the last 12 months.
1. **Parity**: For each publisher, for the _time period_ and _contracting authorities_ covered by the data, there isn’t another dataset by the same publisher that covers more than 25% more contracting processes.

The OCDS Helpdesk is happy to review draft and newly published OCDS data and can work with publishers with advice to meet the above criteria. A publication that does not meet this minimum threshold will not be listed as a publisher by OCP as part of [OCP’s regular reporting](https://www.open-contracting.org/why-open-contracting/learning/).

## Continuous improvement

From the minimum threshold above, we want to support publishers to continue to improve the quality and completeness of their publications across a variety of dimensions, including:

### Completeness

Improvement on the below indicators demonstrate that the published information is becoming more complete about the contracting processes within the publisher’s jurisdiction.

1. Publish subsequent releases per OCID to show how the contracting process is progressing over time
1. Increase the publication of historical information (based on a minimal set of date fields that appear across all sources, e.g. `tender.tenderPeriod`, `awards.date`, and `contracts.dateSigned`)
1. Increase the average coverage of fields per compiled release, for example either new fields not previously published in any release, or an increase in the use of a field across releases (e.g. very little data was published about direct awards and now more is being published about direct awards)
1. Increase the number of contracting authorities covered in the publication
1. Increase the number of concepts covered relative to non-OCDS data

### Correctness

Improvement on the below indicators demonstrates that the concepts are being published more correctly, improving usability.

1. Decrease the types and number of structural errors reported by the OCDS Data Review Tool, e.g. moving from 20 types of errors, each occurring more than 100,000 times, to 10 types of errors, each occurring less than 100 times
1. Decrease the average number of structural errors per release
1. Decrease the number of instances in which a concept is not published in conformance with OCDS semantics
1. Decrease the number of types of quality warnings using OCDS Pelican
1. Decrease the average number of quality warnings per release using OCDS Pelican

### Access

Improvements on the below indicators demonstrate that it is becoming easier for users to access the published information.

11. Publish record packages containing compiled releases
12. Decrease the number of HTTP errors
13. Increase the number of access methods (API endpoints, bulk downloads)

As publishers improve, the OCDS Helpdesk can work with them to identify how they can improve on the above criteria. OCP will note whether a publisher has improved in [OCP’s regular reporting](https://www.open-contracting.org/why-open-contracting/learning/).

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

```{eval-rst}
.. note::

   .. markdown::

      The above described framework for assessing OCDS quality replaces the previous Basic/Intermediate/Advanced and Publication Star ☆ systems.
```
