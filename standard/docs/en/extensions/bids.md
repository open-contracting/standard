# Bid statistics and details

## Metadata

To use this extension, include its URL in the `extension` array of your release or record package.

```json
{
    "extensions": ["https://raw.githubusercontent.com/open-contracting/ocds_bid_extension/v1.1.3/extension.json"],
    "releases": []
}
```

This extension is maintained at [https://github.com/open-contracting/ocds_bid_extension](https://github.com/open-contracting/ocds_bid_extension)

## Documentation

Information on bids submitted as part of a contracting process is important for many forms of analysis, including:

* Market analysis for understanding the competitiveness of a given marketplace;
* Red flag analysis for understanding potential corruption risks; and
* Value for money analysis;

Regulatory regimes vary on the extent to which they allow information on bidding to be proactively published, and at what point in the procurement process. In some systems and processes, a list of invited bidders will be published at the start of tendering, and full details and documents on the bids received may be disclosed when evaluation is complete. In other systems, only summary statistics on the number of bids received may be made public.

The OCDS bid extension introduces a new, flexible, top-level section to each contracting process to capture bidding information. Implementers will need to assess which fields are applicable to their local regulatory regime, and to local use-cases.

### Bid Statistics

The `bids/bidStatistics` array can be used to represent key statistical information about the number of bids and bidders. Each entry in the array is a `BidsStatistic` object containing at least:

* An identifier;
* A measure, from the bidStatistics codelist;
* A value for that measure;

```eval_rst
.. extensiontable::
   :extension: bids
   :definitions: BidsStatistic
```

#### Bid Statistics Codelist

This is an **open** codelist. Publishers can add their own codes to this list. When doing so, publishers are encouraged to engage with the open contracting community to agree upon definitions of each code.

For example, publishers may wish to add statistics on minority or women owned businesses, or bids that meet certain environmental standards and targets.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../../build/codelists/current_lang/bidStatistics.csv
```

### Bid Details

The `bids/details` array is used to provide one or more `Bid` objects, each representing a unique bid received.

```eval_rst
.. extensiontable::
   :extension: bids
   :definitions: Bid
```

#### Bid Status Codelist

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../../build/codelists/current_lang/bidStatus.csv
```

### Example

Below is an example of a bids extension:

```json
{
  "bids": {
    "statistics": [{
      "id": "1.0",
      "measure": "validBids",
      "value": 1,
      "date": "2016-12-09T01:00:00+01:00",
      "notes": "This statistic covers the total number of unique bids received that were considered valid against relevant criteria."
    }, {
      "id": "2.0",
      "measure": "disqualifiedBids",
      "value": 1,
      "date": "2016-12-10T01:00:00+01:00",
      "notes": "This statistic covers the total number of unique bids received that were disqualified."
    }],
    "details": [{
      "id": "1.0",
      "date": "2016-12-09T01:00:00+01:00",
      "status": "valid",
      "value": {
        "amount": 1000,
        "currency": "USD"
      },
      "documents": [{
        "id": "1.0",
        "documentType": "evaluationReports",
        "title": "Mega Consortium Bid Evaluation Report",
        "description": "This document provides details of the evaluation of the bid submitted by Mega Consortium",
        "url": "http://communications.gov.example/example_ppp/evaluationReport_megaConsortium.pdf",
        "datePublished": "2016-11-17T10:00:00-06:00",
        "format": "application/pdf",
        "language": "en",
        "author": "Ministry of Communications"
      }],
      "tenderers": [{
        "id": "MEGA",
        "name": "Mega Consortium"
      }]
    }, {
      "id": "2.0",
      "date": "2016-12-10T01:00:00+01:00",
      "status": "disqualified",
      "value": {
        "amount": 1500,
        "currency": "USD"
      },
      "documents": [{
        "id": "1.0",
        "documentType": "evaluationReports",
        "title": "Beta Consortium Bid Evaluation Report",
        "description": "This document provides details of the evaluation of the bid submitted by Beta Consortium",
        "url": "http://communications.gov.example/example_ppp/evaluationReport_betaConsortium.pdf",
        "datePublished": "2016-11-18T10:00:00-06:00",
        "format": "application/pdf",
        "language": "en",
        "author": "Ministry of Communications"
      }],
      "tenderers": [{
        "id": "BETA",
        "name": "Beta Consortium"
      }]
    }]

  },
  "awards": [{
    "id": "111",
    "title": "Example PPP contract award",
    "description": "Award of Example PPP contract to Mega Consortium",
    "status": "active",
    "date": "2016-12-17T10:00:00-06:00",
    "relatedBid": "1.0"
  }]
}
```

### Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

### Changelog

#### v1.1.3

* Disallow required fields `BidsStatistic.id`, `BidsStatistic.measure`, `BidsStatistic.value` from being null
* Disallow `Bids.statistics` from having null in its array of objects
* Allow `Bids.statistics` to be null
* Add enum to `BidsStatistic.status`
* Move `BidsStatistic.requirementResponses` to requirements extension
* Add descriptions to bidStatus.csv
* List codelists in extension.json
* Add example to documentation
* Add tests and tidy code
