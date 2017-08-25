# Building Blocks

In mapping your data to OCDS, or using OCDS data, you will encounter a number of common data structures.

<table style="margin-bottom:2em;">
    <tr>
        <td width="20%" align="center"><img src="../../../assets/green_organisation.svg.png" width="80%"></td>
        <td width="20%" align="center"><img src="../../../assets/green_value.svg.png" width="80%"></td>
        <td width="20%" align="center"><img src="../../../assets/green_items.svg.png" width="80%"></td>
        <td width="20%" align="center"><img src="../../../assets/green_milestone.svg.png" width="80%"></td>
        <td width="20%" align="center"><img src="../../../assets/green_documents.svg.png" width="80%"></td>
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

The OCDS schema sets out the fields that should be included in each section, making use of simple re-usable building blocks (field structures) to represent data.

For example, common building blocks are provided for:

* **Parties (Organizations)**
* **Amounts**
* **Items**
* **Time periods**
* **Documents**
* **Milestones**

### Examples

```eval_rst

.. jsoninclude:: docs/en/examples/record.json
   :jsonpointer: /records/0/compiledRelease/parties/0
   :expand: identifier, address, contactPoint
   :title: party

```

```eval_rst

.. jsoninclude:: docs/en/examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/value
   :expand:
   :title: amounts

```

```eval_rst

.. jsoninclude:: docs/en/examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/items
   :expand: classification, unit, additionalClassifications, value
   :title: items

```

```eval_rst

.. jsoninclude:: docs/en/examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/contractPeriod
   :expand:
   :title: period

```

```eval_rst

.. jsoninclude:: docs/en/examples/record.json
   :jsonpointer: /records/0/compiledRelease/awards/0/documents
   :expand:
   :title: documents

```

```eval_rst

.. jsoninclude:: docs/en/examples/record.json
   :jsonpointer: /records/0/compiledRelease/tender/milestones/0
   :expand:
   :title: milestones

```

### Using building blocks

These building blocks may be used in various different sections. For example, **items** can occur in tender (to indicate the items that a buyer wishes to buy), in an award object (to indicate the items that an award has been made for) and in a contract object (to indicate the items listed in the contract).

In addition to these building blocks, the OCDS schema sets out the specific ways they can be used in each section, and describes a number of additional fields that can appear in specific section. For example, fields for:

* ```titles``` and ```descriptions``` of tenders, awards and contracts
* ```procurementMethod```
* ```awardCriteria```
* ```submissionMethod```
* etc.

Many of these fields make use of lightweight codelists provided by OCDS.

### Extensions

In some cases, publishers or users need building blocks and fields which are not provided in the core OCDS schema.

We maintain a list of [extensions](../../../extensions/) that provide optional extra building blocks and fields.

<div class="example hint" markdown=1>

<p class="first admonition-title">Field level mapping</p>

The Open Contracting Data Standard helpdesk maintain a [field-level mapping template](http://www.open-contracting.org/resources/ocds-field-level-mapping-template/) that can be used to cross-walk between your internal data systems and OCDS.

</div>

## Codelists

OCDS defines two kinds of codelist:

* **Closed codelists** provide a fixed list of values. When using a field with a closed codelist, publishers must use an option from the published lists. This supports the global comparability of OCDS data on key dimensions.

* **Open codelists** provide recommended values. However, publishers can suggest amendments to these codelists, or provide their own extended values.

<table width="100%">
<tr>
<td valign="top" width="50%" style="padding:10px;" markdown=1>

**Open Codelists**

* Party Role
* Item Classification Scheme
* Unit Classification Scheme
* Organization Identifier Scheme
* Document Type
* Award Criteria
* Submission Method
* Related Process
* Related Process Scheme
* Milestone Type
* Extended Procurement Category

</td>
<td valign="top" width="50%" style="padding:10px;" markdown=1>

**Closed Codelists**

* Release Tag
* Initiation Type
* Tender Status
* Procurement Method
* Procurement Category
* Award Status
* Contract Status
* Currency
* Milestone Status

</td>
</tr>
</table>

Codelist values are case sensitive strings with associated labels, available in each language OCDS has been translated into.

Publishers should map their existing classification systems to OCDS codes wherever possible. Many closed codelist fields are paired with a detail field where more detailed classification information can be provided.

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

In the EU, contracts can be initiated through a number of different procedures including:

* Open procedure;
* Restricted procedure;
* Competitive procedure with negotiation;
* Competitive dialogue; and
* Innovation partnership

However, to support comparison across continents, the main OCDS procurement method codelist is a closed codelist with four values:

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :file: ../../../schema/codelists_translated/method.csv
```

All procedures should be able to be mapped to one of these options.

To publish OCDS data, an EU publisher with data categorized by EU procedures should map the longer list of procedures to the narrower OCDS codelist and provide the codelist value in the ```procurementMethod``` field. They can then provide the more detailed procedure type in an extended ```procurementMethodDetails``` field.

For an Open Procedure, when a free-text justification of why the procedure was chosen is available, this would end up as:

```json
{
    "procurementMethod":"open",
    "procurementMethodDetails":"Open Procedure",
    "procurementMethodRationale":"To maximize competition."

}
```

</div>

<!--ToDo: Add section on mapping - including links to mapping tools -->
