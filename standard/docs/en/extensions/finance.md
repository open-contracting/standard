Financing extension
===================

Sometimes, particularly in the case of Public Private Partnerships, contracts are financed using a range of instruments, including loans, grants, share issues and so-on.

The financing extension provides a space to declare the finance arranged for a contract.

This is declared within the ```contract``` section, based on an understanding that this information is generally only disclosed following the signature of a contract. This information can be updated over the lifetime of the contract.

The finance building block includes:

* **Financing Party** - an organization reference to the id and name of an organisation listed in the main parties array. 
* **Finance Type** - an entry from a FinanceType codelist (to be defined)
* **Finance Category** - an entry from a Finance Category codelist, covering senion, mezzanine and other
* **Period** - a start and end date for the finance
* **interestRate** - an object consisting of:
  * **base** - a constant such as 0.1, or a known rate such as LIBOR
  * **margin** - the component added to this base to give the rate
  * **fixed** - a boolean for whether the rate is fixed or variable
  * **notes** - space to provide more information on the rate


This allows modelling of rates such as 'LIBOR+1%'. 


Outstanding issues
==================

* We need to develop the finance type codelist. 

* Do we need to include a 'duration' field in period, to allow for the specification of finance types without set start and end-dates?