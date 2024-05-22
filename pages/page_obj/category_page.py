import time

from pages.page_obj.base_page import BasePage
from pages.locators.main_page_locators import MainPage_locators
from pages.locators.category_locators import CategoryPage_locators
from playwright.sync_api import Page, expect


class CategoryPage(BasePage):
    path = 'meble/texas.html'
    path_for_check_amount = 'nogi.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path_for_check_amount = CategoryPage.path_for_check_amount
        self.add_to_cart_btns = page.locator(CategoryPage_locators.ADD_TO_CART_BTNS).all()
        self.set_amount_on_listing = page.locator(CategoryPage_locators.SHOW_AMOUNT)
        self.sorting = page.locator(CategoryPage_locators.SORTING_LIST)
        self.sorting_arrow_mal = page.locator(CategoryPage_locators.SORTING_ARROW_malejacy)
        self.sorting_arrow_ros = page.locator(CategoryPage_locators.SORTING_ARROW_rosnacy)
        self.qty_in_cart = page.locator(MainPage_locators.QTY_IN_CART)

        self.pagination = page.locator(CategoryPage_locators.PAGINATION).all()
        self.prods_on_listing = page.locator(CategoryPage_locators.PRODS_ON_LISTING).all()

    # num - How many prods add to the cart from listing
    def add_to_cart_listing(self, num):
        time.sleep(1)
        counter = 0
        # Pobieramy tutaj ponieważ wartość się tu doczytuje
        qty_in_cart_initial = self.qty_in_cart.text_content()
        for btn in self.page.locator(CategoryPage_locators.ADD_TO_CART_BTNS).all():
            if counter < num:
                btn.click()
            counter += 1

        time.sleep(1)
        qty_in_cart_final = self.qty_in_cart.text_content()

        assert int(qty_in_cart_final) > int(qty_in_cart_initial), "Błąd koszyka. Wartość się nie aktualizuje"

    # amount - How many  show prods, 12,24,36,all
    def changeAmountOnListing(self, amount):
        if amount in ["12", "24","36"]:
            self.set_amount_on_listing.select_option(amount)
            time.sleep(1)
            assert len(self.prods_on_listing) <= int(amount), "Ilość produktów na listingu nie koresponduje z selectem"
            for element in self.pagination:
                expect(element).to_be_visible()
            if amount == "12":
                self.page.wait_for_url(f"**/{self.path_for_check_amount }")
            else:
                self.page.wait_for_url(f"**/{self.path_for_check_amount }?product_list_limit={int(amount)}")
        else:
            self.set_amount_on_listing.select_option(value="all")
            time.sleep(1)
            for element in self.pagination:
                expect(element).not_to_be_visible()

            # check url is with querry
            self.page.wait_for_url(f"**/{self.path_for_check_amount }?product_list_limit=all")
