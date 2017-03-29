Financing extension
===================

Sometimes, particularly in the case of Public Private Partnerships, contracts are financed using a range of instruments, including loans, grants, share issues and so-on.

The financing extension provides a space to declare the finance arranged for a contract.

This is declared within the ```contract``` section, based on an understanding that this information is generally only disclosed following the signature of a contract. This information can be updated over the lifetime of the contract.

The finance building block includes:

* **Title** and **Description** - for providing summary information about the finance
* **Financing Party** - an organization reference to the id and name of an organisation listed in the main parties array. 
* **Finance Type** - an entry from a FinanceType codelist
* **Finance Category** - an entry from a Finance Category codelist
* **Step in arrangements** and **Exchange rate guarantee** flags, to indicate whether either apply to this finance
* **Repayment Frequency** - to give an indication of likely repayments
* **Period** - a start, end date and/or duration for the finance
* **interestRate** - an object consisting of:
  * **base** - a constant such as 0.1, or a known rate such as LIBOR
  * **margin** - the component added to this base to give the rate
  * **fixed** - a boolean for whether the rate is fixed or variable
  * **notes** - space to provide more information on the rate

This allows modelling of rates such as 'LIBOR+1%'. 

## Codelists

The 'financeType' codelist is based on the list on [Page 57 of the World Bank PPP Disclosure Framework](http://pubdocs.worldbank.org/en/143671469558797229/FrameworkPPPDisclosure-071416.pdf#page=57)

The 'financeCategory' codelist is used to indicate (a) the rights attached to finance (in terms of equity, mezzanine and senior loans), and (b) to distinguish direct finance from guarantees. 

