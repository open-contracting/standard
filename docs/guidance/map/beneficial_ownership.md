```{workedexample} Beneficial ownership information
:tags: parties
```

# Beneficial ownership information

This example describes how to:

* publish separate contracting and beneficial ownership datasets
* publish beneficial ownership data using OCDS

The Beneficial Ownership Data Standard (BODS) [defines](https://standard.openownership.org/en/0.2.0/primer/whatisbo.html) “beneficial ownership” as:

> The right to some share of a legal entity's income or assets (ownership) or the right to direct or influence the entity's activities (control).

Publishing the beneficial owners of tenderers and suppliers can help users to:

* Identify collusion or deception
* Detect undeclared conflicts of interest
* Identify companies with debarred or sanctioned owners
* Assess risk

```{note}
For more information on the uses of beneficial ownership data in the context of procurement, see [Beneficial ownership data in procurement](https://www.openownership.org/uploads/OO%20BO%20Data%20in%20Procurement.pdf). 
```

Some procurement systems collect beneficial ownership data, usually when companies submit bids. This data is true at the time of collection. But, procurement systems don't track later changes to the ownership and control of suppliers. This limitation is especially challenging for users interested in long-standing contracts, in which there may have been many changes.

Therefore, the preferred approach is to **publish separate contracting and beneficial ownership datasets**:

* Publish contracting data using OCDS.
* Collect beneficial ownership data in a separate beneficial ownership register.
* Periodically confirm the accuracy of data in the register and record changes as they happen.
* Publish beneficial ownership data using BODS, including a history of changes.

To allow users to connect contracting data and beneficial ownership data, you should use the same [organization identifiers](../../schema/identifiers.md#organization-identifiers) in both datasets.

At the same time, you can **publish beneficial ownership data in OCDS** using the [beneficial owners extension](https://extensions.open-contracting.org/en/extensions/beneficialOwners/master/), in particular if:

* You cannot implement a separate beneficial ownership register.
* The companies are not included in any beneficial ownership register: for example, companies based in another country.
* You collect data in both a beneficial ownership register and a procurement system **and** the threshold for disclosure in the procurement system is lower than in the beneficial ownership register.

## Publish separate contracting and beneficial ownership datasets

The UK publishes separate contracting and beneficial ownership datasets. Both datasets use the same organization identifier: the company number from [Companies House](https://www.gov.uk/government/organisations/companies-house).

### Contracting data

A publisher in the United Kingdom collects [Companies House](https://www.gov.uk/government/organisations/companies-house) numbers as its primary organization identifiers for suppliers.

A buyer awards a contract to T.M. ENGINEERS (MIDLANDS) LIMITED. The supplier is listed in the `parties` array with 'supplier' in `.roles`. `.identifier.scheme` is set to the org-id scheme prefix for Companies House ([GB-COH](http://org-id.guide/list/GB-COH)) and `.identifier.id` is set to the supplier's Companies House number (00507062).

```{note}
For more information on publishing organization identifiers in OCDS, see [Organization identifiers](../../schema/identifiers.md#organization-identifiers).
```

```{jsoninclude} ../../examples/beneficial_ownership/award.json
:jsonpointer: /releases/0
:expand: releases, parties, identifier, roles
```

### Beneficial ownership data

The UK government publishes a separate beneficial ownership dataset, the [People with significant control (PSC) snapshot](http://download.companieshouse.gov.uk/en_pscdata.html), which is updated daily and includes a history of changes. Open Ownership publishes [the PSC snapshot in BODS format](https://register.openownership.org/data_sources/uk-psc-register).

This example shows the BODS data for the supplier from the contract award: T.M. ENGINEERS (MIDLANDS) LIMITED. 

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

A publisher in Moldova collects the name and nationality of the beneficial owners of bidders in its procurement system. However, the government of Moldova does not publish a separate beneficial ownership dataset. Therefore, the publisher uses the [beneficial owners extension](https://extensions.open-contracting.org/en/extensions/beneficialOwners) to publish the data in OCDS.

A buyer awards a contract to Microsoft Moldova. The publisher declares the beneficial owners extension in the `extensions` array and publishes the name and nationality of the beneficial owner in `parties.beneficialOwners`.

```{jsoninclude} ../../examples/beneficial_ownership/beneficial_owners_extension.json
:jsonpointer:
:expand: extensions, releases, parties, beneficialOwners
```
