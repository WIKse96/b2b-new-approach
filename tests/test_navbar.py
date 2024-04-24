import pytest
from pages.page_obj.navbar import NavbarMenuOp_PL


@pytest.mark.run
def test_navbar_correct_links(navbar: NavbarMenuOp_PL, pytestconfig: pytest.Config) -> None:
    navbar.load(path=navbar.path)
    navbar.check_menu_root()
