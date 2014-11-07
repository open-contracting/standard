##Publishing models
Given the diversity of systems from which contracting data is drawn, we propose that the Open Contracting Data Standard support a range of different publishing models, although always ensuring that it is possible to construct a contracting record, but allowing that the data for this might be provided in a range of different ways. 

Below we outline a number of possible models by which data might be made available. These are suggestions for consultation and we welcome comment on the appropriateness of each model. 

### Contracting release API standard

Releases could be provided through an open REST API. For example, the standard may develop a common API pattern such that URIs such as:

<code>
/open-contracting/{open-contracting-id}/tender 
</code>

<code>
/open-contracting/{open-contracting-id}/award 
</code>

return serialised representations of the relevant releases, and a call to:

<code>
/open-contracting/{open-contracting-id}
</code>

would provide a list of all the releases related to that **open contracting id**. 

This API call would allow parties would to draw upon all the information on a contracting journey to build a full contracting record. 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>Should we look to propose an API standard as part of the version 1.0 Open Contracting Data Standard?</li>
             <li>Should it be possible for publishers to provide only releases, leaving it to third parties to create the contracting record?</li>
         </ul>     
     </div>
</div>

### Abbreviated contracting record
A publisher may provide an abbreviated contracting record which consists only of:

* A unique open contracting identifier
* Meta-data about the publisher providing information
* Last-updated information
* URLs to related releases

Users would then follow these URLs to look up each individual release and to build a contracting record. These URLs may point to static documents, API endpoints or other locations which return machine-readable data for the relevant contracting release. 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>Will all publishers be able to maintain release information at RESTFUL URIs?</li>
             <li>Should it be possible for publishers to provide only releases, leaving it to third parties to create the contracting record?</li>
         </ul>     
     </div>
</div>

### Full contracting record & releases
Publishers build their own **Contracting Records** and keep these updated throughout the contracting journey. 

These records should contain URLs to each of the related releases, allowing third parties to validate the contents of the contracting record.  

A full contracting record may be available as a single record at a specified URL, or as part of a bulk download file. 

### Bulk download
A publisher may provide contracting records and releases packaged together as part of a single file for bulk download, or as a collection of files together in an archive. 

<div class="panel panel-success">
    <div class="panel-heading">
       <h4 class="panel-title"> <span class="glyphicon glyphicon-question-sign"></span> Consultation questions</h3>
     </div>
     <div class="panel-body">
         <ul>
             <li>Should the standard specify maximum file sizes for bulk downloads?</li>
         </ul>     
     </div>
</div>