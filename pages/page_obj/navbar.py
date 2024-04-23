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
