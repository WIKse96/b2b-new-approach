import pytest

from pages.page_obj.contact_page import ContactPage

@pytest.mark.run
def test_map_vsibility(contact_page: ContactPage):
    contact_page.load(contact_page.path)
