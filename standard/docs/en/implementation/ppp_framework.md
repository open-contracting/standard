# PPP Disclosure Framework

## Basic Project Information

Disclosure timing: Pre-procurement (as available)

Notes: This can be disclosed at the pre-procurement stage with the exception of information on the parties to the contract, which will be disclosed once it becomes available, that is, at the end of the procurement process. 


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
.. csv-table::
   :header-rows: 1
   :file: standard/docs/en/examples/ppp/I2value.csv
```

A detailed breakdown of sources of investment, and anticipated government expenditure and income can be provided using the budget forecast block (TODO) as described in the [financial information](#financial-information) section below. 

(Discussion in [issue 23](https://github.com/open-contracting/public-private-partnerships/issues/23) to confirm definition)

### I.4: Project need: benefits provided, economic and social (including specific information on the public interest aspect)

USE DOCUMENTS

### I.5: Technical description of the physical infrastructure

USE DOCUMENTS

### I.6: High-level description of the services

USE tender.description

### I.7: Estimated demand to be served annually

USE DOCUMENTS

### I.8: Project additionality

(TODO: Clarify this section of the framework)

### I.9: Reason for selection of PPP mode and type in brief

USE DOCUMENTS

### I.10: Dates of various approvals

PLANNING MILESTONES

### Contract Milestones (Estimated and Actual)

USE tender.milestones

#### I.11: Date of commercial close

USE tender.milestones

#### I.12: Date of financial close

USE tender.milestones

#### I.13: Date of commencement of construction or development

USE tender.milestones

#### I. 14: Date of completion of construction or development

USE tender.milestones

#### I.15: Date of commissioning

USE tender.milestones

#### I.16: Date of contract expiry

USE tender.milestones

### I.17: Links to all contract documents

USE DOCUMENTS

### Parties to the contract with contact details

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

#### I.18: Public authority: name of authority, name of representative, address, telephone, fax, e-mail

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

#### I.19: Private party: name of company or consortium, name of representative, address, telephone, fax, e-mail

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

#### I.20: Financiers: name of Lead FI, other FIs, name of representative of lead FI, address, telephone, fax, e-mail

REQUIRES ORGANISATION EXTENSION APPLIED TO SCHEMA

(TODO: Draft proposed organisation roles codelist and raise github issue)

## Procurement Information

Disclosure timing: According to milestones in the procurement process, evaluation and meeting minutes should be uploaded within 2-3 business days.

This information can be disclosed in the public domain during the procurement stage. Disclosure in the public domain can be simultaneous with the availability of the documents to prospective bidders.

### II.1. Timeline, final feasibility study, independent auditor's report

(TODO: Clarify this section of framework)

Dates and summary details, links to all procurement documents, final feasibility study, including land acquisition, social, environmental, and rehabilitation related information, reports of independent procurement  auditors (if any)

### II.2. RFQ documents

USE tender.documents

(TODO: Include guidance on modelling related RFQ/RFP processes)

### II.3. Pre-qualification or shortlist

USE two linked processes: RFQ and RFP - awards in the RFQ represent the shortlist/pre-qualified suppliers for the RFP process

### II.4. RFP documents

Use tender.documents

### II.5. Evaluation criteria: brief description with weightage

Use tender.documents (include note on requirements extension)

### II.6. Brief information on constitution of the evaluation committees

Use tender.documents

### II.7. Negotiation parameters: brief descrtiptoin of the parameters for negotiation with preferred proponent 

Use tender.documents

### II.8. Minutes of pre-bid meetings

Use tender.documents

### II.9. Selection of preferred bidder

Use award section

##   Risk

Disclosure timing: Post commercial close, within 45-60 days of signing contract

### III.1. Individual risk allocation information

(TODO: model extension - see table in framework)

## Evaluation of PPP option

Disclosure timing: Post commercial close, within 45-60 days of signing contract

### IV.1. Link to evaluation report (value for money or other)

Use award.documents

### IV.2. Summary data
•   State the rationale for doing the project as a PPP, including any qualitative or quantitative value-for-money, final feasibility studies (including cost-benefit analysis, if any) or other analysis that might have been used. If nonfinancial benefits have been quantified or considered, these could be stated.

Use award.documents

•   The discount rates used should be specified in the disclosure along with the risk premium used, if any, and an explanation for the rate of risk premium used, referring to guidance, if any, available in this regard or describing project-specific circumstances that justify the risk premium rate used.

(ToDo: model extension for: discount rate + risk premium + explanation )

•   Risk comparison of other financing mechanisms should be specified.

Use award.documents

## Financial Information

Disclosure timing: Post commercial close, within 45-60 days of signing contract

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