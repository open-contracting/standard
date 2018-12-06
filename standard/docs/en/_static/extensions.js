$(function () {
  // FYI:
  // - extensionselectortable appears once on /extensions/community and twice on /extensions
  // - extensionlist appears once on /extensions/party_details and many times on /schema/reference

  var language = location.pathname.split('/')[2];
  var isCommunityExtensionsPage = window.location.pathname.indexOf('/extensions/community/') >= 0;

  // extensionlist directive: A blank definition list for a community extension.
  var template = '<dl><dt><a class="reference external" href=""></a></dt><dd></dd></dl>';

  // extensionlist directive: Append an empty list for community extensions.
  $('.extension_list p.last').after('<br><dl class="docutils hide community-list"></dl>').wrapInner('<small></small>');

  // extensionselectortable directive: The "Extension" column values must be transformed to links, e.g.
  // "Bid statistics and details::https://github.com/open-contracting/ocds_bid_extension"
  // Get the table's data rows, which will only be core extensions.
  $('.extension-selector-table td:nth-child(2)').each (function () {
    var $this = $(this);
    var textAndUrl = $this.text().split('::');
    var htmlString = '<a href="' + textAndUrl[1] + '">' + textAndUrl[0] + '</a>';
    $this.html(htmlString);
  });

  // Get the community extensions to add to the documentation.
  $.ajax({
    'url': 'https://raw.githubusercontent.com/open-contracting/extension_registry/master/build/extensions.json',
    'crossDomain': true,
    'dataType': 'json'
  }).done(function (data) {
    var communityExtensions = $.grep(data.extensions, function (i, extension) {
      return !extension.core;
    });

    // On the extensions page, community extensions go in the second table.
    var tableIndex = isCommunityExtensionsPage ? 0 : 1;
    var $table = $($('.extension-selector-table')[tableIndex]);
    var $template = $($table.find('.row-even')).detach();

    $.each(communityExtensions, function (i, extension) {
      var extensionName, extensionDescription, $item;
      var extensionListId, abbreviatedUrl, category;

      extensionName = extension.name[language] || extension.name['en'];
      extensionDescription = extension.description[language] || extension.description['en'];

      // extensionlist directive: Add community extensions.
      extensionListId = '#extensionlist-' + extension.category;
      $item = $(template);
      $item.find('a').attr('href', extension.documentation_url).text(extensionName);
      $item.find('dd').text(extensionDescription);
      $(extensionListId).find('.community-list').append($item.html()).removeClass('hide');
      $(extensionListId).find('p.last').removeClass('hide');

      // extensionselectortable: Add community extensions.
      $item = $template.clone().removeClass('row-even');

      abbreviatedUrl = extension.url.split('/').slice(3).join('/') + 'extension.json';
      $item.find('td a').attr('href', extension.documentation_url).text(extensionName);
      $item.find('td:nth-child(3)').text(extensionDescription);
      $item.find('td:nth-child(4)').text(extension.category);
      $item.find('td:last-child').html('<a href="' + extension.url + 'extension.json">' + abbreviatedUrl + '</a>');

      // On the community extensions page, the category is moved.
      if (isCommunityExtensionsPage) {
        category = $item.find('td:nth-child(4)').detach().text();
        $item.find('td:nth-child(2) a').after('<br><em><small>' + category + '<small></em>');
      }

      $item.addClass(i % 2 ? 'row-odd' : 'row-even');
      $table.find('tbody').append($item);
    });

    // extensionlist directive: Remove empty extension lists.
    $('.extension_list').each(function () {
      var $this = $(this);
      if (!$this.find('a').attr('href')) {
        $this.remove();
      }
    });

    // extensionselectortable directive: Change the table layout on the community extensions page.
    if (isCommunityExtensionsPage) {
      // Don't apply the fake checkboxes in the next section.
      $table.removeClass('extension-selector-table');
      // Remove the fake checkboxes' header.
      $table.find('tr th:first-child').remove();
      // Remove the fake checkboxes' cells.
      $table.find('tr td:first-child').remove();
      // Remove the category column.
      $table.find('tr th:nth-child(3)').remove();
      // Allow breaking of URLs at any character.
      $table.find('tr td:last-child').css('word-break', 'break-all');
    }

    // extensionselectortable directive: Add fake checkboxes on the extensions page.
    $('.extension-selector-table td:first-child').addClass('extension-selector').click(function () {
        var $this = $(this);
        var url = $this.parent().find('td:last-child a').attr('href');
        var $extensions = $('.highlight-json pre span:nth-child(3)').next();
        var extensions = $extensions.text();

        // Remove the colon and comma and parse the array.
        extensions = JSON.parse(extensions.substring(1, extensions.length - 1));

        if ($this.hasClass('extension-selected')) {
          extensions.splice(extensions.indexOf(url), 1);
          $this.removeClass('extension-selected');
        } else {
          extensions.push(url);
          $this.addClass('extension-selected');
        }

        $extensions.text(':' + JSON.stringify(extensions) + ',');
    });
  });
});
