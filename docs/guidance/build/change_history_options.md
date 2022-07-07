# Change History Implementation Options

The releases and records model allows publishers to disclose the change history of a contracting process and/or its current state. To meet the widest range of user needs, the preferred approach is to [publish both the change history and the current state](../build/incremental_updates).

In order to publish a change history, your data sources need to track what changed and when, for example, by implementing events and/or last modified dates on database records. The [system architecture](../build/system_architectures) for your OCDS implementation also needs to store historic releases. If you cannot store historic releases, you can [publish full releases and update the release `id` and `date` each time there is a change](../build/full_updates).

However, publishing a change history is not always possible. Sometimes, it is only possible to publish the full information about a contracting process at a given time. This might be the case if, for example, your data sources don't implement versioning, events, good identifiers, or proper controls (e.g. allowing users to just change a supplier's name instead of requiring the user to register a new supplier in the system). This also might be the case if you collect non-OCDS data from a data source and re-publish it as OCDS and you don't have direct access to the data source.

In the above scenarios, if you publish data as individual releases, problems can occur if new releases have different array entries from earlier releases, that were intended to replace the entries in the earlier releases. Due to how the [merge routine](../../schema/merging.md#merge-routine) works for most arrays of objects, the new entries wouldn't replace the existing entries but would be added to as new entries, leading to erroneous data.

Therefore, if you cannot publish a change history for the above reasons, you ought to [publish compiled releases only](../build/no_change_history).
