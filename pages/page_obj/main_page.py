import dataclasses
import time
from playwright.sync_api import Page, expect
from pages.locators.main_page_locators import MainPage_locators
from pages.page_obj.base_page import BasePage


class MainPage(BasePage):
    path = ''

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.search_input = page.locator(MainPage_locators.SEARCH_INPUT)
        self.search_btn = page.locator(MainPage_locators.SEARCH_BTN)
        self.search_prompt = page.locator(MainPage_locators.SEARCH_PROMPTS)
        self.qty_in_cart = page.locator(MainPage_locators.QTY_IN_CART)
        self.clear_cart_btns = page.locator(MainPage_locators.CLEAR_CART)
        self.confirm_clear_cart_btn = page.locator(MainPage_locators.CONFIRM_CLEAR_CART)
        self.ok_btn = page.locator(MainPage_locators.OK_BTN)

    def search(self, search_query: str):
        self.search_input.fill(search_query)
        expect(self.search_input).to_be_visible()
        self.search_prompt.first.click()

    def clear_cart(self):
        self.qty_in_cart.click()
        time.sleep(2)
        self.clear_cart_btns.click()
        time.sleep(2)
        self.confirm_clear_cart_btn.click()
        # self.page.pause()
        if self.ok_btn:
            self.ok_btn.click()
