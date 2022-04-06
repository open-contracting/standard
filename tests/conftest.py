import threading
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='module')
def browser(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)

    yield browser

    browser.quit()


@pytest.fixture(scope='module')
def server(request):
    host = 'localhost'
    port_number = 8331

    server = HTTPServer((host, port_number), partial(SimpleHTTPRequestHandler, directory='build'))

    thread = threading.Thread(target=server.serve_forever)
    thread.start()

    yield f'http://{host}:{port_number}/'

    server.shutdown()
    thread.join()
