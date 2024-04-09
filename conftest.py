import pytest
from playwright.sync_api import Page
from pages.page_obj.navbar import Navbar
from pages.page_obj.main_page import MainPage
from pages.page_obj.prod_page import ProdPage
from pages.page_obj.login_page import LoginPage
from pages.page_obj.cart_page import CartPage
from pages.page_obj.checkout_page import CheckoutPage


@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # 'storage_state': './state.json',
        'viewport': {
            'width': 1200,
            'height': 1080,
        },

    }


@pytest.fixture()
def navbar(page: Page):
    return Navbar(page)


@pytest.fixture()
def main_page(page: Page):
    return MainPage(page)


@pytest.fixture()
def prod_page(page: Page):
    return ProdPage(page)


@pytest.fixture()
def login_page(page: Page):
    # new_context(storage_state="state.json")
    return LoginPage(page)


@pytest.fixture()
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture()
def checkout_page(page: Page):
    return CheckoutPage(page)
