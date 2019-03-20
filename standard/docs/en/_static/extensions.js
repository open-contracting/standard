$(function () {
  // FYI: extensionlist appears many times on /schema/reference
  if ($('.extension_list').length) {
    var language = location.pathname.split('/')[2];

    // A blank definition list for a community extension.
    var template = '<dl><dt><a class="reference external" href=""></a></dt><dd></dd></dl>';

    // Append an empty list for community extensions.
    $('.extension_list p.last').after('<br><dl class="docutils hide community-list"></dl>').wrapInner('<small></small>');

    // Get the community extensions to add to the documentation.
    $.ajax({
      'url': 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/build/extensions.json',
      'crossDomain': true,
      'dataType': 'json'
    }).done(function (data) {
      var communityExtensions = $.grep(data.extensions, function (i, extension) {
        return !extension.core;
      });

      // Add community extensions.
      $.each(communityExtensions, function (i, extension) {
        var extensionName = extension.name[language] || extension.name['en'];
        var extensionDescription = extension.description[language] || extension.description['en'];
        var extensionListId = '#extensionlist-' + extension.category;
        var $item = $(template);

        $item.find('a').attr('href', extension.documentation_url).text(extensionName);
        $item.find('dd').text(extensionDescription);
        $(extensionListId).find('.community-list').append($item.html()).removeClass('hide');
        $(extensionListId).find('p.last').removeClass('hide');
      });

      // Remove empty extension lists.
      $('.extension_list').each(function () {
        var $this = $(this);
        if (!$this.find('a').attr('href')) {
          $this.remove();
        }
      });
    });
  }
});
