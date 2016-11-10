# PPP Disclosure Framework




## Basic Project Information

**Disclosure timing:** Pre-procurement (as available)

*Note: This can be disclosed at the pre-procurement stage with the exception of information on the parties to the contract, which will be disclosed once it becomes available, that is, at the end of the procurement process.*

### I.1: Project name, location, sector

#### Project name and description

OCDS 1.1 includes a ```title``` and ```description``` field at the top level of each contracting process release. These titles and descriptions can be used by applications in summary lists, so should be kept concise and jargon free. 

We recommend keeping descriptions to one paragraph or less.

#### Sector classification

Projects should be classified using the UN Classification of the Functions of Government Scheme (COFOG). 

This can be cross-walked to most other PPP clasification schemes in use, and so provides a common framework for understanding the sectoral focus of investments. 

Additional classificaiton schemes can also be provided, such as project classification against the Sustainable Development Goals (SDGs), or against national frameworks. 

**Discussion:** See [#22](https://github.com/open-contracting/public-private-partnerships/issues/22) for further sector classification discussions.

##### Representation

The primary sector classification is provided using a [classification block](../../../schema/reference/#classification) at ```planning/project/sector```. 

Any additional classifications can be provided in an array of [classification blocks](../../../schema/reference/#classification) at ```planning/project/additionalClassifications```. 

The following scheme codes are recognised for ```sector```:

* COFOG - [UN Classification of the Functions of Government](http://unstats.un.org/unsd/cr/registry/regcst.asp?Cl=4) using the dotted numerical notation. (Note: set spreadsheet columns to 'text' to avoid the leading 0 being removed).

#### Example
```eval_rst

.. jsoninclude:: docs/en/examples/ppp/full.json
   :jsonpointer: /releases/0/planning/project
   :expand: sector
```

#### Location

The locations where a project is taking place can be specified using:

* **A gazeteer entry**. For example, the GeoNames code of the administrative division where activity is taking place.
* **A GeoJSON object**. Describing the boundary, or extent, of where activity will take place.

There are a range of tools available to generate GeoJSON data, such as http://geojson.io/

###### Representation

Locations are represented using an array of ```location``` objects at ```planning/project/locations```. Each location can have a description, a gazeteer entry, and/or a GeoJSON object representing a location point or geometery. 

See the location extension (ToDo: Add link) for further modelling details. 

##### Example

The example below uses a gazeteer and GeoJSON LineString to describe the location of a road project. 

```json
{ "releases": [{
        "planning": {
                "project": {
                    "sector": "transport",
                    "subSector": "roads",
                    "locations": [
                        {
                            "description": "Local area and route of the Mersey Gateway Bridge",
                            "gazetteer": {
                                "scheme": "GEONAMES",
                                "identifiers": "2647601.0"
                            },
                            "geometry": {
                                "type": "LineString",
                                "coordinates": [
                                  [
                                    -2.7485561370849605,
                                    53.36141150911515
                                  ],
                                  [
                                    -2.74383544921875,
                                    53.36018219246915
                                  ],
                                  [
                                    -2.741689682006836,
                                    53.35900406407135
                                  ],
                                  [
                                    -2.7359390258789062,
                                    53.357774677973616
                                  ],
                                  [
                                    -2.7240943908691406,
                                    53.35782590310244
                                  ],
                                  [
                                    -2.7213478088378906,
                                    53.35710874569601
                                  ],
                                  [
                                    -2.703065872192383,
                                    53.348348206285024
                                  ],
                                  [
                                    -2.7020359039306636,
                                    53.34517142558946
                                  ],
                                  [
                                    -2.702207565307617,
                                    53.34158445320748
                                  ],
                                  [
                                    -2.7028942108154297,
                                    53.33943212493747
                                  ]
                                ]
                              }
                        }
                    ]
                }
    }
}]
}

```

### I.2: Sponsoring agency/department

The sponsoring agency or department's details should be included in the ```parties``` section, with a role tag of 'sponsor'. 

##### Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/sponsor.json
   :jsonpointer: /releases/0/entities
   :expand: entities,identifier,address,contactPoint
```

```eval_rst
.. jsoninclude-flat:: docs/en/examples/ppp/sponsor.json
   :recursive:
   :jsonpointer: /releases/0/entities
   :ignore_path: /releases/0/
```


### I.3: Project value

The project value should be understood as the total amount project to be invested into the project by both public and private parties over the project lifetime.

This can be entered into ```planning/project/totalValue``` object, and should consist of a single value and currency.

Total budget allocations and a detailed breakdown by period, and contributing party, can be included in the ```planning/budget``` block using the budgetBreakdown extension.

**Discussion** See [#23](https://github.com/open-contracting/public-private-partnerships/issues/23) for a discussion of the exact definition of project value. 

### I.4: Project need: benefits provided, economic and social (including specific information on the public interest aspect)

Information on the project need, benefits provided, and economic and social impact should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'needsAssessment'.


*Note: It is recommended in the PPP process to carry out a preliminary examination of the social and environmental aspects of the project and identify and disclose potential deal-breakers or challenges as early as possible.*

ToDo: Add actual document code & example

ToDo: Document extentension with pageStart / pageEnd 


### I.5: Technical description of the physical infrastructure

This information can be provided in a document, or documents, using the ```documents``` field in the ```planning``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### I.6: High-level description of the services

This information can be provided in in the ```tender``` section of an OCDS release. The ```tender/description``` field can be used to provide a free text description of the services covered by the PPP.

More detailed information can also be provided in a document, or documents, using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### I.7: Estimated demand to be served annually

This information can be provided in a document, or documents, using the ```documents``` field in the ```planning``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

See: https://github.com/open-contracting/public-private-partnerships/issues/27#issuecomment-258170651 

ToDo: Adding to planning a 'measure' block as 'estimatedDemand'
ToDo: Add estimatedDemand to the PPP extension

### I.8: Project additionality

This information can be provided in a document, or documents, using the ```documents``` field in the ```planning``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

(TODO: Clarify this section of the framework)

### I.9: Reason for selection of PPP mode and type in brief

This information can be provided in a document, or documents, using the ```documents``` field in the ```planning``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### I.10: Dates of various approvals

This information can be provided using the ```milestones``` field in the relevant section of an OCDS release, for example information on approvals relating to the planning phase of a PPP should be provided in the ```planning/milestones``` field whilst information on approvals relating to the procurement phase should be provided in the ```tender/milestones``` field. OCDS provides a [milestones building block](../schema/reference/#milestone) for disclosure of information on milestones.

A value from the [milestone type codelist](../schema/codelists/#milestone-type) should be entered into the ```milestone/milestoneType``` field to identify the type of milestone being disclosed, for example a milestone relating to the planning phase of a PPP should be of type ```planning```. This enables applications consuming OCDS data to distinguish between the different types of milestone, whichever section of OCDS the milestone appears in, and allows publishers to be clear about the type of milestone they are publishing.

A value from the [milestone status codelist](../schema/codelists/#milestone-status) should be entered into the ```milestone/status``` field to identify the status of the milestone, for example an approval which has not yet taken place should have ```scheduled``` status whilst an approval which has been completed should have ```met``` status.

(TODO: build ppp-schema with [milestones update](https://github.com/duncandewhurst/ocds-milestones-update) + update codelists documentation)

### Contract Milestones (Estimated and Actual)


#### I.11: Date of commercial close

This information can be provided using the ```milestones``` field in the ```tender``` section of an OCDS release. OCDS provides a [milestones building block](../schema/reference/#milestone) for disclosure of information on milestones.

The ```milestone/milestoneType``` field should be set to ```???```. This enables applications consuming OCDS data to distinguish between the different types of milestone, whichever section of OCDS the milestone appears in, and allows publishers to be clear about the type of milestone they are publishing.

A value from the [milestone status codelist](../schema/codelists/#milestone-status) should be entered into the ```milestone/status``` field to identify the status of the milestone, for example the expected date for the milestone should have ```scheduled``` status and once the milestone has been completed the status should be set to ```met```.

(TODO: see [github issue](https://github.com/open-contracting/public-private-partnerships/issues/25))

#### I.12: Date of financial close

This information can be provided using the ```milestones``` field in the ```tender``` section of an OCDS release. OCDS provides a [milestones building block](../schema/reference/#milestone) for disclosure of information on milestones.

The ```milestone/milestoneType``` field should be set to ```???```. This enables applications consuming OCDS data to distinguish between the different types of milestone, whichever section of OCDS the milestone appears in, and allows publishers to be clear about the type of milestone they are publishing.

A value from the [milestone status codelist](../schema/codelists/#milestone-status) should be entered into the ```milestone/status``` field to identify the status of the milestone, for example the expected date for the milestone should have ```scheduled``` status and once the milestone has been completed the status should be set to ```met```.

(TODO: see [github issue](https://github.com/open-contracting/public-private-partnerships/issues/25))

#### I.13: Date of commencement of construction or development

This information can be provided using the ```milestones``` field in the ```tender``` section of an OCDS release. OCDS provides a [milestones building block](../schema/reference/#milestone) for disclosure of information on milestones.

The ```milestone/milestoneType``` field should be set to ```delivery```. This enables applications consuming OCDS data to distinguish between the different types of milestone, whichever section of OCDS the milestone appears in, and allows publishers to be clear about the type of milestone they are publishing.

A value from the [milestone status codelist](../schema/codelists/#milestone-status) should be entered into the ```milestone/status``` field to identify the status of the milestone, for example the expected date for the milestone should have ```scheduled``` status and once the milestone has been completed the status should be set to ```met```.


#### I. 14: Date of completion of construction or development

This information can be provided using the ```milestones``` field in the ```tender``` section of an OCDS release. OCDS provides a [milestones building block](../schema/reference/#milestone) for disclosure of information on milestones.

The ```milestone/milestoneType``` field should be set to ```delivery```. This enables applications consuming OCDS data to distinguish between the different types of milestone, whichever section of OCDS the milestone appears in, and allows publishers to be clear about the type of milestone they are publishing.

A value from the [milestone status codelist](../schema/codelists/#milestone-status) should be entered into the ```milestone/status``` field to identify the status of the milestone, for example the expected date for the milestone should have ```scheduled``` status and once the milestone has been completed the status should be set to ```met```.


#### I.15: Date of commissioning

This information can be provided using the ```milestones``` field in the ```tender``` section of an OCDS release. OCDS provides a [milestones building block](../schema/reference/#milestone) for disclosure of information on milestones.

The ```milestone/milestoneType``` field should be set to ```delivery```. This enables applications consuming OCDS data to distinguish between the different types of milestone, whichever section of OCDS the milestone appears in, and allows publishers to be clear about the type of milestone they are publishing.

A value from the [milestone status codelist](../schema/codelists/#milestone-status) should be entered into the ```milestone/status``` field to identify the status of the milestone, for example the expected date for the milestone should have ```scheduled``` status and once the milestone has been completed the status should be set to ```met```.


#### I.16: Date of contract expiry

This information can be provided using ```contractPeriod``` field in the ```tender``` section of an OCDS release. OCDS provides a [period building block](../schema/reference/#period) for disclosure of information on time periods.

This expected date of contract expiry can be entered into the ```contractPeriod/endDate``` field.

(TODO: draft tender.contractPeriod extension)

### I.17: Links to all contract documents

Links to contract documents can be provided using the ```documents``` field in the ```planning``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

(TODO: draft documents extension - access details field + add to documentation)

### Parties to the contract with contact details


#### I.18: Public authority: name of authority, name of representative, address, telephone, fax, e-mail

This information can be provided using the ```buyer``` and ```parties``` sections of an OCDS release. OCDS provides an [organization building block](../schema/reference/#organization) for disclosure of information about organizations and their roles.

Details of the public authority should be provided in the ```parties``` section and the ```buyer``` section should be used to reference the relevant organization in the ```parties``` section.

The ```organization/roles``` field should be set to ```publicAuthority``` and the ```organization/contactPoint``` field can be used to provide details of a named representative.

(TODO: [renaming buyer](https://github.com/open-contracting/public-private-partnerships/issues/4)? [organization roles codelist](https://github.com/open-contracting/public-private-partnerships/issues/26))

#### I.19: Private party: name of company or consortium, name of representative, address, telephone, fax, e-mail

This information can be provided using the ```award``` and ```parties``` sections of an OCDS release. OCDS provides an [organization building block](../schema/reference/#organization) for disclosure of information about organizations and their roles.

Details of the public authority should be provided in the ```parties``` section and the ```award/suppliers``` field should be used to reference the relevant organization in the ```parties``` section.

The ```organization/roles``` field should be set to ```privateParty``` and the ```organization/contactPoint``` field can be used to provide details of a named representative.

(TODO: [renaming suppliers](https://github.com/open-contracting/public-private-partnerships/issues/4)? [organization roles codelist](https://github.com/open-contracting/public-private-partnerships/issues/26) add guidance on modelling consortia)

#### I.20: Financiers: name of Lead FI, other FIs, name of representative of lead FI, address, telephone, fax, e-mail

This information can be provided using the ```award``` and ```parties``` sections of an OCDS release. OCDS provides an [organization building block](../schema/reference/#organization) for disclosure of information about organizations and their roles.

Details of the public authority should be provided in the ```parties``` section and the ```award/financiers``` field should be used to reference the relevant organizations in the ```parties``` section.

The ```organization/roles``` field should be set to ```leadFinancier``` or ```financier``` as appropriate and the ```organization/contactPoint``` field can be used to provide details of a named representative.

(TODO: agree where this information should be located + draft financiers extension (see [#28](https://github.com/open-contracting/public-private-partnerships/issues/28))

## Procurement Information

**Disclosure timing:** According to milestones in the procurement process, evaluation and meeting minutes should be uploaded within 2-3 business days.

*Note: This information can be disclosed in the public domain during the procurement stage. Disclosure in the public domain can be simultaneous with the availability of the documents to prospective bidders.*

### II.1. Timeline, final feasibility study, independent auditor's report

(TODO: Clarify this section of framework)

*Dates and summary details, links to all procurement documents, final feasibility study, including land acquisition, social, environmental, and rehabilitation related information, reports of independent procurement  auditors (if any).*

Key dates regarding the procurement process can be provided using the following fields in the ```tender``` section of an OCDS release:

* The ```tenderPeriod``` field can be used to provide the period during which the tender is open for submissions, ```tenderPeriod.endDate``` should contain the closing date for tender submissions.
* The ```enquiryPeriod```field can be used to provide the period during which enquiries may be made and answered.
* The ```awardPeriod``` field can be used to provide the period during which an award is expected to be made.
* The ```contractPeriod``` field can be used to provide the expected start and end dates for the contract.

(TODO: Add guidance on processes with multiple enquiry periods [github issue](https://github.com/open-contracting/public-private-partnerships/issues/10))

(TODO: Add guidance on other fields in tender (e.g. submission method) also add guidance on using documents block for final feasibility study etc.)

REQUIRES tender.contractPeriod extension

### II.2. RFQ documents

Links to RFQ documents can be provided using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

(TODO: Include guidance on modelling related RFQ/RFP processes)

### II.3. Pre-qualification or shortlist

Where the procurement process for a PPP includes a process prior to the RFP, such as an RFQ, pre-qualification or shortlisting stage, the prior process should be modelled as a separate contracting process in OCDS to the main RFP.

Information on pre-qualified or shortlisted bidders can be provided using the ```award``` section an OCDS release about the prior process. AND are put into the ```actors``` table of the primary process with role of 'qualifiedBidder'. 

(TODO: add guidance on linking related processes)

(TODO: draft relatedProcess extension) - Updating proposal to include 'relatedProcess' 

### II.4. RFP documents

Links to RFP documents can be provided using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### II.5. Evaluation criteria: brief description with weightage

This information can be provided in a document, or documents, using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

The ```document/documentType``` field should be set to ```evaluationCriteria``` (from the [document type codelist](../schema/codelists/#document-type)) to identify the type of document being disclosed.

Structured information on evaluation criteria can also be provided using the ```criteria``` field in the ```tender``` section of an OCDS release. OCDS provides a [criteria, requirements, responses model](../schema/reference/#requirements) for disclosure of structured information on evaluation criteria and bidder responses. 

(TODO: draft document type codelist extension (see [#27](https://github.com/open-contracting/public-private-partnerships/issues/27)), add weighting to requirements extension, update requirements extension terminology (buyer etc.))

### II.6. Brief information on constitution of the evaluation committees

This information can be provided in a document, or documents, using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

(TODO: Document type codelist (see [#27](https://github.com/open-contracting/public-private-partnerships/issues/27)))

### II.7. Negotiation parameters: brief descrtiption of the parameters for negotiation with preferred proponent 

This information can be provided in a document, or documents, using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

(TODO: Document type codelist (see [#27](https://github.com/open-contracting/public-private-partnerships/issues/27)))

### II.8. Minutes of pre-bid meetings

This information can be provided in a document, or documents, using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

(TODO: Document type codelist (see [#27](https://github.com/open-contracting/public-private-partnerships/issues/27)))

### II.9. Selection of preferred bidder

This information can be provided using the ```award``` and ```parties``` sections of an OCDS release. OCDS provides an [organization building block](../schema/reference/#organization) for disclosure of information about organizations and their roles.

Details of the preferred bidder should be provided in the ```parties``` section and the ```award/suppliers``` field should be used to reference the relevant organization in the ```parties``` section.

```preferredBidder``` should be added to the list of roles for the organization in the ```organization/roles``` field.

(TODO: see [orgnaization roles issue](https://github.com/open-contracting/public-private-partnerships/issues/26))

##   Risk

**Disclosure timing:** Post commercial close, within 45-60 days of signing contract

*Risk allocation is an important determinant of cost to government and to the paying public/user. Inadequate or excessive transfer of risk is undesirable. Disclosure will provide evidence of proper or improper risk allocation and its effect on costs.*

### III.1. Individual risk allocation information

*Note: Listing of risks with information on who bears the risk. The following table can be used. This is not an exhaustive listing. Countries, sectors, and individual projects may use different categorizations. Several risks can be further broken down into components or listed together. If within a large category of risk subcategories are allocated to different parties, it makes sense to show the subcategories clearly.*

Draft modelling:

```json
"riskAllocation": [
	{
		"id" = "1",
		"type" = "demand",
		"description" = "Actual toll revenues are less than those forecast.",
		"allocation" = "publicAuthority",
		"mitigation" = "The Department for Transport will provide an Additional Availability Support Grant in the event that actual toll revenues are less than those forecast."
	},
	{
		"id" = "2",
		"type" = "preConstruction",
		"description" = "Planning permission for the project is not granted.",
		"allocation" = "privateParty",
		"mitigation" = "A planning strategy was agreed with the local planning authority and was shared with the bidders to mitigate planning risk to acceptable levels."
	}
]
```

(TODO: model extension + risk type codelist)

(TODO: compare codelists of risk types ([EIB](http://www.eib.org/epec/g2g/i-project-identification/12/122/index.htm), [PPPIRC](https://ppp.worldbank.org/public-private-partnership/financing/risk-allocation-mitigation))

## Evaluation of PPP option

**Disclosure timing:** Post commercial close, within 45-60 days of signing contract

### IV.1. Link to evaluation report (value for money or other)

This information can be provided in a document, or documents, using the ```documents``` field in the ```award``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### IV.2. Summary data

#### IV.2.1 State the rationale for doing the project as a PPP, including any qualitative or quantitative value-for-money, final feasibility studies (including cost-benefit analysis, if any) or other analysis that might have been used. If nonfinancial benefits have been quantified or considered, these could be stated.

*Note: Choice of methodology affects the costs to the public and it is important to assure them that the PPP mode selected is the best possible in terms of cost, given equal standards of service in all modes tested.*

This information can be provided in a document, or documents, using the ```documents``` field in the ```award``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

#### IV.2.2 The discount rates used should be specified in the disclosure along with the risk premium used, if any, and an explanation for the rate of risk premium used, referring to guidance, if any, available in this regard or describing project-specific circumstances that justify the risk premium rate used.

(ToDo: model extension for: discount rate + risk premium + explanation )

See: https://data.gov.uk/sib_knowledge_box/discount-rates-and-net-present-value - some discount rates can be staged over years. 

#### IV.2.3 Risk comparison of other financing mechanisms should be specified.

This information can be provided in a document, or documents, using the ```documents``` field in the ```award``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

## Financial Information

**Disclosure timing:** Post commercial close, within 45-60 days of signing contract

### V.1. Equity-debt ratio

(ToDo: model extension - single field (= debt / debt + equity)? In the [World Bank PPI Database](https://ppi.worldbank.org/data) debt-equity ratio values as given as a pair summing to 100, e.g. 60/40, 70/30 etc.)

*Note: The [World Bank PPPIRC](https://ppp.worldbank.org/public-private-partnership/financing/issues-in-project-financed-transactions#debt) defines the debt equity ratio as the ```long term debt / shareholder equity``` of the project company.*

### V.2. Share capital

(ToDo: model extension - single field (total value of share capital)? )

### V.3. Shareholders with proportion held and voting rights

(ToDo: model extension - array of objects made up of an organizationReference + shareholding (%) + voting rights (codelist)? )

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

**Draft modelling**

```json
"shareholders": [
	{
		"id": "01",
		"shareholder": {
			"id": "GB-COH-12345678",
			"name": "Mega Corp"
		},
		"shareholding": 0.75,
		"votingRights":	ordinary,
		"votingRightsDetails": ""
	},
	{
		"id": "02",
		"shareholder": {
			"id": "GB-COH-99999999",
			"name": "Mini Co"
		},
		"shareholding": 0.25,
		"votingRights":	ordinary,
		"votingRightsDetails": ""
	}
]
```

**Draft votingRights codelist**

code | definition
-----|-----------
ordinary | The shareholder is entitled to a single vote per share in all circumstances
none | The shareholder is not entitled to vote under any circumstances
restricted | The shareholder is entitled to vote in specific circumstances only
additional | The shareholder is entitled to more than one vote per share in all circumstances
enhanced | The shareholder is entitled to more than one vote per share in specific circumstances only

**Questions**
* Are there any existing codelists we can defer to for shareholder voting rights?
* For shares with additional voting rights should this be specified as semi-structured data using the votingRightsDetails field or is an additional field required (i.e. votesPerShare)?


### V.4. Equity transfer caps

*Note: Certain contracts provide for caps on equity transfer in different stages of the contract, especially during the construction stage and for a few years thereafter. Give details of any such provisions.*

**Draft modelling**

```json

"equityTransferCaps": [
	{
		"id" : "01",
		"title" : "Construction equity transfer cap",
		"description" : "No equity transfer is permitted until construction is completed.",
		"cap" : 0,
		"milestone" : {
			"id" : "contract-construction-001",
			"title" : "Completion of construction"
		}
	},
	{
		"id" : "02",
		"title" : "Initial equity transfer cap",
		"description" : "No more than 20% equity may be transferred until the project has been in operation for 10 years.",
		"cap" : 0.20,
		"milestone" : {
			"id" : "contract-operation-002",
			"title" : "10 years of operation"
		}
	}
]
```

(See [github issue](https://github.com/open-contracting/public-private-partnerships/issues/30))

### V.5. Lender and investor information

Commercial lenders, institutional investors, bilateral or multilateral lenders, public issue of bonds, supplier credit, other

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

(Array of organizationReferences - should we capture role at this level too?)


### V.6. Categorize senior debt, mezzanine debt, other

(ToDo: model extension - array of objects made up of id + amount + organizationReference (to funder) + debt type (codelist)? )

### V.7. Amount and tenor of each, fixed or floating rate

(ToDo: model extension - array of objects made up of id + rate + period + id (of debt)? )

TABLE OF FINANCING - 

- Could be used to calculate debt-to-equity and total debt capital. 

### V.8. Security and step in arrangements

USE DOCUMENTS (contract)

### V.9. Forecast IRR

(ToDo: model extension, single field?)

## Government Support

Disclosure timing: Post commercial close, within 45-60 days of signing contract

### VI.1. Guarantees

(ToDo: See table in disclosure framework)

### VI.2. Grants


### VI.3. Service payments


### VI.4. Land leases, asset transfers


### VI.5. Revenue-share, if any

## Tariffs

Disclosure timing: Post commercial close, within 45-60 days of signing contract

### VII.1. Tariffs and pricing


### VII.2. Methodology for tariff setting/pricing


### VII.3. Scope for reviews of tariff, pricing, regulatory mechanisms


### VII.4. Links to graphs: tariff increases over time, consumer price index movement


## Contract Termination

### VIII.1. Events of default and termination payments


### VIII.2. Handover


## Renegotiations

Disclosure timing: Within 45-60 days of execution of renegotiated contract

### IX.1. Contract variation details 

State variations to contract, if any, after signing of the original contract detailing each change against original provisions. State in addition the details of renegotiations and circumstances leading to renegotiations. State specifically any change due to the renegotiated clauses in the following: roles and responsibilities relating to the project, risk allocation, fiscal exposure, that is, any change in fiscal commitments and contingent liabilities with a rationale for agreeing to the change. Use the following formats:

## Performance Information

Disclosure timing: Within 15-30 days of receipt of information

### X.1. Annual demand levels


### X.2. Annual revenues


### X.3. Actual IRR


### X.4. Performance


### X.5. Performance Failures


### X.6. Performance Assessments
