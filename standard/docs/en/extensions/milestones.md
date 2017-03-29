## Milestone Extension

Many different events occur over the course of a contracting process. OCDS includes core fields for a number of key dates and periods, such as:

* ```tenderPeriod``` 
* ```awardPeriod```
* ```contract/period```

However, there are many other key dates that may be scheduled or monitored at various stages of a contracting process. These include:

* **preProcurement** events, such as the preparation of key studies
* **engagement** events, such as public hearings or consultations
* **approval** events, such as project sign-off
* **assessment** events, such as the meeting of a commmittee to review proposals, or the dates associated with a multi-step award process
* **delivery** events, such as the predicated date for works to start, or to be finalised
* **reporting** events, such as the deadline for performance reports
* **financing** events, such as planned payments, or equity transfers

These can all be modelled using the milestones extension.

### Extension details

#### Milestones by section

With this extension in use, a ```milestones``` building block is available in the following sections:

* **Planning** - for any milestones relating to the planning process. This is likely to include planning, engagement and approval milestone types.
* **Tender** - for any milestones relating to the tender process. This is likely to include assessment milestones, and in some cases will include engagement and approval milestones.
* **Contract** - for any milestones relating to the signing of the contract itself. 
* **Implementation** - for any milestones relating to delivery, reporting and financial progress. If these milestones are known at the time of award, but before a contract is signed, they can be indicated using a draft contract block (with ```contract/status``` of ```pending```)

(When used alongside the proposed qualfication stage extension, milestones will also be available for the qualfication stage).

Consuming applications may wish to combine milestones from **planning** and **tender** sections together as these will apply to the whole contracting process.

Applications may also wish to combine **contract** and **contract/implementation** milestones for each contract. Care should be taken not to aggregate all milestones regardless of the contract they appear in - as different contracts resulting from a single tender may have different milestones. 

#### Milestone types 

A field for ```milestone/type``` with the following values is introduced. 

* **preProcurement** - for events such as the preparation of key studies
* **engagement** for events such as public hearings or consultations
* **approval** for events such as project sign-off
* **assessment** for events such as the meeting of a commmittee to review proposals, or the dates associated with a multi-step award process
* **delivery** for events such as the predicated date for works to start, or to be finalised
* **reporting** for events such as the deadline for performance reports
* **financial** for events such as planned payments, or equity transfers

#### Milestone status

We will update the milestoneStatus code list to include an extra entry for **scheduled** milestones, and will add definitions, giving a codelist of:

* **scheduled** - Scheduled - This milestone has been scheduled for the date in milestone.dueDate. Progress towards the milestone has not yet been evaluated as of milestone.dateModified
* **met** - Met - This milestone has been achieved. The data on which it was met should be placed in the milestone.dateMet field
* **notMet** - Not Met - This milestone had not been met at the date it was last reviewed (see milestone.dateModified). 
* **partiallyMet** - Partially Met - This milestone was judged to have been partially met at the date it was last reviewed (see milestone.dateModified)

#### dateMet

A field for ```milestone/dateMet``` is introduced to capture the date on which tile milestone was completed. 

#### Milestone codes

A field is included for ```milestone/code``` which can be used by applications to particular classify milestone events that may be important for analysis.

For example, some red flag analysis applications need to track approvals, and so may propose a code for ```projectApproval```. They can then look for projects which have a milestone with the code ```projectApproval``` and a status of 'Met'.

##### PPP Usage

For PPP disclosures, the following ```milestone/code``` values can be used:

* **approval** 
* **commercialClose**
* **financialClose** 

Where no code is required, the code can be left blank.  More details are provided in the OCDS for PPPs documentation. 

### Example

```json 

{
"uri":"http://standard.open-contracting.org/examples/releases/ocds-213czf-000-00001-04-award.json",
"publishedDate":"2010-05-10T09:30:00Z",
"publisher": {
        "scheme": "GB-COH",
        "uid": "09506232",
        "name": "Open Data Services Co-operative Limited",
        "uri": "http://standard.open-contracting.org/examples/"
    },
"license":"http://opendatacommons.org/licenses/pddl/1.0/",
"publicationPolicy":"https://github.com/open-contracting/sample-data/",
"releases":[{
        "language": "en",
        "ocid": "ocds-213czf-000-00001",
        "id": "ocds-213czf-000-00001-04-award",
        "date": "2010-05-10T09:30:00Z",
        "tag": ["award"],
        "initiationType": "tender",
        "entities": {
          "...":"..."
        },
        "buyer": {
            "id":"GB-LAC-E09000003",
            "name": "London Borough of Barnet",
        },
        "tender": {
            "id": "ocds-213czf-000-00001-01-tender",
            "title": "Planned cycle lane improvements",
            "description": "Tenders solicited for work to build new cycle lanes in the centre of town.",
            "status": "active",
            "items": ["..."],
            "minValue": {
                "amount": 600000,
                "currency": "GBP"
            },
            "value": {
                "amount": 1100000,
                "currency": "GBP"
            },
            "procurementMethod": "open",
            "procurementMethodRationale": "An open competitive tender is required by EU Rules",
            "awardCriteria": "bestProposal",
            "awardCriteriaDetails": "The best proposal, subject to value for money requirements, will be accepted.",
            "submissionMethod": [ "electronicSubmission" ],
            "submissionMethodDetails": "Submit through the online portal at http://example.com/submissions/ocds-213czf-000-00001-01/",
            "enquiryPeriod": {
                    "startDate": "2010-03-01T09:00:00Z",
                    "endDate": "2010-03-14T17:30:00Z"
            },
            "hasEnquiries": false,
            "tenderPeriod": {
                "startDate": "2010-03-01T09:00:00Z",
                "endDate": "2010-04-01T18:00:00Z"

            },
            "awardPeriod": {
                "startDate": "2010-06-01T00:00:00Z",
                "endDate": "2011-08-01T23:59:59Z"
            },
            "milestones": [{
                "id": "0001",
                "type":"assessment",
                "title": "Bid Opening ",
                "description": "The data when the bid will be openned.",
                "dueDate": "2010-04-01T18:00:00Z",
                "status":"met",
                "dateMet": "2010-04-01T18:00:00Z",
                "dateModified":"2010-04-01T18:00:00Z"

            },
            {
                "id": "0002",
                "type":"assessment",
                "title": "Review Committee Meeting ",
                "description": "The date when the review committee will meet to assess bids.",
                "dueDate": "2010-04-05T15:00:00Z",
                "status":"met",
                "dateMet": "2010-04-05T16:00:00Z",
                "dateModified":"2010-04-01T18:00:00Z"
              }]
        },
        "contract": [
               {
                   "id": "ocds-213czf-000-00001-award-01",
                   "title": "Contract to build new cycle lanes in the centre of town.",
                   "description": "AnyCorp Ltd has been awarded the contract to build new cycle lanes in the centre of town.",
                   "status": "pending",
                   "date": "2010-05-10T09:30:00Z",
                   "value": {
                       "amount": 11000000,
                       "currency": "GBP"
                   },
                   "items": "...",
                   "contractPeriod": {
                       "startDate": "2010-07-01T00:00:00Z",
                       "endDate": "2011-08-01T23:59:00Z"
                   },
                   "milestones": [
                      {
                        "id":"0003",
                        "type":"delivery",
                        "title":"Building work started",
                        "description":"Building work should start by this date.",
                        "dueDate":"2010-10-01T00:00:00Z",
                        "status":"planned",
                        "dateModified":"2010-05-10T09:30:00Z"
                      },
                      {
                        "id":"0004",
                        "type":"delivery",
                        "title":"Building work complete",
                        "description":"Building work should be complete by this date.",
                        "dueDate":"2011-06-01T00:00:00Z",
                        "status":"planned",
                        "dateModified":"2010-05-10T09:30:00Z"
                      },
                      {
                        "id":"0005",
                        "type":"reporting",
                        "title":"Project initiation report",
                        "description":"A report on project initiation should be provided by the end of 2010",
                        "dueDate":"2010-12-12T00:00:00Z",
                        "status":"planned",
                        "dateModified":"2010-05-10T09:30:00Z"
                      },
                      {
                        "id":"0006",
                        "type":"reporting",
                        "title":"Mid-term project report",
                        "description":"A mid-term project report should be provided by March 2011",
                        "dueDate":"2011-03-31T00:00:00Z",
                        "status":"planned",
                        "dateModified":"2010-05-10T09:30:00Z"
                      },
                      {
                        "id":"0007",
                        "type":"reporting",
                        "title":"Final project report",
                        "description":"The final project report should be provided by the end of the project.",
                        "dueDate":"2011-08-01T23:59:00Z",
                        "status":"planned",
                        "dateModified":"2010-05-10T09:30:00Z"
                      }
                   ]
                }
           ]

    }]
}
```




### Notes:

Draft of milestones update for ODCS V1.1 upgrade. Staged as an extension for inclusion in draft ppp extension.

See [#373](https://github.com/open-contracting/standard/issues/373) for more details.


* This draft does not deprecate ```milestone/documents``` as discussed in [#355](https://github.com/open-contracting/standard/issues/355)
* This draft does not include a ```report``` field for free-text reporting on milestone progress as discussed in [#373](https://github.com/open-contracting/standard/issues/373)

