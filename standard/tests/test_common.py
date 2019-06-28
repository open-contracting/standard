# Update this file from a profile with:
# curl https://raw.githubusercontent.com/open-contracting/standard_profile_template/master/tests/test_common.py -o tests/test_common.py # noqa
import re
import time

import pytest
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from tests import languages, test_basic_params, test_search_params


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


@pytest.mark.parametrize('lang', list(languages))
def test_broken_links(browser, server, lang):
    referrer = ''
    hrefs = set()
    browser.get('{}{}'.format(server, lang))
    while True:
        for link in browser.find_elements_by_partial_link_text(''):
            href = re.sub(r'#.*$', '', link.get_attribute('href'))

            # Don't test proxied or external URLs.
            if '/review/' in href or 'localhost' not in href:
                continue
            # If the URL, without an anchor, has already been visited, don't test it again.
            if href in hrefs:
                continue
            # Keep track of which pages have been tested.
            hrefs.add(href)

            response = requests.get(href)
            assert response.status_code == 200, 'expected 200, got {} for {} linked from {}'.format(
                response.status_code, href, referrer)

        try:
            # Scroll the link into view, to make it clickable.
            link = browser.find_element_by_link_text('Next')
            referrer = link.get_attribute('href')
            browser.execute_script("arguments[0].scrollIntoView();", link)
            link.click()
        except NoSuchElementException:
            break
