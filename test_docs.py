import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process
from collections import OrderedDict
import time
import re


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


@pytest.mark.parametrize('lang,text', [
    ('en', 'Open Contracting Data Standard'),
    ('es', 'Estándar de Datos de Contrataciones Abiertas'),
    ('fr', 'Standard de Données sur la Commande Publique Ouverte'),
])
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
    time.sleep(1)
    assert re.search(regex, browser.find_element_by_tag_name('body').text)
