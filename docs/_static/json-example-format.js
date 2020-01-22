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
                       $(this).siblings(".expandjson").hide();
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
