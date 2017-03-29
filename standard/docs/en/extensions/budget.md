# Budget Breakdown
================

## Background

The ```planning``` section of OCDS can be used to describe the background to a contracting process, which may include details of the budget from which funds are drawn.

OCDS core includes a single ```budget.amount``` field to capture the total value of the budget for the contracting process.

## Providing more detailed budget information

Some OCDS implementations require more detailed information on budgets to be disclosed, for example multi-year budgets or budgets sourced from multiple different government departments. In the case of PPPs, budgets may be sourced from the private sector or from multi-lateral development banks.

This extension provides a way to describe multi-year and multi-source budgets.

Disclosing structured data on multi-source budgets allows users to understand how much of the funds for a project come from government or from a specific department, whilst structured data on multi-year budgets allows users to understand the expected spend profile of a contract.

## Extension fields

This extension adds a ```budgetBreakdown``` property to the ```planning``` section of OCDS. ```budgetBreakdown``` is an array of ```budget``` blocks.

This extension also extends the ```budget``` block with the following additional properties for use in the ```budgetBreakdown``` section:

* ```budget.sourceEntity``` - an organization reference, linking to the entry in the ```parties``` section describing the organization providing the funds for this part of the budget
* ```budget.period``` - a period block, describing the period to which this part of the budget applies

## Guidance

In the core ```planning.budget``` block:

* ```budget.amount``` should be used to capture the total value of the budget for the contracting process.
* ```budget.period``` should be used to capture the total period over which the budget applies.
* ```budget.sourceEntity``` should be ommitted.

Where ```budget.budgetBreakdown``` is used to express a multi-source budget but the organization details are not known for one or more parts of the budget, for example in a PPP where part of the budget will be provided by the successful private sector bidder, the ```sourceEntity.name``` field should be used to provide a free text explanation of the source of the budget, e.g. "Private sector investment from successful bidder".

## Examples

### Multi-source budgets

The following JSON snippet models a single year multi-source budget:

```JSON
"planning":{
    "budget": {
        "period": {
            "startDate": "2016-01-01T00:00:00Z",
            "endDate": "2016-12-31T00:00:00Z"
        },
        "id": "string",
        "description": "string",
        "amount": {
            "amount": 300000,
            "currency": "GBP"
        }
    },
    "budgetBreakdown": [
        {
            "sourceEntity": {
                "id": "GB-LAC-E09000003-557",
                "name" : "London Borough of Barnet - Transport Services" 
            },
            "period": {
                "startDate": "2016-01-01T00:00:00Z",
                "endDate": "2016-12-31T00:00:00Z"
            },
            "id": "001",
            "description": "Budget contribution from the local government",
            "amount": {
                "amount": 150000,
                "currency": "GBP"
            }
        },
        {
            "sourceEntity": {
                "id": "GB-GOV-23",
                "name" : "Department for Transport" 
            },
            "period": {
                "startDate": "2016-01-01T00:00:00Z",
                "endDate": "2016-12-31T00:00:00Z"
            },
            "id": "002",
           "description": "Budget contribution from the national government",
            "amount": {
                "amount": 150000,
                "currency": "GBP"
            }
        }  
    ]
}
```

### Multi-year budgets

The following JSON snippet models a multi-year single source budget:

```JSON
"planning": {
    "budget": {
        "sourceEntity": {
            "id": "GB-LAC-E09000003-557",
            "name" : "London Borough of Barnet - Transport Services" 
        },
        "period": {
            "startDate": "2016-01-01T00:00:00Z",
            "endDate": "2017-12-31T00:00:00Z"
        },
        "amount": {
            "amount": 300000,
            "currency": "GBP"
        }
    },
    "budgetBreakdown": [
        {
            "period": {
                "startDate": "2016-01-01T00:00:00Z",
                "endDate": "2016-12-31T00:00:00Z"
            },
            "id": "001",
            "description": "2016 Budget",
            "amount": {
                "amount": 200000,
                "currency": "GBP"
            }
        },
        {
            "period": {
                "startDate": "2017-01-01T00:00:00Z",
                "endDate": "2017-12-31T00:00:00Z"
            },
            "id": "002",
            "description": "2017 Budget",
            "amount": {
                "amount": 100000,
                "currency": "GBP"
            }
        }  
    ]
}
```

## To do

* Finalise guidance on use of extended fields in the core ```planning.budget``` field.
* Finalise guidance where source entity is not known at time of budgeting


See issue https://github.com/open-contracting/standard/issues/377