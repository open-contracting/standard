## OCDS for Public Private Partnerships

The Open Contracting Data Standard for Public Private Partnerships release draws together a number of general extensions.

This extension provides a number of fields and building blocks that are currenetly seen as specific to PPP disclosure against the World Bank PPP Disclosure Framework.


### Project level information

Building on the [Budget and Projects extension](https://github.com/open-contracting/ocds_budget_projects_extension) this adds to project with:

* Sector classifications - using the [UN Classifications of the Functions of Government](http://unstats.un.org/unsd/cr/registry/regcst.asp?Cl=4)
* Additional classifications - allowing arbitrary additional project categorisation
* Project location - with options for gazetteer or point location

An example is shown below:

```json
{
    "releases":[
        {
            "planning": {
                "project": {
                                    "sector": {
                                        "scheme": "COFOG",
                                        "description": "Road transportation",
                                        "id": "04.5.1"
                                    },
                                    "locations": [
                                        {
                                            "description": "Local Authority Area: Halton Borough Council",
                                            "gazetteer": {
                                                "scheme": "GEONAMES",
                                                "identifiers": "2647601.0"
                                            }
                                        }
                                    ]
                                }
                            }
                  }
        
        ]
}

```

### Financial model information

The PPP disclosure framework calls for a number of different financial indicators to be reported. Whilst some of these may be reported as metrics on an ongoing basis, some are simple single values.

The ```contract/financialModel``` extension provides for an array of ```Indicator``` objects, each with an ```indicatorType``` code drawn from a codelist containing:

* discountRate
* riskPremium
* equityDebtRatio
* shareCapital
* forecastIRR

Each indicator can consist of a title, a code, a value and explanatory notes. 
