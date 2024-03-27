```{workedexample} Unsuccessful processes
:tags: tender
```

# Unsuccessful processes

Contracting processes are sometimes cancelled or unsuccessful, in which case a buyer might restart a process to purchase the same items.

In OCDS, when a buyer restarts a failed contracting process, the restart is modelled as the initiation of a new contracting processes.

To link a new process to the previous attempt at procuring the same items, you ought to add the unsuccessful process to the `relatedProcesses` array of the new process, with a `.relationship` of 'unsuccessfulProcess'.

![Unsuccessful Tender](../../_static/png/unsuccessful_tender.png)

## Example

This example illustrates how to model failed and restarted contracting processes in OCDS.

A buyer attempts to purchase office supplies by announcing an opportunity. The contracting process is assigned an `ocid` of 'ocds-213czf-0000'.

```{jsoninclude} ../../examples/unsuccessful_tender/tender.json
:jsonpointer: /releases/0
:expand: releases, tender
```

The attempt is unsuccessful so the buyer sets `tender.finalStatus` to 'unsuccessful'.

```{jsoninclude} ../../examples/unsuccessful_tender/tenderUpdate.json
:jsonpointer: /releases/0
:expand: releases, tender
```

The buyer announces a second opportunity to purchase the same item. The new contracting process is assigned a new `ocid` of 'ocds-213czf-0001'. The failed attempt is recorded in `.relatedProcesses`.

```{jsoninclude} ../../examples/unsuccessful_tender/new_tender.json
:jsonpointer: /releases/0
:expand: releases, tender, relatedProcesses
```

```{admonition} Unsuccessful and restarted processes with a shared identifier
  In some jurisdictions, such as Paraguay, if a first attempt is unsuccessful in procuring items, the second attempt is considered to be part of the same contracting process and, as a result, shares its identifier. In OCDS, the two attempts need to be modelled as separate contracting processes with different `ocid`s.
  
  If your data sources lack a unique identifier for the second attempt, you can assign its `ocid` by appending an incrementing number to the `ocid` of the first process, e.g. `{first process ocid}-1`.
```
