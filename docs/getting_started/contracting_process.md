# The Contracting Process

There are several stages to a contracting process.

OCDS covers:

<style><!--
.process-table { width:18%; float:left; font-size:10pt; }
.process-table p { font-size:10pt; text-align: center; }
.process-table img { width:80%; }
--></style>

<div style="width:100%">

<div class="process-table" markdown=1>

![Planning](../_static/svg/green_planning.svg)

**Planning**<br/>
*Including:*<br/>
Budgets<br/>
Project plans<br/>
Procurement plans<br/>
Market studies<br/>
Public hearing info<br/>

</div>

<div class="process-table" markdown=1>

![Tender](../_static/svg/green_tendering.svg)

**Initiation (Tender)**<br/>
*Including:*<br/>
Tender notices<br/>
Specifications<br/>
Line items<br/>
Values<br/>
Enquiries

</div>

<div class="process-table" markdown=1>

![Award](../_static/svg/green_awarded.svg)

**Award**<br/>
*Including:*<br/>
Details of award<br/>
Bidder information<br/>
Bid evaluation<br/>
Values

</div>

<div class="process-table" markdown=1>

![Contract](../_static/svg/green_signed.svg)

**Contract**<br/>
*Including:*<br/>
Final details<br/>
Signed contract<br/>
Amendments<br/>
Values

</div>

<div class="process-table" markdown=1>

![Implementation](../_static/svg/green_implementation.svg)

**Implementation**<br/>
*Including:*<br/>
Payments<br/>
Progress updates<br/>
Location<br/>
Extensions<br/>
Amendments<br/>
Completion or Termination info

</div>

</div>
<br clear="all"/>

Not all contracting processes have all stages. For example, direct contracting might start with the award of a contract. However, there will still be information that can be disclosed about the budgets, specifications and selection process even in this case.

You are encouraged to publish OCDS data close to real-time: releasing data as each stage of a contracting process takes place.

This might involve generating output from a range of different systems. Data published from different systems can be tied together by use of a common Open Contracting ID (`ocid`).

## Defining a contracting process

For public procurement OCDS defines a unique contracting process as:

> All the planning, tendering information, awards, contracts and contract implementation information related to a single initiation process.

An initiation process might be a tender, a direct contract award, or a call to award a concession.

## The Open Contracting ID (ocid)

Each unique contracting process needs to be assigned an `ocid`. This is an identifier which can be used to join up data between different stages (as often the data might be stored in different systems).

To make sure the `ocid`s assigned in two different jurisdictions do not clash, publishers need to register an ocid prefix. This can be prepended onto locally generated identifiers, giving a globally unique identifier, and allowing disparate data sources to confidently refer to a unique contracting process.

You can [register your ocid prefix here](../guidance/build).

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

In [Mexico City](http://www.contratosabiertos.cdmx.gob.mx/), an initial mapping identified that identifiers were assigned to each tender process or direct award, using a pattern based on the initials or name of the department involved, a tender or contract number, and the year.

For example:

> OM-DGRMSG-004-13

These identifiers uniquely identify each contracting process. Fields and business processes to capture these identifiers at each contracting process stage were added to the relevant systems.

Mexico City then registered a prefix with the OCDS helpdesk. They have been given the prefix 'ocds-87sd3t' which can be added to their unique process identifiers to give a globally unique ocid.

For example:

> ocds-87sd3t-OM-DGRMSG-004-13

All the award notices, contracts and transactions resulting from the tender with this identifier share this ocid - allowing Mexico City to bring together a complete picture of each contracting process.

</div>

<div class="warning" markdown=1>

<p class="first admonition-title">Note</p>

The `ocid` is case sensitive. Case needs to be used consistently whenever an `ocid` is presented.

</div>

## Mapping your systems

The Open Contracting Data Standard helpdesk provide [a technical assessment template](http://www.open-contracting.org/resources/ocds-technical-assessment-template/) that can be used to identify the different systems involved in managing data on each stage of the contracting process.
