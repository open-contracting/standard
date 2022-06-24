```{workedexample} No change history
:tags: record
```

# No change history

OCDS supports and encourages the publication of the change history of a contracting process. But, for some publishers, publishing this information is not feasible. For example, if your system doesn’t implement versioning or track changes, or if you are collecting non-OCDS data from a source and republishing it as OCDS. Similarly, if you publish historical information that won’t change anymore, you might have only the latest state of the contracting process, without its change history.

If this is your case, the best way to publish this information in OCDS is in a compiled release, as a compiled release represents the state of the contracting process at the time of publication.

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
