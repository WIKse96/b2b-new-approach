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
        self.remove_prod_from_cart_btns = page.locator(MainPage_locators.REMOVE_PROD_FROM_CART)
        self.confirm_clear_cart_btn = page.locator(MainPage_locators.CONFIRM_CLEAR_CART)
        self.ok_btn = page.locator(MainPage_locators.OK_BTN)

    def search(self, search_query: str):
        self.search_input.fill(search_query)
        expect(self.search_input).to_be_visible()
        self.search_prompt.first.click()

    def clear_cart_listing(self):
        index = 0
        self.qty_in_cart.click()
        print(type(self.remove_prod_from_cart_btns))
        if self.remove_prod_from_cart_btns.count() == 1:
            self.remove_prod_from_cart_btns.click()
            self.confirm_clear_cart_btn.click()

        else:
            while index < self.remove_prod_from_cart_btns.count():
                print(self.remove_prod_from_cart_btns.nth(index))
                self.remove_prod_from_cart_btns.nth(index).click()
                self.confirm_clear_cart_btn.click()

