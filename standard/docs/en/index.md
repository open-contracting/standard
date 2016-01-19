Open Contracting Data Standard: Documentation
=============================================

Governments around the world spend an estimated US$9.5 trillion through contracts every year. Yet, contracting information is often unavailable for public scrutiny. 

The Open Contracting Data Standard (OCDS) enables disclosure of data and documents at all stages of the contracting chain. 

OCDS defines a common data model for open data on contracting. It was created to support organisations to increase contracting transparency, and to allow deeper analysis of contracting data by a wide range of users. 

The OCDS approach:

* Publish early, and iterate: improving disclosure step-by-step
* Simple and extensible JSON structure
* Publish data for each step of the contracting chain
* Create summary records for an overall contracting process
* Re-useable objects: organisations, tender information, line-items, amounts, milestones, documents etc.
* Recommended data and documents at basic, intermediate & advanced levels
* Common open data publication patterns 
* Guidance on improving data collection and data quality
* A growing community of users and range of open source tools
* Open governance process: shaping the development of the standard

The Open Contracting Data Standard is stewarded by the [Open Contracting Partnership](http://www.open-contracting.org). 

<!-- Progressive enhancement for documentation slider above. Add a list of images in order that should be associated with the bullet points above. Uses bxSlider and some custom jQuery. Images also need to be in the hidden div block below in order to be copied across to the deployed docs correctly. -->
<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/bxslider/4.2.5/jquery.bxslider.min.css"/>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/bxslider/4.2.5/jquery.bxslider.min.js"></script>
<script type="text/javascript"><!--
images = ['test.png','contracting_process_rc.png'];
$("ul.simple").each(function(key,value) { 
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

The Open Contracting Data Standard is a core product of the [Open Contracting Partnership](http://www.open-contracting.org) (OCP). Version 1.0 of the standard is being developed for the OCP by the [World Wide Web Foundation](http://www.webfoundation.org), through a project supported by the [Omidyar Network](http://www.omidyar.net) and the [World Bank](http://www.worldbank.org).

Lead authors: [Tim Davies](http://www.timdavies.org.uk) ([Web Foundation](http://www.webfoundation.org)) & Sarah Bird ([Aptivate](http://aptivate.org)), with core input from: James McKinney ([Open North](http://opennorth.ca/)), Lindsey Marchessault ([World Bank](http://www.worldbank.org)), Marcela Rozo ([World Bank](http://www.worldbank.org)), Stephen Davenport ([World Bank](http://www.worldbank.org)), Ana Brandusescu, Jose M. Alonso ([Web Foundation](http://www.webfoundation.org)) and Michael Roberts ([Web Foundation](http://www.webfoundation.org)). We extend our thanks to everyone else who has contributed during this project. See the [credits page](../credits) for details of all those involved.


```eval_rst
.. toctree::
   :maxdepth: 2
   :glob:
   :hidden:

   getting_started/index
   schema/index
   implementation/index
   evaluation/index
   support/index

```


Indices and tables
==================

```eval_rst
* :ref:`genindex`
* :ref:`search`
```

