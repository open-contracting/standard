
$(function () {
  var language = location.pathname.split('/')[2];
  // Core extensions only
  $('.extension-selector-table td:nth-child(2)').each(function() {
    var $this = $(this);
    var splitNameDocURL = $this.text().split('::');
    var cellContent = '<a href="' + splitNameDocURL[1] + '">' + splitNameDocURL[0] + '</a>';
    $this.html(cellContent);
  });

  $.ajax({
    "url": "http://standard.open-contracting.org/extension_registry/master/extensions.js", 
    "jsonpCallback": "extensions_callback",
    "crossDomain": true,
    "dataType": "jsonp"
  }).done(function(data) {
      var isCommunityPage = window.location.pathname.indexOf('/extensions/community/') >= 0;
      var $table =isCommunityPage ? $($('.extension-selector-table')[0]) : $($('.extension-selector-table')[1]);
      var row  = $($table.find('.row-even')).detach();
      var isEven = true;
      var rowClass
      var $rowClone;
      var extensionLink;
      var extensionLinkText;

      $.each(data.extensions, function (index, extension) {
        if (!extension.core) {
          rowClass = isEven ? 'row-even' : 'row-odd';
          $rowClone = $(row).clone();
          extensionLinkText = extension.url.split('/').slice(3.6).join('/') + 'extension.js';
          extensionLink = '<a href="' + extension.url + 'extension.json' + '">' + extensionLinkText + '</a>';
          
          $rowClone.find('td a').attr('href', extension.documentation_url);
          $rowClone.find('td a').text(extension.name[language] || extension.name['en']);
          $rowClone.find('td:nth-child(3)').text(extension.description[language] || extension.description['en']);
          $rowClone.find('td:nth-child(4)').text(extension.category);
          $rowClone.find('td:last-child').html(extensionLink);
          
          if (isCommunityPage) {
            var category = $($rowClone.find('td:nth-child(4)').detach()).text();
            $rowClone.find('td:nth-child(2) a').after('<br><em><small>' + category + '<small></em>');
          }
          
          $rowClone.wrap('<tr class="' + rowClass + '"></tr>');
          $table.find('tbody').append($rowClone);
          isEven = !isEven;
        }
      });
      if (isCommunityPage) {
        $table.removeClass('extension-selector-table');
        $table.find('tr th:first-child').remove();
        $table.find('tr td:first-child').remove();
        $table.find('tr th:nth-child(3)').remove();
        $table.find('tr td:last-child').css('word-break', 'break-all');
      }
      //  Fake checkbox in ExtensionSelectorTable
      $('.extension-selector-table td:first-child').addClass('extension-selector');
      $('.extension-selector-table td:first-child').click(function (){
          var $this = $(this);
          var extensions = $('.highlight-json pre span:nth-child(3)').next().text();
          extensions = JSON.parse(extensions.substring(1, extensions.length-1));
          var url = $this.parent().find('td:last-child a').attr('href');
          console.log(url);
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
});
