<style><!--
h3 ~ div {
margin-left:30px;
}
h3 ~ div > h4 {
border:1px solid black;
}
.example-background {
    background:lightGrey;
    padding:5px;
    margin:5px
}
.example-background h5 {
   background:grey;
   margin-bottom:5px  
}
.wy-table td, .rst-content table.docutils td, .rst-content table.field-list td {
  vertical-align: top;
}
--></style>
<script><!--
function defer(method) {
if (window.jQuery)
method();
else
setTimeout(function() { defer(method) }, 50);
}
defer(function() {
$("h5").each(function() { $(this).html(">>" + $(this).html());});
$("h5").click(function() { 
$(this).siblings().toggle('slow');   
});
$("h5").siblings().toggle();   
$("h5").parent().addClass("example-background");
});
--></script>

# PPP Disclosure Framework

<a href="#" onClick='$("h5").siblings().show()'>Show</a> / <a href="#" onClick='$("h5").siblings().hide()'>hide</a> implementation details and examples</a>

## Basic Project Information

> Disclosure timing: Pre-procurement (as available)

*Note: This can be disclosed at the pre-procurement stage with the exception of information on the parties to the contract, which will be disclosed once it becomes available, that is, at the end of the procurement process.*

### I.1: Project name, location, sector

#### Project name and description

OCDS 1.1 includes a ```title``` and ```description``` field at the top level of each contracting process release. These titles and descriptions can be used by applications in summary lists, so should be kept concise and jargon free. 

We recommend keeping descriptions to one paragraph or less.

```eval_rst

.. jsonschema:: ../../../schema/release-schema.json
    :include: title,description

```

#### Sector classification

Projects should be classified using the UN Classification of the Functions of Government Scheme (COFOG). 

This can be cross-walked to most other PPP clasification schemes in use, and so provides a common framework for understanding the sectoral focus of investments. 

Additional classificaiton schemes can also be provided, such as project classification against the Sustainable Development Goals (SDGs), or against national frameworks. 

**Discussion:** See [#22](https://github.com/open-contracting/public-private-partnerships/issues/22) for further sector classification discussions.


```eval_rst

.. jsonschema:: ../../../schema/release-schema.json
    :include: planning/project/sector,planning/project/additionalClassifications

```

##### Representation

The primary sector classification is provided using a [classification block](../../../schema/reference/#classification) at ```planning/project/sector```. 

Any additional classifications can be provided in an array of [classification blocks](../../../schema/reference/#classification) at ```planning/project/additionalClassifications```. 

The following scheme codes are recognised for ```sector```:

* COFOG - [UN Classification of the Functions of Government](http://unstats.un.org/unsd/cr/registry/regcst.asp?Cl=4) using the dotted numerical notation. (Note: set spreadsheet columns to 'text' to avoid the leading 0 being removed).

##### Example
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

See the [location extension](../../extensions/location/)  for further modelling details. 

##### Example

The example below uses a gazeteer and GeoJSON LineString to describe the location of a road project. 
```eval_rst

.. jsoninclude:: docs/en/examples/ppp/geojson.json
   :jsonpointer: /releases
   :expand: planning, projects, locations, gazetteer, geometry, coordinates
```

### I.2: Sponsoring agency/department

The sponsoring agency or department's details should be included in the ```parties``` section, with a role tag of 'sponsor'. 

#### Examples

###### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-pqq-planning-01.json
   :jsonpointer: /releases/0/entities
   :expand: entities,identifier,address,contactPoint
```

###### Spreadsheet Example

```eval_rst
.. jsoninclude-flat:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-pqq-planning-01.json
   :recursive:
   :jsonpointer: /releases/0/entities
   :ignore_path: /releases/0
```


### I.3: Project value

The project value should be the total amount project to be invested into the project by both public and private parties over the project lifetime.

This can be entered into ```planning/project/totalValue``` object, and should consist of a single value and currency.

Total budget allocations and a detailed breakdown by period, and contributing party, can be included in the ```planning/budget``` block using the budgetBreakdown extension.

**Discussion** See [#23](https://github.com/open-contracting/public-private-partnerships/issues/23) for a discussion of the exact definition of project value. 

### I.4: Project need: benefits provided, economic and social (including specific information on the public interest aspect)

Information on the project need, benefits provided, and economic and social impact should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'needsAssessment' in the ```planning/documents``` array. 

#### Examples

##### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/full.json
   :jsonpointer: /releases/0/planning/documents/0
   :expand: 
```

##### Spreadsheet example

```eval_rst
.. jsoninclude-flat:: docs/en/examples/ppp/full.json
   :recursive:
   :jsonpointer: /releases/0/planning/documents/0
   :ignore_path: /releases/0
```

### I.5: Technical description of the physical infrastructure

A technical description of the physical infrastructure should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'technicalSpecifications' in the ```tender/documents``` array. 

### I.6: High-level description of the services

A high-level description of the services should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'serviceDescription' in the ```tender/documents``` array. 

### I.7: Estimated demand to be served annually

Estimated demand can be provided using both structured data, and a document with the ```documentType``` of 'estimatedDemand'. 

Structured demand forecasts are provided through the ```planning/forecast``` building block.

This consists of an array of forecast metrics. A metric with the ```id``` 'demand' should be given, with a series of forecast ```observations``` that capture the estimated demand for a given period.

These estimates can be disaggregated by any number of dimensions contained as simple fields within the ```observation/dimensions``` object. 

#### Example 

##### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-planning-01.json
   :jsonpointer: /releases/0/planning
   :expand: forecasts, observations, period, dimensions, unit
```

### I.8: Project additionality

Information on the project additionality should be provided through planning documents containing:

* A short summary text
* A link to one or more documents that provide additional information

Descriptions should be provided for both:

* The additionality of the project;
* The additionality of the finance method used;

These documents should be tagged with a ```documentType``` value of 'projectAdditionality' or 'financeAdditionality' in the ```planning/documents``` array. 

**Discussion**: How should additionality be defined: https://github.com/open-contracting/public-private-partnerships/issues/32

### I.9: Reason for selection of PPP mode and type

A short summary of the reason for the PPP selection mode should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'pppModeRationale' in the ```planning/documents``` array. 

### I.10: Dates of various approvals

This information can be provided using the [milestones extension](../../extensions/milestones/).

Each approval during the planning stage should be included in the ```planning/milestones``` array with a ```type``` of 'approval', the date the approval is scheduled for (```dueDate```), the status of the approval (```scheduled``` or ```met```) and the date the approval was given (```dateMet```).

Documentation associated with the approval can be given in the associated milestones documents block.

### Contract Milestones (Estimated and Actual)

#### I.11: Date of commercial close

> In a financing, the point at which the commercial documentation has been executed but before conditions precedent have been satisfied or waived; before financial close. ([Source](https://pppknowledgelab.org/glossary#Commercial_Close))

This information can be provided using the [milestones extension](../../extensions/milestones/).

To indicate the date of commercial close, a milestone should be added to the ```contract/milestones``` (the contract may have a ```status``` of 'pending' up until it is signed). 

The milestone should have a ```type``` of 'financing', a ```code``` of 'commercialClose', the status of ```met``` and the date that commercial close took place in ```dateMet```.

Additional documentation, or links to documentation, can be provided using the documents block for the milestone.

#### I.12: Date of financial close

> In a financing, the point at which the documentation has been executed and conditions precedent have been satisfied or waived. Drawdowns become permissible after this point. ([Source](https://pppknowledgelab.org/glossary#Financial_Close))

This information can be provided using the [milestones extension](../../extensions/milestones/).

To indicate the date of commercial close, a milestone should be added to the ```contract/milestones``` (the contract may have a ```status``` of 'pending' up until it is signed). 

The milestone should have a ```type``` of 'financing', a ```code``` of 'financialClose'  the status of ```met``` and the date that commercial close took place in ```dateMet```.

Additional documentation, or links to documentation, can be provided using the documents block for the milestone.

#### I.13: Date of commencement of construction or development

This information can be provided using the [milestones extension](../../extensions/milestones/).

To indicate the date that construction starts, a milestone should be added to the ```contract/implementation/milestones```.

The milestone should have a ```type``` of 'delivery', a ```code``` of 'developmentStarted' or 'constructionStarted'  the status of ```met``` and the date that this milestone was achieved in ```dateMet```.

Additional documentation, or links to documentation, can be provided using the documents block for the milestone.

#### I. 14: Date of completion of construction or development

This information can be provided using the [milestones extension](../../extensions/milestones/).

To indicate the date that construction or development is completed, a milestone should be added to the ```contract/implementation/milestones```.

The milestone should have a ```type``` of 'delivery', a ```code``` of 'developmentComplete' or 'constructionComplete' the status of either ```scheduled``` or ```met``` and either the date that this milestone was achieved in ```dateMet```, or the scheduled date in ```dueDate```.

Additional documentation, or links to documentation, can be provided using the documents block for the milestone.

#### I.15: Date of commissioning

> The testing and inspection of the completed works to verify that the works are ready for commercial operation. ([Source](https://pppknowledgelab.org/glossary#Commissioning))

This information can be provided using the [milestones extension](../../extensions/milestones/).

To indicate the date of commissioning, a milestone should be added to the ```contract/implementation/milestones```.

The milestone should have a ```type``` of 'delivery', a ```code``` of 'commissioning' the status of either ```scheduled``` or ```met``` and either the date that this milestone was achieved in ```dateMet```, or the scheduled date in ```dueDate```.

Additional documentation, or links to documentation, can be provided using the documents block for the milestone.

#### I.16: Date of contract expiry

This information can be provided using ```contractPeriod``` field in the ```tender``` section of an OCDS release. OCDS provides a [period building block](../schema/reference/#period) for disclosure of information on time periods.

This expected date of contract expiry can be entered into the ```contractPeriod/endDate``` field.

(TODO: draft tender.contractPeriod extension)

### I.17: Links to all contract documents

Links to contract documents can be provided using the ```documents``` field in the ```planning``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents which has [a number of available extensions for PPP use cases](../../extensions/documentation_details/)

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### Parties to the contract with contact details

#### I.18: Public authority: name of authority, name of representative, address, telephone, fax, e-mail

> The unit/body/department within a government that is tendering and contracting the project. The public counterpart in the PPP contract. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

This information can be provided using the ```buyer``` and ```parties``` sections of an OCDS release. OCDS provides an [organization building block](../schema/reference/#organization) for disclosure of information about organizations and their roles.

Details of the public authority should be provided in the ```parties``` section and the ```buyer``` section should be used to reference the relevant organization in the ```parties``` section.

The ```organization/roles``` field should be set to ```publicAuthority``` and the ```organization/contactPoint``` field can be used to provide details of a named representative.

(TODO: [renaming buyer](https://github.com/open-contracting/public-private-partnerships/issues/4)? [organization roles codelist](https://github.com/open-contracting/public-private-partnerships/issues/26))

#### I.19: Private party: name of company or consortium, name of representative, address, telephone, fax, e-mail

> The counter party of the procuring authority in the PPP contract. A private entity which has been granted the contract to construct and operate a government asset, and which is usually created under the form of a Special Purpose Vehicle or SPV. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

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

> Disclosure timing: According to milestones in the procurement process, evaluation and meeting minutes should be uploaded within 2-3 business days.

*Note: This information can be disclosed in the public domain during the procurement stage. Disclosure in the public domain can be simultaneous with the availability of the documents to prospective bidders.*

### II.1. Timeline, final feasibility study, independent auditor's report

(TODO: Clarify this section of framework)

*Dates and summary details, links to all procurement documents, final feasibility study, including land acquisition, social, environmental, and rehabilitation related information, reports of independent procurement auditors (if any).*

*Note: See section II.3 for guidance on processes with a pre-qualification stage*

#### Dates & Summary details

Key dates regarding the procurement process can be provided using the ```tender``` section of an OCDS release.

* The ```tender/tenderPeriod``` field can be used to provide the period during which the tender is open for submissions, ```tenderPeriod.endDate``` should contain the closing date for tender submissions.
* The ```tender/enquiryPeriod```field can be used to provide the period during which enquiries may be made and answered.
* The ```tender/awardPeriod``` field can be used to provide the period during which an award is expected to be made.
* The ```tender/contractPeriod``` field can be used to provide the expected start and end dates for the contract.

Information on the procurement method used should be provided using the following fields in the ```tender``` section of an OCDS release:

* ```procurementMethod```
* ```procurementMethodDetails```
* ```procurementMethodRationale```

Information on the submission method for bids should be provided using the following fields in the ```tender``` section of an OCDS release:

* ```submissionMethod```
* ```submissionMethodDetails```

Information on the eligibility criteria for bidders can be provided using the ```eligibilityCriteria``` field in the ```tender``` section of an OCDS release.

(REQUIRES tender.contractPeriod extension)

##### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-qualification-01.json
   :jsonpointer: /releases/0/tender
   :expand: 
```

#### Multiple enquiry periods

Some PPP procurement processes have more than one enquiry period during the tender stage of the procurement. In such cases:

* The ```tender/enquiryPeriod``` field should be used to provide the **next** period during which enquiries may be made and answered, if there are no further enquiry periods scheduled the field should be used to provide the **most recent** period during which enquiries may be made and answered. Where an OCDS release is published during an enquiry period the ```tender/enquiryPeriod``` field should be used to provide the start and end dates of the **current** enquiry period.
* The ```tender/milestones``` block should be used to provide details of any subsequent enquiry periods beyond the next period during which enquiries may be made and answered.

The above guidance should also be followed for processes with multiple enquiry periods during the pre-qualification stage of the procurement, in such cases the same approach should be applied to the equivalent fields from the ```prequalification``` section of an OCDS release.

(TODO: Example/diagram)


#### Documents

Links to procurement documents, feasibility studies, including land acquisition, social, environmental, and rehabilitation related information and reports of independent procurement auditors should be provided using the [document building block](../schema/reference/#document) in the ```tender/documents``` array. A short summary text for each document can also be provided using the ```document/description``` field.

Each document should be tagged with an appropriate ```documentType``` value from the [document type codelist](../schema/codelists/#document-type).

##### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-preferredBidder-01.json
   :jsonpointer: /releases/0/tender/documents/0
   :expand: 
```

##### Spreadsheet example

```eval_rst
.. jsoninclude-flat:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-preferredBidder-01.json
   :recursive:
   :jsonpointer: /releases/0/tender/documents/0
   :ignore_path: /releases/0
```

### II.2. RFQ documents

> The set of documents issued by the procuring authority that constitute the basis of the qualification and potentially the pre-selection of candidates (the short list). Qualified (or short-listed candidates) will then be invited to submit a proposal (or to enter into a new phase prior to bid submission, such as a dialogue phase or interactive phase). ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

Links to RFQ documents can be provided using the ```documents``` field in the ```prequalification``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### II.3. Pre-qualification or shortlist

> The process whereby the number of qualified bidders is limited by reviewing each bidder’s qualifications against a set of criteria, generally involving experience in the relevant field, capitalisation, site country experience, identity of local partners and international reputation. ([Source](https://pppknowledgelab.org/glossary#Pre-qualification))

#### Dates & summary information

Key dates regarding the pre-qualification process can be provided using the ```prequalification``` section of an OCDS release.

* The ```prequalification/tenderPeriod``` field can be used provide the period during which the pre-qualification process is open for submissions, ```prequalification/tenderPeriod/endDate``` should contain the closing date for pre-qualification submissions.
* The ```prequalification/enquiryPeriod```field can be used to provide the period during which enquiries regarding the pre-qualification process may be made and answered.
* The ```prequalification/awardPeriod``` field can be used to provide the period during which the shortlist of qualified suppliers is expected to be selected.

Information on the procurement method used should be provided using the following fields in the ```prequalification``` section of an OCDS release:

* The ```prequalification/procurementMethod``` field should be used to specify the type of pre-qualification process used, the value of this field should be ```open``` if there are no restrictions on the parties that can submit a response to the request for pre-qualification.
* The ```prequalification/procurementMethodDetails``` field can be used to provide additional detail on the type of pre-qualification process, for example the local name of the particular method used.
* The ```prequalification/procurementMethodRationale``` field can be used to provide the rationale for the type of pre-qualification process used, this field should be completed where ```prequalification/procurementMethod``` is not ```open```.

Information about the evaluation criteria for the pre-qualification process should be provided using the ```prequalification/awardCriteriaDetails``` field.

Information about the submission method for responses to the pre-qualification process should be provided using the ```prequalification/submissionMethod``` field, the ```prequalification/submissionMethodDetails``` can be used to provide additional information on the submission method.

##### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-qualification-01.json
   :jsonpointer: /releases/0/qualification
   :expand: 
```

#### Bidder information

OCDS provides an [organization building block](../schema/reference/#organization) which can be used for disclosure of information about bidders and their roles:

* Information about the bidders which have been shortlisted or invited to submit a proposal following the pre-qualification process should be provided using an entry in the ```parties``` section of an OCDS release with the ```organization/role``` field set to ```qualifiedBidder```.

* Information about the bidders which were not shortlisted or invited to submit a proposal follow the pre-qualification process can be provided using an entry in the ```parties``` section of an OCDS release with the ```organization/role``` field set to ```bidder```.


##### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-shortlist-01.json
   :jsonpointer: /releases/0/entities
   :expand: entities
```

### II.4. RFP documents

> The set of documents issued by the procuring authority that set out:
>
> * The basis or requirements for submitting the proposal (which documents and in which format and contents the bidder has to submit)
> * The basis of the evaluation criteria  for selecting the preferred bidder or awardee
> * The PPP contract that will be signed with the successful bidder and other annexed information such as forms, templates, complementary information for reference purposes, and so on.
< ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

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

### II.7. Negotiation parameters: brief description of the parameters for negotiation with preferred proponent 

This information can be provided in a document, or documents, using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) of ```negotiationParameters``` should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### II.8. Minutes of pre-bid meetings

This information can be provided in a document, or documents, using the ```documents``` field in the ```tender``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) of ```minutes``` should be entered into the ```document/documentType``` field to identify the type of document being disclosed.


### II.9. Selection of preferred bidder

This information can be provided using the ```award``` and ```parties``` sections of an OCDS release. OCDS provides an [organization building block](../schema/reference/#organization) for disclosure of information about organizations and their roles.

Details of the preferred bidder should be provided in the ```parties``` section and the ```award/suppliers``` field should be used to reference the relevant organization in the ```parties``` section. ```preferredBidder``` should be added to the list of roles for the organization in the ```organization/roles``` field.

##   Risk

> Disclosure timing: Post commercial close, within 45-60 days of signing contract

*Risk allocation is an important determinant of cost to government and to the paying public/user. Inadequate or excessive transfer of risk is undesirable. Disclosure will provide evidence of proper or improper risk allocation and its effect on costs.*

### III.1. Individual risk allocation information

> The allocation of the consequences of each risk to one of the parties in the contract, or agreeing to deal with the risk through a specified mechanism which may involve sharing the risk. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

The following information should be provided for each risk:

* Risk category
* Description
* Allocation
* Likelihood
* Fiscal impact
* Mitigation

Additional free text information on each risk allocation, for example the rationale for the allocation, can also be provided.

Additional financial modelling for risks can also be linked to or provided in a document.

#### Representation

Risk allocations should be represented using an array of [risk blocks](../../../schema/reference/#organization) in the ```riskAllocation``` field of the ```contract``` section of an OCDS release.

The risk category should be represented using the ```risk/category``` field. The following codes are defined for the [risk category codelist](../schema/codelists/#risk-category) based on the [World Bank Public Private Partnerships Fiscal Risk Assessment Model](http://www.worldbank.org/en/topic/publicprivatepartnerships/brief/ppp-tools#T2):

* governance - Governance risks
* construction - Construction risks
* demand - Demand risks
* operationPerformance - Operation and performance risks
* financial - Financial risks
* forcemajeure - Force majeure risks
* governmentAction - Material adverse government actions (MAGA)
* changeInLaw - Change in law
* rebalancing - Rebalancing of financial equilibrium
* renegotiation - Renegotiation risks
* contractTermination - Contract termination risks

The party retaining each risk should be represented using the ```risk/allocation``` field. The following codes are defined for the [risk allocation codelist](../schema/codelists/#risk-allocation):

* publicAuthority - The risk is wholly or mostly retained by the public authority
* privateParty - The risk is wholly or mostly retained by the private party
* shared - The risk is shared between the public authority and the private party

The likelihood and fiscal impact of the risk occuring should be represented using the ```risk/likelihood``` and ```risk/fiscalImpact``` fields respectively. The following codes are defined for these fields:

* low
* medium
* high

The description of the risk should be provided as free text using the ```risk/description``` field and the mitigation for the risk should be provided as free text using the ```risk/mitigation``` field.

Additional free text information on the risk can be provided using the ```risk/notes``` field.

#### Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-contract-01.json
   :jsonpointer: /releases/0/contracts/0/riskAllocation
   
```

## Evaluation of PPP option

> Disclosure timing: Post commercial close, within 45-60 days of signing contract

### IV.1. Link to evaluation report (value for money or other)

This information can be provided in a document, or documents, using the ```documents``` field in the ```award``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) of ```evaluationReports``` should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

### IV.2. Summary data

#### IV.2.1 State the rationale for doing the project as a PPP, including any qualitative or quantitative value-for-money, final feasibility studies (including cost-benefit analysis, if any) or other analysis that might have been used. If nonfinancial benefits have been quantified or considered, these could be stated.

*Note: Choice of methodology affects the costs to the public and it is important to assure them that the PPP mode selected is the best possible in terms of cost, given equal standards of service in all modes tested.*

This information can be provided in a document, or documents, using the ```documents``` field in the ```award``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

#### IV.2.2 The discount rates used should be specified in the disclosure along with the risk premium used, if any, and an explanation for the rate of risk premium used, referring to guidance, if any, available in this regard or describing project-specific circumstances that justify the risk premium rate used.

The discount rate should captured under ```contract/financialModel``` with a code of 'discountRate'. 

A single value should be given. 

Any risk premium should captured under ```contract/financialModel``` with a code of 'riskPremium'. 

A single value should be given. 

#### IV.2.3 Risk comparison of other financing mechanisms should be specified.

This information can be provided in a document, or documents, using the ```documents``` field in the ```award``` section of an OCDS release. OCDS provides a [document building block](../schema/reference/#document) for disclosure of documents.

The ```document/description``` field can be used to provide a free text summary of the content of the document to enable this information to be displayed in applications consuming OCDS data.

A value from the [document type codelist](../schema/codelists/#document-type) should be entered into the ```document/documentType``` field to identify the type of document being disclosed.

## Financial Information

> Disclosure timing: Post commercial close, within 45-60 days of signing contract

### V.1. Equity-debt ratio

The discount rate should captured under ```contract/financialModel``` with a code of 'equityDebtRatio'. 

A single value should be given. 

### V.2. Share capital

The discount rate should captured under ```contract/financialModel``` with a code of 'shareCapital'. 

A single value should be given. 

### V.3. Shareholders with proportion held and voting rights

The following information should be provided for each shareholder:

* Name
* Address
* Identifier
* Proportion of shares held
* Voting rights

The following information can also be provided:

* Additional identifiers
* Contact details

#### Representation

Shareholders are represented using an array of [organization blocks](../../../schema/reference/#organization) in the ```parties``` section of an OCDS release.

Shareholders are linked to the project company using an array of [shareholder blocks](../../../schema/reference/#shareholder) in the ```shareholders``` field of the [organization block](../../../schema/reference/#organization) describing the project company in the ```parties``` section of OCDS.

The proportion of shares held by the shareholder should be represented as a number between 0 and 1 using the ```shareholder/shareholding``` field.

The votings rights for the shareholder should be represented using the ```shareholder/votingRights``` field. The following codes are defined for the [voting rights codelist](../schema/codelists/#voting-rights):

* ordinary - The shareholder is entitled to a single vote per share in all circumstances
* none - The shareholder is not entitled to vote under any circumstances
* restricted - The shareholder is entitled to vote in specific circumstances only
* additional - The shareholder is entitled to more than one vote per share in all circumstances
* enhanced - The shareholder is entitled to more than one vote per share in specific circumstances only

(See [github issue](https://github.com/open-contracting/public-private-partnerships/issues/35))

Where the shareholder has *restricted*, *additional* or *enhanced* voting rights the ```shareholder/votingRightsDetails``` field should be used to provide details of the shareholder's voting rights.

#### Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-contract-01.json
   :jsonpointer: /releases/0/entities
   
```

### V.4. Equity transfer caps

*Note: Certain contracts provide for caps on equity transfer in different stages of the contract, especially during the construction stage and for a few years thereafter. Give details of any such provisions.*

#### Representation

The equity transfer caps defined in the contract are represented using an array of [equity transfer cap blocks](../../../schema/reference/#equity-transfer-cap) in the ```contract``` section of an OCDS release.

The proportion of equity in the project company which is permitted to be transferred under the cap should be represented as a number between 0 and 1 using the ```equityTransferCap/amount``` field.

The period for which the cap applies should be represented by linking the equity transfer cap to a contract [milestone](../../../schema/reference/#milestone), using the ```equityTransferCap/milestone``` field.

The ```equityTransferCap/milestone/id``` and ```equityTransferCap/milestone/title``` fields should match the ```id``` and ```title``` fields, respectively, of a milestone in the ```milestones``` field of the ```implementation``` section of OCDS.

Where a milestone does not already exist to describe the end of the period during which the equity transfer cap applies, an appropriate milestone should be added to the ```milestones``` field of the ```implementation``` section of OCDS.

A title and description for the equity transfer caps can be provided using the ```equityTransferCap/title``` and ```equityTransferCap/description``` fields respectively.

#### Example

**Equity Transfer Caps:**

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-contract-01.json
   :jsonpointer: /releases/0/contracts/0/equityTransferCaps
   
```

**Associated Milestones**

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-contract-01.json
   :jsonpointer: /releases/0/contracts/0/implementation/milestones
   
```

(See [github issue](https://github.com/open-contracting/public-private-partnerships/issues/30))

### V.5. Lender and investor information

The [finance extension](../../../extensions/finance/) should be used to capture details of:

* Commercial lenders
* Institutional investors
* Bilateral or multilateral lenders
* Public issue of bonds
* Supplier credit
* Other finance

For all finance from identified organisations, the organisation should be included in the ```parties``` array, with a role of ```financier```. 

For other forms of finance a title and description can be given.

ToDo: Check what codelists should be used here

### V.6. Categorize senior debt, mezzanine debt, other

The details of all debts should be captured using the [finance extension](../../../extensions/finance/) in ```contract/finance```.

### V.7. Amount and tenor of each, fixed or floating rate

The interest rates relating to each form of financing should be captured using the [finance extension](../../../extensions/finance/) in ```contract/finance```.

### V.8. Security and step in arrangements

Brief information on security and step in arrangements for particular finance can be provided using the ```description``` field against each entry in the ```contract/finance``` block. 

General information on the security and step in arrangements should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'financeArrangements' in the ```contract/documents``` array. 

### V.9. Forecast IRR

The forecast IRR should captured under ```contract/financialModel``` with a code of 'forecastIRR'. 

A single value should be given. 

If this forecast is updated later in the project, the new value should be substituted in. 

## Government Support

> Disclosure timing: Post commercial close, within 45-60 days of signing contract

Structured information about government grants and guarantees can be provided in the [finance block](../../../extensions/finance/) under ```contract/finance```.

Structured information about actual payments can be provided using the transactions block in ```contract/implementation/transactions```.

Structured information about subsidy, service payment and lease milestones can be provided using entries in the ```contract/milestones``` array. 

For all other disclosures required by the framework, documentation blocks should be provided.

### VI.1. Guarantees

#### Guarantee details

Details of the type and exact details of the guarantees provided should be included in a documentation block, covering both explicit and contingent guarantees—such as minimum revenue guarantee, exchange rate guarantee, debt repayment guarantee, and other guarantees. This should be captured through:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'contractGuarantees' in the ```contract/documents``` array. 

#### Disclosure reports

Document entries should also be provided for any fiscal commitments and contingent liabilities disclosure reports that exist. 

These documents should be tagged with a ```documentType``` value of 'guaranteeReports' in the ```contract/implementation/documents``` array. 

### VI.2. Grants

Documents relating to grants agreed should be placed in the ```contract/documents``` array with a  ```documentType``` value of 'grants'. 

Documents relating to the payment of grants and subsidies over the implementation of the project should be placed in the  ```contract/implementation/documents``` array with a  ```documentType``` value of 'grants'. 

The information in these documents should cover:

* Subsidy as a proportion of project value
* Capital subsidies paid during construction with periodicity or
milestones
* Operating subsidies and their periodicity or milestones

Subsidy a proportion of project value can be reported in the ```contract/financialModel``` block, with a code of 'subsidyRatio'. 

### VI.3. Service payments

Documents relating to service payments agreed should be placed in the ```contract/documents``` array with a  ```documentType``` value of 'servicePayments'. 

Documents relating to the payment of service payments over the implementation of the project should be placed in the  ```contract/implementation/documents``` array with a  ```documentType``` value of 'servicePayments'. 

Structure information about individual service payments can be included in ```contract/implementation/transactions```. 

### VI.4. Land leases, asset transfers

Documents relating to leases and asset transfers agreed in the contract should be placed in the ```contract/documents``` array with a  ```documentType``` value of 'lease' or 'assetTransfer'. 

Documents relating to leases and asset transfers in operation over the implementation of the project should be placed in the  ```contract/implementation/documents``` array with a  ```documentType``` value of 'lease' or 'assetTransfer'. 

### VI.5. Revenue-share, if any

Documents relating to revenue share agreed in the contract should be placed in the ```contract/documents``` array with a  ```documentType``` value of 'revenueShare'. 

Documents relating to revenue share in operation over the implementation of the project should be placed in the  ```contract/implementation/documents``` array with a  ```documentType``` value of 'revenueShare'. 

## Tariffs

> Disclosure timing: Post commercial close, within 45-60 days of signing contract

The [tariffs extension](../../extensions/tariffs/) can be used to capture structured information about tariff levels. 

Documentation blocks are used to provide links to methodology, tariff regulation information, and links to graphs.

### VII.1. Tariffs and pricing

##### JSON Example

```eval_rst

.. jsoninclude:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-contract-01.json
   :jsonpointer: /releases/0/contracts/0
   :expand: tariffs, value, dimensions
```

##### Spreadsheet example

```eval_rst
.. jsoninclude-flat:: docs/en/examples/ppp/ocds-eg0001-pf-hmt-835-contract-01.json
   :recursive:
   :jsonpointer: /releases/0/contracts/0/tariffs
   :ignore_path: /releases/0
```


### VII.2. Methodology for tariff setting/pricing

Details of the methodology for tariff setting and pricing should be provided using a documentation block with:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'tariffMethod' in the ```contract/documents``` array. 

### VII.3. Scope for reviews of tariff, pricing, regulatory mechanisms

Details of the methodology for tariff review should be provided using a documentation block with:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'tariffReview' in the ```contract/documents``` array. 

### VII.4. Links to graphs: tariff increases over time, consumer price index movement

Links to graphs concerning tariffs over time should be provided in a documentation block with:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'tariffs' in the ```contract/implementation/documents``` array. 


## Contract Termination

### VIII.1. Events of default and termination payments

TODO: Clarify whether this is reporting on actual events, or setting out the events provided for in the contract. 

### VIII.2. Handover

Arrangements for handover set out in the contract should be included in ```contract/documents``` with the ```documentType``` of 'handover' and including: 

* A short summary text
* A link to one or more documents that provide additional information

Information on handover taking place should be included in ```contract/implementation/documents``` with the ```documentType``` of 'handover' and should state details of hand over of assets back to state, condition of assets,
and any other conditions relating to hand over. Include details of
provisions for continuity of service.

## Renegotiations

> Disclosure timing: Within 45-60 days of execution of renegotiated contract

### IX.1. Contract variation details 

State variations to contract, if any, after signing of the original contract detailing each change against original provisions. State in addition the details of renegotiations and circumstances leading to renegotiations. State specifically any change due to the renegotiated clauses in the following: roles and responsibilities relating to the project, risk allocation, fiscal exposure, that is, any change in fiscal commitments and contingent liabilities with a rationale for agreeing to the change. Use the following formats:

## Performance Information

> Disclosure timing: Within 15-30 days of receipt of information

### X.1. Annual demand levels

Reporting on annual demand levels can be provided using the [metrics extension](../../../extensions/metrics/) at ```contracts/implementation/metrics```. 

The demand metric should be identified with an id of 'demand'.

### X.2. Annual revenues

Aggregate reporting on annual revenues can be provided using the [metrics extension](../../../extensions/metrics/) at ```contracts/implementation/metrics```. 

The demand metric should be identified with an id of 'revenue'.

### X.3. Actual IRR

Reporting on the actual IRR can be provided using the [metrics extension](../../../extensions/metrics/) at ```contracts/implementation/metrics```. 

The demand metric should be identified with an id of 'irr'.

ToDo: Check how often this would be reported? How much does this vary? 

### X.4. Performance

Reporting on performance against agreed metrics can be provided using the [metrics extension](../../../extensions/metrics/) at ```contracts/implementation/metrics```. 

The agreed metrics and targets can be provided in ```contracts/agreedMetrics``. 

### X.5. Performance Failures

ToDo: See table in framework

### X.6. Performance Assessments

Performance assessment reports can be provided through documents using:

* A short summary text
* A link to one or more documents that provide additional information

These documents should be tagged with a ```documentType``` value of 'performanceReport' in the ```planning/documents``` array. 
