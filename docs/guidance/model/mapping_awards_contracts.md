# Mapping to the award and contract sections of OCDS

OCDS separates data about the contract award and data about the signed contract into the `awards` and `contracts` sections respectively. Source systems may contain data on awards, on contracts, or on both.

If the data in the source system relates only to contract awards, then only the `award` section of OCDS ought to be populated, unless the law governing procurement permits no changes between award and signature of a contract, in which case the `contract` section may be populated.

If the data in the source system relates only to the signed contract and no changes are permitted between the award and signature of a contract, then:

* Add an `Award` object to `awards` and a `Contract` object to `contracts`
* Set `awards.id` and `contracts.id` to the same value
* Populate the `awards.value`, `awards.contractPeriod` and `awards.items` fields with the initial contract value, period and items respectively
* If the contract value, period or items are subsequently updated, populate the `contracts.value`, `contracts.period` and `contracts.items` fields with the updated value

The above approach is also applicable to direct call-offs from framework agreements with multiple suppliers, since the call-off is, conceptually, an award.

## Example: Changes between award and contract

The Zambia Public Procurement Authority provides a central e-procurement system, used by procuring entities to manage the tender and award stages of the contracting processes, which publishes OCDS data.

Once an award is published by the e-procurement system, there is a 10-day standstill period for unsuccessful bidders to appeal the award decision.

If an appeal is made and upheld, then the award is cancelled. If no appeals are upheld by the end of the standstill period, then a contract is signed between the buyer and the supplier, outside of the e-procurement system. No OCDS data is published or updated from this stage of the contracting process onward.

In this example, the Ministry of Finance uses the e-procurement system to solicit bids for the development of a new website. A contract is awarded to 360nx Designs for 3,000,000 ZMK, through the e-procurement system.

An unsuccessful bidder appeals the award decision and the appeal is upheld, resulting the award being cancelled.

If both the `award` and `contract` sections of OCDS had been populated when the award was made through the e-procurement system, this would have resulted in the presence of a contract in the OCDS data that had never existed in reality.
