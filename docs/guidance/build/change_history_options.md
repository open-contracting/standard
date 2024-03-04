# Change history implementation options

First, you need to decide whether or not to publish a change history.

To publish a change history, you need to be able to determine what changed and when within your data sources: for example, by using event-based triggers or last-modified dates. You also need to use a [system architecture](system_architectures) that has a [separate OCDS datastore]((system_architectures.md#separate-ocds-datastore), so that you can provide access to historic releases.

Sometimes, it isn't possible to determine what changed and when: for example, because your data sources don't implement triggers, timestamps, versioning, or consistent identifiers. If identifiers are inconsistent, publishing a change history can lead to incoherent data, due to how the [merge routine](../../schema/merging.md#merge-routine) handles array entries.

If you choose to publish a change history, you need to decide whether to publish [incremental or full updates](#incremental-or-full-updates).

If you choose not to publish a change history, you need to decide whether to publish [individual releases or compiled releases](#individual-releases-or-compiled-releases).

## Incremental or full updates

A *full* update is a [release](../../schema/reference) that contains all the available information about the contracting (or planning) process. An *incremental* update is a release that contains a subset of the available information, focusing on what's new or changed.

Incremental updates are smaller than full updates. Smaller releases reduce the OCDS datastore's size and users' download times. If you anticipate many releases per contracting process or very many contracting processes, you ought to consider incremental updates.

If you choose to publish incremental updates, the preferred approach is to also publish [compiled releases](../../schema/records_reference.md#compiled-release), so that users can easily access the latest state of the contracting process.

Read about how to [publish a change history](change_history).

## Individual releases or compiled releases

If you can determine what changed and when within your data sources – but cannot implement a separate OCDS datastore – then you ought to publish individual releases. To publish individual releases, you need to update the release identifier along with each change to the data about a contracting process. That way, users can track each update to the contracting process. You also need to ensure that identifiers are consistent for objects in arrays.

If you cannot determine what changed and when, then you ought to [publish compiled releases only](no_change_history).
