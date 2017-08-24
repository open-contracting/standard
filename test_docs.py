import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process


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


@pytest.mark.parametrize('lang', ['en', 'es'])
def test_test(browser, server, lang):
    browser.get('{}{}'.format(server, lang))
