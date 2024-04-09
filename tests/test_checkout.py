import pytest

from pages.page_obj.main_page import MainPage
from pages.page_obj.checkout_page import CheckoutPage

@pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [
    {'storage_state': './state_login.json'}
])
def test_simpleorder(main_page: MainPage, checkout_page: CheckoutPage):
    main_page.load()
    main_page.goto_checkout()
    checkout_page.simple_order()