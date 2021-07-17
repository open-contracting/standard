## Unsuccessful processes

In most jurisdictions, if a procedure is cancelled or unsuccessful, and a **new procedure** is started to procure the same items, the two procedures are considered two **different** contracting processes. This is in keeping with the OCDS definition of a contracting process.

However, in some jurisdictions, such as Paraguay, the planning stage is considered as the initiation of the process. In these jurisdictions when a tender fails and a new tender is started, the two tenders are considered part of the same contracting process. This differs from the OCDS definition of a contracting process. OCDS, instead, records the cancelled procedure as a `relatedProcess` to the new procedure with the 'unsuccessfulProcess' relationship type.  

![Unsuccessful Tender](../../_static/png/unsuccessful-tender.png)

### Example: Modelling unsuccessful tenders in Paraguay

The [Sistema de Información de las Contrataciones Públicas (SICP)](https://contrataciones.gov.py/) discloses information about contracting processes for all public entities in Paraguay. SICP is managed by the National Directorate of Public Procurement (DNCP in Spanish).

Paraguay discloses all stages of the contracting process, from planning to implementation. The first data disclosed is about the planning stage. Planning data includes an estimate of what an entity is going to buy, when and for how much. SICP assigns an `ocid` when the planning data is first disclosed, before the tender stage. In this example, the ocid is 'ocds-03ad3f-331547-1'.

```eval_rst
.. jsoninclude:: ../../examples/unsuccessful-tender-planning.json
   :jsonpointer:
   :expand: releases, planning
   :title: unsuccessful-tender-planning

```

Next, the tender data is disclosed, but the tender was unsuccessful, so the tender status is ‘unsuccessful’.

```eval_rst
.. jsoninclude:: ../../examples/unsuccessful-tender-tender.json
   :jsonpointer:
   :expand: releases, tender, status
   :title: unsuccessful-tender-tender

```

The buyer issues another tender to buy the same item, based on the same planning as the first tender.

Paraguay considers the two tenders part of the same contracting process. But, in OCDS the two tenders are separate contracting processes.

To construct an `ocid` for the second contracting process, Paraguay adds a consecutive number to the `ocid` of the first process. In this example the new `ocid` is 'ocds-03ad3f-331547-2'

Paraguay could also have used the identifier for the second tender as the `ocid` for the second contracting process.

The `relatedProcess` block links the two processes, with the relationship set to ‘unsuccessfulProcess’.

```eval_rst
.. jsoninclude:: ../../examples/unsuccessful-tender-related-process.json
   :jsonpointer:
   :expand: releases, relatedProcesses, relationship
   :title: unsuccessful-tender-related-process

```
