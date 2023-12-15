# Merging

An OCDS [record](../schema/records_reference) aggregates all the releases available for a contracting (or planning) process at a given time, and can include:

* a compiled release, which expresses the current state of the contracting (or planning) process, by showing only the most recent field values
* a versioned release, which expresses all historical states of the contracting (or planning) process, by showing all the field values over time

**Merging** is the process of combining individual releases with the same OCDS version into a compiled or versioned release, described in more detail below. At a high level:

* A compiled release is created by taking only the most recent values of fields from releases in a given contracting (or planning) process.
* A versioned release is created by taking all values of fields from releases in a given contracting (or planning) process, copying metadata about the release from which they are taken, and putting them in chronological order.

```{seealso}
Guidance: [Updates and deletions](../guidance/build/merging)
```

## Merging specification

### Discarded fields

In the release schema, `"omitWhenMerged": true` is declared on fields that must be discarded during merging. These are presently: `id`, `date` and `tag`.

* For a compiled release:
  * Both the fields and their values are discarded, because they are metadata about the individual releases; the compiled release replaces these with its own metadata.
* For a versioned release:
  * The fields are discarded, but their values are moved, as described below, in order to indicate from which releases each other field value is taken.

If `omitWhenMerged` is set to `false`, ignore it.

```{note}
The compiled release presently uses the same schema as the release schema, which means that the `id`, `date` and `tag` fields are required in a compiled release. We invite discussion on whether to change these requirements in a separate compiled release schema in issue [#330](https://github.com/open-contracting/standard/issues/330).

In the meantime, an intermediate solution is to set `tag` to `["compiled"]`, `date` to the maximum `date` among the individual releases used to create the compiled release, and `id` to `{ocid}-{date}`, like in the [reference implementation](#reference-implementation) of the merge routine.
```

### Versioned values

To convert a field's value in a release to a **versioned value**, you must:

1. Create an empty JSON object
1. Set its `releaseID`, `releaseDate`, `releaseTag` fields to the release's `id`, `date`, `tag` values
1. Set its `value` field to the field's value in the release

A **versioned value** thus describes a field's value in a specific release.

For example, in worked example 1 in [Updates and deletions](../guidance/build/merging), the method by which the procurement is taking place is stated as limited (in the first release `tender/procurementMethod` was `limited`). In the initial release this looks like:

```{jsoninclude} ../examples/merging/updates/ghana_tender1.json
:jsonpointer: /releases/0/tender
:include_only: procurementMethod
:expand: procurementMethod
:title: Value
```

Following the steps above, the versioned value is:

```{jsoninclude} ../examples/merging/updates/ghana_versioned.json
:jsonpointer: /records/0/versionedRelease/tender
:include_only: procurementMethod
:expand: procurementMethod
:title: Versioned_values
```

In a **versioned release**, with a few exceptions, a field's value is replaced with an array of versioned values, which should be in chronological order by `releaseDate`.

For example, in the worked example referenced above, the value of the tender was $13,000 in the release published October 21, 2020 and then $12,000 in the release published November 5, 2020.

```{jsoninclude} ../examples/merging/updates/ghana_tender1.json
:jsonpointer: /releases/0/tender
:include_only: tender/value
:expand: value
:title: initial_value
```

```{jsoninclude} ../examples/merging/updates/ghana_tender2.json
:jsonpointer: /releases/0/tender
:include_only: tender/value
:expand: value
:title: updated_value
```

In a versioned release, this is serialized as below:

```{jsoninclude} ../examples/merging/updates/ghana_versioned.json
:jsonpointer: /records/0/versionedRelease/tender
:include_only: tender/value
:expand: value,amount,releaseTag
:title: Versioned_values
```

The structure of the versioned release is described by the [versioned release schema](../../build/current_lang/versioned-release-validation-schema.json); note that the `ocid` field's value is not versioned.

### Merge routine

To create a compiled or versioned release, you must:

1. Get all releases with the same `ocid` value and same OCDS version
1. Order the releases in chronological order by `date`
1. Create an empty JSON object for the compiled or versioned release
1. For a compiled release:
  1. Set `date` to the maximum `date` among the releases.
  1. Set `id` to `{ocid}-{date}`.
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

An **input** array must be treated as a literal value if the corresponding field in a [dereferenced copy](../../build/current_lang/dereferenced-release-schema.json) of the release schema has `"array"` in its `type` and if any of the following are also true:

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

```{note}
In this case, to remove an object from an array, you need to instead set each of its fields to `null`. We invite discussion on how to remove objects from arrays in issue [#232](https://github.com/open-contracting/standard/issues/232).
```

### Reference implementation

A reference implementation of the merge routine [is available in Python on GitHub](https://github.com/open-contracting/ocds-merge). We strongly encourage any re-implementations to [read its commented code and use its test cases](https://ocds-merge.readthedocs.io/en/latest/#reference-implementation), to ensure correctness.
