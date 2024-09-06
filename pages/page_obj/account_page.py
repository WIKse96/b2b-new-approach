import time
import pytest
from playwright.sync_api import Page, expect
from pages.page_obj.base_page import BasePage
from pages.locators.account_page_locators import AccountPageLocators
from secret_conf import PASSWORD


class AccountPage(BasePage):
    path = "customer/account/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.h1 = page.locator(AccountPageLocators.H1)
        self.nav_ul_account = page.locator(AccountPageLocators.NAV_ACCOUNT)
        self.contact_data = page.locator(AccountPageLocators.CONTACT_DATA)
        self.change_contact_data_btn = page.locator(AccountPageLocators.CHANGE_CONTACT_DATA)
        self.h2_change_email_password = page.locator(AccountPageLocators.H2_PASS_OR_EMAIL)
        self.current_password_Error = page.locator(AccountPageLocators.CURRENT_PASSW_ERROR)
        self.email_Error = page.locator(AccountPageLocators.CURRENT_EMAIL_ERROR)
        self.new_password_Error = page.locator(AccountPageLocators.NEW_PASSW_ERROR)
        self.confirm_password_Error = page.locator(AccountPageLocators.CONFIRM_PASSW_ERROR)

        # get_by zamiast locator
        self.name_input = AccountPageLocators.name_by_label(page)
        self.surname_input = AccountPageLocators.surname_by_label(page)
        self.nip_input = AccountPageLocators.NIP_by_label(page)
        self.save_data_btn = AccountPageLocators.save_data(page)
        self.data_saved_info_i = AccountPageLocators.data_saved_info(page)
        self.change_email_checkbox = AccountPageLocators.change_email_checkbox(page)
        self.change_passw_checkbox = AccountPageLocators.change_password_checkbox(page)

        self.confirm_passw_input = AccountPageLocators.confirm_passw_input(page)
        self.email_input = AccountPageLocators.email_input(page)
        self.new_password_input = AccountPageLocators.new_password_input(page)
        self.current_password_input = AccountPageLocators.current_password_input(page)

        self.save_data_btn = AccountPageLocators.save_data_btn(page)

    def verify_nav(self, current: str):
        # self.page.pause()
        lis = ['Moje konto', 'Zamówienia', 'Książka adresowa', 'Dane konta']

        # Znalezienie wszystkich elementów li z klasą "nav item"
        nav_items = self.nav_ul_account.locator('//li')

        # Pobranie liczby znalezionych elementów
        count = nav_items.count()
        # Pobranie aktualnie zaznaczonego li
        current_item = self.nav_ul_account.locator("//li[@class='nav item current']/strong")
        expect(current_item).to_have_text(current)
        # Dla li niezaznaczonych
        for i in range(count):
            nav_item_text = nav_items.nth(i).text_content()
            # Na stronie są " " i musiałem jakoś je wykluczyć bo psuły mi asercje
            if not " ":
                assert nav_item_text.strip() in lis, f'{nav_item_text} nie ma w liscie'

    def change_contact_data(self, name, surname, nip, default: bool = False):
        self.change_contact_data_btn.click()
        # zweryfikuj dane jeśli sprawdzamy dane default
        if not default:
            self.verify_contact_data('wiktor', 'TEST', 'ze sklepu PL')
        # Uzupełnij inputy
        self.name_input.fill(name)
        self.surname_input.fill(surname)
        self.nip_input.fill(nip)
        # Kliknij przycisk zapisz
        self.save_data_btn.click()
        self.data_saved_info(name, surname, 'test@seart.pl')

    # Sprawdz czy jest info o zapisanych danych i czy dane się zmieniły
    def data_saved_info(self, name, surname, email):
        expect(self.data_saved_info_i).to_be_visible(timeout=5000)
        expect(self.contact_data).to_contain_text(f'{name} {surname} {email}')

    def verify_contact_data(self, name, surname, nip):
        expect(self.page).to_have_url("https://b2b.seartgroup.com/pl/customer/account/edit/")
        expect(self.name_input).to_have_value(name)
        expect(self.surname_input).to_have_value(surname)
        expect(self.nip_input).to_have_value(nip)

    def save_creditials(self, email: str, passw: str):
        if email == '':
            pass
        elif passw == '':
            pass

    def change_creditials(self, new_email: str, new_password: str):
        self.change_contact_data_btn.click()
        if new_email != '' and new_password == '':
            # Jeśli wpisany jest email a hasło puste
            self.change_email_checkbox.click()
            expect(self.h2_change_email_password).to_have_text("Zmień adres email")
            self.email_input.fill(new_email)  # uzupełnij pole email
            self.current_password_input(PASSWORD)  # uzupełnij pole hasło
            # Kliknij zapisz
            self.save_creditials(new_email, new_password)

        elif new_email == '' and new_password != '':
            # jeśli email pusty, a haslo uzupelnione
            self.change_passw_checkbox.click()
            # aktualne haslo
            self.current_password_input.fill(PASSWORD)
            # nowe haslo
            self.new_password_input.fill(new_password)
            # potwierdz haslo
            self.confirm_passw_input.fill(new_password)
            expect(self.h2_change_email_password).to_have_text("Zmień hasło")

            self.save_creditials(new_email, new_password)
            # self.

            self.save_creditials(new_email, new_password)
        elif new_email == '' and new_password == '':
            # hasło i email puste
            expect(self.h2_change_email_password).not_to_be_visible()

        else:
            # Oba pola uzupełnione
            self.change_passw_checkbox.click()
            self.change_email_checkbox.click()
            self.current_password_input.fill(PASSWORD)
            # nowe haslo
            self.new_password_input.fill(new_password)
            # potwierdz haslo
            self.confirm_passw_input.fill(new_password)
            expect(self.h2_change_email_password).to_have_text("Zmień hasło")

            self.save_creditials(new_email, new_password)
            
            self.save_creditials(new_email, new_password)
            expect(self.h2_change_email_password).to_have_text("Zmień adres E-mail i hasło")
