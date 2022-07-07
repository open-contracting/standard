```{workedexample} No change history
:tags: record
```

# No change history

If you cannot use releases to publish incremental or full updates for the reasons outlined in [Change History Implementation Options](change_history_options.md), you ought to publish the current state of each contracting process using compiled releases.

```{note}
For an introduction to the concept of a change history, see the [releases and records](../../primer/releases_and_records) primer.
```

## Worked Example

A civil society organization from Mexico collects and transforms government public procurement data from different non-OCDS data sources into OCDS format. They only have the information about the process at the time of their collection, so no change history is available. To publish this information, they use a record including only the `ocid` and the `compiledRelease`. As there is no change history information available, they omit the list of `releases`.

```{jsoninclude} ../../examples/no_change_history/no_change_history.json
:jsonpointer: /records
:expand: compiledRelease
:title: no change history
```
