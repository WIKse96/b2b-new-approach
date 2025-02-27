import time

from playwright.sync_api import Page, expect
from pages.locators.login_page_locators import LoginPage_locators
from pages.page_obj.base_page import BasePage


class LoginPage(BasePage):
    path = "customer/account/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator(LoginPage_locators.EMAIL_INPUT)
        self.pass_input = page.locator(LoginPage_locators.PASS_INPUT)
        self.login_btn = page.locator(LoginPage_locators.LOGIN_BTN)
        self.error_login = page.locator(LoginPage_locators.ERROR_LOGIN).first
        self.error_password = page.locator(LoginPage_locators.PASS_ERROR)
        self.error_email = page.locator(LoginPage_locators.EMAIL_ERROR)

    def get_errors(self):
        errors = {'pass_error': self.error_password,
                  'email_error': self.error_email
                  }
        return errors

    # Poprawne zalogowanie się
    def login(self, email, password):
        time.sleep(2)
        self.email_input.fill(email)
        self.pass_input.fill(password)
        self.login_btn.click()
        # self.page.pause()

    def correct_login_info(self):
        expect(self.error_login, "Komunikat o niezalogowaniu").not_to_be_visible()

    def incorrect_login_info(self):
        expect(self.error_login, "Komunikat o niezalogowaniu").to_be_visible()

    # Metoda do zapisania stanu zalogowania. Potem ten stan używamy za pomocą @pytest.mark.parametrize(
    # "browser_context_args", [{'storage_state': './state_login.json'}]) w teście
    def save_context(self):
        # Time sleep jest potrzebny bo stan nie zdąży się zapisać bez niego
        time.sleep(1)
        context = self.page.context
        context.storage_state(path="state_login.json")
