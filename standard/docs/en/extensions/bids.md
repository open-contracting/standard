Bid statistics and details
==========================

## Metadata

To use this extension, include its URL in the ```extension``` array of your release or record package.

```json
{
    "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_bid_extension/v1.1.1/extension.json"],
    "releases":[]
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

The ```bids/bidStatistics``` array can be used to represent key statistical information about the number of bids and bidders. Each entry in the array is a ```BidsStatistic``` object containing at least:

* An identifier;
* A measure, from the bidStatistics codelist;
* A value for that measure;

#### Bid Statistics Schema 

```eval_rst
.. extensiontable::
   :extension: bids
   :exclude_definitions: Bids Bid
```

#### Bid Statistics Codelist

This is an **open** codelist. Publishers can add their own codes to this list. When doing so, publishers are encouraged to engage with the open contracting community to agree upon definitions of each code. 

For example, publishers may wish to add statistics on minority or women owned businesses, or bids that meet certain environmental standards and targets. 

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: codelists_translated/bidStatistics.csv
```

### Bid details

The ```bids/details``` array is used to provide one or more ```Bid``` objects, each representing a unique bid received. 

```eval_rst
.. extensiontable::
   :extension: bids
   :exclude_definitions: statistics BidsStatistic 
```

#### Bid Status Codelist

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: codelists_translated/bidStatus.csv
```

### Example

ToDo
