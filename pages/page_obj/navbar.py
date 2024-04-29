import time

from pages.locators.navbar_locators import NavbarLocators
from pages.page_obj.base_page import BasePage
from playwright.sync_api import Page, expect


class NavbarMenuOp_PL(BasePage):
    path = ""

    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = page.locator(NavbarLocators.NAV_LI)
        self.page = page
        # Locators z get_by_role w init
        self.ROOT_NOWOSCI = page.get_by_role("link", name="Nowości")
        self.ROOT_MEBLE = page.get_by_role("link", name="Meble")
        self.ROOT_DRZWI = page.get_by_role("link", name="Systemy drzwi przesuwnych")
        self.ROOT_NOGI = page.get_by_role("link", name="Nogi")
        self.ROOT_BLATY = page.get_by_role("link", name="Blaty")
        self.ROOT_KRANY = page.get_by_role("link", name="Krany")
        self.ROOT_AKCESORIA = page.locator("//a[@title='Akcesoria']")
        self.ROOT_DEKORACJE = page.get_by_role("link", name="Dekoracje")
        self.ROOT_DRZ_ROZW = page.get_by_role("link", name="Drzwi rozwierane")
        self.ROOT_WYPRZ = page.get_by_role("link", name="Wyprzedaż")

    # Dostań się do rodzica elementu. list_name - string. Jeśli 'parrent' to zwraca listę z tymi elementami, które mają dzieci. W przeciwnym wypadku wypluwa te, które nie mają
    def get_a_list_navbar(self, list_name: str):
        PARRENT_ROOT_DRZWI = self.page.get_by_role("listitem").filter(has=self.ROOT_DRZWI)
        PARRENT_ROOT_NOGI = self.page.get_by_role("listitem").filter(has=self.ROOT_NOGI)
        PARRENT_ROOT_BLATY = self.page.get_by_role("listitem").filter(has=self.ROOT_BLATY)
        PARRENT_ROOT_KRANY = self.page.get_by_role("listitem").filter(has=self.ROOT_KRANY)
        PARRENT_ROOT_AKCESORIA = self.page.get_by_role("listitem").filter(has=self.ROOT_AKCESORIA)
        PARRENT_ROOT_DEKORACJE = self.page.get_by_role("listitem").filter(has=self.ROOT_DEKORACJE)
        PARRENT_ROOT_DRZ_ROZW = self.page.get_by_role("listitem").filter(has=self.ROOT_DRZ_ROZW)
        PARRENT_ROOT_WYPRZ = self.page.get_by_role("listitem").filter(has=self.ROOT_WYPRZ)
        PARRENT_ROOT_MEBLE = self.page.get_by_role("listitem").filter(has=self.ROOT_MEBLE)
        PARRENT_ROOT_NOWOSCI = self.page.get_by_role("listitem").filter(has=self.ROOT_NOWOSCI)
        #
        if list_name == 'parrents':
            parrents = [PARRENT_ROOT_MEBLE, PARRENT_ROOT_DEKORACJE,
                        PARRENT_ROOT_AKCESORIA, PARRENT_ROOT_KRANY,
                        PARRENT_ROOT_DRZWI]
            return parrents
        else:
            noparrents = [PARRENT_ROOT_NOWOSCI, PARRENT_ROOT_WYPRZ, PARRENT_ROOT_DRZ_ROZW,
                          PARRENT_ROOT_BLATY, PARRENT_ROOT_NOGI]
            return noparrents

    def container_submenu(self):
        navbar = NavbarMenuOp_PL(self.page)
        # Dla każdego z rodziców tworzy pętlę, następnie najeżdża na element i sprawdza czy div z klasa container jest widoczny
        for parrent in navbar.get_a_list_navbar('parrents'):

            parrent.hover()
            expect(parrent.locator("div.container")).to_be_visible()
    def without_container_submenu(self):
        navbar = NavbarMenuOp_PL(self.page)
        # Dla każdego z elementów bez submenu tworzy pętlę, następnie najeżdża na element i sprawdza czy div z klasa container jest niewidoczny
        for parrent in navbar.get_a_list_navbar('non'):

            parrent.hover()
            expect(parrent.locator("div.container")).not_to_be_visible()

    def get_submenu_links(self):
        navbar = NavbarMenuOp_PL(self.page)

        for element in navbar.get_a_list_navbar('parrents'):
            element.hover()
            # self.page.pause()

            for li in element.locator("li.ui-menu-item.level1").all():
                element.hover()
                li.click()
                time.sleep(2)


    def get_all_texts(self):
        print(self.navbar)

    # Klika po wszystkich kategoriach i sprawdza czy url zawiera daną frazę. W przeciwny wypadku zraca błąd
    def check_menu_root(self):

        self.ROOT_NOWOSCI.click()
        current_url = self.page.url
        assert "wszystkie" in current_url

        self.ROOT_MEBLE.click()
        current_url = self.page.url
        assert "meble" in current_url

        self.ROOT_DRZWI.click()
        current_url = self.page.url
        assert "przesuwnych" in current_url

        self.ROOT_NOGI.click()
        current_url = self.page.url
        assert "nogi" in current_url

        self.ROOT_BLATY.click()
        current_url = self.page.url
        assert "blaty" in current_url

        self.ROOT_KRANY.click()
        current_url = self.page.url
        assert "krany" in current_url

        self.ROOT_AKCESORIA.click()
        current_url = self.page.url
        assert "akcesoria" in current_url

        self.ROOT_DEKORACJE.click()
        current_url = self.page.url
        assert "dekoracje" in current_url

        self.ROOT_DRZ_ROZW.click()
        current_url = self.page.url
        assert "rozwierane" in current_url


        self.ROOT_WYPRZ.click()
        current_url = self.page.url
        assert "wyprzedaz" in current_url
