import pytest
from pages.page_obj.navbar import NavbarMenuOp_PL


@pytest.mark.run
def test_navbar_correct_links(navbar: NavbarMenuOp_PL, pytestconfig: pytest.Config) -> None:
    navbar.load(path=navbar.path)
    # ODKOMENTOWAC

    navbar.check_menu_root()
    # Sprawdź czy wyświetla się/nie wyświetla container z submenu
    navbar.container_submenu()
    navbar.without_container_submenu()
    # navbar.get_submenu_links()