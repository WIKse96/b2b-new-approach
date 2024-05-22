import time

from playwright.sync_api import Page, expect
from pages.locators.prod_card_page_locators import ProdCardPage_locators
from pages.page_obj.base_page import BasePage
from pages.locators.main_page_locators import MainPage_locators


class ProdPage(BasePage):
    path = None
    path_prod_simple = 'catalog/product/view/id/5224/s/bateria-kuchenna-stojaca-czarna-flower/category/56/'
    path_prod_prgr = 'drzwi-szklane-wewnetrzne-factor.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.sku_grouped = page.locator(ProdCardPage_locators.SKU_GR)
        self.sku_marked = page.locator(ProdCardPage_locators.SKU_SIMPLE_marked)
        self.qty_down_arrow = page.locator(ProdCardPage_locators.QTY_DOWN_ARROW)
        self.qty_up_arrow = page.locator(ProdCardPage_locators.QTY_UP_ARROW)
        self.qty_input = page.locator(ProdCardPage_locators.QTY_INPUT)
        self.add_to_cart_btn = page.locator(ProdCardPage_locators.ADDTOCART_BTN)
        self.qty_in_cart = page.locator(MainPage_locators.QTY_IN_CART)
        self.qty_control_prgr = page.locator(ProdCardPage_locators.QTY_CONTROL_PRGR_1ST).first
        self.add_to_cart_btn_progr = page.locator(ProdCardPage_locators.ADDTOCART_BTN_PRGR)
        #specyfikacja
        self.prod_details_container = page.locator(ProdCardPage_locators.SPEC_CONTAINER)
        self.prod_details_close = page.locator(ProdCardPage_locators.SPEC_CLOSE_BTN)
        self.prod_details_table = page.locator(ProdCardPage_locators.SPEC_BODY)
        self.prod_details_btn = page.locator(ProdCardPage_locators.SPEC_GR)
        # download
        self.download = page.locator(ProdCardPage_locators.DOWNLOAD)

    # Sprawdź czy można otworzyć specyfikacje, zamknać i czy sie wyświetla poprawnie
    def check_prod_details(self):
        expect(self.prod_details_table).not_to_be_visible()
        self.prod_details_btn.first.click()
        expect(self.prod_details_table).to_be_visible()
        self.prod_details_close.click()
        expect(self.prod_details_table).not_to_be_visible()
        self.prod_details_btn.first.click()
        expect(self.prod_details_table).to_be_visible()
        self.prod_details_table.click()
        expect(self.prod_details_table).not_to_be_visible()

    def add_to_cart_by_plus_minus(self, set_qty: str):
        # self.page.pause()
        up_btn = self.qty_control_prgr.locator('//div/a/i[@class="porto-icon-up-dir"]')
        down_btn = self.qty_control_prgr.locator('//div/a/i[@class="porto-icon-down-dir"]')
        input = self.qty_control_prgr.locator('//input[@class="input-text qty"]')
        if set_qty == '+':
            initial_number = int(input.input_value())
            expected_number = initial_number + 1
            up_btn.click()
            assert initial_number < expected_number

        else:
            initial_number = int(input.input_value())
            expected_number = initial_number - 1
            down_btn.click()
            assert initial_number > expected_number

        self.add_to_cart_btn_progr.click()

    def get_download_link(self):
        expect(self.download).to_be_enabled()
        self.download.click()

    def assert_search(self, search_query: str):
        expect(self.sku_grouped).to_be_visible()
        expect(self.sku_marked).to_have_text(search_query)

    # w set_qty'+'; - dodaje '-' lub inny - odejmuje - używane do zwiększenia lub zmniejszenia ilośći dodanej do koszyka
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
