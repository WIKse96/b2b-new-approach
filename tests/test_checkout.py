import pytest

from pages.page_obj.main_page import MainPage
from pages.page_obj.checkout_page import CheckoutPage
from pages.page_obj.prod_page import ProdPage
# @pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [
    {'storage_state': './state_login.json'}
])
def test_simpleorder(main_page: MainPage, checkout_page: CheckoutPage, prod_page:ProdPage):
    prod_page.load(path=prod_page.path_prod_simple)
    prod_page.add_to_cart_by_arrow('+')
    main_page.goto_checkout()
    checkout_page.simple_order()