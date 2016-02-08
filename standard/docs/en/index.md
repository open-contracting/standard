Open Contracting Data Standard: Documentation
=============================================

Governments around the world spend an estimated US$9.5 trillion through contracts every year. Yet, contracting information is often unavailable for public scrutiny. 

The Open Contracting Data Standard (OCDS) enables disclosure of data and documents at all stages of the contracting process by defining a common data model. It was created to support organisations to increase contracting transparency, and allow deeper analysis of contracting data by a wide range of users.

The OCDS approach:

* Publish early, and iterate: improving disclosure step-by-step
* Simple and extensible JSON structure
* Publish data for each step of the contracting process
* Create summary records for an overall contracting process
* Re-useable objects: organisations, tender information, line-items, amounts, milestones, documents etc.
* Recommended data and documents at basic, intermediate & advanced levels
* Common open data publication patterns 
* Guidance on improving data collection and data quality
* A growing community of users and range of open source tools



<!-- Progressive enhancement for documentation slider above. Add a list of images in order that should be associated with the bullet points above. Uses bxSlider and some custom jQuery. Images also need to be in the hidden div block below in order to be copied across to the deployed docs correctly. -->
<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/bxslider/4.2.5/jquery.bxslider.min.css"/>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/bxslider/4.2.5/jquery.bxslider.min.js"></script>
<script type="text/javascript"><!--
images = ['test.png','contracting_process_rc.png'];
$("ul.simple-REMOVE").each(function(key,value) { 
    if($( this ).children("li").size() == 10) { 
        $( this ).addClass("bxslider");
        for (i = 0; i < images.length; i++) { 
            $( this ).children("li:eq("+i+")").html('<img src="_images/'+images[i]+'" title="'+$( this ).children("li:eq("+i+")").html()+'">');
        }
    }
});
$('.bxslider').bxSlider({
  mode: 'horizontal',
  auto: true,
  captions: true
});
--></script>

<div style="display:none;">
![Test](../../assets/slider/test.png)
</div>




## About

The Open Contracting Data Standard is a core product of the [Open Contracting Partnership](http://www.open-contracting.org) (OCP). 

Version 1.0 of the standard was developed for the OCP by the [World Wide Web Foundation](http://www.webfoundation.org), through a project supported by the [Omidyar Network](http://www.omidyar.net) and the [World Bank](http://www.worldbank.org). Ongoing development is managed by [Open Data Services Co-operative](http://www.opendataservices.coop) under contract to [OCP](http://www.open-contracting.org).

## Support

A [free helpdesk service](support/index.md) is available to support implementation and use of OCDS.


```eval_rst
.. toctree::
   :maxdepth: 2
   :glob:
   :hidden:

   getting_started/index
   schema/index
   implementation/index
   extensions/index
   support/index

```

