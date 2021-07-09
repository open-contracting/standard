# Beneficial ownership information

This worked example describes how to:

* publish separate contracting and beneficial ownership datasets
* publish beneficial ownership data using OCDS

The Beneficial Ownership Data Standard (BODS) [defines](https://standard.openownership.org/en/0.2.0/primer/whatisbo.html) “beneficial ownership” as:

> The right to some share of a legal entity’s income or assets (ownership) or the right to direct or influence the entity’s activities (control).

Publishing the beneficial owners of tenderers and suppliers can help users to:

* Identify collusion or deception
* Detect undeclared conflicts of interest
* Identify companies with debarred or sanctioned owners
* Assess risk

```{note}
For more information on the uses of beneficial ownership data in the context of procurement, see [Beneficial ownership data in procurement](https://www.openownership.org/uploads/OO%20BO%20Data%20in%20Procurement.pdf). 
```

Some procurement systems collect beneficial ownership data, usually when companies submit bids. This data is true at the time of collection. But, procurement systems don’t track later changes to the ownership and control of suppliers. This limitation is especially challenging for users interested in long-standing contracts, in which there may have been many changes.

Therefore, the preferred approach is to **publish separate contracting and beneficial ownership datasets**:

* Publish contracting data using OCDS.
* Collect beneficial ownership data in a separate beneficial ownership register.
* Periodically confirm the accuracy of data in the register and record changes as they happen.
* Publish beneficial ownership data using BODS, including a history of changes.

To allow users to connect contracting data and beneficial ownership data, you should use the same [organization identifiers](https://standard.open-contracting.org/latest/en/schema/identifiers/#organization-ids) in both datasets.

At the same time, you can **publish beneficial ownership data in OCDS** using the [beneficial owners extension](https://extensions.open-contracting.org/en/extensions/beneficialOwners/master/), in particular if:

* You cannot implement a separate beneficial ownership register.
* The companies are not included in any beneficial ownership register: for example, companies based in another country.
* You collect data in both a beneficial ownership register and a procurement system **and** the threshold for disclosure in the procurement system is lower than in the beneficial ownership register.

## Publish separate contracting and beneficial ownership datasets

The UK publishes separate contracting and beneficial ownership datasets. Both datasets use the same organization identifier: the company number from [Companies House](https://www.gov.uk/government/organisations/companies-house).

### Contracting data

The UK publishes OCDS data from [Contracts Finder](https://www.contractsfinder.service.gov.uk/). 

This example shows a contract award to T.M. ENGINEERS (MIDLANDS) LIMITED. `parties.identifier.id` is set to the supplier’s company number (00507062) and `parties.identifier.scheme` is set to ‘GB-COH’ to identify the register the number is drawn from. 

```{note}
For more information on publishing organization identifiers in OCDS, see [Organization IDs](https://standard.open-contracting.org/latest/en/schema/identifiers/#organization-ids).
```

```{jsoninclude} ../../examples/beneficial_ownership/award.json
:jsonpointer:
:expand: releases, parties, identifier, awards, suppliers
:title: award
```

### Beneficial ownership data

The UK also publishes a separate beneficial ownership dataset: the [People with significant control (PSC) snapshot](http://download.companieshouse.gov.uk/en_pscdata.html). This dataset is updated daily and includes a history of changes. The OpenOwnership Register publishes [the PSC snapshot in BODS format](https://register.openownership.org/data_sources/uk-psc-register).

This example shows the beneficial ownership data for the supplier from the contract award: T.M. ENGINEERS (MIDLANDS) LIMITED. 

BODS is based on statements, where each statement describes ownership or control, entities, or natural persons. For more information, see the [BODS documentation](http://standard.openownership.org/). The example includes:

* An entity statement that describes the company and includes the company number: 00507062. This is the same organization identifier used in the OCDS data.
* An ownership/control statement that describes the relationship between an interested party and the company.
* A person statement that includes the details of the beneficial owner of the company. 

```{jsoninclude} ../../examples/beneficial_ownership/beneficial_ownership_statement_entity.json
:jsonpointer:
:expand: identifiers
:title: beneficial_ownership_statement_entity
```

```{jsoninclude} ../../examples/beneficial_ownership/beneficial_ownership_statement_ownership.json
:jsonpointer:
:expand: subject, interestedParty, interests
:title: beneficial_ownership_statement_ownership
```

```{jsoninclude} ../../examples/beneficial_ownership/beneficial_ownership_statement_person.json
:jsonpointer:
:expand: names, nationalities, birthDate, addresses
:title: beneficial_ownership_statement_person
```

## Publish beneficial ownership data in OCDS

Moldova [collects the name and nationality](https://tender.gov.md/ro/content/formularul-standard-al-documentului-unic-de-achizi%C8%9Bii-european?fbclid=IwAR14CSxh6bo45cTq-hzVbwhnEkk9OEkY1aF86j1hVIU8kTnvaW3cU4q5loc) of the beneficial owners of bidders in its procurement system. But, Moldova does not maintain a separate beneficial ownership register.

Therefore, Moldova can use the beneficial owners extension to publish the data in OCDS. For more information on using the beneficial ownership extension, see the [extension documentation](https://extensions.open-contracting.org/en/extensions/beneficialOwners/master/).

This example shows a fictional contract award to Microsoft Moldova:

* In the package metadata, the `extensions` array includes the beneficial owners extension.
* In the `parties` array:
  * `beneficialOwners.name` is set to the name of the beneficial owner
  * `beneficialOwners.nationality` is set to the country code for the nationality of the beneficial owner

```{jsoninclude} ../../examples/beneficial_ownership/beneficial_owners_extension.json
:jsonpointer:
:expand: extensions, releases, parties, identifier, beneficialOwners
:title: beneficial-owners-extension
```
