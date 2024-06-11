import time

from pages.page_obj.base_page import BasePage
from pages.locators.main_page_locators import MainPage_locators
from pages.locators.category_locators import CategoryPage_locators
from playwright.sync_api import Page, expect


class CategoryPage(BasePage):
    path = 'meble/texas.html'
    path_legs = 'nogi.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path_legs = CategoryPage.path_legs
        self.add_to_cart_btns = page.locator(CategoryPage_locators.ADD_TO_CART_BTNS).all()
        self.set_amount_on_listing = page.locator(CategoryPage_locators.SHOW_AMOUNT)
        self.sorting = page.locator(CategoryPage_locators.SORTING_LIST)
        self.sorting_arrow_mal = page.locator(CategoryPage_locators.SORTING_ARROW_malejacy)
        self.sorting_arrow_ros = page.locator(CategoryPage_locators.SORTING_ARROW_rosnacy)
        self.qty_in_cart = page.locator(MainPage_locators.QTY_IN_CART)

        self.pagination = page.locator(CategoryPage_locators.PAGINATION).all()
        self.prods_on_listing = page.locator(CategoryPage_locators.PRODS_ON_LISTING).all()
        self.prod_names = page.locator(CategoryPage_locators.PROD_NAMES).all()
        self.next_page_btn = page.locator(CategoryPage_locators.NEXT_PAGE)

        self.prods_on_p_pages = []

    # Check prices in listing are in range.
    def filter_price(self, start=10, end=55):
        current_url = self.page.url
        new_url = f"{current_url}?price={start}-{end}&product_list_limit=all"
        self.page.goto(new_url)

        for price in self.page.locator(CategoryPage_locators.PRICES_ON_LISTING).all():
            price_stripped = price.text_content()[:-3].replace(",", ".")
            assert start <= float(price_stripped) <= end, f"Price {price_stripped} out of range {start}-{end}"

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
        if amount in ["12", "24", "36"]:
            self.set_amount_on_listing.select_option(amount)
            time.sleep(1)
            assert len(self.prods_on_listing) <= int(amount), "Ilość produktów na listingu nie koresponduje z selectem"
            for element in self.pagination:
                expect(element).to_be_visible()
            if amount == "12":
                self.page.wait_for_url(f"**/{self.path_legs}")
            else:
                self.page.wait_for_url(f"**/{self.path_legs}?product_list_limit={int(amount)}")
        else:
            self.set_amount_on_listing.select_option(value="all")
            time.sleep(1)
            for element in self.pagination:
                expect(element).not_to_be_visible()

            # check url is with querry
            self.page.wait_for_url(f"**/{self.path_legs}?product_list_limit=all")

    def checkPaginationAllUI(self):

        while True:
            prods_on_current_page = [prod_name.inner_text()[:-14] for prod_name in
                                     self.page.locator(CategoryPage_locators.PROD_NAMES).all()]
            self.prods_on_p_pages.extend(prods_on_current_page)

            assert prods_on_current_page not in self.prods_on_p_pages

            if not self.next_page_btn.is_visible():
                break

            self.next_page_btn.click()
            self.page.wait_for_load_state('networkidle')  # Czekaj na załadowanie nowej strony

    def checkPaginationAPI(self, pageIndex):
        self.page.goto(f"https://b2b.seartgroup.com/pl/{self.path_legs}?p={str(pageIndex)}")
        assert self.page.locator(CategoryPage_locators.PROD_NAMES).all() , 'No products on site'

