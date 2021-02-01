# Updates and Deletions

The [merging documentation](../../schema/merging) specifies how individual releases are merged into compiled releases (the latest version of the contracting process) and versioned releases (the change history for each field), which form part of a [record](../../getting_started/releases_and_records). 

The merge routine also allows a publisher to correct a publication error by deleting a field, object or array entry from the compiled release. To do so, a publisher sets the field's value to `null` in an individual release (more on this below). As such, as a publisher, it is important to **never use a `null` value in an individual release, unless you intend to delete that field**. If you don't have a value to assign to a field, simply omit the field from the JSON, or assign an empty value like `""`, `[]` or `{}`. Using `null` values correctly means that publishers and/or users can create compiled releases reliably.

The following examples show how updates and deletions are reflected in compiled and versioned releases.

## Example 1: Updates

A public procurement agency publishes a release to announce an opportunity on January 1, 2016 in which the total estimated value of the procurement is $1,000. On January 31, it publishes a release to expand the description of the procurement. On February 5, it publishes a release to amend the opportunity, in which the total estimated value is increased to $2,000.

The agency decides to award the opportunity to two of the bidders. On March 1, the agency publishes a release to announce that Company A is awarded a contract of $750. On March 3, the agency publishes a release to announce that Company B is awarded a contract of $750.

Through these individual releases, the agency provides real-time data about the contracting process.

In each release, the agency also updates the record, which combines all the releases to date. In the final record:

* The compiled release contains all the information about the opportunity and awards, using the same schema as a release.
* The versioned release makes it easy to see how the description and total estimated value changed over time.

```{eval-rst}
.. jsoninclude:: ../../examples/merging/merge-tender-1.json
   :jsonpointer:
   :expand: releases, tag, tender
   :title: tender
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/merge-tender-2.json
   :jsonpointer:
   :expand: releases, tag, tender
   :title: tenderUpdate
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/merge-tender-3.json
   :jsonpointer:
   :expand: releases, tag, tender
   :title: tenderAmendment
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/merge-award-1.json
   :jsonpointer:
   :expand: releases, tag, awards
   :title: awardOne
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/merge-award-2.json
   :jsonpointer:
   :expand: releases, tag, awards
   :title: awardTwo
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/versioned.json
   :jsonpointer:
   :expand: records, compiledRelease, versionedRelease, tag, tender, awards
   :title: record
```

## Example 2: Deletion of fields and objects

### Fields

A government agency in Colombia publishes the planning of a procurement opportunity, including draft data for the tender, as shown below.

After a few weeks, the tender is ready to be announced. The officer in charge notices that the rationale of the planning is a duplication of the budget description and decides to leave the `rationale` field blank, judging that the `budget/description` field has all the information needed. A release with a 'tender' tag is published, and the record for the process is updated.

In the final record, both the compiled and versioned releases show the changes. The `planning/rationale` field has disappeared from the `compiledRelease`, and the `versionedRelease` shows both its previous value and the `null` value used to delete the field. The entry with the `null` value can be used to determine when the field was deleted.

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example02-field-planning.json
   :jsonpointer:
   :expand: releases, tag, planning
   :title: planning
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example02-field-tender.json
   :jsonpointer:
   :expand: releases, tag, planning, tender
   :title: tender
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example02-field-record.json
   :jsonpointer:
   :expand: records, compiledRelease, versionedRelease
   :title: record
```

### Objects

Another government agency in Colombia publishes a new procurement opportunity. Details are provided in an OCDS release, as shown below.

A few days after releasing the tender notice, the government agency receives feedback for potential bidders, and they realize that the estimated contract period set for the tender could be infeasible. They decide to instead negotiate the contract period with the awarded supplier, and they remove the contract period from the opportunity to avoid confusing potential bidders.

A release with a 'tenderAmendment' tag is published, in which both the `startDate` and `endDate` of the `contractPeriod` block have been set to `null`. Also, an `amendments` block is provided to explain the changes.

The final record is shown below. Note that the fields in the `contractPeriod` block have disappeared in the `compiledRelease`, and the `versionedRelease` contains the previous values.

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example02-object-tender.json
   :jsonpointer: 
   :expand: releases, tag, tender
   :title: tender
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example02-object-tenderAmendment.json
   :jsonpointer: 
   :expand: releases, tag, tender, amendments
   :title: tenderAmendment
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example02-object-record.json
   :jsonpointer: 
   :expand: records, compiledRelease, versionedRelease
   :title: record
```

## Example 3: Deletion of array items

The public procurement authority in Zambia publishes an award notice, as well as an OCDS release with an 'award' tag. A NGO collects the individual releases published by the procurement authority on a weekly basis to merge into their own records, which they use to display information on their website.

Two weeks later, the authority publishes a new release. Due to negotiations with the awarded supplier, one of the items in the award is being deleted and two new ones have been added to replace it, as show below. The two new items have been added at the end of the `items` array, and the item to remove has all its fields set to `null`.

The NGO generates a record. In the record, all the fields of the removed item have disappeared, and only its `id` is left.

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example03-award.json
   :jsonpointer: 
   :expand: releases, tag, awards
   :title: award
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example03-awardAmendment.json
   :jsonpointer: 
   :expand: releases, tag, awards, amendments, items
   :title: awardAmendment
```

```{eval-rst}
.. jsoninclude:: ../../examples/merging/example03-record.json
   :jsonpointer: 
   :expand: records, compiledRelease, versionedRelease
   :title: record
```

```{eval-rst}
.. note::

    The current `merge routine <../../../schema/merging#merge-routine>`__ does not include a strategy to completely remove an entry from an array. We invite discussion on how to remove objects from arrays in issue `#232 <https://github.com/open-contracting/standard/issues/232>`__.
```
