# Identifiers

Consistent identifiers are essential to help join up open contracting data.

* The open contracting process identifier (ocid) is a globally unique identifier used to join up all the data about a single contracting (or planning) process;
* Organization identifiers are important to know who is involved in each contract;
* Release, award and contract identifiers are important to help cross-reference information.

## Types of identifiers

In OCDS there are two kinds of identifiers: globally unique and local.

### Globally unique identifiers

Across the whole universe of OCDS publishers these identifiers refer to one specific process or organization.

We create globally unique process identifiers by adding a prefix to the internal identifiers held by publishers.

```{admonition} Worked Example
:class: hint

Two government publishers (Town A and Town B) number their contracting processes from 0 upwards.

Town A publishes information on a contracting process to build a new road. Internally they know this as contract 0005.

Town B publishes information on a contracting process to buy textbooks for a school. Internally they also know this as contract 0005.

When they publish their OCDS data, each government adds a unique prefix onto their internal identifiers.

Now Town A's contracting process has the `ocid` of 'ocds-fh349f-0005' and Town B's contracting process has the `ocid` of 'ocds-twb234-0005'.

There is now no chance of these getting mixed up in a system which imports data from both towns.

And, if an independent civil society contract monitoring group want to publish a report about implementation of Town A's road project, or Town B's text-book procurement, they have distinct identifiers they can use in their own data to refer to these.
```

You can read more about the OCDS approach to identify organizations below.

### Local identifiers

Not all the identifiers in OCDS need to be globally unique. Most only need to be unique among the identifiers used for the same type of object within the same scope. For example:

* A release ID must be unique within the scope of the process of which it is a part;
* Award and contract identifiers must be unique within the scope of the process of which they are a part;
* An item, milestone or document ID must be unique within the array it is part of.

Local identifiers must be used consistently. For example, if the `id` of an award is "22" in one release, then the `id` of the same award in another release must also be "22".

## Open contracting process identifier (ocid)

<img src="../../_static/svg/green_compilation.svg" width="150" align="right"/>

An open contracting process identifier (ocid) is a **globally unique identifier** for a contracting process. Every contracting process in OCDS is assigned an ocid.

The contracting process to which an OCDS release or record relates is identified by the `ocid` field. Therefore, a contracting process's ocid be used to join up data that is published at different times or from different systems.

In the context of a release, the `ocid` field is described as:

```{field-description} ../../build/current_lang/release-schema.json /properties/ocid
```

In the context of a record, it is described as:

```{field-description} ../../build/current_lang/record-package-schema.json /definitions/Record/properties/ocid
```

An ocid is composed of two parts:

1. An [ocid prefix](#ocid-prefix) that establishes an identifier series, for which there is one publisher with the authority to mint ocids
1. An internal contracting process identifier that is unique within the scope of the identifier series

The ocid is case-sensitive; in other words, the letter case of an ocid must be consistent. It is encouraged to separate the ocds prefix and the internal identifier with a hyphen (`-`).

Before assigning an ocid to a contracting process, you need to [register an ocid prefix](../guidance/build.md#register-an-ocid-prefix) and decide on suitable identifier to use as the internal contracting process identifier. You might need to consider changes to existing systems to ensure that different systems handling information about your contracting and planning processes share a common internal contracting process identifier.

```{admonition} Worked Example
:class: hint

In Mexico City, each time a tender or direct contract award process is initiated, the department responsible assigns an identifier.

These are made up of an identifier for the department responsible for the procurement, a tender number, and the year.

For example:

> OM-DGRMSG-004-13

This internal identifier can be exchanged with, and recorded in, any other systems which process information about this contracting process. For example, systems for reporting or recording spending transactions to suppliers.

Mexico City then registered a prefix with the Data Support Team. They have been given the prefix ‘ocds-87sd3t’ which can be added to their unique process identifiers to give a globally unique `ocid`. E.g.

> ocds-87sd3t-OM-DGRMSG-004-13
```

### ocid prefix

The purpose of the ocid prefix is to ensure that each ocid is globally unique. To ensure that their ocids do not conflict with those of another publisher, publisher must [register an ocid prefix](../guidance/build.md#register-an-ocid-prefix).

An ocid prefix is made up of two parts:

1. A prefix agency identifier that establishes a prefix series, for which there is one agency with the authority to mint prefixes
2. A randomly generated six character lowercase alphanumeric string

```{admonition} Who can mint ocid prefixes?
:class: hint

Currently, only the Open Contracting Partnership can mint ocid prefixes, under the 'ocds' prefix agency identifier. In future, other organizations might be able to issue prefixes, each with their own prefix agency identifiers.

```

ocid prefixes are 'dumb' identifiers. They are not intended to carry any semantics and their sole purpose is to turn internal identifiers into globally unique identifiers.

All registered OCID prefixes are accessible as a [web page](https://docs.google.com/spreadsheets/d/1E5ZVhc8VhGOakCq4GegvkyFYT974QQb-sSjvOfaxH7s/pubhtml?gid=506986894&single=true&widget=true) or [CSV file](https://docs.google.com/spreadsheets/d/e/2PACX-1vQP8EwbUhsfxN7Fx7vX3mTA6Y8CXyGi04bHUepdcfxvM6VRVP9f5BWAYEG6MPbnJjWJp-La81DgG8wx/pub?gid=506986894&single=true&output=csv).

### Publisher namespace

Earlier versions of this documentation imposed a stricter pattern on how internal identifiers ought to be combined with the ocid prefix, including a requirement for local namespaces. This requirement has been relaxed in practice and can be considered deprecated.

However, publishers are encouraged to consider whether there are any risks of clashes in local identifiers (e.g. the possibility that two parts of the publishing body might use the same identifier for different contracting or planning processes) and to plan to mitigate this when establishing their own patterns to generate their `ocid`

## Organization identifiers

<img src="../../_static/svg/green_organisation.svg" width="150" align="right"/>

Reliably identifying the legal entities involved in a contracting (or planning) process is vital for transparency and accountability, and for carrying out analysis to improve procurement and contract management.

Publishers should seek to collect and record the **legal identifier** from an official register of any organization involved in a contracting (or planning) process (including buyers, tenderers and suppliers), and should include this in their OCDS files.

There are two parts to expressing an **organization identifier** in open contracting data.

* A prefix for the organization list (also known as registry or register) from which the identifier is drawn: for example, a company register.
* The existing identifier for the organization within that list.

````{admonition} Worked Example
:class: hint

The prefix for the UK's Companies House is "GB-COH". The organization Development Initiatives has been assigned the company number ‘06368740’ by Companies House. The globally unique organization identifier for Development Initiatives can be expressed as below:

```json
{
  "scheme": "GB-COH",
  "id": "06368740",
  "uri": "http://data.companieshouse.gov.uk/doc/company/06368740",
  "legalName": "Development Initiatives Poverty Research Limited"
}
```
````

In OCDS, the list's prefix is disclosed via the `scheme` field of an identifier object, with the existing identifier in the `id` field. If there is a recognized public URL that uniquely identifies the organization (like in the above example), this can be disclosed via the `uri` field.

### Organization lists

There are many kinds of organization lists:

* **Primary registers** - such as national or state company registrars. An identifier issued by these bodies has a specific legal meaning. There is a one to one equivalence between the identifier and a legal entity of a particular form in a given jurisdiction. The identifier is created at the same time that the organization is formally constituted. Changes to the status of the organization are recorded against this identifier in an official register. **Identifiers from a primary register are encouraged in OCDS.**

* **Secondary registers** - which record a particular property of an organization, such as being registered for VAT, or registered as an employer. An organization's identifier in such a registry might change without the organization itself changing in nature. For example, in some jurisdictions, an organization might de-register from VAT, and then re-register, being assigned a new number in the process; or different branches of the same legal entity might register for different VAT numbers.

* **Third-party databases** - which compile a list of organizations, and sometimes their sub-units, on an on-demand basis. These databases do not confer any legal status or special properties on the organizations, but might record a mapping between their own identifiers and other primary or secondary registers' identifiers for the organization. A common example of a third-party database is the proprietary Dun & Bradstreet number. Identifiers from *non-proprietary* databases are preferred, so that users can lookup the identifiers.

* **Local lists** - Some publishers do not map their data to external identifiers, maintaining instead a local list of suppliers. In these cases, the publisher may use their internal identifiers, and should assign a prefix for their organization list. Where possible, the publisher should also provide their local list on the web, with as much additional data about each supplier as possible, in order to maximize the chance of data users matching their local list to some more authoritative register.

See the [full worked example](../guidance/map/organization_identifiers) for more information on implementing identifiers from these different kinds of organization lists.

If you want to disclose identifiers for natural persons, see the [personal identifiers guidance](../guidance/map/organization_personal_identifiers).

## Local organization IDs

Each of the organizations involved in a contracting (or planning) process is declared in the [parties section](reference.md#parties).

Each organization has a local identifier (`id`) used to reference it from elsewhere in the data. For example, `buyer/id` references the buyer's entry in the parties section at `parties/id`.

An organization's `id` is distinct from its organization identifier and need only be unique within the scope of the (contracting or planning) process in which it is involved. An organization’s `id` must be consistent across all releases with the same `ocid` value.

See the [guidance](../guidance/map/organization_identifiers.md#organization-identifiers) for more information on organization identifiers and local IDs.

## Release ID

A release identifier must be unique within the scope of the (contracting or planning) process of which it is a part. In other words, across all releases with the same `ocid` value, each release identifier refers to exactly one release; no two releases use the same release identifier.

A release identifier must also be consistent within this scope. For example, if the `id` of a release is "12345" in one release package, then the `id` of the same release in another release package must also be "12345".

## Award and Contract IDs

Award and contract identifiers must be unique within the scope of the contracting process of which they are a part. In other words, across all releases with the same `ocid` value, each contract identifier refers to exactly one contract; no two contracts use the same contract identifier.

Award and contract identifiers must also be consistent within this scope. For example, if the `id` of an award is "22" in one release, then the `id` of the same award in another release must also be "22".

Contracts must cross-reference a related award (using the `awardID` field), as key information such as suppliers can be contained in the related award. Multiple contracts may refer to a single award, as in the case of a framework contract where multiple contract are issued against a single award.

## Item, Document and Milestone IDs

An item, document or milestone identifier must be unique within a given array of items, and must be used consistently across all the releases in a (contracting or planning) process.

The same `id` value may be re-used in another array of items within the same release, and no cross-reference between these identifiers is implied.

The use of an identifier means that subsequent releases can update prior identified items, documents or milestones, without needing to republish all the items, documents or milestones.

For example:

* A first release sets the items to be procured in `tender/items` and the items awarded in one award in `awards/0/items`:
  * `tender/items` contains three items, with `id` values of "1", "2", and "3"
  * `awards/0/items` contains two items, with `id` values of "3" and "4"

There is *no* relationship between the item to be procured with `id` "3" and the item awarded with `id` "3"; these can be different items. Continuing the example:

* A second release updates the items awarded in the single award in `awards/0/items`:
  * `awards/0/items` contains three items, with `id` values of "3", "4", "5"

Here, there *is* a relationship between the items awarded with `id` "3" and "4" in the first release and the items awarded with `id` "3" and "4" in the second release. The second release is interpreted as updating the existing items "3" and "4" and adding a new item "5".
