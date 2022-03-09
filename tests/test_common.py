import os
import re
import time
import warnings

import pytest
from selenium.webdriver.support.ui import Select

from tests import languages, test_basic_params, test_search_params

cwd = os.getcwd()


def custom_warning_formatter(message, category, filename, lineno, line=None):
    return str(message).replace(cwd + os.sep, '')


warnings.formatwarning = custom_warning_formatter


@pytest.mark.parametrize('lang,text', test_basic_params.items())
def test_basic(browser, server, lang, text):
    browser.get(f'{server}{lang}')
    assert text in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize('lang,regex', test_search_params)
def test_search(browser, server, lang, regex):
    browser.get(f'{server}{lang}')
    search_box = browser.find_element_by_id('rtd-search-form').find_element_by_tag_name('input')
    search_box.send_keys('tender\n')
    time.sleep(2)
    assert re.search(regex, browser.find_element_by_tag_name('body').text)


def test_language_switcher(browser, server):
    if 'localhost' in server:
        pytest.skip()

    browser.get(f'{server}en/')

    for lang, lang_name in languages.items():
        select = Select(browser.find_element_by_xpath("//select[@name='lang']"))
        select.select_by_visible_text(lang_name)
        assert browser.current_url == f'{server}{lang}/'
        assert test_basic_params[lang] in browser.find_element_by_tag_name('body').text
