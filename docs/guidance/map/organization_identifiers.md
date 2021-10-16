# Organization identifiers

Publishers regularly collect the *legal identifiers* of the organizations involved in a contracting process. These [organization identifiers](../../schema/identifiers.md#organization-identifiers) can be disclosed using OCDS. An organization identifier is composed of two parts:

* A prefix for the organization list (also known as registry or register) from which the identifier is drawn: for example, the company register.
* The existing identifier for the organization within that list.

To disclose an organization identifier, first, use [org-id.guide](http://org-id.guide) to find the prefix for the organization list. If the list is not described by org-id.guide, contact the [OCDS Helpdesk](../../support/index) to register the list.

If you choose not to register an organization list with org-id.guide, you ought to describe the list in a [publication policy](../publish.md#finalize-your-publication-policy), and select a prefix that is not in use by another list in org-id.guide, by following the [org-id meta-data guide](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code).

## Worked example

The Government of the United Kingdom uses identifiers from [Companies House](https://www.gov.uk/government/organisations/companies-house) to identify suppliers. Companies House is assigned the "GB-COH" prefix in [org-id.guide](http://org-id.guide/list/GB-COH). IBM has been assigned the company number ‘04336774’ by the Companies House.  The globally unique organization identifier for IBM can be disclosed in the organization's `identifier` section, as below:

```{jsoninclude} ../../examples/organization-identifiers.json
:jsonpointer: /releases/0/parties/1
:expand: identifier, additionalIdentifiers
```

The publisher collects an additional identifier, which is disclosed using the `additionalIdentifiers` array. This is the VAT identification number for the supplier. The VAT list is not described by org-id.guide, so the publisher followed the instructions in the [org-id meta-data guide](http://docs.org-id.guide/en/latest/metadata/#assigning-a-code) to assign the "GB-VAT" prefix. This prefix is composed of the two-letter country code ("GB") and a short abbreviation for the list ("VAT"). The publisher checked that this prefix was not in use by another list in org-id.guide.

## Local IDs

Each of the organizations in the [parties section](../../schema/reference.md#parties) ought to have a [local ID](../../schema/identifiers.md#local-identifiers) (`id`), which is used to reference the organization from elsewhere in the data.

For organizations with an organization identifier, you ought to construct the local `id` following the pattern `{identifier.scheme}-{identifier.id}`.

For organizations without an organization identifier, you can populate the local `id` with a fixed or sequential value. For example, you can set the buyer's `id` to "1" and set each supplier's `id` sequentially from "2" onwards. Alternatively, you can set the organization's `id` to its `role` and add a sequential number for roles with multiple organizations, e.g. "buyer", "tenderer-1", "tenderer-2", etc. An organization's local `id` needs to be consistent across all releases in a contracting process. For example, if the `id` of an organization is "tenderer-1" in one release, then the `id` of the same organization in another release needs to also be "tenderer-1".
