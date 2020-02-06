# Merging and Deletion

The [merging documentation](../../schema/merging/) specifies how releases can be merged to produce compiled releases (latest version of the contracting process) and versioned releases (change history for each field in the standard) that are usually included in a record. An important matter that arises along with merging is how to delete fields, objects or array items in releases.

Deletions are not a frequent occurrence, but it is important that deletion rules are considered when transforming data to OCDS. Even if the publisher doesn’t publish records or compiled releases, a correct implementation allows users to build them themselves for their own needs.

As the merge routine shows, the use of the `null` keyword in JSON has a role in the deletion of data, **that’s why is important to never include `null` values in data that are not meant to delete a field**.

## Worked examples

The following examples show how updates and deletions are reflected in compiled and versioned releases.

### Example 1: Updates

A public procurement agency publishes a release to announce an opportunity on January 1, 2016 in which the total estimated value of the procurement is $1,000. On January 31, it publishes a release to correct the information, in which the description of the procurement is expanded. On February 5, the agency publishes a release to amend the opportunity, in which the total estimated value of the procurement is increased to $2,000.

The agency decides to award the opportunity to two of the bidders. On March 1, the agency publishes a release to announce that Company A is awarded a contract of $750. On March 3, the agency publishes a release to announce that Company B is awarded a contract of $750.

Through these individual releases, the agency provides real-time data about the contracting process.

At each release, the agency also updates the record, which combines all the releases to date. In the final record:

* The compiled release contains all the information about the opportunity and awards, using the same schema as a release.
* The versioned release makes it easy to see how the description and total estimated value changed over time.

```eval_rst
.. jsoninclude:: ../../examples/merging/merge-tender-1.json
   :jsonpointer:
   :expand: releases, tag, tender
   :title: tender

```

```eval_rst
.. jsoninclude:: ../../examples/merging/merge-tender-2.json
   :jsonpointer:
   :expand: releases, tag, tender
   :title: tenderUpdate

```

```eval_rst
.. jsoninclude:: ../../examples/merging/merge-tender-3.json
   :jsonpointer:
   :expand: releases, tag, tender
   :title: tenderAmendment

```

```eval_rst
.. jsoninclude:: ../../examples/merging/merge-award-1.json
   :jsonpointer:
   :expand: releases, tag, awards
   :title: awardOne

```

```eval_rst
.. jsoninclude:: ../../examples/merging/merge-award-2.json
   :jsonpointer:
   :expand: releases, tag, awards
   :title: awardTwo

```

```eval_rst
.. jsoninclude:: ../../examples/merging/record.json
   :jsonpointer:
   :expand: records, compiledRelease, versionedRelease, tag, tender, awards
   :title: record

```

### Example 2: Deletion of fields and objects

#### Fields

A government agency in Colombia publishes the planning of a procurement opportunity, including draft data for the tender. See the JSON example below.

After a few weeks, the tender is ready to be announced. The officer in charge notices that the rationale of the planning is a duplication of the budget description and decides to leave the `rationale` field in blank, judging that the `budget/description` field has all the information needed. A new OCDS release with the “tender” tag is created, and the record for the process is updated. See the JSON example below.

In the final record, both the compiled and versioned releases show the changes. The `planning/rationale` field has dissapeared from the compiledRelease, and the versionedRelease shows both its previous value and the `null` value used to delete the field. The `null` entry can be used to identify when the field has been deleted.

```eval_rst
.. jsoninclude:: ../../examples/merging/example02-field-planning.json
   :jsonpointer:
   :expand: releases, tag, planning
   :title: planning

```

```eval_rst
.. jsoninclude:: ../../examples/merging/example02-field-tender.json
   :jsonpointer:
   :expand: releases, tag, planning, tender
   :title: tender

```

```eval_rst
.. jsoninclude:: ../../examples/merging/example02-field-record.json
   :jsonpointer:
   :expand: records, compiledRelease, versionedRelease
   :title: record

```

#### Objects

Another government agency in Colombia publishes a new procuring opportunity. Details are provided in an OCDS release, as shown below.

A few days after releasing the tender notice, the government agency receives feedback for potential bidders, and they realize that the estimated contract period set for the tender could be inaccurate. They decide to negotiate the contract periods with the supplier once the contract is awarded, and remove the contract period to avoid confusion with potential bidders. 

A tenderAmendment release is provided, in which both the `startDate` and `endDate` of the `contractPeriod` block have been set to `null`. Also, an `amendments` block is provided to explain these changes.

The final record is shown below. Note that the fields in the `contractPeriod` block have dissappeared in the compiledRelease, and the versionedRelease contains the previous values.

```eval_rst
.. jsoninclude:: ../../examples/merging/example02-object-tender.json
   :jsonpointer: 
   :expand: releases, tag, tender
   :title: tender

```

```eval_rst
.. jsoninclude:: ../../examples/merging/example02-object-tenderAmendment.json
   :jsonpointer: 
   :expand: releases, tag, tender, amendments
   :title: tenderAmendment

```

```eval_rst
.. jsoninclude:: ../../examples/merging/example02-object-record.json
   :jsonpointer: 
   :expand: records, compiledRelease, versionedRelease
   :title: record

```

### Example 3: Deletion of array items

The public procurement authority in Zambia publishes an award notice, as well as an OCDS release using the 'award' tag. A NGO collects the releases published by the procurement authority on a weekly basis to build their own records, which are more appropriate to display information on their webpage. 

Two weeks later, the procurement authority publishes a new release. Due to negotiations with the supplier selected, one of the items in the award is being deleted and two new ones have been added to replace it. See the JSON example below: the two new items have been added at the end of the `items` array, and the item to remove has all its fields set to `null`.

The NGO generates a record (see below). In the record, all the fields of the removed item have dissappeared, and only its `id` is left.

```eval_rst
.. jsoninclude:: ../../examples/merging/example03-award.json
   :jsonpointer: 
   :expand: releases, tag, awards
   :title: award

```

```eval_rst
.. jsoninclude:: ../../examples/merging/example03-awardAmendment.json
   :jsonpointer: 
   :expand: releases, tag, awards, amendments, items
   :title: awardAmendment

```

```eval_rst
.. jsoninclude:: ../../examples/merging/example03-record.json
   :jsonpointer: 
   :expand: records, compiledRelease, versionedRelease
   :title: record

```

```eval_rst
.. note::

    The current `merge routine <../../../schema/merging#merge-routine>`__ does not include a strategy to completely remove an entry from an array. We invite discussion on how to remove objects from arrays in issue `#232 <https://github.com/open-contracting/standard/issues/232>`__.

```
