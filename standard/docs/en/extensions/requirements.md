# Requirements

The requirements extension is based on the EU's [Core Criterion and Core Evidence Vocabulary (CCCEV)](https://joinup.ec.europa.eu/node/153001) model for communicating criteria and responses.

The extension is designed to allow procuring entities or buyers to express criteria, relating to either items being procured or bidders themselves, as structured data.

Criteria can be responded to either by bidders, buyers or procuring entities, for example a buyer may respond with information about an item whilst a procuring entity may respond with information on whether a bidder is disbarred.

## CCCEV Model

The CCCEV model defines the following concepts:

**Criterion**
A criterion represents a rule or principle used to judge, evaluate or assess either an item or bidder. A criterion is satisfied when one or more of it's requirement groups are satisfied.

**Requirement Group**
A requirement group is a collection of one or more individual requirements. A requirement group is satisfied when all of it's requirements are satisfied.

**Requirement**
An atomic requirement which can be expressed as either an expected value or a range of accepted values.

**Requirement Response**
A requirements response is an assertion that responds to a specific requirement.

Therefore the CCCEV model can be used to express both **AND** conditions, where a group of requirements must be met to satisfy a criterion, and **OR** conditions, where there are alternative requirements that can satisfy a criterion.

## Schema

The extension introduces a new building block for each of the concepts described above, these are added to the following locations in the OCDS schema:

- *tender.criteria* - an array of criteria
- *tender.criteria.requirementGroups* - an array of requirement groups
- *tender.criteria.requirementGroups.requirements* - an array of requirements
- *bids.requirementResponses* - an array of requirement responses (Note: depends on *bid* extension)
- *awards.requirementResponses* - an array of requirements responses
- *contracts.requirementResponses* - an array or requirement responses

## Background

There are number of scenarios in which structured information on requirements is neccessary. See discussion in Github issue [#223](https://github.com/open-contracting/standard/issues/223).

## Example usage

Below is an example of requirements specified against both an item and a bidder which demonstrates both **AND** and **OR** conditions:

````json
"tender": {
	"criteria": [
		{
			"id": "0001",
			"title": "Air intake",
			"description": "The vacuum cleaner air intake must be at least 100W",
			"source": "tenderer",
			"code": "OCDS-123454-AIR",
			"featureOf": "item",
			"relatedItem": "0001",
			"requirementGroups": [
				{
					"id": "0001-001",
					"description": "The vacuum cleaner air intake must be at least 100W",
					"requirements": [
						{
							"id": "0001-001-01",
							"title": "Air intake",
							"description": "Power of vacuum cleaner air intake in W",
							"dataType": "integer",
							"pattern": "[0-9]*",
							"minValue": 100
						}
					]
				}
			]
		},
		{
			"id": "0002",
			"title": "Warranty",
			"description": "The vacuum cleaner must have warranty support options for at least 36 months",
			"source": "tenderer",
			"code": "OCDS-123454-WARRANTY",
			"featureOf": "item",
			"relatedItem": "0001",
			"requirementGroups": [
				{
					"id": "0002-001",
					"description": "The standard warranty period for the vacuum cleaner must be at least 36 months",
					"requirements": [
						{
							"id": "0002-001-01",
							"title": "Standard warranty period",
							"description": "Length of the vacuum cleaner standard warranty period in months",
							"dataType": "integer",
							"pattern": "[0-9]*",
							"minValue": 36
						}
					]
				},
				{
					"id": "0002-002",
					"description": "The standard warranty period for the vacuum cleaner must be at least 12 months with an option to extend to 36 months",
					"requirements": [
						{
							"id": "0002-002-01",
							"title": "Standard warranty period",
							"description": "Length of the vacuum cleaner standard warranty period in months",
							"dataType": "integer",
							"pattern": "[0-9]*",
							"minValue": 12
						},
						{
							"id": "0002-002-02",
							"title": "Extended warranty option",
							"description": "There is an extended warranty option for at least 36 months",
							"dataType": "boolean",
							"expectedValue": true
						}
					]
				}
			]
		},
		{
			"id": "0003",
			"title": "Years trading",
			"description": "Number of years the bidder has been trading",
			"source": "tenderer",
			"code": "OCDS-123454-YEARS",
			"featureOf": "tenderer",
			"requirementGroups": [
				{
					"id": "0003-001",
					"description": "Number of years the bidder has been trading",
					"requirements": [
						{
							"id": "0003-001-01",
							"title": "Years trading",
							"description": "Number of years the bidder has been trading",
							"dataType": "integer",
							"pattern": "[0-9]*",
							"minValue": 3
						}
					]
				}
			]
		}
	]
}
````
Below is an example of responses which meet the above requirements:

````json
"bids": [
	{
		"requirementResponses": [
			{
				"id": "air",
				"value": 125,
				"requirement": "0001-001-01",
				"relatedItem": "0001"
			},
			{
				"id": "warranty",
				"value": 36,
				"requirement": "0002-001-01",
				"relatedItem": "0001"
			},
			{
				"id": "years",
				"value": 10,
				"requirement": "0003-001-01"
			}
		]
	}
]
````

## Further extensions

The CCCEV model also defines a number of additional concepts including **formalFrameworks**, used to specify the legal instruments from criteria are derived, **evidence**, used both to specify and provide the evidence required to support a requirement response, and additional properties of *requirements* such as **certificationLevel** which are not currently implemented in this extension.

## Outstanding issues

The extension does not describe formulae for calculated computed values.

The extension does not describe whether data should be published openly or not.

