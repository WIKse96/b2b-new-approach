import time
import pytest

from playwright.sync_api import Page, expect
from pages.page_obj.base_page import BasePage


class ContactPage(BasePage):
    path = "contact"


    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

