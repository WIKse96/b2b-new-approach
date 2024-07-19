import time
from pages.page_obj.prod_page import ProdPage
import pytest
from pages.page_obj.main_page import MainPage
from pages.page_obj.category_page import CategoryPage

@pytest.mark.parametrize("browser_context_args", [
    {'storage_state': './state_login.json'}
])
# @pytest.mark.run
def test_change_currency_cat(main_page: MainPage, cat_page: CategoryPage, prod_page: ProdPage):
    main_page.load(cat_page.path_taps)

    first_check = cat_page.check_currency()
    main_page.set_curr()
    second_check = cat_page.check_currency()
    assert first_check != second_check


@pytest.mark.parametrize("browser_context_args", [
    {'storage_state': './state_login.json'}
])
# @pytest.mark.run
def test_change_currency_prod(main_page: MainPage, cat_page: CategoryPage, prod_page: ProdPage):

    prod_page.load(prod_page.path_prod_simple)
    first_check = cat_page.check_currency()
    main_page.set_curr()
    second_check = cat_page.check_currency()
    assert first_check != second_check
