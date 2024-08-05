```{workedexample} Change history
:tags: release,record
```

# Change history

To publish a change history for a contracting (or planning) process, you ought to publish a [record](../../schema/records_reference.md) for the process and, for each change, publish a [release](../../schema/reference.md) and update the record.

The following example illustrates how to publish a change history for a contracting process, using both [incremental and full updates](change_history_options.md#change-history-incremental-or-full-updates).

```{note}
For an introduction to the concept of a change history, see the [releases and records](../../primer/releases_and_records) primer.
```

## Tender

A buyer announces an opportunity for the purchase of office supplies.

An OCDS publisher creates a release that describes the opportunity. The 'tender' code in `.tag` indicates that the release contains information about the needed items and their estimated value.

Since this is the first release related to the contracting process, it makes no difference whether the publisher implements incremental updates or full updates.

```{jsoninclude} ../../examples/change_history/incremental/tender.json
:jsonpointer: /records/0/releases/0
:expand: releases, tag, tender, value
```

The publisher also creates a record that describes the new contracting process. The record consists of:

* `releases`: A list of the releases for the contracting process.
* `compiledRelease`: The latest value of each field describing the contracting process.
* `versionedRelease`: A history of changes to each field.

At this stage, there is only one release. Therefore, the only fields that differ in the compiled release are `id` and `tag`, which are set according to the [merging specification](../../schema/merging.md#merging-specification). Likewise, the versioned release contains only one value for each field.

```{jsoninclude} ../../examples/change_history/incremental/tender.json
:jsonpointer: /records/0
:expand: releases, tag, tender, compiledRelease, versionedRelease
```

## Tender update

The buyer now indicates the opportunity's main procurement category.

The OCDS publisher creates a release describing the updated information. The 'tenderUpdate' code in `.tag` indicates that the release is an update to an existing tender release.

`````{tab-set}

````{tab-item} Incremental updates
:sync: incremental

The release contains only new, changed and required fields.

```{jsoninclude} ../../examples/change_history/incremental/tenderUpdate.json
:jsonpointer: /records/0/releases/1
:expand: releases, tag, tender
```

````

````{tab-item} Full updates
:sync: full

The release contains new, changed and required fields, and repeats unchanged fields.

```{jsoninclude} ../../examples/change_history/full/tenderUpdate.json
:jsonpointer: /records/0/releases/1
:expand: releases, tag, tender
```

````

`````

The publisher also updates the OCDS record for the contracting process: They add the new release to the `releases` list and update the `compiledRelease` and `versionedRelease` with the new `mainProcurementCategory` field.

With the exception of the fields contained in the new release, the publisher's choice of incremental or full updates makes no difference to the record.

`````{tab-set}

````{tab-item} Incremental updates
:sync: incremental

```{jsoninclude} ../../examples/change_history/incremental/tenderUpdate.json
:jsonpointer: /records/0
:expand: releases, tag, tender, compiledRelease, versionedRelease
```

````

````{tab-item} Full updates
:sync: full

```{jsoninclude} ../../examples/change_history/full/tenderUpdate.json
:jsonpointer: /records/0
:expand: releases, tag, tender, compiledRelease, versionedRelease
```

````

`````
