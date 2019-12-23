# Organization References

Multiple organization can be part of a procurement process, and sometimes the same organization may have multiples roles
in the same process, for example a supplier can be first a tenderer and then become a supplier. 

To avoid data repetition, since OCDS 1.1, there is a `parties` array where all the parties involved in the procurement
process must be in with the whole information about itself, as its `contactPoint`, `identifier`, etc. And each
time an Organization is mentioned in the data, you should use an `OrganizationReference` object to **reference** an
existing Organization.

# Worked Example

In the example below:

* An Organization is declared in the `parties` array with the `id` *GB-COH-09506232* and `name` *Open Data Services* and also
the information related to its legal `identifier` and `contactPoint` is disclosed here.
* An OrganizationReference object is used to reference *Open Data Services* in the `tenderers` and `suppliers` array, 
**without** duplicating the organization's detailed information.
* If an user looks at the `tenderers` block and wants to contact with *Open Data Services*, then the user has to search for
the `id` *GB-COH-09506232* in the `parties` array.
* The same must be applied to each `OrganizationReference` instance. 

.. jsoninclude:: ../examples/organization_reference.json
   :jsonpointer: 
   :expand: parties, tender, awards
   :title: organizationReference