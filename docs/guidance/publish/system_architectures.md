# System architectures

The publication of OCDS data involves the creation of a conversion process. Like an ETL process, data has to be extracted from one or more sources, converted and either served or stored.

This process needs an adequate architecture to support it. Its design depends on several factors:

* Whether is possible to extend existing systems, or a new system will be built,
* The number and nature of the live systems,
* The technical resources available to the publisher, like storage and processing capabilities. This includes the availability of technical personnel to maintain systems and modules.

Other considerations that affect the design are:

* Individual OCDS documents for each process should be available at unique persistent URLs.
* Bulk downloads in JSON, CSV (and, if appropriate, Excel) formats should be available. These files should be segmented according to one or more criteria, like time periods.
* Users should be able to locate the collections of releases and records they want.

This guidance describes some design approaches with their advantages and disadvantages. This is not an exhaustive list, but it can be used to inform the design of the publication system.

## On-demand transformation from live systems

In this scenario, each source system converts data in OCDS format on demand. Data is not stored but gets converted each time a user or third party invokes the conversion process. This is the easiest path when a single live system manages all contracting processes. But it requires modifications to the system to add an OCDS conversion module.

An API performs data transformation on the fly each time it receives a request.

![Direct Publication 2](../../_static/png/directPublication2.png)

The conversion module produces OCDS releases and/or records wrapped in packages.

This approach does not need extra storage space. But it may be not possible to provide persistent URLs for releases, nor a change history for each process.

The [easy releases guidance](easy_releases) explains how to achieve a conformant OCDS implementation where it is not possible to provide a full change history.

Bulk downloads can be provided as part of the API. Live queries may stress the live systems if they need to scan large portions of data.


## Separate OCDS datastore

In the scenarios that follow, a middleware component converts and stores the data in OCDS format. This has some advantages:

* It is possible to merge an centralize data from more than one systems in a single datastore.
* It may relieve live systems from expensive queries.
* It may enable the generation of the change history for each contracting process.

On the other hand, there is a cost of maintaining a separate datastore. In these scenarios, we assume an API provides access to OCDS data.

Publishers should consider how to store OCDS data. Releases are immutable so can be stored as they are, but records change over time. The process can build records on each API call, or store and update them each time a new release is created. The API must return OCDS data wrapped in a release or record package. Usually there is no need to store wrapped OCDS data, since package data can be generated in real time.

The [change history guidance](../../getting_started/change_history) describes OCDS releases and records and their different components.


### Pull and convert

In this scenario an automated process pulls data from live systems to the middleware system. The middleware performs the conversion to OCDS and maintains a datastore in OCDS format.

![Pull and Convert](../../_static/png/pullAndConvert.png)

The key benefit of this approach is that the middleware system can store the change history. This is especially good when source systems do not maintain historic data.

This approach may need some changes to live systems to allow the middleware to pull data. The middleware system merges and centralizes data in a single place.

To add more source systems, the OCDS conversion module needs to be updated to pull data from the new system(s).

An important decision in the implementation is the frequency to pull data. If the frequency is low, there is a risk of losing the detail of individual changes.

An alternative to the pull mechanism is to use a push mechanism in each source system. Specific events or changes to the data would trigger a data push to the middleware. This approach can mitigate the risk of losing individual changes. But this may need bigger modifications to the source system(s).

European Dynamics developed an e-procurement system with a similar approach for OCDS output. The system was built for the Zambian Public Procurement Agency.

### Convert and push

This scenario is a combination of the two previous scenarios. Live systems perform the conversion of data to OCDS format. They push converted data to a middleware, which maintains an OCDS format datastore. An API in the middleware system serves the OCDS data.

![Convert and Push](../../_static/png/convertAndPush.png)

This approach puts the burden of data conversion in live systems. Yet it may be a solution for publishers with a single source system which does not store the change history.

This approach may also be suitable to combine data from many source systems. Each source system becomes an OCDS publisher. The middleware becomes less complex since it only ingests data in a single format.

The [OpenProcurement](http://openprocurement.org/en/) system adopted a similar approach. This system was developed in Ukraine and it's the base for the [Prozorro](https://prozorro.gov.ua/en/) platform. Prozorro uses OCDS building blocks as the foundation for live systems data models.

A variant in this scenario is to store files in a web-accessible file system, as shown below. A periodical invocation of the conversion module updates the file system.

![Direct Publication 1](../../_static/png/directPublication1.png)

The file system ensures that each OCDS document has a persistent URL for access. But a downside is that the volume of data may grow fast, as plain files can take significant space. The file system can provide a change history as long as releases are never overwritten. Bulk downloads can be generated periodically and stored in the file system. Records may be impossible to produce if there is more than one system.

### Manual import

In this scenario a middleware system sits between live systems and the API.

Data is manually exported from live systems into files. The files are uploaded to the middleware system, which converts the data to OCDS. The system stores the data in OCDS format.

![Manual Import](../../_static/png/manualImport.png)

A disadvantage in this approach is the potential of failures. Input files may be corrupted or have unexpected formats due to changes or errors in the live systems.

There’s a documented example of this approach in the work Development Gateway did in [Vietnam](https://www.developmentgateway.org/blog/under-hood-open-source-dashboard-procurement-vietnam).

## Additional considerations

When designing an architecture, publishers should consider the following:

* **Search endpoints**. An API can provide more than individual releases and records. Endpoints help to filter data by different parameters like suppliers and product types. Another consideration is providing alternative formats, like CSV and Excel data. This is important for users who are more familiar with spreadsheets.
* **Documents**. OCDS includes the disclosure of documents. Often, systems link out to documents on external platforms, where link-rot can set-in. The best systems will ensure that documents are archived but still available.
