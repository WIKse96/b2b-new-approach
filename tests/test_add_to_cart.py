import pytest
from pages.page_obj.prod_page import ProdPage
from pages.page_obj.main_page import MainPage


@pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [{'storage_state': './state_login.json'}])
def test_add_arrow(prod_page: ProdPage, main_page: MainPage):
    prod_page.load(path=prod_page.path_prod_simple)
    main_page.page.pause()
    # jesli w koszyku są produkty to je usun. Ilosci w koszyku zapisywane sa na koncie
    while main_page.qty_in_cart.text_content() != "0":
        main_page.clear_cart()
    prod_page.page.pause()
    prod_page.add_to_cart_by_arrow('+')
    prod_page.add_to_cart_by_arrow('+')
    prod_page.add_to_cart_by_arrow('-')
    prod_page.add_to_cart_by_arrow('+')
