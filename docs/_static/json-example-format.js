/* global $, renderjson */

$('.expandjson').each(function () {
  const classList = $(this).attr('class').split(/\s+/)
  const expand = []
  let filename
  classList.forEach(function (item) {
    if (item.indexOf('expand') === 0) {
      expand.push(item.replace('expand-', ''))
    }
    if (item.indexOf('file') === 0) {
      filename = item
    }
  })
  const jsontext = $(this).text().trim()
  let json = JSON.parse(jsontext)
  if (json.length) {
    json = json[0]
  }
  $(this).html(renderjson.set_show_to_level(1).set_max_string_length(100).set_default_open(expand)(json))
  if ($(this).siblings('.selection-container').length === 0) { // NEED TO FIX THE CODE HERE. MOVE THINGS INTO THE PARENT CLASS CORRECTLY!
    const id = Math.floor(5 * (Math.random() % 1))
    $(this).wrap("<div class='selection-container'></div>")
    $(this).parent().prepend(
      $("<select name='select-" + id + "'></select>")
        .change(function () {
          $(this).siblings('.expandjson').hide()
          $(this).siblings('.' + $(this).val()).show()
        }))
    $(this).siblings('select').append($('<option></option>').attr('value', filename).text(filename.replace('file-', '')))
  } else {
    const container = $(this).siblings('.selection-container')
    $(this).detach().appendTo(container)
    $(this).siblings('select').append($('<option></option>').attr('value', filename).text(filename.replace('file-', '')))
    $(this).hide()
  }
})
