# Governance

The Open Contracting Data Standard (OCDS) has many stakeholders: governments (procuring entities, monitoring & oversight authorities, project managers and policy makers), the private sector, and civil society organizations. The needs and interests of these stakeholders, as publishers and users of the data, are varied. As OCDS develops over time, with updated versions and new features, it is important that a diverse group of stakeholders are engaged in the process.

This document sets out the revision processes for OCDS.

## Overview

OCDS was initially developed through a year long iterative process, resulting in version 1.0 in November 2014. Over 2015/16 many organisations have been piloting use of the standard. 

In 2016, we are working towards a first revised version of the standard. This is intended to fix a number of bugs identified through wider adoption of the standard over recent months, and will add a number of features which did not make it into 1.0. 

This document outlines a process for management of changes to OCDS during the move from version 1.0 to 1.1. 

Following this revision process, the Open Contracting Partnership will evaluate either:

* Continuing to operate a self-managed revision process;

* Submitting OCDS into a formal standards process, such as W3C community group, OASIS or other body;

We welcome views on this approach of short-term self-managed revisions, followed by exploration of formal standards processes. 

## Stewardship and governance

The [Open Contracting Partnership (OCP)](http://www.open-contracting.org) was established as an independent non-profit in early 2015 and acts as the lead steward of the Open Contracting Data Standard. 

OCP is led by an executive director, and is supported by a multi-stakeholder advisory board with representation from governments, multilateral organisations, academia, NGOs and business. 

As of February 2016, OCP is fiscally hosted by the [Fund for the City of New York](https://www.fcny.org/fcny/) (FCNY). Under the terms of this agreement, Intellectual Property is held by FCNY on behalf of OCP, but will transfer to any future legal entity hosting OCP. 

The OCDS **technical team** work under contract to OCP, under the direction of the OCP Data & Engagement manager, providing a help desk service, and responsible for the day-to-day management of the standard documentation and validation tools. The technical team can be contacted via [data@open-contracting.org](mailto:data@open-contracting.org) 

In the pursuit of a consensus and **community-driven process**, subscribers to the [standard-discuss@open-contracting.org](mailto:standard-discuss@open-contracting.org) (Join by sending an email to [standard-discuss+subscribe@open-contracting.org](standard-discuss+subscribe@open-contracting.org)) discussion list and those watching and engaging with the [standard GitHub repository](https://github.com/open-contracting/standard) should be kept informed at all stages about planned revisions to OCDS, and should be offered clear and timely opportunities to input and comment.

To ensure the relevance, quality and effective implementation of proposed updates to the standard, new version releases will be subjected to a process of **peer review** with invited reviewers from publisher and user communities, and an open review process. 

A lightweight **standard governance working group**, made up of representatives from OCP staff, the multi-stakeholder advisory board, and the technical team will be responsible for giving final approval to formal upgrades of the standard and ensuring the processes in this document have been properly carried out. 

### Intellectual property

The Open Contracting Data Standard is the Intellectual Property of the Open Contracting Partnership. The schema is licensed under the **[Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0)** license, with accompanying documentation under a **[Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/)** where stated. 

Contributors to the standard agree to transfer any copyright in their contributions to the Open Contracting Partnership (via it's fiscal sponsor) through a contributor agreement process, in order that those contributions are held in trust as part of the standard.

No content infringing upon third-party Intellectual Property Rights will be included in the standard. 

## Governance principles

We are committed to the [Open Stand principles](https://open-stand.org/about-us/principles/) for standards development. The Open Contracting Data Standard will be developed with:

* **Due process.** Decisions made with equity and fairness among participants. Through an open process for submitting issues, extensions and requests for updates, no one party will dominate or guide standard development. All processes will be transparent and opportunities will exist to appeal decisions. Processes for periodic standards review and updating are well defined in this document.

* **Broad consensus.** The process will allow for all views to be considered and addressed, such that agreement can be found across a range of interests.

* **Transparency.** We will provide advance public notice of proposed standards development activities, the scope of work to be undertaken, and conditions for participation. Easily accessible records of decisions and the materials used in reaching those decisions will be provided. Public comment periods will be provided before final standards approval and adoption.

* **Balance.** Standards activities will not exclusively dominated by any particular person, company or interest group.

* **Openness.** The Open Contracting Data Standard processes are open to all interested and informed parties.

In the future, the Open Contracting Data Standard may be submitted to a formal standardisation body, such as the World Wide Web Consortium, or OASIS. Before such a decision is made, a model of community-driven governance shall be established based on an open and consensus-based processes for updating the standard.

## Versioning and upgrade process

Over time, changes will be needed to the standard, including addition of new codes and fields, and occasionally involving changes to existing fields and structures. 

The revision process should ensure:

* The consequences of any change for different stakeholders are identified and considered;

* It is clear why changes are needed, and that there is broad support for any proposed changes;

* Changes are easy to identify and are transparent, and publishers, users and intermediaries have clear documentation to allow them to update their data and tools;

Changes to the OCDS schema should be made periodically, with the version number of the standard incremented to indicate that changes have been made, and a change-log maintained. 

### Versions

Distinct **branches** of the standard will be maintained within Github for each version. 

Branches can be in one of two states:

* **Development** - indicated by a -dev suffix (e.g. 1.1-dev)
Both schema and documentation on a development branch can be updated and should only be implemented on an experimental basis.

* **Live** - with no suffix ( e.g. 1.0)
Only documentation updates are permitted on a live branch. All documentation changes must be reviewed to ensure they do not make any changes to the meaning of the standard. 

Semantic Versioning practices will be used to distinguish between:

* **Major versions** which make backwards-incompatible API changes

* **Minor** **versions** which add functionality in a backwards-compatible manner

These are captured by a version number in the format MAJOR.MINOR

## Revision process

To release a new minor or major version upgrade will involve a number of stages outlined in the flowchart below, and described in more depth in the following sections. 

![image alt text](../../../assets/upgrade_process_feb_2016.png)

**General principles:**

* **Publicity:** All stages of the revision process will be announced via the standard-discuss mailing list, and through GitHub issues. These are the formal channels for notification during the process.

* **Consensus:** All processes should aim towards gaining community consensus for changes. 

The technical team are responsible for generating key documentation during the process, but should always be guided by community consensus, submitting all decisions for discussion. 

* **Appeal:** Any party may appeal against decisions made during the process by writing to the standard governance working group (address tbc.). The working group has the authority to reject proposed revisions on the standard in response to appeals. 

### Proposals

Changes to OCDS can be proposed by anyone at any point via the public, online, [standard issue tracker](https://github.com/open-contracting/standard/issues) either as issues for discussion, or pull requests with a clear description of the proposed change.

Contributors are encouraged to raise discussions prior to pull requests to seek consensus on proposed changes.

Changes may be proposed as:

* **Extensions** - which add new features to the standard.

* **Changes** - such as updated field definitions or codelist entries. 

If there are at least two parties interested in using an extension, and following discussion of the extension draft, then it may be displayed in the current version of the documentation as an ‘experimental feature’. 

### Prioritisation

The technical team, with reference to community views, identify change proposals and extensions which should be considered for adoption in the next version of the standard, assigning these to milestones in the issue tracker where they are open for discussion. 

Periodically, at the start of a revision process a cut-off date for proposals will be announced  with at least two weeks notice. After that date a prioritised list of updates is produced. Any new proposed extensions or changes received after this period may not be considered until the next prioritisation phase. 

### Prioritisation review

The list is shared for feedback, with at least a two-week window for discussion.

Based on discussions, a final list is then proposed by the technical team with all the issues that will be taken forward into the rest of the process. A proposals that has made it this far may or may not make it into the final upgrade. As the proposal is worked into final concrete examples and schema changes further issues may arise.

### Development & docs

The technical team, working with community members, will work on a development branch to prepare updates to the schema, documentation and codelists, according to the prioritised list. 

This stage is likely to involve broad community engagement and discussion of specific decisions through GitHub issues. 

At the point where all open issues are suitably addressed, the development branch can be submitted for peer review.

### Peer-review

The updated schema, documentation along with a change log and narrative description of the changes will be released for peer-review.

A group of invited reviewers, representing different stakeholders, and including data publishers and users, will be asked to complete a full review of the changes, and to submit:

* A judgement on whether the overall upgrade, and/or specific changes should be **accepted**, **accepted with minor changes**, **substantially revised**, or **rejected**.

* Comments on each request for revisions or rejection.

All reviews, with reviewer names, will be published. Community members may also submit their own reviews of the whole revision, or specific elements. The minimum period for peer-review is one month. 

### Revisions

The technical team, with reference to the working group as appropriate, should evaluate reviews, and decide whether the whole upgrade, or specific features thereof, need to be revised, rejected or postponed to future processes.

If only minor changes are suggested, then the revised standard can be submitted back to reviewers for a brief review period of at least two weeks.

If major changes are required, then a longer follow up review process of at least one month should be allowed for.

### Release

Once all reviewer comments have been addressed to the satisfaction of the reviewer in question, then the updated version of the standard should be submitted to the **standard governance working group** for final approval, along with a short report of the process. 

Following **working group** approval, the revision branch can be set to live. 

## Deprecation policy 

See https://github.com/open-contracting/standard/issues/189

If a term (a class or property) is scheduled to be renamed or removed from the specification as a result of the revision process, the next minor release of the specification must [deprecate](https://en.wikipedia.org/wiki/Deprecation) the term within the schema, and the following major release must rename or remove the term from the schema, making the term obsolete. Implementations may use deprecated terms, but will receive warnings from the OCDS validator described below. Implementations may not use obsolete terms, and will receive errors from the OCDS validator.

## Support policy

Support will be offered for one prior version of the standard. Support for any earlier versions than this will be ended when a new version is released. 

For example, when 1.1 is the latest release, 1.0 will be supported in the validator and other tooling. When 1.2 is released, support for 1.0 will end.

Publishers are encouraged to review each new version when it released, and to consider how they might adopt new features. 

Publishers should aim to move to a new **major** version within 18 months of its release. 

## Definitions & procedures

**Stakeholder**

Anyone who is a current or potential publisher or user of the standard can be considered a stakeholder. When engaging with stakeholders, attention should be paid to representation of both publishers and users; representation of public and private sectors and civil society; and broad geographical representation.

**Consensus**

"The principle of consensus has its origins in the desire to achieve the general acceptance and application of a Standard within its intended sphere of influence. This entails trying to ensure that the interests of all those likely to be affected by it are taken into account, and that individual concerns are carefully and fairly balanced against the wider public interest." [BSI, 2012](http://www.bsigroup.com/Documents/about-bsi/NSB/BSI-pocket-guide-to-standards-development-UK-EN.pdf) 

   

