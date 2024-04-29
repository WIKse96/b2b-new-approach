import time

import pytest
from pages.page_obj.prod_page import ProdPage
from pages.page_obj.main_page import MainPage

# @pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [{'storage_state': './state_login.json'}])
def test_prod_grouped(prod_page: ProdPage):
    prod_page.load(prod_page.path_prod_prgr)
    # Spec
    prod_page.check_prod_details()

@pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [{'storage_state': './state_login.json'}])
def test_download_link(prod_page: ProdPage):
    prod_page.load(prod_page.path_prod_prgr)
    prod_page.get_download_link()