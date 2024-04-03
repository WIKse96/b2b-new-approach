import time

from playwright.sync_api import Page
from pages.locators.login_page_locators import LoginPage_locators
from pages.page_obj.base_page import BasePage
class LoginPage(BasePage):
    path = "customer/account/login"
    def __init__(self, page:Page):
        super().__init__(page)
        self.email_input = page.locator(LoginPage_locators.EMAIL_INPUT)
        self.pass_input = page.locator(LoginPage_locators.PASS_INPUT)
        self.login_btn = page.locator(LoginPage_locators.LOGIN_BTN)

    def login(self,email,password):
        self.email_input.fill(email)
        self.pass_input.fill(password)
        self.login_btn.click()

#Metoda do zapisania stanu zalogowania
    def save_context(self):
        time.sleep(5)
        context = self.page.context
        context.storage_state(path="state_login.json")

