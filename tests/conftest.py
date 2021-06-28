import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='module')
def browser(request):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(3)
    request.addfinalizer(lambda: browser.quit())

    return browser


@pytest.fixture(scope='module')
def server(request):
    host = 'localhost'
    port_number = 8331

    def run():
        os.chdir('build')
        HTTPServer((host, port_number), SimpleHTTPRequestHandler).serve_forever()

    p = Process(target=run)
    p.start()

    def stop():
        p.terminate()
    request.addfinalizer(stop)

    return 'http://{}:{}/'.format(host, port_number)
