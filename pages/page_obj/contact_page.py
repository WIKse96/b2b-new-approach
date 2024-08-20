import time
import pytest

from playwright.sync_api import Page, expect
from pages.page_obj.base_page import BasePage
from pages.locators.contact_page_locators import ContactPageLocators


class ContactPage(BasePage):
    path = "contact"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.company_name = page.locator(ContactPageLocators.COMPANY_NAME_INPUT)
        self.subject = page.locator(ContactPageLocators.SUBJECT_INPUT)
        self.email = page.locator(ContactPageLocators.EMAIL_INPUT)
        self.phone = page.locator(ContactPageLocators.PHONE_NR_INPUT)
        self.message = page.locator(ContactPageLocators.MESSAGE_INPUT)
        self.rodo_checkbox = page.locator(ContactPageLocators.RODO_CHECKBOX)
        self.submit = page.locator(ContactPageLocators.SUBMIT_BTN)
        self.subject = page.locator(ContactPageLocators.SUBJECT_INPUT)
        self.header1 = page.locator(ContactPageLocators.SPAN1)
        self.header2 = page.locator(ContactPageLocators.SPAN2)
        self.phone_icon = page.locator(ContactPageLocators.PHONE_ICON)
        self.phone_nr_link = page.locator(ContactPageLocators.PHONE_NR_LINK)
        self.email_icon = page.locator(ContactPageLocators.EMAIL_ICON)
        self.email_link = page.locator(ContactPageLocators.EMAIL_LINK)
        # Errors
        self.name_error = page.locator(ContactPageLocators.NAME_ERROR)
        self.subject_error = page.locator(ContactPageLocators.SUBJECT_ERROR)
        self.comment_error = page.locator(ContactPageLocators.COMMENT_ERROR)
        self.email_error = page.locator(ContactPageLocators.EMAIL_ERROR)
        self.rodo_error = page.locator(ContactPageLocators.RODO_ERROR)


    def map_checker(self):
        google_map = self.page.frame_locator('iframe >> nth=0').locator('.gm-style > div > div:nth-child(2)')
        google_walker = self.page.frame_locator("iframe >> nth=1").locator("canvas").first
        expect(google_map, "Mapa niewidoczna").to_be_visible()
        expect(google_walker, "Spacer google niewidoczny").to_be_visible()

    def check_ic_email_and_phone(self):
        expect(self.phone_icon).to_be_visible()
        expect(self.email_icon).to_be_visible()
        expect(self.phone_nr_link).to_be_visible()
        expect(self.phone_nr_link).to_be_visible()
        expect(self.email_link).to_be_enabled()
        expect(self.email_link).to_be_enabled()
    def blank_form(self):
        self.company_name.fill('')
        self.subject.fill('')
        self.email.fill('')
        self.phone.fill('')
        self.message.fill('')
        self.subject.fill('')
        # self.page.pause()
        self.rodo_checkbox.uncheck()
        time.sleep(4)

        self.submit.click()
        errors = [self.name_error, self.rodo_error, self.email_error, self.comment_error, self.subject_error]
        # Errors are visible
        for error in errors:
            expect(error, "Error niewidoczny").to_be_visible()

    def only_rodo(self):
        self.rodo_checkbox.check()
        self.submit.click()
        expect(self.rodo_error).to_be_hidden()
        errors = [self.name_error, self.email_error, self.comment_error, self.subject_error]
        # Errors are visible
        for error in errors:
            expect(error, "Error niewidoczny").to_be_visible()

