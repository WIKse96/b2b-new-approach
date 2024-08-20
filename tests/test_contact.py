from pages.page_obj.contact_page import ContactPage
import pytest
def test_map_vsibility(contact_page: ContactPage):
    contact_page.load(contact_page.path, wait='domcontentloaded')
    contact_page.map_checker()
    contact_page.check_ic_email_and_phone()


@pytest.mark.run
def test_contact_blank_form(contact_page: ContactPage):
    contact_page.load(contact_page.path, wait='domcontentloaded')
    contact_page.blank_form()
@pytest.mark.run
def test_contact_rodo_only(contact_page: ContactPage):
    contact_page.load(contact_page.path, wait='domcontentloaded')
    contact_page.only_rodo()
