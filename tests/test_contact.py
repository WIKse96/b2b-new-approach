import time

from playwright.sync_api import expect
from support.support import check_text
from pages.page_obj.contact_page import ContactPage

import pytest



def perform_contact_form(contact_page: ContactPage,
                         company_name: str,
                         subject: str,
                         email: str,
                         message: str,
                         rodo: bool,
                         phone_nr: str,
                         ):
    contact_page.load(contact_page.path, wait='domcontentloaded')
    time.sleep(2)

    # Wypełnij formularz danymi z parametrów
    if company_name:
        contact_page.compan_name_only(company_name)
    if subject:
        contact_page.subject_only(subject)
    if email:
        contact_page.email_only(email)
    if phone_nr:
        contact_page.phone_only(phone_nr)
    if message:
        contact_page.message_only(message)
    contact_page.rodo_only(rodo)

    # Kliknij przycisk Submit
    # time.sleep(3)
    # contact_page.pause()
    contact_page.submit_click()

    # Sprawdź, czy oczekiwane błędy pojawiły się
    errors_dic = contact_page.get_errors()

    if company_name == '':
        expect(errors_dic['name_error']).to_be_visible()
    if subject == '':
        expect(errors_dic['subject_error']).to_be_visible()
    if message == '':
        expect(errors_dic['comment_error']).to_be_visible()

    if not rodo:
        expect(errors_dic['rodo_error']).to_be_visible()
    if email == '':
        expect(errors_dic['email_error']).to_be_visible()
    else:
        check_text(email)
        expect(errors_dic['email_error']).to_contain_text("Podaj poprawny adres email (np.: johndoe@domain.com).")

def test_map_vsibility(contact_page: ContactPage):
    contact_page.load(contact_page.path, wait='domcontentloaded')
    contact_page.map_checker()
    contact_page.check_ic_email_and_phone()


@pytest.mark.run
@pytest.mark.parametrize("company_name, subject, email, message, rodo, phone_nr",
                         [
                         ('', '', '', '', False, ''),  # Wszystko puste
                          ('', '', '', '', True, ''),  # Wszystko puste, checkbox zaznaczony
                          ('NAZWA FIRMY ĄŚĆŻ', '', '', '', False, ''),  # Tylko company_name
                          ('', '', '', '', False, '55566644-'),  # Tylko telefon
                          ('', '', 'test@seart.pl', '', False, ''),  # Tylko email
                          ('', '', '', 'Wiadomość żźćół 86 /*-', False, ''),  # Tylko wiadomość
                          ('', '', '', '', True),  # Przypadek pozytywny
                          ('', '', 'test.seart.pl', '', False, ''),  # Niepoprawny email (bez @)
                          ('', '', 'test@pl', '', False, ''), # Niepoprawny email (bez .com)
                          ])
def test_contact_form(contact_page: ContactPage, company_name: str, subject: str,
                      email: str, message: str, rodo: bool, phone_nr: str):

    perform_contact_form(
        contact_page=contact_page,
        company_name=company_name,
        subject=subject,
        email=email,
        message=message,
        rodo=rodo,
        phone_nr=phone_nr,

    )
