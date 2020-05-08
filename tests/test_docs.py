import pytest
from selenium.webdriver.support.ui import Select

from . import languages


@pytest.mark.parametrize('lang', list(languages))
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
