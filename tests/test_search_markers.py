import time

import pytest
from playwright.sync_api import Page

from pages.page_obj.prod_page import ProdPage
from pages.page_obj.main_page import MainPage
#Dodanie parametrów do browser context args. W tym przypadku dodajemy stan zalogowania
@pytest.mark.parametrize("browser_context_args", [
    {'storage_state': './state.json'}
])
@pytest.mark.search
def test_search(main_page: MainPage, prod_page: ProdPage, pytestconfig: pytest.Config) -> None:
    search_query = 'PRI-80x160'

    main_page.load(path=main_page.path)
    main_page.search(search_query)
    context = prod_page.page.context
    cookies = context.cookies()
    print(cookies)
    prod_page.assert_search(search_query)



