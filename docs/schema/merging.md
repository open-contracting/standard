# Merging

An OCDS [record](../schema/records_reference) aggregates all the releases available for a contracting process at a given time, and can include:

* a compiled release, which expresses the current state of the contracting process, by showing only the most recent field values
* a versioned release, which expresses all historical states of the contracting process, by showing all the field values over time

**Merging** is the process of combining individual releases into a compiled or versioned release, described in more detail below. At a high level:

* A compiled release is created by taking only the most recent values of fields from releases in a given contracting process.
* A versioned release is created by taking all values of fields from releases in a given contracting process, copying metadata about the release from which they are taken, and putting them in chronological order.

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

A public procurement agency publishes a release to announce an opportunity on January 1, in which the total estimated value of the procurement is $1,000. On January 31, it publishes a release to correct the information, in which the description of the procurement is expanded. On February 5, the agency publishes a release to amend the opportunity, in which the total estimated value of the procurement is increased to $2,000.

The agency decides to award the opportunity to two of the bidders. On March 1, the agency publishes a release to announce that Company A is awarded a contract of $750. On March 3, the agency publishes a release to announce that Company B is awarded a contract of $750.

Through these individual releases, the agency provides real-time data about the contracting process.

At each release, the agency also updates the record, which combines all the releases to date. In the final record:

* The compiled release contains all the information about the opportunity and awards, using the same schema as a release.
* The versioned release makes it easy to see how the description and total estimated value changed over time.

```{eval-rst}
.. jsoninclude:: ../examples/merging/merge-tender-1.json
   :jsonpointer: /releases
   :expand: releases, tag, tender
   :title: tender

```

```{eval-rst}
.. jsoninclude:: ../examples/merging/merge-tender-3.json
   :jsonpointer: /releases
   :expand: releases, tag, tender
   :title: tenderAmendment

```

```{eval-rst}
.. jsoninclude:: ../examples/merging/merge-award-1.json
   :jsonpointer: /releases
   :expand: releases, tag, awards
   :title: awardOne

```

```{eval-rst}
.. jsoninclude:: ../examples/merging/merge-award-2.json
   :jsonpointer: /releases
   :expand: releases, tag, awards
   :title: awardTwo

```

```{eval-rst}
.. jsoninclude:: ../examples/merging/merged.json
   :jsonpointer:
   :expand: records, compiledRelease, tag, tender, awards
   :title: record

```

```{eval-rst}
.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer:
   :expand: records, versionedRelease, tag, tender, awards
   :title: versioned

```

</div>

## Merging specification

### Discarded fields

In the release schema, `"omitWhenMerged": true` is declared on fields that must be discarded during merging. These are presently: `id`, `date` and `tag`.

* For a compiled release:
  * Both the fields and their values are discarded, because they are metadata about the individual releases; the compiled release replaces these with its own metadata.
* For a versioned release:
  * The fields are discarded, but their values are moved, as described below, in order to indicate from which releases each other field value is taken.

If `omitWhenMerged` is set to `false`, ignore it.

```{eval-rst}
.. note::

   .. markdown::

      The compiled release presently uses the same schema as the release schema, which means that the `id`, `date` and `tag` fields are required in a compiled release. We invite discussion on whether to change these requirements in a separate compiled release schema in issue [#330](https://github.com/open-contracting/standard/issues/330), and on how to identify and date compiled and versioned releases in issue [#834](https://github.com/open-contracting/standard/issues/834).

      In the meantime, an intermediate solution is to set `tag` to `["compiled"]`, `date` to the date of the most recent release, and `id` to `{ocid}-{date}`, like in the [reference implementation](#reference-implementation) of the merge routine.
```

### Versioned values

To convert a field's value in a release to a **versioned value**, you must:

1. Create an empty JSON object
1. Set its `releaseID`, `releaseDate`, `releaseTag` fields to the release's `id`, `date`, `tag` values
1. Set its `value` field to the field's value in the release

A **versioned value** thus describes a field's value in a specific release.

For example, in the above worked example, the estimated value of the procurement was $1,000 in a release (`tender/value/amount` was `1000`). Following the steps above, the versioned value is:

```json
{
  "releaseID": "ocds-213czf-000-00002-01-tender",
  "releaseDate": "2016-01-01T09:30:00Z",
  "releaseTag": [
    "tender"
  ],
  "value": 1000
}
```

In a **versioned release**, with a few exceptions, a field's value is replaced with an array of versioned values, which should be in chronological order by `releaseDate`.

For example, in the above worked example, the estimated value was $1,000 in a release published January 1, 2016 and then $2,000 in a release published February 5, 2016. In a versioned release, this is serialized as below:

```{eval-rst}
.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer: /records/0/versionedRelease/tender/value
   :expand: value, amount
   :title: Versioned_values

```

```{eval-rst}
.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer:
   :expand: records, versionedRelease
   :title: Versioned_release

```

The structure of the versioned release is described by the {download}`versioned release schema <../../build/current_lang/versioned-release-validation-schema.json>`; note that the `ocid` field's value is not versioned.

### Merge routine

To create a compiled or versioned release, you must:

1. Get all releases with the same `ocid` value
1. Order the releases in chronological order by `date`
1. Create an empty JSON object for the compiled or versioned release
1. Merge each release (**input**), in order, into the JSON object (**output**), as follows:

#### Object values

The release is itself an object, so this case is encountered first.

If the object is empty in **input**, do nothing. For each field within the object in **input**:

* For a compiled release:
  * If the field in **input** has a value of `null`, remove the field from the object in **output**, if present
  * If the field isn't in **output**, add the field to the object in **output**, and set it to its value in **input**
  * If the field is in **output**, merge the field's values in **output** and **input** according to the [merge routine](#merge-routine)
* For a versioned release:
  * Merge the field's values in **output** and **input** according to the [merge routine](#merge-routine); if there is a result, add the field to the object in **output** if not already added, and set it to the result

#### Literal values

If the **input** value is neither an object nor an array, then:

* For a compiled release:
  * If the **input** value is different from the **output** value, replace the **output** value with the **input** value
* For a versioned release:
  * If there is no **output** value, set the **output** value to an empty JSON array, convert the **input** value to a [versioned value](#versioned-values), and append it to the new array of versioned values in **output**
  * If the **input** value is different from the value of the `value` field of the most recent versioned value in **output**, convert the **input** value to a [versioned value](#versioned-values), and append it to the array of versioned values in **output**

#### Array values

If the **input** array contains anything other than objects, treat the array as a literal value. Otherwise, there are two sub-routines for arrays of objects: whole list merge and identifier merge.

##### Whole list merge

An **input** array must be treated as a literal value if the corresponding field in a {download}`dereferenced copy <../../build/current_lang/dereferenced-release-schema.json>` of the release schema has `"array"` in its `type` and if any of the following are also true:

* The field has `"wholeListMerge": true`
* The field sets `items/type`, and has anything other than `"object"` in `items/type`
* The field has `"object"` in its `items/type`, sets `items/properties`, and has no `id` field in `items/properties`

##### Identifier merge

This case is encountered if the above conditions aren't met. If the array is empty in **input**, do nothing. For each object within the array in **input**:

* For a compiled release:
  * If there is an object in the array in **output** with the same `id` value as the object in **input**, merge the matching objects in **input** and **output** according to the [merge routine](#merge-routine)
  * Otherwise, append the object in **input** to the array in **output**
* For a versioned release:
  * If there is an object in the array in **output** with the same `id` value as the object in **input**, merge the matching objects in **input** and **output** according to the [merge routine](#merge-routine) *except for the `id` field*, which is not versioned and instead kept as-is
  * Otherwise, merge an empty JSON object and the object in **input** according to the [merge routine](#merge-routine) *except for the `id` field*, which is not versioned and instead kept as-is, and append the result to the array in **output**

```{eval-rst}
.. note::

   .. markdown::

      In this case, to remove an object from an array, you need to instead set each of its fields to `null`. We invite discussion on how to remove objects from arrays in issue [#232](https://github.com/open-contracting/standard/issues/232).

```

```{eval-rst}
.. note::

   .. markdown::

      In the release schema, `"versionId": true` is declared on `id` fields that must be versioned. This is only for convenience and might be removed in future versions of OCDS (see issue [#812](https://github.com/open-contracting/standard/issues/812)). If `"versionId": true` is declared on the `id` field of an object within an array, it is ignored. `"versionId": false` has no meaning and is ignored.

```

### Reference implementation

A reference implementation of the merge routine [is available in Python on GitHub](https://github.com/open-contracting/ocds-merge). We strongly encourage any re-implementations to [read its commented code and use its test cases](https://github.com/open-contracting/ocds-merge#reference-implementation), to ensure correctness.
