# Merging

An OCDS [record](../getting_started/releases_and_records.md) aggregates all the releases available for a contracting process at a given time, and optionally includes:

* a compiled release, which expresses the current state of the contracting process, by showing only the most recent field values
* a versioned release, which expresses all historical states of the contracting process, by showing all the field values over time

**Merging** is the process of combining individual releases into a compiled or versioned release, described in more detail below.

The versioned release makes it easy to see how field values have changed over time: for example, to see how contract values have been modified or how milestones have been re-scheduled during implementation.

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

A publisher provides a tender release on 1st January, with a planned contract value of $1000.

On 5th February, the publisher provides an amended tender release updating the planned contract value to $2000.

After assessing bids, it is decided to award the contract in two lots.

On 1st March, the publisher provides an award release, announcing Company A has been awarded a contract for $750.

On 3rd March, the publisher provides an separate award release, announcing that company B has been awarded a contract for $750.

These independent releases each provide real-time information about what is happening in the contracting process. The record will combine them together. Using the same schema and structure as the releases, the main body of the record will contain a tender with contract value of $1500, and details of both awards.

If the record is complete with versioning information, then the versioning section will reveal that the planned contract value changed from $1000 to $1500 on 31st January.

```eval_rst

.. jsoninclude:: ../examples/merging/merge-tender-1.json
   :jsonpointer: /releases
   :expand: releases, tag, tender
   :title: tender

```

```eval_rst

.. jsoninclude:: ../examples/merging/merge-tender-3.json
   :jsonpointer: /releases
   :expand: releases, tag, tender
   :title: tenderAmendment

```

```eval_rst

.. jsoninclude:: ../examples/merging/merge-award-1.json
   :jsonpointer: /releases
   :expand: releases, tag, awards
   :title: awardOne

```

```eval_rst

.. jsoninclude:: ../examples/merging/merge-award-2.json
   :jsonpointer: /releases
   :expand: releases, tag, awards
   :title: awardTwo

```

```eval_rst

.. jsoninclude:: ../examples/merging/merged.json
   :jsonpointer:
   :expand: records, compiledRelease, tag, tender, awards
   :title: record

```

```eval_rst

.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer:
   :expand: records, versionedRelease, tag, tender, awards
   :title: versioned

```

</div>

## Merging specification

### Discarded fields

In the release schema, `"omitWhenMerged": true` is declared on fields that should be discarded during merging. These are presently: `id`, `date` and `tag`.

The compiled release discards both the fields and their values, whereas the versioned release discards the fields but *moves* their values, as described below.

If `omitWhenMerged` is set to `false`, ignore it.

```eval_rst
.. note::

  The compiled release presently uses the same schema as the release schema, which means that the ``id``, ``date`` and ``tag`` fields are required in a compiled release. We invite discussion of a separate compiled release schema in issue `#330 <https://github.com/open-contracting/standard/issues/330>`__ to re-consider these requirements, and discussion on how to identify and date compiled and versioned releases in issue `#834 <https://github.com/open-contracting/standard/issues/834>`__. In the meantime, an intermediate solution is to set ``tag`` to ``["compiled"]``, ``date`` to the date of the most recent release, and ``id`` to ``{ocid}-{date}``, like in the reference implementation of the merge routine.
```

### Versioned values

To convert a field's value in a release to a **versioned value**:

1. Create an empty JSON object
1. Set its `releaseID`, `releaseDate` and `releaseTag` fields to the `id`, `date` and `tag` values in the release
1. Set its `value` field to the field's value in the release

This versioned value thus describes the field's value in the referenced release.

For example, in the above worked example, the estimated value of the procurement (`tender/value/amount`) was $1000 (`1000`) in a release. Following the steps above, the versioned value is:

```eval_rst

.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer: /records/0/versionedRelease/tender/value/amount/0
   :expand: value, amount
   :title: Versioned value

```

In a versioned release, with a few exceptions, a field's value is replaced with an array of versioned values, which should be in chronological order by `releaseDate`.

For example, in the above worked example, the estimated value was $1000 in a release published January 1, 2016 and then $2000 in a release published February 5, 2016. In a versioned release, this is serialized as below:

```eval_rst

.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer: /records/0/versionedRelease/tender
   :expand: value, amount
   :title: Versioned values

```

```eval_rst

.. jsoninclude:: ../examples/merging/versioned.json
   :jsonpointer:
   :expand: records, versionedRelease
   :title: Versioned release

```

The structure of the versioned release is described by the [versioned release schema](../../../../versioned-release-validation-schema.json); note that the `ocid` field's value is not versioned.

### Merge routine

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
  * If the field is in **output**, merge the field's values in **output** and **input** according to the merge routine
* For a versioned release:
  * Merge the field's values in **output** and **input** according to the merge routine; if there is a result, add the field to the object in **output** if not already added, and set it to the result

#### Literal values

If the **input** value is neither an object nor an array, then:

* For a compiled release:
  * If the **input** value is not `null` and is different from the **output** value, replace the **output** value with the **input** value
* For a versioned release:
  * If there is no **output** value, set the **output** value to an empty JSON array, convert the **input** value to a [versioned value](#versioned-values), and append it to the **output** array of versioned values
  * If the **input** value is different from the value of the `value` field of the most recent versioned value in **output**, convert the **input** value to a [versioned value](#versioned-values), and append it to the **output** array of versioned values

#### Array values

If the **input** array contains anything other than objects, treat the array as a literal value.

Otherwise, there are two sub-routines for arrays of objects: whole list merge and identifier merge.

##### Whole list merge

An **input** array of objects should be treated as a literal value if the corresponding field in a [dereferenced copy](https://jsonref.readthedocs.io/en/latest/) of the release schema has `"array"` in its `type` and if any of the following are also true:

* The field has `"wholeListMerge": true`
* The field sets `items/type`, and has anything other than `"object"` in `items/type`
* The field has `"object"` in its `items/type`, sets `items/properties`, and has no `id` field in `items/properties`

##### Identifier merge

This case is encountered if the above conditions weren't met. If the array is empty in **input**, do nothing. For each object within the array in **input**:

* For a compiled release:
  * If there is an object in the array in **output** with the same `id` value as the object in **input**, merge the matching objects in **input** and **output** according to the merge routine
  * Otherwise, append the object in **input** to the array in **output**
* For a versioned release:
  * If there is an object in the array in **output** with the same `id` value as the object in **input**, merge the matching objects in **input** and **output** according to the merge routine *except for the `id` field*, which is not versioned and instead kept as-is
  * Otherwise, merge an empty JSON object and the object in **input** according to the merge routine *except for the `id` field*, which is not versioned and instead kept as-is, and append the result to the array in **output**

```eval_rst
.. note::

  In this case, to remove an object from an array, you must instead set each of its fields to `null`. We invite discussion on how to remove objects from arrays in issue `#232 <https://github.com/open-contracting/standard/issues/232>`__.

```

```eval_rst
.. note::

  In the release schema, ``"versionId": true`` is declared on ``id`` fields that should be versioned. This is only for convenience and might be removed in future versions of OCDS (see issue `#812 <https://github.com/open-contracting/standard/issues/812>`__). If ``"versionId": true`` is declared on the ``id`` field of an object within an array, it is ignored. ``"versionId": false`` has no meaning and is ignored.

```

### Reference implementation

A reference implementation of the merge routine [is available in Python on GitHub](https://github.com/open-contracting/ocds-merge). We strongly encourage any re-implementations to [read its commented code and use its test cases](https://github.com/open-contracting/ocds-merge#reference-implementation), to ensure correctness.
