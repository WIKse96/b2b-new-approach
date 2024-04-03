from playwright.sync_api import Page, expect
from pages.locators.prod_card_page_locators import ProdCardPage_locators

from pages.page_obj.base_page import BasePage


class ProdPage(BasePage):
    path = None
    path_prod_simple = 'catalog/product/view/id/5224/s/bateria-kuchenna-stojaca-czarna-flower/category/56/'

    def __init__(self, page: Page):
        super().__init__(page)
        self.sku_grouped = page.locator(ProdCardPage_locators.SKU_GROUPED)
        self.sku_marked = page.locator(ProdCardPage_locators.SKU_SIMPLE_marked)

    def assert_search(self, search_query: str):
        expect(self.sku_grouped).to_be_visible()
        expect(self.sku_marked).to_have_text(search_query)

    def add_to_cart_by_arrow(self, qty: str):
        pass