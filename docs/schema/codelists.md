# Codelists

Some schema fields refer to codelists, to limit and standardize the possible values of the fields, in order to promote data interoperability.

Codelists can either be open or closed. **Closed codelists** are intended to be comprehensive; for example, the [currency](#currency) codelist covers all currencies in the world. **Open codelists** are intended to be representative, but not comprehensive.

Publishers must use the codes in the codelists, unless no code is appropriate. If no code is appropriate and the codelist is **open**, then a publisher may use a new code outside those in the codelist. If no code is appropriate and the codelist is **closed**, then a publisher is encouraged to create an issue in the [OCDS GitHub repository](https://github.com/open-contracting/standard/issues) about adding a new code.

```{eval-rst}
.. admonition:: Extending open codelists
   :class: note

   .. markdown::

      If you use new codes outside those in an open codelist, please document the codes in an [OCDS extension](../guidance/map/extensions) and in your [publication policy](../../guidance/publish/#finalize-your-publication-policy). Please also create an issue in the [OCDS GitHub repository](https://github.com/open-contracting/standard/issues), so that the codes can be considered for inclusion in the codelist.
```

The release schema, in {download}`JSON Schema <../../build/current_lang/release-schema.json>`, has a `codelist` property to indicate the <a href="../../codelists/">CSV File</a> that defines the codes in the codelist (shown as tables below). It also has an `openCodelist` property, to indicate whether the codelist is open or closed.

Codes are case-sensitive, and are generally provided as English language camelCase. Codes must not be translated, though the OCDS team will work with publishers to translate code titles and definitions.

## Open Codelists

### Party Role

The organizations, economic operators or other participants in a contracting process are listed in the [parties section](../reference/#parties). A single party can have one or more roles in the contracting process.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/partyRole.csv
```

### Item Classification Scheme

Items should be classified using existing item classification schemes, such as the [EC Common Procurement Vocabulary (CPV)](https://simap.ted.europa.eu/web/simap/cpv).

The `itemClassificationScheme` codelist is referenced by the `scheme` field of the `Classification` object, which can be used in multiple contexts. You can find the codes relevant to a given context by filtering the codelist by its `Category` column.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/itemClassificationScheme.csv
```

### Unit Classification Scheme

Item quantities can be provided using an established codelist for units of measurement. Codelists might provide human-readable descriptions of units, or symbols for use in input and display interfaces.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/unitClassificationScheme.csv
```

### Organization Identifier Scheme

<style><!--img[alt="org-id.guide"] {
   width:200px;
   float:right;
}--></style>

![org-id.guide](../_static/png/org-id-logo-full.png)

The Organization Identifier Scheme uses the codes from [org-id.guide](http://www.org-id.guide). The latest version of the codelist can be [downloaded](http://org-id.guide/download) or [browsed](http://org-id.guide/) from its website.

To add new codes to the codelist, contact the [OCDS Helpdesk](../../support/index).

```{eval-rst}
.. note::

   This list was formerly maintained by the International Aid Transparency Initiative and contained in OCDS documentation as organizationIdentifierRegistrationAgency_iati.csv. This was removed in OCDS 1.1.1.
```

### Document Type

The following list describes documents and documentation recommended for publication as part of an open contracting implementation. The codelist indicates whether documents are considered 'basic', 'intermediate' or 'advanced', and the section of an OCDS release they are most likely to be applicable within. 

The code descriptions are necessarily broad, to cover their usage in a range of contracting processes, including for goods, works and services, and in other contexts, such as public private partnerships, infrastructure or concession contracts. 

Publishers must map their existing document codes to this list, where possible. If using this list within a user interface, publishers can re-write the codelist titles and descriptions appropriately for the context they are being used in. 

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :widths: 10 10 10 20 50
   :file: ../../build/current_lang/codelists/documentType.csv
```

### Award Criteria

The award criteria codelist describes the basis on which contract awards will be made. 

```{eval-rst}
.. note:: 

  This codelist was revised in OCDS 1.1, deprecating earlier codes and introducing a new set of codelist entries. Publishers ought to review the mapping from their internal systems to this updated list of award criteria.

```

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :widths: 20 20 50 10
   :file: ../../build/current_lang/codelists/awardCriteria.csv
```

### Submission Method

The submission method codelist is used to identify the mechanism through which a submission can be made. 

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/submissionMethod.csv
```

### Related Process

The related process block is used at the release level to point backwards to prior processes, such as planning or framework establishment, and at the contract level to point onwards to subcontracts or to renewal or replacement processes. The related process codelist determines the kind of relationship that is being described.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/relatedProcess.csv
```

### Related Process Scheme

The related process scheme describes the kind of identifier used to cross-reference another process. 

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/relatedProcessScheme.csv
```


### Milestone Type

The milestone block can be used to represent a wide variety of events in the lifetime of a contracting process. The milestone type codelist is used to indicate the nature of each milestone.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/milestoneType.csv
```

### Extended Procurement Category

The extended procurement category codelist is used to provide additional detail about the focus of a contracting process. 

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/extendedProcurementCategory.csv
```


## Closed Codelists 

### Release Tag

A contracting process can result in a number of releases of information over time. These must be tagged to indicate the stage of the contracting process they relate to. 

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/releaseTag.csv
```

### Initiation Type

Contracting processes can be formed under a number of different processes. Currently, only 'tender' is supported in this codelist. Future versions of the standard might support other initiation types. The initiation type is used to provide information to consuming applications on the different blocks of data and releases they can expect from a contracting process.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/initiationType.csv
```

### Tender Status

The `tender.status` field is used to indicate the current status of a tender process. The following options are available:

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/tenderStatus.csv
```

```{eval-rst}
.. note:: 
   The 'planning' status was introduced in version 1.1.
```

### Method

A contracting process aims to fulfill the requirements identified at the planning stage. The procurement method is the procedure used to purchase the relevant works, goods or services. The method codelist draws upon [the definitions of open, selective and limited provided by the WTO Government Procurement Agreement](http://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm), and adds an additional 'direct' code for awards without competition.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/method.csv
```

Note: The 'direct' code was introduced in Version 1.1. Publishers who completed a codelist mapping prior to 1.1 might have included direct procurement within limited, and ought to review their mappings.

### Procurement Category

The procurement category codelist is used to indicate the **primary** focus of a contracting process. Where a contracting process covers more than one of the options below, publishers should use the `additionalProcurementCategories` field with an array of entries from the open [extendedProcurementCategory](#extended-procurement-category) codelist.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/procurementCategory.csv
```

### Award Status

An award moves through multiple states. Releases over time can update the status of an award. 

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/awardStatus.csv
```

The `awardStatus` field and codelist is used to indicate when a tender did not result in an award (through the `"awardStatus":"unsuccessful"` value)

### Contract Status

Contracts can move through multiple states. Releases over time can update the status of a contract.

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/contractStatus.csv
```

### Milestone Status

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/milestoneStatus.csv
```

### Currency

The currency for each amount must be specified using the uppercase 3-letter currency code from [ISO4217](http://www.iso.org/iso/home/standards/currency_codes.htm).

```{eval-rst}
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/currency.csv
```
