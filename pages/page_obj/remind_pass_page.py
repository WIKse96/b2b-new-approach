import time

from playwright.sync_api import expect
from pages.locators.remind_pass_locators import Remind_pass_locator
from playwright.sync_api import Page
from pages.page_obj.base_page import BasePage


class LostPasswordPage(BasePage):
    path = "customer/account/forgotpassword/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.subimt_btn = page.locator(Remind_pass_locator.SUBMIT_BTN)
        self.title_page_pl = page.locator(Remind_pass_locator.TITLE)
        self.email_input = page.locator(Remind_pass_locator.EMAIL_INPUT)
        self.capcha_input = page.locator(Remind_pass_locator.CAPCHA_INPUT)
        self.pl_header = 'Nie pamiętasz hasła?'
        self.capcha = page.locator(Remind_pass_locator.CAPCHA)
        self.reload_capcha_btn = page.locator(Remind_pass_locator.RELOAD_CAPCHA_BTN)
        self.email_error = page.locator(Remind_pass_locator.EMAIL_ERROR)
        self.capcha_error = page.locator(Remind_pass_locator.CAPCHA_ERROR)

    def assertions(self):
        expect(self.capcha_input).to_be_visible()
        expect(self.capcha).to_be_visible()
        expect(self.reload_capcha_btn).to_be_enabled()
        expect(self.title_page_pl).to_have_text(self.pl_header)

    def fillout_form(self, email):
        capcha_img_state = self.capcha.get_attribute('src')

        self.reload_capcha_btn.click()
        capcha_img_state_new = self.capcha.get_attribute('src')
        # sprawdzenie czy załadowal sie nowy obrazek
        assert capcha_img_state_new != capcha_img_state
        self.email_input.fill(email)

        self.reload_capcha_btn.click()
        self.page.pause()
        # wpisanie capcha recznie
        # klikniecie w btn

    def blank_inputs(self):
        expect(self.capcha_error).not_to_be_visible()
        expect(self.email_error).not_to_be_visible()
        time.sleep(1)
        self.subimt_btn.click()
        expect(self.capcha_error).to_be_visible(timeout=1000)
        expect(self.email_error).to_be_visible(timeout=1000)

    def invalid_email(self):
        self.email_input.fill("email@")
        self.subimt_btn.click()
        expect(self.email_error).to_have_text("Podaj poprawny adres email (np.: johndoe@domain.com).")
