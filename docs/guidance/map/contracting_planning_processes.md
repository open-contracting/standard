# Contracting processes and planning processes

There are two types of processes in OCDS: contracting processes and planning processes. Each process has a [unique contracting process identifier](../../schema/identifiers.md#contracting-process-identifier-ocid) (`ocid`). This section helps map your contracting activities (most often procurement procedures) to the OCDS processes. 

OCDS defines a contracting process as:

> All the actions aimed at implementing one or more contracts. This covers tendering, awarding, contracting and implementation. It does not include actions linked to planning, as these are often less structured and may be linked to multiple contracting processes. In multiple stage procedures (e.g. framework agreements with reopening of competition), each round of competition is treated as a separate contracting process.

> Procedures that failed and were restarted are considered new processes.

> Boundaries between processes (e.g. whether two contracts result from a single process or from two processes) are set by buyers depending on their needs (e.g. efficient division of labor, clear communication with the market) and legislation (e.g. rules on using procedures and lots).

and a planning process as: 

> All the actions aimed at planning one or more contracting processes. This covers, for example, establishing the rationale for the procurement, giving the market a general description of the purchase, getting the necessary budget, forecasting and conducting market research.

> Planning processes are often less structured than contracting processes, so one or more planning process may end up leading to one or more contracting process.'

![Contracting Process](../../_static/png/contracting_process.png)

A planning process ought to have `releaseTag` set to 'planning' (or 'planningUpdate'). A contracting process can have `releaseTag` set to [any other value from the codelist](../../schema/codelists.md#release-tag). A planning process should not contain the `releaseTag` 'tender' even if it contains the `Tender` block. The two processes ought to be linked together using the `relatedProcesses` array in the releases concerning the contracting process, with `.relationship` set to 'planning'.

```{note}
When publishing data, we recommend separating data about the planning and contracting processes in line with the definitions above. However, publications of both planning and contracting data within a single contracting process continue to be conformant with OCDS 1.2 and earlier. Requiring the publication of this data in separate planning and contracting processes is being considered for a future, backwards incompatible version of the standard ([GitHub issue](https://github.com/open-contracting/standard/issues/866)).
```

```{note}
In OCDS 1.2 and earlier, it is not possible to publish all information about multi-stage procedures under a single contracting process. There is guidance on how to deal with this for [framework agreements guidance](related_processes) and [pre-qualification and pre-selection](pre-qualification). If you want to disclose this type of information (including other types of multi-stage procedures, such as competitive dialogues and innovation partnerships), contact the [helpdesk](../../support/index.md). The approach to modelling multi-stage procedures in a future, backwards incompatible version of the standard is under discussion on [Github](https://github.com/open-contracting/standard/issues/440).
```
