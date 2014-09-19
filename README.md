Open Contracting Data standard
==============================

[![Build Status](https://travis-ci.org/open-contracting/standard.svg?branch=master)](https://travis-ci.org/open-contracting/standard)

To run tests locally:

````
pip install -r requirements.txt
py.test
````

To produce a new versioned-release-validation-schema:

````
cd standard/schema/utils
./make_validation_schema.py
````

Some things to bear in mind:

* If you make a change to release-schema.json, you must also make a change to
  versioned-release-schema.json as they should always be in sync. Versioned
release schema exists to layout the mergeStrategies for merging releases, but
it must have the correct types in it from release schema.
* If you make a change to versioned-release-schema, you must update the
  versioned-release-validation-schema.json.

The tests, which run automatically on every commit, check for both of these
points of consistency.

###Notes

We have to be careful when defining mergeStrategies on items that are accessed
by reference. In particular if they are used differently i.e. sometimes in
arrays and sometimes individualls. Here is a list of all items that use refs,
in order of how they appear in the schema (last updated on Sep 19, 2014)

*  buyer - organization
*  milestone - attachments - [attachment]
*  performance - milestones - [milestone]
*  performance - reports - [attachment]
*  planning - publicHearingNotice - [notice]
*  planning - anticipatedMilestones - [milestone]
*  tender - notice - notice
*  tender - itemsToBeProcured - [item]
*  tender - totalValue - value
*  tender - tenderPeriod - period
*  tender - clarificationPeriod - period
*  tender - awardPenriod - period
*  tender - bidders - [organization]
*  tender - procuringEntity - organization
*  tender - attachments - [attachment]
*  award - notice - notice
*  award - awardValue - value
*  award - suppliers - [organization]
*  award - itemsAwarded - [item]
*  contract - contractPeriod - period
*  contract - contractValue - value
*  contract - amendment - amendment
*  contract - itemsContracted - [item]
*  contract - deliverables - [deliverable]
*  contract - attachments - [attachment]
*  notice - amendment
*  deliverable - amendment

And here they are, but grouped by the item being referenced:

*  buyer - organization
*  tender - procuringEntity - organization
*  tender - bidders - [organization]
*  award - suppliers - [organization]

*  notice - amendment
*  deliverable - amendment
*  contract - amendment - amendment

*  milestone - attachments - [attachment]
*  performance - reports - [attachment]
*  tender - attachments - [attachment]
*  contract - attachments - [attachment]

*  contract - deliverables - [deliverable]

*  tender - itemsToBeProcured - [item]
*  contract - itemsContracted - [item]
*  award - itemsAwarded - [item]

*  performance - milestones - [milestone]
*  planning - anticipatedMilestones - [milestone]

*  planning - publicHearingNotice - notice
*  award - notice - notice
*  tender - notice - notice

*  tender - tenderPeriod - period
*  tender - clarificationPeriod - period
*  contract - contractPeriod - period
*  tender - awardPeriod - period

*  tender - totalValue - value
*  award - awardValue - value
*  contract - contractValue - value

In the case where we have items that are available both in an array and as an
object, we have to be very careful with merging and specify the merge strategy
at the parent level, not the object level.
