## Building blocks: the data

In mapping your data to OCDS, or using OCDS data, you will encounter a number of common data structures.

### Sections and structure

An OCDS document is made up of a number of sections. In the procurement case, the main sections are:

* **Meta-data** - contextual information about each release of data;
* **buyer** - information about the key contracting party;
* **planning** - information about the goals, budgets and projects a contracting process relates to;
* **tender** - information about how a tender will take place, or has taken place;
* **awards** - information on awards made as part of a contracting process;
* **contract** - information on contracts signed as part of a contracting process;
  * **implementation** - information on the progress of each contract towards completion.

These are represented in a JSON document as follows:

```eval_rst
.. code-block:: json
   :emphasize-lines: 8-13
   
        {
            "language": "en",
            "ocid": "contracting-process-identifier",
            "id": "release-id",
            "date": "ISO-date",
            "tag": ["tag-from-codelist"],
            "initiationType": "tender",
            "buyer": {},
            "planning": {},
            "tender": {},
            "awards": [ {} ],
            "contracts":[ {
                "implementation":{}
            }]
        }
```

<div class="example hint" markdown=1>
    
<p class="first admonition-title">Note</p>
Awards and contracts are arrays of objects, whereas tender is an object. This is because of a contracting process has a single initiation stage, but can result in multiple awards and contracts. 

</div>

### Building blocks and fields

The OCDS schema sets out the fields that should be included in each section, making use of simple re-usable building blocks to represent data. 

For example, common building blocks are provided for:

* **Organizations** 
* **Amounts** 
* **Items**
* **Time periods**
* **Documents** 
* **Milestones**


TODO - ADD IN PREVIEW WIDGET FOR THESE BUILDING BLOCKS.


These building blocks may be used in various different sections. For example, **items** can occur in tender (to indicate the items that a buyer wishes to buy), in an award object (to indicate the items that an award has been made for) and in a contract object (to indicate the items listed in the contract). 

In addition to these building blocks, the OCDS schema sets out the specific ways they can be used in each section, and describes a number of additional fields that can appear in specific section. For example, fields for:

* ```titles``` and ```descriptions``` of tenders, awards and contracts
* ```procurementMethod```
* ```awardCriteria```
* ```submissionMethod```
* etc.

Many of these fields make use of lightweight codelists provided by OCDS. 

### Codelists

OCDS defines two kinds of codelist:

* **Closed codelists** provide a fixed list of values. When using a field with a closed codelist, publishers must use an option from the published lists. This supports the global comparability of OCDS data on key dimensions.

* **Open codelists** provide recommended values. However, publishers can suggest amendments to these codelists, or provide their own extended values prefixed with x_

TABLE OF CODELISTS


Codelist values are case sensitive strings. OCDS publish labels for many codes in English and Spanish (TODO - CONFIRM). 

Publishers should map their existing classification systems to OCDS codes wherever possible. Many closed codelist fields are paired with a detail field where more detailed classification information can be provided. 


