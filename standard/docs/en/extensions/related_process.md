Related processes
=================

In OCDS each contracting process can have only one planning and tender stage. There are a number of cases where it is important to know about related planning and tendering processes, including:

* When one planning process results in many tenders;
* What a contract is awarded following two or more invitation to tender processes, such as in some processes involving pre-qualification, of frameworks with mini-competitions;
* When a contract results in the award of sub-contracts also tracked through OCDS data;
* When a contract is coming up for renewal or replacement, and there is a contracting process to award  the renewal/replacement contract;

In all these cases, the ```relatedProcess``` block can be used to cross-reference between the relevant open contracting processes using their ```OCID```.

## Process and contract relationships

A related process can be declared at two points in an OCDS release.

**(1) A the release level** - used to point backwards to prior processes, such as planning, PQQ or framework establishment.

**(2) At the contract level** - used to point onwards to sub-contracts, renewal or replacement processes that relate solely to the particular contract the property appears in.  

As well as providing this machine-readable link between processes, publishers may also provide links to human-readable documentation in the relevant ```documents``` blocks. For example:

* When recording a ```release/relatedProcess``` pointing to the ocid of the planning process that resulted in a tender, a ```tender/documents``` entry with a ```documentType``` of 'procurementPlan' and a link to web pages about the procurement plan could be provided;
* When recording a ```contract/relatedProcess``` pointing to the ocid of a  sub-contracting process, a ```contract/documents``` entry with a ```documentType``` of 'subContract' and a title that describes it as the subcontracting process, could be provided;
* When recording a ```contract/relatedProcess``` pointing to the ocid of a tender process to renew a given contract, a ```contract/documents``` entry with a ```documentType``` of 'tenderNotice' and a title that describes it as the successor process, could be provided;

## Codelists

The relatedProcess codelist is given below. 

| Code                | Title                                     | Description| 
|---------------------|-------------------------------------------|-----------------------------------------------------------------------| 
| preQualification    | Pre-qualification process                 | This contracting process follows on from the related pre-Qualification process. The qualified suppliers are listed in the award section of the related process.                                                                                                                                                             | 
| preSelection        | Pre-selection process                     | "This contracting process follows on from the related pre-selection process which sought to identify, prior to solicitation, a limited number of suppliers or contractors that best meet the qualification criteria for the procurement concerned. These suppliers are listed in the award section of the related process." | 
| framework           | Framework agreement procedure first stage | This contracting process follows on from the related process to establish a framework. The suppliers on the framework are listed in the award section of the related process.                                                                                                                                               | 
| planning            | Planning process                          | This contracting process follows on from the related planning process.                                                                                                                                                                                                                                                      | 
| parent              | Parent contract (for sub-contracts)       | This contracting process may result in a sub-contract of the related process.                                                                                                                                                                                                                                               | 
| prior               | Prior process                             | This contracting process is the renewal or replacement of the related prior process.                                                                                                                                                                                                                                        | 
| unsuccessfulProcess | Unsuccessful process                      | This contracting process follows on from an previous unsuccessful process.                                                                                                                                                                                                                                                  | 
| subContract         | Sub-contract                              | The related process may result in a sub-contract of this contract.                                                                                                                                                                                                                                                          | 
| replacementProcess  | Replacement process                       | The related process may result in the replacement of this contract.                                                                                                                                                                                                                                                         | 
| renewalProcess      | Renewal process                           | The related process may result in the renewal of this contract.                                                                                                                                                                                                                                                             | 



See issue [#371](https://github.com/open-contracting/standard/issues/371).