# Participation fees

## Metadata

To use this extension, include its URL in the ```extension``` array of your release or record package.

```json
{
    "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_participationFee_extension/v1.1.1/extension.json"],
    "releases":[]
}
```

This extension is maintained at [https://github.com/open-contracting/ocds_participationFee_extension](https://github.com/open-contracting/ocds_participationFee_extension)

## Documentation

### Background

There are a number of cases where there may be costs to access documents for, or to participate within, a tender process. 

Potential bidders will want to be aware of the fees that a process might involve.

Procurement monitors may wish to ensure that participation fees are within legal parameters (often set as a fixed maximum, or a percentage of total contract value), or to monitor how participation fees are being used.

### Extension fields

This extension adds a ```participationFees``` field to the ```tender``` section of OCDS and introduces a new ```participationFee``` building block.

The ```participationFees``` field is an array of ```participationFee``` building blocks.

The ```participationFee``` building block is made up of three fields:

* ```type``` - a value from the ```participationFeeType``` codelist, describing the type of the fee
* ```value``` - the amount and currency of the fee
* ```description``` - an optional field with more information on the fee requirements. For example, sometimes a document fee is only applicable to the hard copy of the documents.
* ```methodOfPayment``` - an optional field providing information on methods of payment accepted for the documentation. This is currently an array of strings, but an open codelist may be introduced in future. 

### Extension codelists

This extension adds **closed** ```participationFeeType``` codelist with the following codes:

* document - a fee payable for access to bidding documents
* deposit - a refundable fee payable for the submission of bids
* submission - a non-refundable fee payable for the submission of bids
* win - a fee payable by the winning bidder

### Example

The following JSON snippet models a contracting process where fees are applicable for both access to documents and submission of bids:

```JSON
{
  "tender": {
    "participationFees": [
      {
        "type": "document",
        "value": {
          "currency": "GBP",
          "amount": 8.00
        },
        "description": "Fee payable for both soft and hard copies of documents.",
          "methodOfPayment":["electronic","cheque"]
      },
      {
        "type": ["submission"],
        "value": {
          "currency": "GBP",
          "amount": 10.00
        },
        "description": "Fee payable within e-procurement system.",
        "methodOfPayment":["electronic"]
      }
    ]
  }
}
```

### Usage notes

In some cases, a fee may be levied for 'official copies' of procurement documents (although copies may also be available freely online), and bidders required to prove they have paid for an official copy of the documents as part of their submission. 

In this case, the fee should be modelled as a **submission** fee, as submission is only possible when this document access fee has been paid. 

### To do

* participation / submission terminology
* finalize codelist
