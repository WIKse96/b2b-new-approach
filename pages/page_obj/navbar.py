from pages.locators.navbar_locators import NavbarLocators
from pages.page_obj.base_page import BasePage
import dataclasses
from playwright.sync_api import Page

@dataclasses.dataclass
class NavbarMenuOp_PL:
    NEWEST: str = "Nowości"
    FURNITURES: str = "Meble"
    SLIDING_DOORS: str = "Systemy drzwi przesuwnych"
    LEGS: str = "Nogi"
    WOOD_TOPS: str = "Blaty"

    def get_all_texts(self):
        return dataclasses.astuple(self)


class Navbar(BasePage):
    path = ''