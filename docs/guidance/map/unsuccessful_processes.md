# Unsuccessful processes

In the case of procurement, a contracting process can be defined as a procurement procedure. There is a one-to-one correspondence between the first stage of a procurement procedure (tender) and a contracting process.

In OCDS, at a conceptual level, a contracting process is intended to match each concrete attempt to start a procedure that leads to one or more contracts. Attempts can include: an invitation to tender (in open procedure); an invitation to request to participate; a competition for a concession; a direct award, etc.

![Contracting Process](../../_static/png/contracting_process.png)

In OCDS, the `ocid` is the unique identifier for a contracting process. As the initiation of the procurement process is the tender, normally the identifier for a tender can be used as the `ocid`.

In most jurisdictions, if a procedure is cancelled or unsuccessful, and a **new procedure** is started to procure the same items, the two procedures are considered two **different** contracting processes. This is in keeping with the OCDS definition of a contracting process.

But in other jurisdictions, such as Paraguay, planning is considered as initiating the process. In these jurisdictions when a tender fails and a new tender is started, the two tenders are considered part of the same contracting process. This differs from the OCDS definition of a contracting process.

In OCDS, it is relevant and desirable to disclose information about planning, but the contracting process is not interpreted as "starting" with planning. In OCDS, the planning process is something that comes **before** the initiation of a contracting process. The initiation of the procedure is not the planning process, because at least one of the following is true of a planning process: it is not a concrete attempt to award one or more contracts like a request for tender, etc.; it is not a concrete opportunity for potential suppliers to participate in; it does not describe the competitive conditions.

However a jurisdiction treats unsuccessful tenders and subsequent tenders, in OCDS they are considered separate but related contracting processes.

This relationship can be modelled using the `relatedProcess` array at the release level, with the ‘unsuccessfulProcess’ relationship type.  

![Unsuccessful Tender](../../_static/png/unsuccessful_tender.png)

## Example: Modelling unsuccessful tenders in Paraguay

The [Sistema de Información de las Contrataciones Públicas (SICP)](https://contrataciones.gov.py/) discloses information about contracting processes for all public entities in Paraguay. SICP is managed by the National Directorate of Public Procurement (DNCP in Spanish).

The first data disclosed is about the planning process. Planning data includes an estimate of what an entity is going to buy, when and for how much. SICP assigns an `ocid` when the planning data is first disclosed, before the tender stage. In this example, the ocid is 'ocds-03ad3f-331547'.

```{jsoninclude} ../../examples/unsuccessful_tender/planning.json
:jsonpointer:
:expand: releases, planning
:title: unsuccessful-tender-planning
```

Next, the contracting process is disclosed, using a new `ocid`, 'ocds-03ad3f-331547-1'. The `relatedProcess` block links the planning process and the contracting process, with the relationship set to 'planning'.

The tender was unsuccessful, so the tender status is set to ‘unsuccessful’.

```{jsoninclude} ../../examples/unsuccessful_tender/tender.json
:jsonpointer:
:expand: releases, relatedProcesses, tender, status
:title: unsuccessful-tender-tender
```

The buyer issues another tender to buy the same item, following from the same planning process.

Paraguay considers the two tenders part of the same contracting process. But, in OCDS the two tenders are separate contracting processes.

To construct an `ocid` for the second contracting process, Paraguay adds a consecutive number to the `ocid` of the first process. In this example the new `ocid` is 'ocds-03ad3f-331547-2'

Paraguay could also have used the identifier for the second tender as the `ocid` for the second contracting process.

The `relatedProcess` block links to the unsuccessful contracting process with the relationship set to ‘unsuccessfulProcess’, and to the initial planning process with the relationship set to ‘planning’.

```{jsoninclude} ../../examples/unsuccessful_tender/related_process.json
:jsonpointer:
:expand: releases, relatedProcesses, relationship
:title: unsuccessful-tender-related-process
```
