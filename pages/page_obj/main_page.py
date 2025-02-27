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
        self.goto_checkout_btn = page.locator(MainPage_locators.GOTOCHECKOUT_BTN)
        self.currency_switch_btn = page.locator(MainPage_locators.CURRENCY_SWITCHER)
        self.currency_li = page.locator(MainPage_locators.CURRENCY_LI)
    # Wyszukiwanie proste
    def search(self, search_query: str):
        self.search_input.fill(search_query)
        expect(self.search_input).to_be_visible()
        self.search_prompt.first.click()

    # Czyszczenie małego koszyka z listingu
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

    def goto_checkout(self):
        self.qty_in_cart.click()
        self.goto_checkout_btn.click()
    #
    # def change_currency(self, currency: str):
    #     # self.page.pause()
    #     self.page.goto("https://b2b.seartgroup.com/pl/currency=PLN&uenc=aHR0cHM6Ly9iMmIuc2VhcnRncm91cC5jb20vcGwvZHJ6d2ktei1sdXN0cmVtLW1pcnJvci5odG1s&form_key=oYMm9C0Z5DkvwhXH")


