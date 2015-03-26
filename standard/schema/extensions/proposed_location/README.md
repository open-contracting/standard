There are a number of use cases that demand specifying a location for delivery of an item. Discussion can be found in [Issue 26](https://github.com/open-contracting/standard/issues/26)

Use case 1
==========

The Department of Health may wish to purchase 10 medical devices for 10 separate hospitals in Australia.

These items are all part of a single contracting process as the same supplier is expected to deliver all 10 units, but 
we wish to express the location of the seperate hospital to which the items are to be delivered.

See schema_usecase_1.json


Use case 2
==========

A government issues a tender and wishes to specify either:

* The exact location where the contract should take place;
* The region where the contract should take place;

Drawing also on:

* The need to describe polygon locations, for example, for describing the location a mining concession will apply to;
* The need to provide a delivery address for goods and services for logistics and fulfilment; 
* The need to provide multiple gazetteer entries against a particular tender (e.g. relevant in multiple regions)

schema_usecase_2.json models location by offering a choice between:

* geometry - using the [GeoJSON](http://geojson.org/) geometry object, with an array of coordinates able to describe 
* gazetteer entry - using a single scheme, and an array of identifiers. The codelist_usecases2.csv file details some of the suggested codelists, including Open Street Map Nodes, Relations and Ways, and NUTS. 

With a publisher able to use one or both.

### Notes

* No space is given in the gazeteer entry to individually name each entry. However, the 'description' of the overall location block can be used for this, providing text that can be used in interfaces;
* The nested arrays approach of GeoJSON may have implications for flattening scripts;
* The nested arrays approach of GeoJSON is not terribly intuitive in CSV formats, where Lat,Lng ends up in the same cell, rather than split out in ways that support easy mapping;
* The single URI may be too limited, but introducing a URI for each gazeteer entry introduces more nesting than is idea for flattening the data out; 
