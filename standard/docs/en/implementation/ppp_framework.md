# PPP Disclosure Framework

## Basic Project Information

**Disclosure timing:** Pre-procurement (as available)

*Note: This can be disclosed at the pre-procurement stage with the exception of information on the parties to the contract, which will be disclosed once it becomes available, that is, at the end of the procurement process.*


### I.1: Project name, location, sector

TODO. 

### I.2: Sponsoring agency/department

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

### I.3: Project value

The project value is the total amount invested into the project by both public and private parties.

This can be entered into ```budget``` fields in the ```planning``` section of an OCDS release. The ```budget/description``` field can be used to provide a free text explanation of the way the project value has been calculated. 

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/full.json
   :jsonpointer: /releases/0/planning/budget
   :expand: amount
```

```eval_rst
.. jsoninclude-flat:: docs/en/examples/ppp/full.json
   :recursive:
   :jsonpointer: /releases/0/planning/budget
   :ignore_path: /releases/0/
```

A detailed breakdown of sources of investment, and anticipated government expenditure and income can be provided using the budget forecast block (TODO) as described in the [financial information](#financial-information) section below. 

(Discussion in [issue 23](https://github.com/open-contracting/public-private-partnerships/issues/23) to confirm definition)

### I.4: Project need: benefits provided, economic and social (including specific information on the public interest aspect)

This information can be provided in a document, or documents, using the ```documents``` field in the ```planning``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

*Note: It is recommended in the PPP process to carry out a preliminary examination of the social and environmental aspects of the project and identify and disclose potential deal-breakers or challenges as early as possible.*

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

### I.8: Project additionality

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

REQUIRES tender.contractPeriod extension

### II.2. RFQ documents

Links to RFQ documents can be provided using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

(TODO: Include guidance on modelling related RFQ/RFP processes)

### II.3. Pre-qualification or shortlist

Where the procurement process for a PPP includes a process prior to the RFP, such as an RFQ, pre-qualification or shortlisting stage, the prior process should be modelled as a separate contracting process in OCDS to main RFP.

Information on pre-qualified or shortlisted bidders can be provided using the ```award``` section an OCDS release about the prior process.

(TODO: add guidance on linking related processes)

(TODO: draft relatedProcess extension)

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

### II.7. Negotiation parameters: brief descrtiptoin of the parameters for negotiation with preferred proponent 

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

#### IV.2.3 Risk comparison of other financing mechanisms should be specified.

This information can be provided in a document, or documents, using the ```documents``` field in the ```award``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

## Financial Information

**Disclosure timing:** Post commercial close, within 45-60 days of signing contract

### V.1. Equity-debt ratio

(ToDo: model extension - single field (= debt / debt + equity)? )

### V.2. Share capital

(ToDo: model extension - single field (total value of share capital)? )

### V.3. Shareholders with proportion held and voting rights

(ToDo: model extension - array of objects made up of an organizationReference + shareholding (%) + voting rights (codelist)? )

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

### V.4. Equity transfer caps

Certain contracts provide for caps on equity transfer in different stages of the contract, especially during the construction stage and for a few years thereafter. Give details of any such provisions

USE DOCUMENTS

### V.5. Lender and investor information

Commercial lenders, institutional investors, bilateral or multilateral lenders, public issue of bonds, supplier credit, other

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

(Array of organizationReferences - should we capture role at this level too?)

### V.6. Categorize senior debit, mezzanine debit, other

(ToDo: model extension - array of objects made up of id + amount + organizationReference (to funder) + debt type (codelist)? )

### V.7. Amount and tenor of each, fixed or floating rate

(ToDo: model extension - array of objects made up of id + rate + period + id (of debt)? )

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
