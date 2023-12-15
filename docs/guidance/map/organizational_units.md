```{workedexample} Organizational units
:tags: parties
```

# Organizational units

For some use cases, publishers might need to disclose the organizational units involved in the contracting (or planning) process, e.g agency branches or divisions.

There is more than one approach to model organizational units in OCDS:

1. **Use the fields available in the Organization sub-schema**. This is the preferred approach, when possible. 

    * Unit names can be included in the `name` field alongside the organization name. 
    * The `additionalIdentifiers` array can be used to provide any unit identifiers. It is important to note that `identifier` and `additionalIdentifiers` need to point toward the *same legal entity*. The main `identifier` ought to belong to the organization and the `legalName` field can be used to provide the organization name alone. 
    * The `address` and `contactPoint` objects can be filled with the unit information. 
    * Unit identifiers can also be appended to `parties/id`.

2. When the first option is not enough to model the publisher's case, **use or create an extension**. Any additional fields can be placed under the `details` field of the `Organization` sub-schema.

Some publishers use the [memberOf](https://github.com/open-contracting-extensions/ocds_memberOf_extension) extension to represent organization hierarchies, including organizational units. This is strongly discouraged unless there is a clear use case to support it, because OCDS is not designed to disclose hierarchical organization information. Ideally, organizational hierarchies would be represented in separate, non-OCDS datasets, and organizational units would be modelled using one of the alternatives described above. 

## Worked examples

### 1. Using the Organization sub-schema

In Honduras, the Ministry of Health is planning the procurement of food supplies for the San Felipe Hospital. For the purposes of the example, San Felipe Hospital is considered to be a unit belonging to the Ministry of Health, and it is not a legal entity of its own.

In the release below, the publisher adds the hospital name at the end of the procuring entity name. The main identifier for the organization (*Secretaría de Salud Pública*) is extracted from a local list in the "HonduCompras" platform, used to publish procurement information in the country.

An identifier for the hospital has been added using the "HN-ONCAE-UNIT" list code. The `address` and `contactPoint` information belongs to the hospital only.

```{jsoninclude} ../../examples/organizations/organizational_units/honduras_organization_identifier_scheme.json
:jsonpointer:
:expand: releases, parties, identifier, additionalIdentifiers
:title: release
```

### 2. Defining a new Extension

In Moldova, the national procurement agency needs to include a division code for particular organizations. Since divisions can be separate legal entities in some cases, the publisher chooses to use the `identifier` object to point to the main organization for all cases, and use an additional field to provide the division code that enables data users to locate the departments and branches involved.

In the release below, a branch of the Bank of Moldova announces a contract opportunity for the provision of consumables for electrical appliances.

```{jsoninclude} ../../examples/organizations/organizational_units/moldova_organization_extension.json
:jsonpointer:
:expand: releases, parties, identifier, additionalIdentifiers, details
:title: release
```

```{jsoninclude} ../../examples/organizations/organizational_units/ocds_divisionCode_extension/extension.json
:jsonpointer:
:expand: name, description, schemas, compatibility
:title: extension
```

```{jsoninclude} ../../examples/organizations/organizational_units/ocds_divisionCode_extension/release-schema.json
:jsonpointer:
:expand: definitions, Organization, properties, details, properties, divisionCode
:title: release-schema
```

The branch name (*Chişinău Branch*) is appended at the end of the name of the buyer. A new extension called "Division code" has been defined to add the `divisionCode` field in the `parties/details` section. The branch code in the example is "101".

The `extension.json` and `release-schema.json` files for the Division code extension can be displayed using the combo box above the JSON example. Instructions on how to create an OCDS extension can be found [here](https://github.com/open-contracting/standard_extension_template).

### 3. Using the Organization sub-schema with an organizational hierarchy

The *Hospital de Clínicas* is planning to procure supplies for their Blood Center. The Hospital is part of the Medical School in the National University of Asuncion. Since the hospital is key in the provision of healthcare for low income groups in the community, it is in the interest of many to clearly identify the procurement of the Hospital only. It is also important for the publisher that users can group the data following organizational hierarchies.

It is important to note that OCDS ought to not be used to publish organizational hierarchies unless there is a strong case to support it. Organizational hierarchies can be disclosed in additional datasets. Publishers can refer to the [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) to design a hierarchy-oriented dataset.

The release below shows how the publisher chooses to model the hospital as an organizational unit of the Medical School (*Facultad de Ciencias Médicas*). The source systems collect the name of the organizational unit only, and this is appended to the organization name.

```{jsoninclude} ../../examples/organizations/organizational_units/paraguay_organization_name.json
:jsonpointer:
:expand: releases, tag, parties, identifier
:title: release
```

In a separate dataset, the publisher discloses the organizational hierarchy. This dataset, in combination with the OCDS publication,  would allow users to summarize contracting information. The table below shows an extract of the dataset.

```{csv-table-no-translate}
:header-rows: 1
:file: ../../examples/organizations/organizational_units/paraguay_organizations.csv
```

