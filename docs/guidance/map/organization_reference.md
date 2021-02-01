# Organization references

Many parties can be involved in the lifecycle of a contracting process. Sometimes the same party can have multiple roles. For example, an organization can first be a tenderer and then become a supplier.

To avoid data repetition, OCDS 1.1 introduced a top-level parties array, where the detailed information about all the organizations and other participants involved in a particular contracting process is declared.

When a **reference** is needed to an entry in the parties array, e.g. to provide a link between a `tenderer` declared in the `tender` section and its organization details, use an `OrganizationReference` object. This object includes just the `name` and `id` of the organization, instead of repeating all its relevant data again.

## Worked Example

In the example below:

* An Organization is declared in the `parties` array with the `id` *GB-COH-09506232* and `name` *Open Data Services*. Information related to its legal `identifier` and `contactPoint` is also disclosed here.
* An OrganizationReference object is used in the `tenderers` and `suppliers` array to reference *Open Data Services*, **without** duplicating the organization's detailed information.
* If a user looks at the `tenderers` block and wants to contact *Open Data Services*, then the user has to search for the `id` *GB-COH-09506232* in the `parties` array.
* The same needs to be applied to each `OrganizationReference` instance.


```{eval-rst}

.. jsoninclude:: ../../examples/organization_reference.json
   :jsonpointer:
   :expand: releases, parties, tender, tenderers, awards, suppliers
   :title: organizationReference

```
