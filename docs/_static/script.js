/* global XMLHttpRequest, location, renderjson */

var pathComponents = window.location.pathname.split('/')
if (pathComponents[pathComponents.length - 2] == 'codelists') {
  document.querySelector('.wy-nav-content').style.maxWidth = 'none';
}

// FYI: extensionlist appears many times on /schema/reference/
if (document.querySelector('.extension_list')) {
  const language = location.pathname.split('/')[2]

  // Append an empty list for community extensions.
  document.querySelectorAll('.extension_list .hide').forEach(element => {
    const dl = document.createElement('dl')
    dl.className = 'simple community-list hide'
    element.insertAdjacentElement('afterend', dl)
    element.innerHTML = `<small>${element.innerHTML}</small>`
  })

  // Get the community extensions to add to the documentation.
  const request = new XMLHttpRequest()
  request.open('GET', 'https://raw.githubusercontent.com/open-contracting/extension_registry/main/build/extensions.json')
  request.responseType = 'json'

  request.onload = () => {
    if (request.status >= 200 && request.status < 400) {
      // Add community extensions.
      request.response.extensions.forEach(extension => {
        if (!extension.core) {
          const div = document.getElementById(`extensionlist-${extension.category}`)
          if (div) {
            div.querySelector('.community-list').insertAdjacentHTML('beforeend', `
              <dt>
                <a class="reference external" href="${extension.documentation_url}">
                  ${extension.name[language] || extension.name.en}
                </a>
              </dt>
              <dd>
                ${extension.description[language] || extension.description.en}
              </dd>
            `)
            div.querySelectorAll('.hide').forEach(element => {
              element.classList.remove('hide')
            })
          }
        }
      })

      // Remove empty extension lists.
      document.querySelectorAll('.extension_list').forEach(element => {
        if (!element.querySelector('a')) {
          element.remove()
        }
      })
    }
  }

  request.send()
}

document.querySelectorAll('.expandjson').forEach(element => {
  const defaultOpen = []
  let fileClassName
  element.classList.forEach(className => {
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
    // Hide additional examples.
    element.style.display = 'none'
    container.appendChild(element)

    // Display the select element if there are multiple options.
    select = container.querySelector('select')
    select.style.display = ''
  } else {
    const div = document.createElement('div')
    element.insertAdjacentElement('beforebegin', div)
    div.className = 'selection-container'
    div.appendChild(element)

    select = document.createElement('select')
    div.insertAdjacentElement('afterbegin', select)

    // Hide the select element if there is one option.
    select.style.display = 'none'
    select.addEventListener('change', () => {
      div.querySelectorAll('.expandjson').forEach(child => {
        child.style.display = 'none'
      })
      div.querySelector(`.${select.value}`).style.display = ''
    })
  }

  const option = document.createElement('option')
  option.value = fileClassName
  option.textContent = fileClassName.replace('file-', '')
  select.appendChild(option)
})
