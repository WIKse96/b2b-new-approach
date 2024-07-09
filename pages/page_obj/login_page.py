import time

from playwright.sync_api import Page, expect
from pages.locators.login_page_locators import LoginPage_locators
from pages.page_obj.base_page import BasePage


class LoginPage(BasePage):
    path = "customer/account/login"
    log_out_path = "customer/account/logout/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator(LoginPage_locators.EMAIL_INPUT)
        self.pass_input = page.locator(LoginPage_locators.PASS_INPUT)
        self.login_btn = page.locator(LoginPage_locators.LOGIN_BTN).first
        self.error_login = page.locator(LoginPage_locators.ERROR_LOGIN)

    # Poprawne zalogowanie się
    def login(self, email, password):
        context = self.page.context
        context.clear_cookies()
        self.email_input.fill(email)
        self.pass_input.fill(password)
        self.login_btn.click()
        time.sleep(1)

    def assert_correcnt_login(self):
        expect(self.error_login, "Komunikat o niezalogowaniu").not_to_be_visible()

    def assert_incorrecnt_login(self):
        expect(self.error_login, "Komunikat o niezalogowaniu").to_be_visible()
        self.page.pause()

    # Metoda do zapisania stanu zalogowania. Potem ten stan używamy za pomocą @pytest.mark.parametrize(
    # "browser_context_args", [{'storage_state': './state_login.json'}]) w teście
    def save_context(self):
        # Time sleep jest potrzebny bo stan nie zdąży się zapisać bez niego
        time.sleep(1)
        context = self.page.context
        context.storage_state(path="state_login.json")
