import time

from pages.locators.navbar_locators import NavbarLocators
from pages.page_obj.base_page import BasePage
from playwright.sync_api import Page



class NavbarMenuOp_PL(BasePage):
    path = ""

    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = page.locator(NavbarLocators.NAV_LI)


    def get_all_texts(self):
        print(self.navbar)

    # klikanie po kategorich
    def check_menu_root(self):

        self.page.get_by_role("link", name="Nowości").click()
        current_url = self.page.url
        if "wszystkie" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Meble").click()
        current_url = self.page.url
        if "meble" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Systemy drzwi przesuwnych").click()
        current_url = self.page.url
        if "przesuwnych" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Nogi").click()
        current_url = self.page.url
        if "nogi" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Blaty").click()
        current_url = self.page.url
        if "blaty" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Krany").click()
        current_url = self.page.url
        if "krany" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Akcesoria").click()
        current_url = self.page.url
        if "akcesoria" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Dekoracje").click()
        current_url = self.page.url
        if "dekoracje" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Drzwi rozwierane").click()
        current_url = self.page.url
        if "rozwierane" in current_url:
            pass
        else:
            assert True == False

        self.page.get_by_role("link", name="Wyprzedaż").click()
        current_url = self.page.url
        if "wyprzedaz" in current_url:
            pass
        else:
            assert True == False




