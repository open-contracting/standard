jQuery(function () {
  jQuery.ajax({
    "url": "https://open-contracting.github.io/extension_registry/extensions.js", 
    "jsonpCallback": "extensions_callback",
    "crossDomain": true,
    "dataType": "jsonp"
  }).done(function(data) {
    jQuery(".extension_list").each(function (index, item) {
      var $item = jQuery(item);
      var category = $item.attr('id').split("-")[1];
      var anyExtensions = false
      var $commuityExtensionList

      jQuery.each(data.extensions, function (index, extension) {
        if (extension.core) {
          return
        }
        //if (extension.category != category) {
        //  return
        //}
        if (!anyExtensions) {
          anyExtensions = true
          $commuityExtensionList = $('<dl>').addClass("docutils")
          $item.append($commuityExtensionList)
          $item.find('.hide').css({"display": "block"});
        }
        var $dt = $('<dt>')
        console.log(extension)
        $dta = $('<a>').attr({"href": extension.documentaion_url, "class": "reference external"}).text(extension.name.en)
        $dt.append($dta)
        $commuityExtensionList.append($dt)

        var $dd = $('<dd>').text(extension.description.en)
        $commuityExtensionList.append($dd)
        

      })
    })
  })

})
