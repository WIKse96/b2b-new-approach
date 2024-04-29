import pytest
from pages.page_obj.navbar import NavbarMenuOp_PL


#ogólne testy navbaru
# @pytest.mark.run
def test_navbar(navbar: NavbarMenuOp_PL, pytestconfig: pytest.Config) -> None:
    navbar.load(path=navbar.path)
    navbar.check_menu_root()
    # Sprawdź czy wyświetla się/nie wyświetla container z submenu.
    navbar.container_submenu()
    navbar.without_container_submenu()

    #TODO: Dodać asercje i sprawdzenie linków pozycji w submenu
    # navbar.get_submenu_links()