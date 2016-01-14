## Building Blocks

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

### Sections and structure

An OCDS document is made up of a number of sections. In the procurement case, the main sections are:

* **Meta-data** - contextual information about each release of data;
* **buyer** - information about the key contracting party;
* **planning** - information about the goals, budgets and projects a contracting process relates to;
* **tender** - information about how a tender will take place, or has taken place;
* **awards** - information on awards made as part of a contracting process;
* **contract** - information on contracts signed as part of a contracting process;
  * **implementation** - information on the progress of each contract towards completion.

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
            "buyer": {},
            "planning": {},
            "tender": {},
            "awards": [ {} ],
            "contracts":[ {
                "implementation":{}
            }]
        }
```

<div class="example hint" markdown=1>
    
<p class="first admonition-title">Note</p>
Awards and contracts are arrays of objects, whereas tender is an object. This is because of a contracting process has a single initiation stage, but can result in multiple awards and contracts. 

</div>

### Building blocks and fields

The OCDS schema sets out the fields that should be included in each section, making use of simple re-usable building blocks to represent data. 

For example, common building blocks are provided for:

* **Organizations** 
* **Amounts** 
* **Items**
* **Time periods**
* **Documents** 
* **Milestones**

#### Examples

```eval_rst

.. jsoninclude:: docs/en/examples/record.json
   :jsonpointer: /records/0/compiledRelease/buyer
   :expand: identifier, address, contactPoint
   :title: organization

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

#### Using building blocks

These building blocks may be used in various different sections. For example, **items** can occur in tender (to indicate the items that a buyer wishes to buy), in an award object (to indicate the items that an award has been made for) and in a contract object (to indicate the items listed in the contract). 

In addition to these building blocks, the OCDS schema sets out the specific ways they can be used in each section, and describes a number of additional fields that can appear in specific section. For example, fields for:

* ```titles``` and ```descriptions``` of tenders, awards and contracts
* ```procurementMethod```
* ```awardCriteria```
* ```submissionMethod```
* etc.

Many of these fields make use of lightweight codelists provided by OCDS. 


### Codelists

OCDS defines two kinds of codelist:

* **Closed codelists** provide a fixed list of values. When using a field with a closed codelist, publishers must use an option from the published lists. This supports the global comparability of OCDS data on key dimensions.

* **Open codelists** provide recommended values. However, publishers can suggest amendments to these codelists, or provide their own extended values prefixed with x_.

<table width="100%">
<tr>
<td valign="top" width="50%" style="padding:10px;" markdown=1>

**Open Codelists**

* Item Classification Scheme
* Organization Identifier Scheme
* Document Type
* Award Criteria
* Submission Method

</td>
<td valign="top" width="50%" style="padding:10px;" markdown=1>

**Closed Codelists**

* Release Tag
* Initiation Type
* Method
* Tender Status
* Award Status
* Contract Status
* Milestone Status
* Currency

</td>
</tr>
</table>


Codelist values are case sensitive strings. OCDS publish labels for many codes in English and Spanish (TODO - CONFIRM). 

Publishers should map their existing classification systems to OCDS codes wherever possible. Many closed codelist fields are paired with a detail field where more detailed classification information can be provided. 

<div class="example hint" markdown=1>

<p class="first admonition-title">Worked Example</p>

In the EU, contracts can be initiated through a number of different procedures including:

* Open procedure;
* Restricted procedure; 
* Competitive procedure with negotiation; 
* Competitive dialogue; and
* Innovation partnership

However, to support comparison across continents, the main OCDS procurement method code list is a closed codelist with three values based on [GPA definitions](http://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm):

* open
* selective
* limited

To publish OCDS data, an EU publisher with data categorised by EU procedures should map the longer list of procedures to the narrower OCDS codelist and provide the codelist value in the ```procurementMethod``` field. They can then provide the more detailed procedure type in an extended ```procurementMethodDetails``` field.

For an Open Procedure, when a free-text justification of why the procedure was chosen is available, this would end up as:

```json
{
    "procurementMethod":"open",
    "procurementMethodDetails":"Open Procedure",
    "procurementMethodRationale":"To maximise competition."
    
}
```

</div>




<style>
    pre.renderjson { overflow: scroll; font-size:smaller; border: 1px solid grey;}
    .renderjson a { text-decoration: none; }
    .renderjson .disclosure { color: crimson; font-size: 150%; }
    .renderjson .syntax { color: grey; }
    .renderjson .string { color: darkred; }
    .renderjson .number { color: darkcyan; }
    .renderjson .boolean { color: blueviolet; }
    .renderjson .key    { color: darkblue; }
    .renderjson .keyword { color: blue; }
    .renderjson .object.syntax { color: lightseagreen; }
    .renderjson .array.syntax  { color: orange; }
  </style>
  <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
  <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
  <script type="text/javascript" defer><!--
  var module;(module||{}).exports=renderjson=function(){function n(i,c,f,y,_,d){var p=f?"":c,g=function(n,o,i,c,f){var _,d=a(c),g=function(){_||e(d.parentNode,_=r(f(),u(l.hide,"disclosure",function(){_.style.display="none",d.style.display="inline"}))),_.style.display="inline",d.style.display="none"};e(d,u(l.show,"disclosure",g),t(c+" syntax",n),u(o,null,g),t(c+" syntax",i));var h=e(a(),s(p.slice(0,-1)),d);return y>0&&g(),h};return null===i?t(null,p,"keyword","null"):void 0===i?t(null,p,"keyword","undefined"):"string"==typeof i&&i.length>_?g('"',i.substr(0,_)+" ...",'"',"string",function(){return e(a("string"),t(null,p,"string",JSON.stringify(i)))}):"object"!=typeof i?t(null,p,typeof i,JSON.stringify(i)):i.constructor==Array?0==i.length?t(null,p,"array syntax","[]"):g("["," ... ","]","array",function(){for(var r=e(a("array"),t("array syntax","[",null,"\n")),o=0;o<i.length;o++)e(r,n(i[o],c+"    ",!1,y-1,_,d),o!=i.length-1?t("syntax",","):[],s("\n"));return e(r,t(null,c,"array syntax","]")),r}):o(i)?t(null,p,"object syntax","{}"):g("{","...","}","object",function(){var r=e(a("object"),t("object syntax","{",null,"\n"));for(var o in i)var u=o;var f=Object.keys(i);d&&(f=f.sort());for(var p in f){var o=f[p];e(r,t(null,c+"    ","key",'"'+o+'"',"object syntax",": "),n(i[o],c+"    ",!0,l.default_open.indexOf(o)>-1?y+1:y-1,_,d),o!=u?t("syntax",","):[],s("\n"))}return e(r,t(null,c,"object syntax","}")),r})}var t=function(){for(var n=[];arguments.length;)n.push(e(a(Array.prototype.shift.call(arguments)),s(Array.prototype.shift.call(arguments))));return n},e=function(){for(var n=Array.prototype.shift.call(arguments),t=0;t<arguments.length;t++)arguments[t].constructor==Array?e.apply(this,[n].concat(arguments[t])):n.appendChild(arguments[t]);return n},r=function(n,t){return n.insertBefore(t,n.firstChild),n},o=function(n){for(var t in n)if(n.hasOwnProperty(t))return!1;return!0},s=function(n){return document.createTextNode(n)},a=function(n){var t=document.createElement("span");return n&&(t.className=n),t},u=function(n,t,e){var r=document.createElement("a");return t&&(r.className=t),r.appendChild(s(n)),r.href="#",r.onclick=function(){return e(),!1},r},l=function i(t){var r=e(document.createElement("pre"),n(t,"",!1,i.show_to_level,i.max_string_length,i.sort_objects));return r.className="renderjson",r};return l.set_icons=function(n,t){return l.show=n,l.hide=t,l},l.set_show_to_level=function(n){return l.show_to_level="string"==typeof n&&"all"===n.toLowerCase()?Number.MAX_VALUE:n,l},l.set_max_string_length=function(n){return l.max_string_length="string"==typeof n&&"none"===n.toLowerCase()?Number.MAX_VALUE:n,l},l.set_sort_objects=function(n){return l.sort_objects=n,l},l.set_show_by_default=function(n){return l.show_to_level=n?Number.MAX_VALUE:0,l},l.set_default_open=function(n){return l.default_open=n?n:[],l},l.set_icons("⊕","⊖"),l.set_show_by_default(!1),l.set_sort_objects(!1),l.set_max_string_length("none"),l.set_default_open([]),l}();
  $( document ).ready(function() {
      $(".expandjson").each(function(){
       classList = $(this).attr("class").split(/\s+/);
       expand = []
       $.each(classList, function(index, item) {
         if (item.indexOf('expand') === 0) {
           expand.push(item.replace('expand-',''))
         }
         if (item.indexOf('file') === 0) {
           filename = item
         }
       });
       jsontext = $(this).text().trim()
       json = JSON.parse(jsontext)
       if(json.length) {
           json = json[0]
       }
       $(this).html(renderjson.set_show_to_level(1).set_max_string_length(100).set_default_open(expand)(json))
       if($(this).siblings(".selection-container").length === 0) { // NEED TO FIX THE CODE HERE. MOVE THINGS INTO THE PARENT CLASS CORRECTLY!
           id = Math.floor(5 * (Math.random() % 1));
           $(this).wrap("<div class='selection-container'></div>")
           $(this).parent().prepend(
               $("<select name='select-"+id +"'></select>")
               .change(function(){ 
                    $(this).siblings(".highlight-json").hide();
                    $(this).siblings("."+ $(this).val()).show();
                }))
           $(this).siblings("select").append($("<option></option>").attr("value",filename).text(filename.replace("file-",""))) 
       } else {   
           container = $(this).siblings(".selection-container")
           $(this).detach().appendTo(container)
           $(this).siblings("select").append($("<option></option>").attr("value",filename).text(filename.replace("file-",""))) 
           $(this).hide()
       }
    });
});
--></script>