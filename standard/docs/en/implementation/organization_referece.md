# Organization References

During a contracting process many parties can be involved in it. Some times the same party may have multiples roles. 
For example a supplier can be first a tenderer and then become a supplier.

To avoid data repetition, since OCDS 1.1, there is a parties array where the information about all the parties is set. 
And then, when you need to **reference** one of these parties you use a OrganizationReference object. 
This object includes just the name and id of it instead of its whole data again.

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