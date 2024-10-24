```{workedexample} Processes with pre-qualification and pre-selection
:tags: tender
```

# Processes with pre-qualification and pre-selection

In single-stage procedures, buyers or procuring entities invite potential suppliers to bid without submitting any prior information.  Such procedures are straightforward to model in OCDS.

But, many jurisdictions also use multi-stage procedures. Such procedures follow a process like:

````{grid} 1 2 2 2
:gutter: 2

```{grid-item-card} First stage
* The buyer or procuring entity issues an invitation to participate in the process
* Potential suppliers submit expressions of interest
* The buyer or procuring entity assesses the expressions of interest
* The buyer or procuring entity establishes a list of qualified or selected potential suppliers
```

```{grid-item-card} Second stage
* The buyer or procuring entity issues an invitation to bid to the potential suppliers on the list
* Potential suppliers submit bids
* The buyer or procuring entity evaluates the bids
* The buyer or procuring entity awards a contract to the supplier(s)
```
````

This example describes 3 types of multi-stage procedure and explains how to model them in OCDS.

## Definitions

The term "pre-qualification" describes different types of multi-stage procedure:

### Pre-qualification with no limit on the number of qualified potential suppliers

The [UNCITRAL Model Law on Public Procurement (2011)](https://uncitral.un.org/en/texts/procurement/modellaw/public_procurement) was developed through extensive consultation and so reflects the procurement practices and concepts used in many different jurisdictions. The UNCITRAL model law defines pre-qualification as a procedure to:

> ...identify, prior to solicitation, suppliers or contractors that are qualified.

The model law obliges buyers and procuring entities to publish an invitation to pre-qualify. The invitation needs to specify the criteria and procedure for assessing the qualifications of potential suppliers. Much of the information that would usually appear on an invitation to tender is provided on the invitation to pre-qualify.

The buyer or procuring entity assesses the qualifications of the potential suppliers based on their responses. Only pre-qualified potential suppliers can take part in the later proceedings.

```{note}
The European Union's restricted procedure, competitive procedure with negotiation, competitive dialogue and innovation partnership use pre-qualification (see Articles 28-31, [Directive 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj)).
```

### Pre-qualification with a limit on the number of qualified potential suppliers (pre-selection)

The UNCITRAL model law defines pre-selection as a procedure to:

> ...identify, prior to solicitation, a **limited number** of suppliers or contractors that best meet the qualification criteria for the procurement concerned.

Pre-selection follows the same process as pre-qualification, with some additional requirements. The invitation to pre-qualify needs to specify how many potential suppliers the buyer or procuring entity will later request proposals from. The invitation also needs to specify how the buyer or procuring entity will select the potential suppliers to request proposals from.

```{note}
The European Union's restricted procedure, competitive procedure with negotiation, competitive dialogue procedure and innovation partnership all permit the use of pre-selection (see Article 65, [Directive 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj)).
```

### Pre-qualification in Paraguay

In Paraguay, buyers and procuring entities can carry out a single pre-qualification for several tenders of the same nature (see article 22, [law Nº 2.051/03](https://www.contrataciones.gov.py/documentos/download/marco-legal/12760)). The details of this procedure will become clearer in the example below.

## The OCDS model

In OCDS, a contracting process has a single competitive stage, the `tender` section. This represents the initiation of the process, when buyers or procuring entities invite potential suppliers to take part:

<div style="width:100%">

<div class="process-table">

![Planning](../../_static/svg/grey_planning.svg)

**Planning**

</div>

<div class="process-table">

![Tender](../../_static/svg/green_tendering.svg)

**Initiation (Tender)**

</div>

<div class="process-table">

![Award](../../_static/svg/grey_awarded.svg)

**Award**

</div>

<div class="process-table">

![Contract](../../_static/svg/grey_signed.svg)

**Contract**

</div>

<div class="process-table">

![Implementation](../../_static/svg/grey_implementation.svg)

**Implementation**

</div>

</div>
<br clear="all"/>

The `tender` section is also used to disclose information about the procedure used by the contracting process. In particular:

- The `tender.expressionOfInterestDeadline` field discloses the submission deadline for expressions of interest from potential suppliers.
- The `tender.tenderPeriod.endDate` field discloses the submission deadline for bids from qualified potential suppliers.
- The `tender.procurementMethod` field classifies the procedure using the following codelist:

```{csv-table-no-translate}
:header-rows: 1
:file: ../../../build/current_lang/codelists/method.csv
```

## Example: Pre-qualification

A buyer in the European Union invites potential suppliers to participate in a restricted procedure for the purchase of office supplies.

The invitation represents the initiation of the contracting process, so it is modelled using the `tender` section in OCDS.

```{jsoninclude} ../../examples/pre-qualification/pre-qualification_tender.json
:jsonpointer: /releases/0/tender
```

Any potential supplier can submit a request to take part in the first stage, but only qualified potential suppliers will be invited to submit a bid for the contract. Therefore, `tender.procurementMethod` is set to 'selective'.

```{note}
OCDS does not currently provide a way to disclose information on the second stage of multi-stage procedures. The approach to modelling multi-stage procedures is under discussion on [GitHub](https://github.com/open-contracting/standard/issues/440).

Contact the [Data Support Team](../../support/index) if you want to disclose this type of information.
```

## Example: Pre-selection

A buyer in the European Union invites potential suppliers to participate in a restricted procedure for the purchase of IT equipment.

The invitation represents the initiation of the contracting process, so it is modelled using the `tender` section in OCDS.

The buyer will invite a maximum of 5 qualified potential suppliers to submit a bid at the next stage, so `tender.procurementMethod` is set to 'selective'. The [selectionCriteria extension](https://extensions.open-contracting.org/en/extensions/selectionCriteria/master/) is used to disclose the criteria for choosing which potential suppliers to invite proposals from.

```{jsoninclude} ../../examples/pre-qualification/pre-selection_tender.json
:jsonpointer: /releases/0/tender
```

## Example: Pre-qualification in Paraguay

The buyer in Paraguay invites potential suppliers to pre-qualify for two road construction tenders. Each tender will reuse the list of pre-qualified potential suppliers established as a result of the pre-qualification procedure.

The invitation represents the initiation of a contracting process to establish a list of pre-qualified potential suppliers, so it is modelled using the `tender` section in OCDS.

Only qualified potential suppliers will be invited to bid in subsequent tenders that use the list, so `tender.procurementMethod` is set to 'selective'.

```{jsoninclude} ../../examples/pre-qualification/pre-qualification_paraguay.json
:jsonpointer: /releases/0/tender
```

```{note}
OCDS does not currently provide a way to disclose information on the second stage of multi-stage procedures. The approach to modelling multi-stage procedures is under discussion on [GitHub issue](https://github.com/open-contracting/standard/issues/440).

Contact the [Data Support Team](../../support/index) if you want to disclose this type of information.
```
