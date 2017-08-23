Milestone Documents
===================

In OCDS 1.1, core support for documents attached to individual milestones was removed from the milestones block to simplify the standard.

This extension re-introduces the ```documents``` block to ```milestones```, providing fields to detail the documents related to each individual milestone.

## Guidance

Publishers should consider that many consuming applications will only look at the ```tender/documents```, ```award/documents```, ```contracts/documents``` and ```contracts/implementation/documents``` section to access and display relevant documentation to users. 

Document titles, document types, and descriptions can be used to indicate to human readers the particular nature of the documents and any milestones they relate to.

However, in cases where it is important to track documents on a milestone-by-milestone basis this extension can be introduced. 

Depending on the nature of the documents, publishers should consider duplicating information in the parent sections documents block also. 

