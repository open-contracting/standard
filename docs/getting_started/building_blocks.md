# Building Blocks

In mapping your data to OCDS, or using OCDS data, you will encounter a number of common data structures.

<table style="margin-bottom:2em;">
    <tr>
        <td width="20%" align="center"><img src="../../_static/svg/green_organisation.svg" width="80%"></td>
        <td width="20%" align="center"><img src="../../_static/svg/green_value.svg" width="80%"></td>
        <td width="20%" align="center"><img src="../../_static/svg/green_items.svg" width="80%"></td>
        <td width="20%" align="center"><img src="../../_static/svg/green_milestone.svg" width="80%"></td>
        <td width="20%" align="center"><img src="../../_static/svg/green_documents.svg" width="80%"></td>
    </tr>
</table>

## Sections and structure

An OCDS document is made up of a number of sections. These are:

* **release metadata** - contextual information about each release of data;
  * **parties** - information about the organizations and other participants involved in the contracting process;
  * **planning** - information about the goals, budgets and projects a contracting process relates to;
  * **tender** - information about how a tender will take place, or has taken place;
  * **awards** - information on awards made as part of a contracting process;
  * **contract** - information on contracts signed as part of a contracting process;
    * **implementation** - information on the progress of each contract towards  completion.

These are represented in a JSON document as follows:

```{eval-rst}
.. code-block:: json
   :emphasize-lines: 8-13
       
       {
            "language": "en",
            "ocid": "contracting-process-identifier",
            "id": "release-id",
            "date": "ISO-date",
            "tag": ["tag-from-codelist"],
            "initiationType": "tender",
            "parties": {},
            "buyer": {},
            "planning": {},
            "tender": {},
            "awards": [ {} ],
            "contracts":[ {
                "implementation":{}
            }]
        }
```

## Building blocks: fields

The OCDS schema sets out the fields that ought to be included in each section (where applicable), making use of simple re-usable building blocks (field structures) to represent data. 

For example, common building blocks are provided for:

* **Parties (Organizations)** 
* **Amounts** 
* **Items**
* **Time periods**
* **Documents** 
* **Milestones**

### Examples

```{eval-rst}
.. jsoninclude:: ../examples/record.json
   :jsonpointer: /records/0/compiledRelease/parties/0
   :expand: identifier, address, contactPoint
   :title: party

```

```{eval-rst}
.. jsoninclude:: ../examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/value
   :expand: 
   :title: amounts

```

```{eval-rst}
.. jsoninclude:: ../examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/items
   :expand: classification, unit, additionalClassifications, value
   :title: items

```

```{eval-rst}
.. jsoninclude:: ../examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/contractPeriod
   :expand: 
   :title: period

```

```{eval-rst}
.. jsoninclude:: ../examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/documents
   :expand: 
   :title: documents

```

```{eval-rst}
.. jsoninclude:: ../examples/record.json
   :jsonpointer: /records/0/compiledRelease/tender/milestones/0
   :expand: 
   :title: milestones

```

### Using building blocks

These building blocks can be used in various different sections. For example, **items** can occur in tender (to indicate the items that a buyer wishes to buy), in an award object (to indicate the items that an award has been made for) and in a contract object (to indicate the items listed in the contract). 

In addition to these building blocks, the OCDS schema sets out the specific ways they can be used in each section, and describes a number of additional fields that can appear in specific section. For example, fields for:

* `titles` and `descriptions` of tenders, awards and contracts
* `procurementMethod`
* `awardCriteria`
* `submissionMethod`
* etc.

Many of these fields make use of lightweight codelists provided by OCDS. 

### Extensions

In some cases, publishers or users need building blocks and fields which are not provided in the core OCDS schema. 

We maintain a list of [extensions](../guidance/map/extensions) that provide additional building blocks and fields.

<div class="example hint" markdown=1>

<p class="first admonition-title">Field level mapping</p>

The Open Contracting Data Standard helpdesk maintain a [field-level mapping template](http://www.open-contracting.org/resources/ocds-field-level-mapping-template/) that can be used to cross-walk between your internal data systems and OCDS.  

</div>

## Codelists

OCDS defines two kinds of codelist:

* **Closed codelists** provide a fixed list of values. When using a field with a closed codelist, publishers need to use an option from the published lists. This supports the global comparability of OCDS data on key dimensions.

* **Open codelists** provide representative values. However, publishers can suggest amendments to these codelists, or provide their own extended values.

Codelist values are case sensitive strings with associated labels, available in each language OCDS has been translated into. 

Publishers need to map their existing classification systems to OCDS codes wherever possible. Many closed codelist fields are paired with a detail field where more detailed classification information can be provided. 

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

In the EU, contracts can be initiated through a number of different procedures including:

* Open procedure;
* Restricted procedure; 
* Competitive procedure with negotiation; 
* Competitive dialogue; and
* Innovation partnership

However, to support comparison across continents, the main OCDS procurement method codelist is a closed codelist with four values:

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/method.csv
```

All procedures need to be mapped to one of these options. 

To publish OCDS data, an EU publisher with data categorized by EU procedures needs to map the longer list of procedures to the narrower OCDS codelist and provide the codelist value in the `procurementMethod` field. They can then provide the more detailed procedure type in an extended `procurementMethodDetails` field.

For an Open Procedure, when a free-text justification of why the procedure was chosen is available, this would end up as:

```json
{
    "procurementMethod":"open",
    "procurementMethodDetails":"Open Procedure",
    "procurementMethodRationale":"To maximize competition."
    
}
```

</div>
