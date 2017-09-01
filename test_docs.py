import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process
from collections import OrderedDict
import time
import re
from selenium.webdriver.support.ui import Select


BROWSER = os.environ.get('BROWSER', 'ChromeHeadless')


@pytest.fixture(scope="module")
def browser(request):
    if BROWSER == 'ChromeHeadless':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
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
    ('en', 'found \d+ page\(s\) matching'),
    ('es', 'encontró \d+ página\(s\) acorde'),
    ('fr', '\d+ page\(s\) trouvée\(s\) qui corresponde\(nt\)'),
])
def test_search(browser, server, lang, regex):
    browser.get('{}{}'.format(server, lang))
    search_box = browser.find_element_by_id('rtd-search-form').find_element_by_tag_name('input')
    search_box.send_keys('tender\n')
    time.sleep(2)
    assert re.search(regex, browser.find_element_by_tag_name('body').text)


@pytest.mark.parametrize('lang', ['en', 'es', 'fr'])
def test_community_extensions(browser, server, lang):
    browser.get('{}{}/extensions'.format(server, lang))
    community_extensions = browser.find_element_by_id('community-extensions').find_element_by_tag_name('table')
    # Currently community extensions aren't translated
    link = community_extensions.find_element_by_link_text('Budget breakdown')
    assert (link.get_attribute('href') ==
            'https://github.com/open-contracting/ocds_budget_breakdown_extension/blob/master/README.md')
    cells = link.find_elements_by_xpath('../../td')
    assert cells[2].text == 'For providing a detailed budget breakdown.'
    assert cells[3].text == 'ppp, 1.1'

    assert 'ocds_budget_breakdown_extension' not in browser.find_element_by_id('using-extensions').text
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
