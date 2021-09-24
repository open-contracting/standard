# Processes with pre-qualification and pre-selection

In single-stage procedures, buyers or procuring entities invite potential suppliers to bid without submitting any prior information.  Such procedures are straightforward to model in OCDS.

But, many jurisdictions also use multi-stage procedures. Such procedures follow a process like:

```{csv-table}
:header-rows: 1
:widths: auto
:file: ../../examples/pre-qualification/multi-stage.csv
```

This worked example describes 3 types of multi-stage procedure and explains how to model them in OCDS.

## Definitions

The term ‘pre-qualification’ describes different types of multi-stage procedure:

### Pre-qualification with no limit on the number of qualified potential suppliers

The [UNCITRAL Model Law on Public Procurement (2011)](https://uncitral.un.org/en/texts/procurement/modellaw/public_procurement) was developed through extensive consultation and so reflects the procurement practices and concepts used in many different jurisdictions. The UNCITRAL model law defines pre-qualification as a procedure to:

> ...identify, prior to solicitation, suppliers or contractors that are qualified.

The model law obliges buyers and procuring entities to publish an invitation to pre-qualify. The invitation needs to specify the criteria and procedure for assessing the qualifications of potential suppliers. Much of the information that would usually appear on an invitation to tender is provided on the invitation to pre-qualify.

The buyer or procuring entity assesses the qualifications of the potential suppliers based on their responses. Only pre-qualified potential suppliers can take part in the later proceedings.

```{note}
The European Union’s restricted procedure, competitive procedure with negotiation, competitive dialogue and innovation partnership use pre-qualification (see Articles 28-31, [Directive 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj)).
```

### Pre-qualification with a limit on the number of qualified potential suppliers (pre-selection)

The UNCITRAL model law defines pre-selection as a procedure to:

> ...identify, prior to solicitation, a **limited number** of suppliers or contractors that best meet the qualification criteria for the procurement concerned.

Pre-selection follows the same process as pre-qualification, with some additional requirements. The invitation to pre-qualify needs to specify how many potential suppliers the buyer or procuring entity will later request proposals from. The invitation also needs to specify how the procuring entity will select the potential suppliers to request proposals from.

```{note}
The European Union’s restricted procedure, competitive procedure with negotiation, competitive dialogue procedure and innovation partnership all permit the use of pre-selection (see Article 65, [Directive 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj)).
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

The `tender` section is also used to disclose information about the procedure used by the contracting process. In particular, the `tender.procurementMethod` field classifies the procedure using the following codelist:

```{csv-table-no-translate}
:header-rows: 1
:widths: auto
:file: ../../../build/current_lang/codelists/method.csv
```

## Example: Pre-qualification

The Bank of England issues a [restricted procedure contract notice](https://ted.europa.eu/udl?uri=TED:NOTICE:90873-2019:TEXT:EN:HTML) to invite potential suppliers to pre-qualify for a tender to provide facilities management services.

The notice represents the initiation of the contracting process, so it is modelled using the `tender` section in OCDS:

```{jsoninclude} ../../examples/pre-qualification/pre-qualification-package.json
:jsonpointer: /releases/0/tender
:title: Tender section
```

Any potential supplier can submit a request to take part in the first stage, but only qualified potential suppliers will be invited to submit a bid for the contract. Therefore, `tender/procurementMethod` is set to ‘selective’.

```{note}
OCDS does not currently provide a way to disclose information on the second stage of multi-stage procedures. The approach to modelling multi-stage procedures is under discussion on [GitHub](https://github.com/open-contracting/standard/issues/440).

Contact the [helpdesk](../../support/index.md) if you want to disclose this type of information.
```

## Example: Pre-selection

The National Nuclear Laboratory issues a [restricted procedure contract notice](https://ted.europa.eu/udl?uri=TED:NOTICE:28681-2020:TEXT:EN:HTML&src=0) to invite potential suppliers to pre-qualify for a project to update its physical security system arrangements.

The notice represents the initiation of the contracting process, so it is modelled using the `tender` section in OCDS.

The procuring entitiy will invite a maximum of 5 qualified potential suppliers to submit a bid at the next stage, so `tender/procurementMethod` is set to ‘selective’. The [selectionCriteria extension](https://extensions.open-contracting.org/en/extensions/selectionCriteria/master/) is used to disclose the criteria for choosing which potential suppliers to invite proposals from.

```{jsoninclude} ../../examples/pre-qualification/pre-selection-package.json
:jsonpointer: /releases/0/tender
:title: Tender section
```

## Example: Pre-qualification in Paraguay

The Ministry of Public Works and Communications issues an [invitation for potential suppliers to pre-qualify for two tenders for road construction in different neighbourhoods](https://contrataciones.gov.py/licitaciones/convocatoria/338229-servicios-consultoria-estudios-factibilidad-diseno-final-ingenieria-tramos-caminos-1/precalificacion.html). Each tender will re-use the list of pre-qualified potential suppliers established as a result of this first procedure.

The invitation represents the initiation of a contracting process to establish a list of pre-qualified potential suppliers, so it is modelled using the `tender` section in OCDS.

Only qualified potential suppliers will be invited to bid in subsequent tenders that use the list, so `tender.procurementMethod` is set to ‘selective’.

```{jsoninclude} ../../examples/pre-qualification/pre-qualification-paraguay-package.json
:jsonpointer: /releases/0/tender
:title: Tender section
```

```{note}
OCDS does not currently provide a way to disclose information on the second stage of multi-stage procedures. The approach to modelling multi-stage procedures is under discussion on [GitHub issue](https://github.com/open-contracting/standard/issues/440).

Contact the [helpdesk](../../support/index.md) if you want to disclose this type of information.
```
