import dataclasses
import time

from playwright.sync_api import Page, expect
from pages.locators.main_page_locators import MainPage_locators
from pages.page_obj.base_page import BasePage


class MainPage(BasePage):
    path = ''

    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.locator(MainPage_locators.SEARCH_INPUT)
        self.search_btn = page.locator(MainPage_locators.SEARCH_BTN)
        self.search_prompt = page.locator(MainPage_locators.SEARCH_PROMPTS)

    def search(self, search_query: str):
        self.search_input.fill(search_query)
        expect(self.search_input).to_be_visible()
        self.search_btn.click()
