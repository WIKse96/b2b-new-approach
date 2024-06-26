# todo: Dodaj do koszyka, pokaz ilość, sortowanie, strzałki

import pytest

from pages.page_obj.category_page import CategoryPage


@pytest.mark.parametrize("browser_context_args", [
    {'storage_state': './state_login.json'}
])
def test_addToCart(cat_page: CategoryPage):
    cat_page.load(path=cat_page.path)
    cat_page.add_to_cart_listing(2)


# @pytest.mark.run()
def test_showAmount(cat_page: CategoryPage):
    cat_page.load(path=cat_page.path_legs)
    cat_page.changeAmountOnListing("24")
    cat_page.changeAmountOnListing("12")
    cat_page.changeAmountOnListing("36")
    cat_page.changeAmountOnListing("all")


def test_pagination(cat_page: CategoryPage):
    cat_page.load(path=cat_page.path_legs)
    cat_page.checkPaginationAllUI()
    cat_page.checkPaginationAPI(3)
    cat_page.checkPaginationAPI(4)
    cat_page.checkPaginationAPI(5)
    cat_page.checkPaginationAPI(88)






