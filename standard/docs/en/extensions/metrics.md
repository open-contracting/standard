Metrics Extension
=================

The metrics extension provides a common building block for reporting structured performance information on contracts. 

Metrics are structured like an [OLAP data cube](https://en.wikipedia.org/wiki/OLAP_cube) with each instance of ```Metric``` representing a single **observation**, categorised by a number of **dimensions**.


```json
{
  "metrics":[
    {
      "id":"annualDemand",
      "title":"Annual Demand",
      "description":"The annual demand",
      "observations":[
        {
          "period":{
            "startDate":"2015-01-01T00:00:00Z",
            "endDate":"2015-12-31T23:59:59Z"
          },
          "quantity":"10000",
          "dimensions":{
            "vehicleType":"Car"
          }
        },
        {
          "period":{
            "startDate":"2015-01-01T00:00:00Z",
            "endDate":"2015-12-31T23:59:59Z"
          },
          "quantity":"1000",
          "dimensions":{
            "vehicleType":"Trucks"
          },
          "note":"Simple note"
        }
      ]
    },
    {

    }
  ]
}
```


## Use with requirements

Metrics can be used along with the **requirements extension** which will add a 'relatedRequirementID' property to metrics. 

With the requirements extension, bids, awards and contracts can include a ```requirementResponse``` indicating the values against each metric that a supplier intends to meet. 

This can allow a degree of comparison between performance anticipated at bid, award, contract and implementation phases.

## To Do

* [ ] Check oneOf schema syntax for value **or** quantity
* [ ] Add relatedRequirementID to requirements extension
* [ ] Validate schema updates