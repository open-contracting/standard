import os
import re
import time
from collections import OrderedDict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process

import pytest
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


BROWSER = os.environ.get('BROWSER', 'ChromeHeadless')


@pytest.fixture(scope="module")
def browser(request):
    if BROWSER == 'ChromeHeadless':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(chrome_options=chrome_options)
    else:
        browser = getattr(webdriver, BROWSER)()
    browser.implicitly_wait(3)
    request.addfinalizer(lambda: browser.quit())
    return browser


@pytest.fixture(scope="module")
def server(request):
    if 'CUSTOM_SERVER_URL' in os.environ:
        return os.environ['CUSTOM_SERVER_URL']

    host = 'localhost'
    port_number = 8331

    def run():
        os.chdir('build')
        server_address = (host, port_number)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        httpd.serve_forever()

    p = Process(target=run)
    p.start()

    def fin():
        p.terminate()
    request.addfinalizer(fin)

    return 'http://{}:{}/'.format(host, port_number)


lang_basic_text = OrderedDict([
    ('en', 'Open Contracting Data Standard'),
    ('es', 'Estándar de Datos de Contrataciones Abiertas'),
    ('fr', 'Standard de Données sur la Commande Publique Ouverte'),
])


@pytest.mark.parametrize('lang,text', lang_basic_text.items())
def test_basic(browser, server, lang, text):
    browser.get('{}{}'.format(server, lang))
    assert text in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize('lang,regex', [
    ('en', r'found \d+ page\(s\) matching'),
    ('es', r'encontró \d+ página\(s\) acorde'),
    ('fr', r'\d+ page\(s\) trouvée\(s\) qui corresponde\(nt\)'),
])
def test_search(browser, server, lang, regex):
    browser.get('{}{}'.format(server, lang))
    search_box = browser.find_element_by_id('rtd-search-form').find_element_by_tag_name('input')
    search_box.send_keys('tender\n')
    time.sleep(2)
    assert re.search(regex, browser.find_element_by_tag_name('body').text)


@pytest.mark.parametrize('lang', ['en', 'es', 'fr'])
def test_community_extensions(browser, server, lang):
    url = 'https://raw.githubusercontent.com/open-contracting-extensions/ocds_budget_breakdown_extension/master/extension.json'  # noqa
    extension = requests.get(url).json()

    browser.get('{}{}/extensions'.format(server, lang))
    community_extensions = browser.find_element_by_id('community-extensions').find_element_by_tag_name('table')
    # Currently community extensions aren't translated
    link = community_extensions.find_element_by_link_text(extension['name']['en'])
    assert (link.get_attribute('href') == extension['documentationUrl']['en'])
    cells = link.find_elements_by_xpath('../../td')
    assert cells[2].text == extension['description']['en']
    assert cells[3].text == 'ppp'

    assert 'ocds_budget_breakdown_extension' not in browser.find_element_by_id('using-extensions').text
    browser.execute_script("arguments[0].scrollIntoView();", cells[0])
    cells[0].click()
    assert 'ocds_budget_breakdown_extension' in browser.find_element_by_id('using-extensions').text


@pytest.mark.parametrize('lang', ['en', 'es', 'fr'])
def test_examples(browser, server, lang):
    browser.get('{}{}/getting_started/releases_and_records'.format(server, lang))
    examples = browser.find_element_by_id('examples')
    select = Select(examples.find_element_by_tag_name('select'))

    assert 'ocds-213czf-000-00001-01-planning' in examples.text

    select.select_by_visible_text('tender')
    assert 'ocds-213czf-000-00001-02-tender' in examples.text
    assert 'ocds-213czf-000-00001-01-planning' not in examples.text

    # test collapse expand
    # xs = examples.find_element_by_link_text('⊖')


def test_language_switcher(browser, server):
    if 'localhost' in server:
        pytest.skip()

    browser.get('{}en'.format(server))

    for lang, lang_name in [
            ('es', 'Español'),
            ('fr', 'Français'),
            ('en', 'English'),
            ]:
        select = Select(browser.find_element_by_xpath("//select[@name='lang']"))
        select.select_by_visible_text(lang_name)
        assert browser.current_url == '{}{}/'.format(server, lang)
        assert lang_basic_text[lang] in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize('lang', ['en', 'es', 'fr'])
def test_broken_links(browser, server, lang):
    browser.get('{}{}'.format(server, lang))
    while True:
        for link in browser.find_elements_by_partial_link_text(''):
            href = link.get_attribute('href')
            if '/review/' in href or 'localhost' not in href:
                continue
            r = requests.get(href)
            assert r.status_code == 200, 'expected 200, got {} for {}'.format(r.status_code, href)
        try:
            next = browser.find_element_by_link_text('Next')
            browser.execute_script("arguments[0].scrollIntoView();", next)
            next.click()
        except NoSuchElementException:
            break
