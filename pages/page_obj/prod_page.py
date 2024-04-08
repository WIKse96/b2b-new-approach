import time

from playwright.sync_api import Page, expect
from pages.locators.prod_card_page_locators import ProdCardPage_locators
from pages.page_obj.base_page import BasePage
from pages.locators.main_page_locators import MainPage_locators


class ProdPage(BasePage):
    path = None
    path_prod_simple = 'catalog/product/view/id/5224/s/bateria-kuchenna-stojaca-czarna-flower/category/56/'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.sku_grouped = page.locator(ProdCardPage_locators.SKU_GROUPED)
        self.sku_marked = page.locator(ProdCardPage_locators.SKU_SIMPLE_marked)
        self.qty_down_arrow = page.locator(ProdCardPage_locators.QTY_DOWN_ARROW)
        self.qty_up_arrow = page.locator(ProdCardPage_locators.QTY_UP_ARROW)
        self.qty_input = page.locator(ProdCardPage_locators.QTY_INPUT)
        self.add_to_cart_btn = page.locator(ProdCardPage_locators.ADDTOCART_BTN)
        self.qty_in_cart = page.locator(MainPage_locators.QTY_IN_CART)

    def assert_search(self, search_query: str):
        expect(self.sku_grouped).to_be_visible()
        expect(self.sku_marked).to_have_text(search_query)

    # w set_qty'+'; - dodaje '-' lub inny - odejmuje
    def add_to_cart_by_arrow(self, set_qty: str):
        # self.page.pause()

        if set_qty == '+':
            initial_number = int(self.qty_input.input_value())
            expected_number = initial_number + 1
            self.qty_up_arrow.click()
            assert initial_number < expected_number

        else:
            initial_number = int(self.qty_input.input_value())
            expected_number = initial_number - 1
            self.qty_down_arrow.click()
            assert initial_number > expected_number

        self.add_to_cart_btn.click()
