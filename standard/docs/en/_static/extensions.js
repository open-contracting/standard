
jQuery(function () {
  var language = location.pathname.split('/')[2]
  jQuery.ajax({
    "url": "http://standard.open-contracting.org/extension_registry/master/extensions.js", 
    "jsonpCallback": "extensions_callback",
    "crossDomain": true,
    "dataType": "jsonp"
  }).done(function(data) {
    jQuery(".extension_list").each(function (index, item) {
      var $item = jQuery(item);
      var category = $item.attr('id').split("-")[1];
      var anyExtensions = false
      var $communityExtensionList

      jQuery.each(data.extensions, function (index, extension) {
        if (extension.core) {
          return
        }
        if (extension.category != category) {
          return
        }
        if (!anyExtensions) {
          anyExtensions = true
          $communityExtensionList = $('<dl>').addClass("docutils")
          $item.append($communityExtensionList)
          $item.find('.hide').css({"display": "block"});
        }
        var $dt = $('<dt>')
        $dta = $('<a>').attr({"href": extension.documentation_url, "class": "reference external"}).text(extension.name[language] || extension.name["en"])
        $dt.append($dta)
        $communityExtensionList.append($dt)

        var $dd = $('<dd>').text(extension.description[language] || extension.description.en)
        $communityExtensionList.append($dd)
      })
    })
    template = '<div class="section" id="example">' + 
               '<h2></h2>' +
               '<p><input class="extension extension_url" value="" READONLY/> <a class="documentation reference external"></a></p>' + 
               '<p class="description"></p>' +
               '</div>'
    template_anchor = '<a class="headerlink" href="#example" title="Permalink to this headline">¶</a>'

    var documentation_text = jQuery(jQuery('#community-extensions').find("p")[1]).text()
    jQuery(jQuery('#community-extensions').find("p")[1]).remove()

    //still 1 as previous has been removed
    var repository_text = jQuery(jQuery('#community-extensions').find("p")[1]).text()
    jQuery(jQuery('#community-extensions').find("p")[1]).remove()

    jQuery.each(data.extensions, function (index, extension) {
      if (extension.core) {
        return
      }
      var new_item = jQuery(template);
      var new_anchor = jQuery(template_anchor).attr({"href": "#" + (extension.name[language] || extension.name["en"])});
      new_item.attr({"id": extension.name.en})
              .find("h2")
              .text(extension.name[language] || extension.name["en"])
              .append(new_anchor);
      new_item.find(".description").text(extension.description[language] || extension.description.en)
      new_item.find(".documentation").attr({"href": extension.documentation_url}).text(documentation_text)
      new_item.find(".extension_url").attr({"value": extension.url + "extension.json"})

      jQuery('#community-extensions').append(new_item)
    })
  });

  // last-child contains the url for the extension
  $('.extension-selector-table th:last-child').hide();
  $('.extension-selector-table td:last-child').hide();
  $('.extension-selector-table td:first-child').addClass('extension-selector');

  $('.extension-selector-table td:first-child').click(function (){
      var $this = $(this);
      var extensions = $('.highlight-json pre span:nth-child(3)').next().text();
      console.log(extensions.substring(1, extensions.length-1));
      extensions = JSON.parse(extensions.substring(1, extensions.length-1))
      var url = $this.parent().find('a').text()
      var url_index = extensions.indexOf(url);

      if ($this.hasClass('extension-selected')) {
        extensions.splice(url_index, 1);
        $this.removeClass('extension-selected')
        
      } else {
        extensions.push(url);
        $this.addClass('extension-selected')
      }

      $('.highlight-json pre span:nth-child(3)').next().text(':' + JSON.stringify(extensions) + ',');
  });

});
