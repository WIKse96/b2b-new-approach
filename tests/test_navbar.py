import pytest
from pages.page_obj.navbar import Navbar, NavbarMenuOp_PL


def test_navbar_correct_links(navbar: Navbar, pytestconfig: pytest.Config) -> None:

    # menu_items = list(NavbarMenuOp_PL().get_all_texts())
    # menu_links = {
    #     f'{base_url}/{menu_text.lower()}'
    #     for menu_text in menu_items
    #     if menu_text !=''
    # }

    # navbar.load(path=navbar.path)
    pass