import time

from playwright.sync_api import Page

from pages.locators.cart_page_locators import CartPageLocators
from pages.page_obj.base_page import BasePage


class CartPage(BasePage):
    path = 'checkout/cart/'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.remove_prod = page.locator(CartPageLocators.REMOVE_X_BTNS)

    def remove_all(self):
        index = 0

        # to dziwne ale tylko ten sposób zadzaiałał
        for e in self.remove_prod.all():
            print(index)
            self.remove_prod.nth(index).click()
