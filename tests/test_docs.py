import pytest
from selenium.webdriver.support.ui import Select

from . import languages


@pytest.mark.parametrize('lang', list(languages))
def test_examples(browser, server, lang):
    browser.get(f'{server}{lang}/guidance/build/merging')
    examples = browser.find_element_by_id('updates-and-deletions')
    select = Select(examples.find_element_by_tag_name('select'))

    assert '"date": "2016-01-01T09:30:00Z"' in examples.text

    select.select_by_visible_text('tenderAmendment')
    assert '"date": "2016-02-05T10:30:00Z"' in examples.text
    assert '"date": "2016-01-01T09:30:00Z"' not in examples.text

    # test collapse expand
    # xs = examples.find_element_by_link_text('⊖')
