import pytest

from pages.page_obj.category_page import CategoryPage
# todo: material, kolekcja, czas realizacji, rodzaj wykonczenia
# @pytest.mark.run()
@pytest.mark.parametrize("browser_context_args", [
    {'storage_state': './state_login.json'}
])
def test_price_filter(cat_page: CategoryPage):
    cat_page.load(path=cat_page.path_legs)
    cat_page.filter_price(10, 55)
    cat_page.load(path=cat_page.path_legs)
    cat_page.filter_price(50, 55)
    cat_page.load(path=cat_page.path_legs)
    cat_page.filter_price(20, 25)