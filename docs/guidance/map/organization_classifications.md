```{workedexample} Organization classifications
:tags: parties
```

# Organization classifications

Tracking certain characteristics of organizations, for example whether an organization is women-owned and/or indigenous-owned, is an important part of monitoring participation in public procurement. Many publishers wish to disclose classifications of the organizations involved in contracting (or planning) processes. Examples of organization classifications include ownership, incorporation, sector, location, and number of employees.

## Organization scale

To classify an organization's scale, i.e. its size or number of employees, you ought to use the the `parties.details.scale` field and [party scale codelist](../../schema/codelists.md#party-scale).

## Other classifications

If your classification does not map to any OCDS fields or codes, you ought to use the  [organization classification extension](https://extensions.open-contracting.org/en/extensions/organizationClassification/1.1/). The extension adds a [`classifications`](../../schema/reference.md#classification) array to the `parties.details` object.

A classification consists of at least two parts: an identifier for the list (scheme) from which the classification is taken, and an identifier for the category from that list being applied. It is useful to also publish a text label and/or URI that users can draw on to interpret the classification.

If the list from which your classifications are taken is listed in the 'organization' category of the open [classificationScheme codelist](../../schema/codelists.md#classification-scheme), you ought to set `parties.details.classifications.scheme` to the scheme's code, e.g. "COFOG" for the [Classification of the Functions of Government](https://unstats.un.org/unsd/classifications/Econ/). Otherwise, you ought to assign your own 'scheme code' and prefix it with your country's [ISO-3166-1 alpha-3 country code](https://en.wikipedia.org/wiki/ISO_3166-1) to reduce the risk of clashing with another publisher's code.

In either case, your [publication policy](../publish.md#finalize-your-publication-policy) ought to explain the classification schemes and codes used in your data.

```{admonition} Standardization and backwards compatibility
:class: note
Future versions of OCDS might add standardized fields like `parties.details.scale` to disclose classifications. If a new field matches the semantics of a classification that you already publish using the organization classifications extension, in order to preserve backwards compatibility, you can publish both the standardized field and the extension fields.
```

## Examples

### Organization scale

A publisher uses the [partyScale codelist](../../schema/codelists.md#party-scale) to classify organization scale.

A large organization, Microsoft, bids for an opportunity. `parties.details.scale` is set to 'large'.

```{jsoninclude} ../../examples/organizations/organization_classification/scale.json
:jsonpointer: /releases/0
:expand: parties,   details
```

```{admonition} Party scale extension
:class: note

This example previously used the [party scale extension](https://extensions.open-contracting.org/en/extensions/partyScale/master/) for OCDS 1.1. That extension has been merged into OCDS 1.2.
```

### Other classifications: Common schemes

A European Union publisher classifies buyers using the 'EU Type of contracting authority' scheme from the Tenders Electronic Daily (TED) schema. A buyer, the London Borough of Haringey, is classified as a regional or local authority.

The organization classification extension is declared in the `extensions` array. The classification is modelled as a `Classification` object in `parties.details.classification` and:

* `.scheme` is set to the scheme's code in the [classificationScheme codelist](../../schema/codelists.md#classification-scheme): "TED_CA_TYPE".
* `.id` is set to the code from TED schema: "REGIONAL_AUTHORITY".
* `.description` is set to the code's description from the TED schema: "Regional or local authority".

```{jsoninclude} ../../examples/organizations/organization_classification/ted_buyer_type.json
:jsonpointer:
:expand: releases, extensions, parties, details, classifications
```

### Other classifications: Local schemes

A publisher in Colombia uses a local classification scheme to track the participation of women-owned businesses in procurement. A tenderer, Contadores de Medellín, is classified as women-owned.

The organization classification extension is declared in the `extensions` array. The classification is modelled as a `Classification` object in `parties.details.classification` and:

* `.scheme` is set to the ISO-3166-1 alpha-3 country code for Colombia followed by an abbreviation of the classification scheme's name: "COL-AN-ME-PDM"
* `.id` is set to the code from the classification scheme: "NPDM".
* `.description` is set to the code's description from the classification scheme: "Negocio propiedad de mujeres".

```{jsoninclude} ../../examples/organizations/organization_classification/women_owned.json
:jsonpointer:
:expand: releases, extensions, parties, details, classifications
```

The publisher's publication policy describes how the ownership of businesses is classified, including the meaning of the codes in the local classification scheme.
 
> *Business ownership is classified using a local scheme, identified by "COL-AN-ME-PDM" in `parties.details.classifications.scheme`.*
> *The possible values of `parties.details.classifications.id` are:*
> * *NPDM: Negocio propiedad de mujeres (women-owned business)*

```{admonition} Mapping boolean data elements
:class: note
If you are mapping boolean data elements that describe characteristics of an organization, try to create logical groups of characteristics and create a local classification scheme for each group. It is allowed for a scheme to contain a single code.

For example: The City of Boston's Department of Supplier Diversity defines minority-owned businesses (MBE), women-owned businesses (WBE) and small local business enterprises (SLBE), among others. Depending on your use cases, two logical groups might be ownership-based characteristics and location-based characteristics. Instead of three booleans, this information can be modelled as a USA-MA-BOS-OWNER scheme with 'MBE' and 'WBE' codes and a USA-MA-BOS-LOCATION scheme with an 'SLBE' code.
```
