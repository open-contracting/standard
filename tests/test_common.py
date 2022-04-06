import re
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from tests import languages, test_basic_params, test_search_params


@pytest.mark.parametrize('lang,text', test_basic_params.items())
def test_basic(browser, server, lang, text):
    browser.get(f'{server}{lang}')
    assert text in browser.find_element(By.TAG_NAME, 'body').text


@pytest.mark.parametrize('lang,regex', test_search_params)
def test_search(browser, server, lang, regex):
    browser.get(f'{server}{lang}')
    search_box = browser.find_element(By.ID, 'rtd-search-form').find_element(By.TAG_NAME, 'input')
    search_box.send_keys('tender\n')
    time.sleep(3)
    assert re.search(regex, browser.find_element(By.TAG_NAME, 'body').text)


# This seems to be an issue in Selenium and/or ChromeDriver.
@pytest.mark.filterwarnings("ignore:unclosed <socket.socket fd=:ResourceWarning")
def test_language_switcher(browser, server):
    if 'localhost' in server:
        pytest.skip()

    browser.get(f'{server}en/')

    for lang, lang_name in languages.items():
        select = Select(browser.find_element(By.XPATH, "//select[@name='lang']"))
        select.select_by_visible_text(lang_name)
        assert browser.current_url == f'{server}{lang}/'
        assert test_basic_params[lang] in browser.find_element(By.TAG_NAME, 'body').text
