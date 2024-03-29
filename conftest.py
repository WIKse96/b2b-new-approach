import pytest
from playwright.sync_api import Page
from pages.page_obj.navbar import Navbar
from pages.page_obj.main_page import MainPage

@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1200,
            'height': 1080,
        },
    }

@pytest.fixture()
def navbar(page:Page):
    return Navbar(page)

@pytest.fixture()
def main_page(page:Page):
    return MainPage(page)