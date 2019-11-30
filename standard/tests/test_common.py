import os
import re
import time
import warnings

import pytest
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from tests import languages, last_path, test_basic_params, test_navigation_params, test_search_params

cwd = os.getcwd()


def custom_warning_formatter(message, category, filename, lineno, line=None):
    return str(message).replace(cwd + os.sep, '')


warnings.formatwarning = custom_warning_formatter


@pytest.mark.parametrize('lang,text', test_basic_params.items())
def test_basic(browser, server, lang, text):
    browser.get('{}{}'.format(server, lang))
    assert text in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize('lang,regex', test_search_params)
def test_search(browser, server, lang, regex):
    browser.get('{}{}'.format(server, lang))
    search_box = browser.find_element_by_id('rtd-search-form').find_element_by_tag_name('input')
    search_box.send_keys('tender\n')
    time.sleep(2)
    assert re.search(regex, browser.find_element_by_tag_name('body').text)


def test_language_switcher(browser, server):
    if 'localhost' in server:
        pytest.skip()

    browser.get('{}en'.format(server))

    for lang, lang_name in languages.items():
        select = Select(browser.find_element_by_xpath("//select[@name='lang']"))
        select.select_by_visible_text(lang_name)
        assert browser.current_url == '{}{}/'.format(server, lang)
        assert test_basic_params[lang] in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize('lang,link_text', test_navigation_params)
def test_broken_links(browser, server, lang, link_text):
    status_codes = {}
    browser.get('{}{}'.format(server, lang))
    failures = []
    while True:
        for element in browser.find_elements_by_xpath('//*[@href]|//*[@src]'):
            url = element.get_attribute('href') or element.get_attribute('src')

            # Don't test proxied or external URLs.
            if '/review/' in url or 'localhost' not in url:
                continue

            url = re.sub(r'#.*$', '', url)
            if url not in status_codes:
                status_codes[url] = requests.get(url).status_code

            status_code = status_codes[url]
            if status_code != 200:
                failures.append([status_code, url, browser.current_url])

        try:
            # Scroll the link into view, to make it clickable.
            link = browser.find_element_by_link_text(link_text)
            browser.execute_script("arguments[0].scrollIntoView();", link)
            link.click()
        except NoSuchElementException:
            assert browser.current_url.endswith(last_path)
            break

    for status_code, url, referrer in failures:
        warnings.warn('expected 200, got {} for {} linked from {}\n'.format(status_code, url, referrer))
    assert not failures, 'One or more links are broken. See warnings below.'
