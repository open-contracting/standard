```{workedexample} Organization identifiers
:tags: parties
```

# Organization identifiers

Publishers regularly collect the *legal identifiers* of the organizations involved in a contracting (or planning) process. These [organization identifiers](../../schema/identifiers.md#organization-identifiers) can be disclosed using OCDS. An organization identifier is composed of two parts:

* A prefix for the organization list (also known as registry or register) from which the identifier is drawn: for example, the company register.
* The existing identifier for the organization within that list.

To disclose an organization identifier, first, use [org-id.guide](http://org-id.guide) to find the prefix for the organization list. If the list is not described by org-id.guide, contact the [Data Support Team](../../support/index) to register the list.

If you choose not to register an organization list with org-id.guide, you ought to describe the list in a [publication policy](../publish.md#finalize-your-publication-policy), and select a prefix that is not in use by another list in org-id.guide, by following the [org-id meta-data guide](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code).

## Worked example

A publisher in the United Kingdom collects [Companies House](https://www.gov.uk/government/organisations/companies-house) numbers as its primary organization identifiers for suppliers.

A buyer awards a contract to IBM. In IBM's entry in the `parties` array, `.identifier.scheme` is set to the org-id scheme prefix for Companies House ([GB-COH](http://org-id.guide/list/GB-COH)) and `.identifier.id` is set to IBM's Companies House number (04336774).

```{jsoninclude} ../../examples/organizations/identifiers.json
:jsonpointer: /releases/0/parties/0
:expand: identifier
```

The publisher also collects an additional identifier: A VAT identification number.

The VAT identification number list is not described by org-id.guide so the publisher follows the [instructions](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code) and assigns a new prefix: GB-VAT. The prefix is composed of the two-letter country code for the United Kingdom and an abbreviation of the list name. The publisher checks that the prefix is not already assigned in org-id.guide

In IBM's entry in the `parties` array, `.additionalIdentifiers.scheme` is set to the new list prefix and `.additionalIdentifiers.id` is set to IBM's VAT identification number.

```{jsoninclude} ../../examples/organizations/identifiers.json
:jsonpointer: /releases/0/parties/0
:expand: additionalIdentifiers
```

## Local IDs

Each of the organizations in the [parties section](../../schema/reference.md#parties) ought to have a [local ID](../../schema/identifiers.md#local-organization-ids) (`id`), which is used to reference the organization from elsewhere in the data.

For organizations with an organization identifier, you ought to construct the local `id` following the pattern `{identifier.scheme}-{identifier.id}`.

For organizations without an organization identifier, you can populate the local `id` with a fixed or sequential value. For example, you can set the buyer's `id` to "1" and set each supplier's `id` sequentially from "2" onwards. Alternatively, you can set the organization's `id` to its `role` and add a sequential number for roles with multiple organizations, e.g. "buyer", "tenderer-1", "tenderer-2", etc. An organization's local `id` needs to be consistent across all releases in a (contracting or planning) process. For example, if the `id` of an organization is "tenderer-1" in one release, then the `id` of the same organization in another release needs to also be "tenderer-1".
