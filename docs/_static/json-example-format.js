/* global $, renderjson */

let groupIndex = 0;

document.querySelectorAll('.expandjson').forEach(function (element) {
  const defaultOpen = []
  let fileClassName
  element.classList.forEach(function (className) {
    if (className.substring(0, 7) === 'expand-' && className.length > 7) {
      defaultOpen.push(className.substring(7))
    }
    if (className.substring(0, 5) === 'file-') {
      fileClassName = className
    }
  })

  let data = JSON.parse(element.textContent)
  // If the jsoninclude directive indexed to a JSON array (a common mistake), only display the first entry.
  if (data.length) {
    data = data[0]
  }

  const replacement = renderjson.set_show_to_level(1).set_max_string_length(100).set_default_open(defaultOpen)(data)
  // element.firstElementChild.replaceWith(replacement) // https://caniuse.com/mdn-api_parentnode_firstelementchild
  element.replaceChild(replacement, element.querySelector('.highlight-json'))

  const container = element.previousElementSibling
  let select
  if (container && container.classList.contains('selection-container')) {
    element.style.display = 'none'
    container.appendChild(element)
    select = container.querySelector('select')
    select.style.display = ''
  } else {
    const div = document.createElement('div')
    element.insertAdjacentElement('beforebegin', div)
    div.className = 'selection-container'
    div.appendChild(element)

    select = document.createElement('select')
    div.insertAdjacentElement('afterbegin', select)
    select.style.display = 'none'
    select.addEventListener('change', function () {
      div.querySelectorAll('.expandjson').forEach(function (sibling) {
        sibling.style.display = 'none'
      })
      div.querySelector(`.${select.value}`).style.display = ''
    })
  }

  const option = document.createElement('option')
  option.value = fileClassName
  option.textContent = fileClassName.replace('file-', '')
  select.append(option)
})
