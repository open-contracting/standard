/* global XMLHttpRequest, location */

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
