# Identifiers

Consistent identifiers are essential to help join up open contracting data.

* The open contracting process identifier (ocid) is a globally unique identifier used to join up all the data about a single contracting (or planning) process;
* Organization identifiers are important to know who is involved in each contract;
* Release, award and contract identifiers are important to help cross-reference information.

## Open contracting process identifier (ocid)

<img src="../../_static/svg/green_compilation.svg" width="150" align="right"/>

OCDS defines a release's `ocid` field as:

```{field-description} ../../build/current_lang/release-schema.json /properties/ocid
```

(The definition of a record's `ocid` field replaces "release" with "record".)

Since the `ocid` field is a required field and is globally unique, it can be used to join up data that is published at different times or from different systems.

An `ocid` is composed of two parts:

1. An [OCID prefix](#ocid-prefix), which identifies the series of identifiers to which the `ocid` belongs
1. An internal identifier for the contracting (or planning) process, which is unique within the series

It is encouraged to separate the OCID prefix and the internal identifier with a hyphen (`-`).

The `ocid` is case-sensitive; in other words, the letter case of an ocid must be consistent.

To assign an `ocid` to a contracting (or planning) process, you need to [register an OCID prefix](../guidance/build.md#register-an-ocid-prefix) and choose an internal identifier.

````{admonition} Example
:class: hint

Two publishers, the UK Atomic Energy Authority and Health Canada, use sequential numbers as internal identifiers for their contracting processes.

The UK Atomic Energy Authority initiates a contracting process to purchase productivity software and assigns it the internal identifier "0005". Health Canada initiates a contracting process to purchase office furniture and also assigns it the internal identifier "0005".

To create a globally unique `ocid`, each publisher prepends their internal identifier with their OCID prefix: "ocds-fh349f" for the UK Atomic Energy Authority and "ocds-twb234" for Health Canada.

The UK Atomic Energy Authority assigns the `ocid` "ocds-fh349f-0005".

```json
{
  "ocid": "ocds-fh349f-0005",
  "publisher": {
    "name": "UK Atomic Energy Authority"
  },
  "tender": {
    "id": "0005",
    "title": "Productivity software"
  }
}
```

Health Canada assigns the `ocid` "ocds-twb234-0005".

```json
{
  "ocid": "ocds-twb234-0005",
  "publisher": {
    "name": "Health Canada"
  },
  "tender": {
    "id": "0005",
    "title": "Office furniture"
  }
}
```

As such, users and tools that work with both publishers' data will not confuse the two contracting processes.

````

### OCID prefix

The only purpose of the OCID prefix is to turn *locally* unique identifiers into *globally* unique identifiers, without coordination between publishers.

To ensure that your `ocid`s do not conflict with those of another publisher, you must [register an OCID prefix](../guidance/build.md#register-an-ocid-prefix).

Only the publisher that registered an OCID prefix is authorized to assign new `ocid`s with that OCID prefix, or to delegate this responsibility.

```{note}
All registered OCID prefixes are accessible as a [web page](https://docs.google.com/spreadsheets/d/1E5ZVhc8VhGOakCq4GegvkyFYT974QQb-sSjvOfaxH7s/pubhtml?gid=506986894&single=true&widget=true) or [CSV file](https://docs.google.com/spreadsheets/d/e/2PACX-1vQP8EwbUhsfxN7Fx7vX3mTA6Y8CXyGi04bHUepdcfxvM6VRVP9f5BWAYEG6MPbnJjWJp-La81DgG8wx/pub?gid=506986894&single=true&output=csv).
```

An *OCID prefix* is composed of two parts, separated by a hyphen (`-`):

1. The identifier of the issuer of the OCID prefix
2. Six randomly generated lowercase alphanumeric characters

OCID prefixes have no meaning, deliberately (they are "dumb" identifiers).

```{admonition} Who can issue OCID prefixes?
:class: hint

Currently, only the [Open Contracting Partnership](https://www.open-contracting.org) can issue OCID prefixes, with the `ocds` issuer identifier. In the future, other organizations might be able to issue OCID prefixes, with their own issuer identifier.
```

### Internal identifier

You must choose a single, unique internal identifier for each contracting (or planning) process.

If such an identifier doesn't already exist, you need to develop a method to create one. You might need to:

* Reconcile different identifiers across different systems (for example, across tender management and contract management)
* Concatenate non-unique values to construct a unique identifier (for example, the year, the buyer, and a sequential number)
* Change existing systems to use a common, unique identifier

## Organization identifiers

<img src="../../_static/svg/green_organisation.svg" width="150" align="right"/>

Reliably identifying the legal entities involved in a contracting (or planning) process is vital for transparency and accountability, and for carrying out analysis to improve procurement and contract management.

Publishers should seek to collect and record the **legal identifier** from an official register of any organization involved in a contracting (or planning) process (including buyers, tenderers and suppliers), and should include this in their OCDS files.

There are two parts to expressing an **organization identifier** in open contracting data.

* A prefix for the organization list (also known as registry or register) from which the identifier is drawn: for example, a company register.
* The existing identifier for the organization within that list.

In OCDS, the list's prefix is disclosed via the `scheme` field of an identifier object, with the existing identifier in the `id` field. If there is a recognized public URL that uniquely identifies the organization, this can be disclosed via the `uri` field.

````{admonition} Example
:class: hint

[Companies House](https://www.gov.uk/government/organisations/companies-house) registers company information in the United Kingdom. The prefix for Companies House is "GB-COH". Companies House registered a company with the name "MICROSOFT LIMITED" and the number "01624297". The company's organization identifier can be expressed as:

```json
{
  "parties": [
    {
      "identifier": {
        "scheme": "GB-COH",
        "id": "01624297",
        "legalName": "MICROSOFT LIMITED",
        "uri": "https://data.companieshouse.gov.uk/doc/company/01624297"
      } 
    }
  ]
}
```
````

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
