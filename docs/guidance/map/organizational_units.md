```{workedexample} Organizational units
:tags: parties
```

# Organizational units

Publishers sometimes need to disclose an organizational unit that is involved in a contracting (or planning) process, like a branch or division of a government agency.

The preferred approach to modelling organization units in OCDS is to use the fields in the [`Organization` object](../../schema/reference.md#organization):

* Set `.name` to `{organization name}-{unit name}`.
* Set `.identifier` to the organization's identifier. That is, the identifier of the legal entity of which the unit is a part.
* If the unit has a separate identifier to the organization:
  * Set `.id` to `{identifier.scheme}-{identifier.id}-{unit identifier}`.
  * Add the unit's identifier to `additionalIdentifiers`. Note that `.additionalIdentifiers` need to reference the same legal entity as `.identifier`.
* Set `address` and `contactPoint` to the unit's address and contact point, respectively.

If the fields in the `Organization` object are not sufficient to express your data, you can use or create an extension to add fields to the `parties.details` object.

Disclosing organizational hierarchies in OCDS is strongly discouraged unless there is a clear use case to support it. Ideally, organizational hierarchies ought to be represented in separate, non-OCDS datasets that use the same organization and unit identifiers. To design a hierarchy-oriented dataset, refer to the [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/). However, if you need to represent organizational hierarchies in OCDS, you can use the [memberOf extension](https://github.com/open-contracting-extensions/ocds_memberOf_extension).

## Worked examples

### Using the Organization object

San Felipe Hospital in Honduras announces a planning process for the purchase of food supplies. The hospital is a unit of the Ministry of Health (Secretaría de Salud Pública) and is not a separate legal entity.

The hospital is listed in the `parties` section and:

* `.id` is set to `{identifier.scheme}-{identifier.id}-{unit identifier}`: HN-ONCAE-H1-10001-102.
* `.name` is set to `{organization name}-{unit name}`: Secretaría de Salud Pública - Hospital San Felipe.
* `.identifier` is set to the identifier for the legal entity to which the organizational unit belongs, the Ministry of Health.
* the identifier for the organizational unit is listed in `.additionalIdentifiers`.
* `address` and `contactPoint` are set to the address and contact point of the hospital.

```{jsoninclude} ../../examples/organizations/organizational_units/honduras_organization_identifier_scheme.json
:jsonpointer: /releases/0/parties/0
:expand: parties, identifier, additionalIdentifiers
```

### Publishing a separate organizational hierarchy dataset

The Hospital Clinic (Hospital de Clínicas) in Paraguay is an organizational unit of the Faculty of Medical Sciences (Facultad de Ciencias Médicas) at the National University of Asuncion (Universidad Nacional de Asunción). The hospital is part of the same legal entity as the faculty, but the faculty is a separate legal entity from the university.

Users need to analyse procurement at hospital, faculty and university level. To serve that need, Paraguay publishes an OCDS dataset and a separate organizational hierarchy dataset.

In the OCDS dataset, the hospital is listed in `parties` section and:

* `.name` is set to `{organization name}-{unit name}`: Facultad de Ciencias Médicas - Hospital de Clínicas.
* `.identifier` is set to the Faculty of Medical Sciences' identifier.

Users can group by `.name` to identify the hospital's contracting processes and by `.identifier` to identify the faculty's contracting processes.

```{jsoninclude} ../../examples/organizations/organizational_units/paraguay_organization_name.json
:jsonpointer: /releases/0/parties/0
:expand: identifier
:title: release
```

The organizational hierarchy dataset describes the relationship between the faculty and the university. It uses the same organization identifiers as the OCDS dataset.

Users can use the organization identifiers to join the datasets and identify the university's contracting processes.

```{csv-table-no-translate}
:header-rows: 1
:file: ../../examples/organizations/organizational_units/paraguay_organizations.csv
```
