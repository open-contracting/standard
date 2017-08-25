# Location Data

## Metadata

To use this extension, include its URL in the ```extension``` array of your release or record package.

```json
{
    "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_location_extension/v1.1.1/extension.json"],
    "releases":[]
}
```

This extension is maintained at [https://github.com/open-contracting/ocds_location_extension](https://github.com/open-contracting/ocds_location_extension)

## Documentation

Communicating the location of proposed or executed contract delivery is important to make users of contracting data. 

This extension introduces two properties at the ```items``` level to describe location:

* ```deliveryAddress``` - a standard ```Address``` block which can be used to provide a postal address where services should be delivered.
* ```deliveryLocation``` - a new block consisting of GeoJSON and Gazetteer entries to describe a wider range of locations to which the contract line item relates.

### Schema reference

```eval_rst
.. extensiontable::
   :extension: location
```

### Gazetteer Codelist

See locationGazeteers.csv

### Example
Below is an example of a geolocated item:

```json
{
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
}
```

If the procurement related to the rebuilding of a road, then the item could also specify more complex geometries such as:

```json
{
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
}
}
```

You can take the contents of the geometry object, excluding the ```geometry``` keyword, and plug this into any GeoJSON tool to see the shape that is described. 
