Lots
====

## Metadata

To use this extension, include its URL in the ```extension``` array of your release or record package.

```json
{
    "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_lots_extension/v1.1.1/extension.json"],
    "releases":[]
}
```

This extension is maintained at [https://github.com/open-contracting/ocds_lots_extension](https://github.com/open-contracting/ocds_lots_extension)

## Documentation

When a single tender is broken down into parts that can be bid upon, and awarded, separately, this is modelled using the **lots extension**.

The lots extension maintains the overall structure of an OCDS release, with items, documents and milestones nested immediately within ```tender```, ```award``` and ```contract``` items, but it introduces an array of Lots in the ```tender``` section, and the ability to cross-reference a specific ```relatedLot``` for each item, and an array of ```relatedLots``` for documents, milestones and awards.

Optional ```lotDetails``` and ```lotGroups``` section allow more complex conditions around the award of lots to be expressed, such as the maximum value of a group of lots.

This means that systems which are not 'lot aware' can still understand the overall value of contracting taking place, key events, and relationships between buyers and suppliers. At the same time, 'lot aware' systems can make use of the cross-referenced information to present a lot-centric view on the information to users, or to analyze contracting lot by lot.

### Related Lot

The ```relatedLot``` (singular) property is available for:

* items

An array of ```relatedLots``` (plural) can be provided for each of:

* documents
* milestones
* awards

When lots are used, **all** items should have a ```relatedLot``` property.

Documents and milestones can optionally have a ```relatedLots``` property. Those without this property should be interpreted as applicable to the tender as a whole.

The items within an award should each have a ```relatedLot``` property, but publishers may choose to also reference all the lots an award relates to at the award level using ```relatedLots```

Where the bid extension is also in use, each bid can also declare its related lots.

### Worked example

A tender is issued for consultancy in the development of a new public building. This might include items for:

* Architectural design
* Architectural advisory services
* Civil engineering consultancy
* Structural engineering consultancy

Although part of the same tender, the buyer is willing to award these different items to different firms, and so divides the tender into three lots.

```json
{
  "publishedDate": "2017-02-08T14:00:00Z",
  "publisher": {
    "scheme": "GB-COH",
    "uid": "09506232",
    "name": "Open Data Services Co-operative Limited",
    "uri": "http://standard.open-contracting.org/examples/"
  },
  "license": "http://opendatacommons.org/licenses/pddl/1.0/",
  "publicationPolicy": "https://github.com/open-contracting/sample-data/",
  "uri": "https://github.com/open-contracting/ocds_lots_extension/blob/master/examples/lots.json",
  "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_lots_extension/v1.1/extension.json"],
  "version": "1.1",
  "releases": [
    {
      "language": "en",
      "ocid": "ocds-213czf-lots-00001",
      "id": "ocds-213czf-lots-00001-01-tender",
      "date": "2017-02-08T14:00:00Z",
      "tag": [
        "tender"
      ],
      "initiationType": "tender",
      "buyer": {
          "id": "ZZ-MISC-anytown",
          "name": "AnyTown Council "
      },
      "tender": {
        "id": "ocds-213czf-lots-00001-01-tender",
        "title": "Architecture and engineering services",
        "description": "The authority is seeking support to construct a new public building.",
        "procurementMethod": "open",
        "status": "active",
        "items": [
          {
            "id": "0001",
            "description": "Architectural advice",
            "classification": {
              "scheme": "CPV",
              "id": "71210000",
              "description": "Advisory architectural services"
            },
            "relatedLot":"lot-1"
           },
           {
            "id": "0002",
            "description": "Architectural design",
            "classification": {
              "scheme": "CPV",
              "id": "71220000",
              "description": "Architectural design services"
            },
            "relatedLot":"lot-1"
           },
           {
            "id": "0003",
            "description": "Civil engineering consultant",
            "classification": {
              "scheme": "CPV",
              "id": "71311000",
              "description": "Civil engineering consultancy services"
            },
            "relatedLot":"lot-2"
           },
           {
            "id": "0004",
            "description": "Structural engineering services",
            "classification": {
              "scheme": "CPV",
              "id": "71312000",
              "description": "Structural engineering consultancy services"
            },
            "relatedLot":"lot-1"
           }
        ],
        "value": {
          "amount": 1200000,
          "currency": "GBP"
        },
        "lots":[
            {
                "id":"lot-1",
                "title":"Architectural services",
                "description":"For architectural services delivered in the project",
                "status":"active",
                "value":{
                    "currency":"GBP",
                    "amount":200000
                }
            },
            {
                "id":"lot-2",
                "title":"Civil engineering services",
                "description":"For civil engineering services delivered in the project",
                "status":"active",
                "value":{
                    "currency":"GBP",
                    "amount":600000
                }
            }
            ,{
                "id":"lot-3",
                "title":"Structural engineering",
                "description":"For structural engineering consultancy delivered in the project",
                "status":"active",
                "value":{
                    "currency":"GBP",
                    "amount":600000
                }
            }
        ],
        "lotGroups":[{
            "id":"lot-group-1",
            "relatedLots":["lot-2","lot-3"],
            "optionToCombine":true,
            "maximumValue":{
              "currency":"GBP",
              "amount":1000000
            }
        }],
        "lotDetails":{
            "maximumLotsBidPerSupplier":4,
            "maximumLotsAwardedPerSupplier":2
        }
      }
    }
  ]
}
```

### Schema

```eval_rst
.. extensiontable::
    :extension: lots
    :definitions: Lots
```
