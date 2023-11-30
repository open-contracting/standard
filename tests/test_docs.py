import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from . import languages


@pytest.mark.parametrize('lang', list(languages))
# This seems to be an issue in Selenium and/or ChromeDriver.
@pytest.mark.filterwarnings("ignore:unclosed <socket.socket fd=:ResourceWarning")
def test_examples(browser, server, lang):
    browser.get(f'{server}{lang}/guidance/build/merging')
    examples = browser.find_element(By.ID, 'updates-and-deletions')
    select = Select(examples.find_element(By.TAG_NAME, 'select'))

    assert '"date": "2020-10-21T13:02:26Z"' in examples.text

    select.select_by_visible_text('tenderUpdate')
    assert '"date": "2020-11-05T14:36:54Z"' in examples.text
    assert '"date": "2020-10-21T13:02:26Z"' not in examples.text

    # test collapse expand
    # xs = examples.find_element(By.LINK_TEXT, '⊖')
