# People in Organizations

In some scenarios, publishers may have the need to disclose information about individuals involved at some stage in the contracting process.

Although the parties array may seem to be the place to include people, this block is reserved for organizations. Therefore, information of individuals should be disclosed using extensions. The only exceptions are tenderers and suppliers, which are typically treated as they were organizations by the procurement authorities.

Usually, these individuals already belong to an organization that participates in the contracting process. A few examples are:

* Legal representatives of suppliers and buyers: a legal representative acts in representation of an organization, and they are not parties themselves.
* Owners, authorized agents, signing officers, contact points, etc.: these are members of an organization who can also act on behalf of that organization, within the legal limits of the rights/privileges accorded to their role/office. They are not parties themselves either.

When including information about individuals, it is important to link them clearly to the organizations they belong to, either by including them as attributes in the party block or through organization references. 

We invite for discussion at [Github](https://github.com/open-contracting/standard/issues/883) about how to include individual information in a generic way for future versions of the standard.

## Worked examples

### Example #1: Legal representatives

In Moldova, the *Primaria s. Elizaveta* is awarding a contract on food supplies to the  *Slavena Lux* company. By local regulations the supplier's legal representative in charge of signing the contract must be disclosed.

The release example shown below uses the [eOCDS-Persons](https://github.com/eOCDS-Extensions/eOCDS-persons) local extension from Moldova, which adds a `persons` block to the `parties` section. Besides providing basic data of individuals, the extension also adds information on the role(s) the individual has within the organization.

```eval_rst
.. jsoninclude:: ../../examples/people-in-organizations/moldova.json
   :jsonpointer: /releases
   :expand: parties, persons
   :title: award

```

### Example #2: Members of the award committee

In Guatemala, the information about the award committee members are disclosed once the supplier is awarded. 

In the following example, the National Institute of Forensic Science is procuring lab supplies. The award release introduces a few updates to the tender information, including the names and roles of the award committee members. A local extension is used to include the information as part of the procuring entity party, in the `details` section.

```eval_rst
.. jsoninclude:: ../../examples/people-in-organizations/moldova.json
   :jsonpointer: /releases
   :expand: parties, awardCommitteeMembers
   :title: award
```

#### Extension

The `release.json` and `extension.json` files from the *awardCommitteeMembers* extension are shown below.

```eval_rst
.. jsoninclude:: ../../examples/people-in-organizations/award-committee-members-extension/extension.json
   :jsonpointer:
   :expand: name,description,documentationUrl,schemas,codelists,compatibility
   :title: extension.json
```

```eval_rst
.. jsoninclude:: ../../examples/people-in-organizations/award-committee-members-extension/extension.json
   :jsonpointer:
   :expand: name,description,documentationUrl,schemas,codelists,compatibility
   :title: release.json
```



The *membershipType* codelist is shown in the following table.

```eval_rst
.. csv-table-no-translate::
   :file: ../../examples/people-in-organizations/award-committee-members-extension/codelists/membershipType.csv
   :header-rows: 1
```

The [Extension Template Repository](https://github.com/open-contracting/standard_extension_template) includes a guidance to create OCDS extensions.