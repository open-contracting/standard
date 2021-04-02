"""
This script implements the following policy:

"Minor, non-normative, documentation updates will be translated promptly, but may not always be translated before the
updates are released. The documentation will clearly display when the English documentation is 'ahead' of translations
for a particular version."

https://standard.open-contracting.org/1.1/en/governance/#translation-and-localization-policy
"""

import gettext
import os

import lxml.etree
import lxml.html
import requests
from babel.messages.pofile import read_po
from docutils.utils import relative_path

from helper import base_dir

localedir = os.path.join(base_dir, 'docs', 'locale')
base_url = 'https://standard.open-contracting.org/1.1'
supported_translations = ['es', 'fr']
excluded = ('.doctrees', '_downloads', '_images', '_sources', '_static', 'codelists', 'genindex', 'search')


def add_translation_notes():
    for language in supported_translations:
        build_dir = os.path.join(base_dir, 'build', language)
        language_dir = os.path.join(localedir, language, 'LC_MESSAGES')

        for root, dirs, files in os.walk(build_dir):
            # Skip Sphinx directories.
            for directory in excluded:
                if directory in dirs:
                    dirs.remove(directory)

            if root == build_dir:
                continue

            for name in files:
                # See `sphinx.transforms.i18n.Locale.apply()`.
                # https://github.com/sphinx-doc/sphinx/blob/v2.2.1/sphinx/transforms/i18n.py
                source = os.path.join(root, os.path.dirname(name))
                domain = relative_path(build_dir, source)

                path = os.path.join(language_dir, domain, 'index.po')
                if not os.path.isfile(path):
                    path = os.path.join(language_dir, '%s.po' % domain)
                if not os.path.isfile(path):
                    add_translation_note(os.path.join(root, name), language, domain)
                    continue

                # Check the PO files, because Babel sets the msgstr to the msgid if the msgstr is missing.
                with open(path) as f:
                    for message in read_po(f):
                        if not message.string:
                            add_translation_note(os.path.join(root, name), language, domain)
                            break


def add_translation_note(path, language, domain):
    with open(path) as f:
        document = lxml.html.fromstring(f.read())

    translator = gettext.translation('notes', localedir, languages=[language])
    _ = translator.gettext

    pattern = '{}/{{}}/{}/'.format(base_url, domain)
    response = requests.get(pattern.format(language))

    # If it's a new page, add the note to the current version of the page.
    if response.status_code == 404:
        message = _('This page was recently added to the <a href="%(url)s">English documentation</a>. '
                    'It has not yet been translated.')

    # If it's an existing page, add the note the last version of the page.
    else:
        response.raise_for_status()
        xpath = '//div[@itemprop="articleBody"]'

        replacement = lxml.html.fromstring(response.content).xpath(xpath)[0]
        replacement.make_links_absolute('{}/{}'.format(base_url, language))

        # Remove any existing translation notes.
        parent = replacement.xpath('//h1')[0].getparent()
        for div in replacement.xpath('//h1/following-sibling::div[@class="admonition note"]'):
            parent.remove(div)

        parent = document.xpath(xpath)[0].getparent()
        parent.getparent().replace(parent, replacement)

        message = _('This page was recently changed in the <a href="%(url)s">English documentation</a>. '
                    'The changes have not yet been translated.')

    template = '<div class="admonition note"><p class="first admonition-title">%(note)s</p><p class="last">' \
               '%(message)s</p></div>'

    document.xpath('//h1')[0].addnext(lxml.etree.XML(template % {
        'note': _('Note'), 'message': message % {'url': pattern.format('en')}}))

    with open(path, 'wb') as f:
        f.write(lxml.html.tostring(document, encoding='utf-8'))


if __name__ == '__main__':
    add_translation_notes()
