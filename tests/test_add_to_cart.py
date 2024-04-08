import time

import pytest
from pages.page_obj.prod_page import ProdPage
from pages.page_obj.main_page import MainPage
from pages.page_obj.cart_page import CartPage



@pytest.mark.parametrize("browser_context_args", [{'storage_state': './state_login.json'}])
def test_add_arrow(prod_page: ProdPage, main_page: MainPage):
    prod_page.load(path=prod_page.path_prod_simple)
    time.sleep(2)
    initial_qty = prod_page.qty_in_cart.text_content().strip()
    prod_page.add_to_cart_by_arrow('+')
    # prod_page.add_to_cart_by_arrow('+')
    # prod_page.add_to_cart_by_arrow('-')
    # prod_page.add_to_cart_by_arrow('+')
    final_qty = prod_page.qty_in_cart.text_content().strip()
    # asercja czy ilość w koszyku się zmienila
    print('initial', initial_qty, 'final', final_qty)
    assert int(initial_qty) < int(final_qty)


def test_clear_cart_listing(main_page: MainPage, prod_page: ProdPage):
    prod_page.load(path=prod_page.path_prod_simple)
    prod_page.add_to_cart_by_arrow('+')
    time.sleep(2)
    if main_page.qty_in_cart.text_content().strip() != "0":
        main_page.clear_cart_listing()
    else:
        print('No prods in cart')

@pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [{'storage_state': './state_login.json'}])
def test_clear_cart(cart_page: CartPage):
    cart_page.load(cart_page.path)

    cart_page.remove_all()
    time.sleep(1)

