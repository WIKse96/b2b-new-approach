from playwright.sync_api import Page, expect
from pages.locators.cart_page_locators import CartPageLocators
from pages.page_obj.base_page import BasePage


class CartPage(BasePage):
    path = 'checkout/cart/'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.remove_prod = page.locator(CartPageLocators.REMOVE_X_BTNS)
        self.empty_text = page.locator(CartPageLocators.EMPY_CART_TEXT)

    def remove_all(self):
        # to dziwne ale tylko ten sposób zadzaiałał
        for e in self.remove_prod.all():
            self.remove_prod.nth(0).click()
            expect(self.empty_text.text_content()).to_have_text('Nie masz produktów w koszyku.')

