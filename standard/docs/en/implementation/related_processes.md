# Frameworks and related processses

OCDS defines a contracting process as:

> All the planning, tendering information, awards, contracts and contract implementation information related to a single initiation process.

A contracting process brings together, under a single identifier, the information that users need to answer questions such as:

* Was a contract signed as a result of this tender?
* What was the total value of spending that resulted from this award?
* Was an renewal of this contract signed?

In some cases, complex contracting processes cannot be represented under a single identifier because:

* There are multiple initiation stages: for example, when a framework is setup, and then mini-competitions are used for purchases from the framework;
* The procurement systems through which stages of the process are managed are managed by different bodies, and are not integrated;

There are also cases when users want to know about related, but separate, contracting processes - such as the tender for renewal of a contract, or sub-contracting processes.

The ```relatedProcess``` block can be used in these cases to link together multiple contracting processes. 

## Framework types 

The table below provides a number of examples of when to use related process, and when to keep information within a single contracting process. 

<table>
<thead>
<tr>
<th>Framework type</th>
<th>OCDS approach</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single supplier with direct call-offs</td>
<td><strong>A single contracting process</strong> using award(s) to represent the framework agreement and contract(s) to represent the call-offs.</td>
</tr>
<tr>
<td>Multiple suppliers with direct call offs</td>
<td><strong>A single contracting process</strong> using award(s) to represent the framework agreement and contract(s) to represent the call-offs.</td>
</tr>
<tr>
<td>Multiple suppliers with mini-competitions for call-offs</td>
<td><strong>Multiple contracting processes</strong>: One process using awards to represent suppliers on the framework agreement; Multiple selective or limited processes to represent the mini-competitions linked to the framework agreement via relatedProcess.</td>
</tr>
<tr>
<td>Multiple suppliers with either direct call-offs or mini-competitions</td>
<td><strong>Multiple contracting processes</strong>: One process using awards to represent suppliers on the framework agreement and contract(s) to represent the direct call-offs; Multiple selective or limited processes to represent the mini-competitions linked to the framework agreement via relatedProcess.</td>
</tr>
<tr>
<td>Dynamic Purchasing System</td>
<td><strong>Multiple contracting processes</strong>: One process using awards to represent suppliers joining the DPS. <code>tender/status</code> should be active for the lifetime of the dynamic purchasing system with <code>tender/tenderPeriod</code> and <code>tender/awardPeriod</code> reflecting that suppliers can join the DPS at any time. Multiple selective or limited processes to represent competitions between suppliers on the DPS for individual contracts, linked to the DPS via relatedProcess.</td>
</tr>
</tbody>
</table>