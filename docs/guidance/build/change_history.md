```{workedexample} Change history
:tags: release,record
```

# Change history

The following example shows how to publish a change history data using the releases and records model: publish a release for each event in the process and update the record each time you publish a release.

Each subsection refers to a stage or event in a contracting process. The example illustrates both [incremental and full updates](change_history_options.md#incremental-or-full-updates).

```{note}
For an introduction to the concept of a change history, see the [releases and records](../../primer/releases_and_records) primer.
```

```{note}
For guidance on how to set the `id` field on each release, see the [individual releases](individual releases) worked example.
```

## Tender

A buyer publishes an opportunity for the purchase of office supplies.

An OCDS publisher creates a release that describes the opportunity. The 'tender' code in `.tag` indicates that the release contains information about the needed items and their estimated value.

Since this is the first release of information about the opportunity, it makes no difference whether the publisher implements incremental updates or full updates.

`````{tab-set}

````{tab-item} Incremental updates
:sync: incremental

```{jsoninclude} ../../examples/change_history/incremental/tender.json
:jsonpointer: /records/0/releases/0
:expand: releases, tag, tender, value
```

````

````{tab-item} Full updates
:sync: full

The release contains new, changed and required fields, and repeats unchanged fields.

```{jsoninclude} ../../examples/change_history/full/tender.json
:jsonpointer: /records/0/releases/0
:expand: releases, tag, tender, value
```

````

`````

The publisher also creates a record that describes the new contracting process. The record consists of:

* `releases`: A list of the releases for the contracting process.
* `compiledRelease`: The latest value of each field describing the contracting process.
* `versionedRelease`: A history of changes to each field.

At this stage, there is only one release. Therefore, the only differences between the release and the compiled release are the values of the `id` and `tag` fields. Likewise, the versioned release contains only one value for each field.

`````{tab-set}

````{tab-item} Incremental updates
:sync: incremental

```{jsoninclude} ../../examples/change_history/incremental/tender.json
:jsonpointer: /records/0
```

````

````{tab-item} Full updates
:sync: full

```{jsoninclude} ../../examples/change_history/full/tender.json
:jsonpointer: /records/0
```

````

`````

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

The publisher also updates the OCDS record for the contracting process:

* The new release is added to the `releases` list
* The compiled release is updated with the new `mainProcurementCategory` field
* The versioned release is updated with the new `mainProcurementCategory` field

With the exception of the fields contained in the new release, the publisher's choice of incremental or full updates makes no difference to the record.

`````{tab-set}

````{tab-item} Incremental updates
:sync: incremental

```{jsoninclude} ../../examples/change_history/incremental/tenderUpdate.json
:jsonpointer: /records/0
```

````

````{tab-item} Full updates
:sync: full

```{jsoninclude} ../../examples/change_history/full/tenderUpdate.json
:jsonpointer: /records/0
```

````

`````
