```{workedexample} Compiled releases with no change history
:tags: record
```

# Compiled releases with no change history

If you cannot publish a change history as described in the [change history implementation options guidance](change_history_options.md) and you cannot publish [individual releases](change_history_options.md#no-change-history-individual-or-compiled-releases), you ought to publish the current state of each contracting process using compiled releases.

Compiled releases need to be published as part of an [record](../../schema/records_reference.md) and packaged in a [record package](../../schema/record_package.md). Compiled releases need to conform to the [merging specification](../../schema/merging.md#merging-specification), which defines rules for omitting or setting the value of certain fields.

```{note}
For an introduction to the concept of a change history, see the [releases and records](../../primer/releases_and_records) primer.
```

## Worked Example

A publisher periodically collects procurement data from different non-OCDS data sources and transforms it into OCDS format. The publisher cannot detect changes in the data because the data sources do not provide access to historical data and because the publisher does not store previous versions of the data it collects or publishes. Therefore, the publisher uses compiled releases to publish the current state of each contracting process.

The compiled releases are published as part of an OCDS record, contained within a record package. No change history is available so only the `ocid` and `compiledRelease` are published. The list of `releases` and the `versionedRelease` are omitted.

The `id`, `date` and `tag` fields in the compiled release are set according to the merging specification.

```{jsoninclude} ../../examples/compiled_releases.json
:expand: records, compiledRelease, tag, tender
```
