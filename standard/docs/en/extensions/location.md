# Location Data

Communicating the location of proposed or executed contract delivery is important to make users of contracting data. 

This extension proposes the addition of two properties to ```items``` to describe location:

* ```deliveryAddress``` - a standard ```Address``` block which can be used to provide a postal address where services should be delivered.
* ```deliveryLocation``` - a new block consisting of GeoJSON and Gazetteer entries to describe a wider range of locations to which the contract line item relates.

It also creates a new gazetteer codelist, currently contained in codelist_usecase2.csv.

**Advantages of this approach**

* It captures a wide range of possible location specifications, including point locations, polygons and lines (useful for roads projects, extractives concessions etc.)
* Delivery Address information provides information that can be used for both geocoding, and for logistics fulfilment;
* It allows different locations to be specified for different line items;

**Disadvantages/limitations of this approach**

* Locations are only specified for ```items```, not at the overall tender, contract or award level. In some cases this may lead either to location data being duplicated across items, or ambiguity about which item the location information should apply to;
* We have to maintain a codelist of recognised Gazetteers;

**Background** 

There are a number of use cases that demand specifying a location for delivery of an item. Discussion can be found in [Issue 26](https://github.com/open-contracting/standard/issues/26).

**Questions**

* Should we allow location to also be attached to other elements aside from items? 


Example usage
=============

Below is an example of a geolocated item:

```json
"items": [
    {
        "id": "item1",
        "description": "Ceremonial Trumpets for Oxford Town Hall",
        "classification": {
            "description": "Trumpets",
            "scheme": "CPV",
            "id": "37312100",
            "uri": "http://purl.org/cpv/2008/code-37312100"
        },
        "deliveryLocation": {
            "geometry": {
                "type": "Point",
                "coordinates": [51.751944, -1.257778]
            },
            "gazetteer": {
                "scheme": "GEONAMES",
                "identifiers": ["2640729"]
            },
            "description": "Central Oxford",
            "uri": "http://www.geonames.org/2640729/oxford.html"
        },
        "deliveryAddress": {
            "postalCode": "OX1 1BX",
            "countryName": "United Kingdom",
            "streetAddress": "Town Hall, St Aldate's",
            "region": "Oxfordshire",
            "locality": "Oxford"
        },
        "unit": {
            "name": "Items",
            "value": {
                "currency": "GBP",
                "amount": 10000
            }
        },
        "quantity": 10
    }
]
```

If the procurement related to the rebuilding of a road, then the item could also specify more complex geometries such as:

```
"deliveryLocation": {
    "geometry": {
        "type": "LineString",
        "coordinates": [ [ -1.256503402048622, 51.747792026616821 ], [ -1.256477837243949, 51.747500168748303 ], [ -1.256466773131763, 51.747365723021403 ], [ -1.256471969911729, 51.747246699996332 ], [ -1.256481860557471, 51.747182243160943 ], [ -1.256497618535434, 51.747079648666102 ] ]
    },
    "gazetteer": {
        "scheme": "OSMW",
        "identifiers": ["27895985"]
    },
    "description": "St Aldate's",
    "uri": "http://www.geonames.org/2640729/oxford.html"
},
```

You can take the contents of the geometry object, excluding the ```geometry``` keyword, and plug this into any GeoJSON tool to see the shape that is described. 
