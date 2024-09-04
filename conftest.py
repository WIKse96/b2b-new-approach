from pathlib import Path
from slugify import slugify
import pytest
from playwright.sync_api import Page
from pages.page_obj.category_page import CategoryPage
from pages.page_obj.contact_page import ContactPage
from pages.page_obj.navbar import NavbarMenuOp_PL
from pages.page_obj.main_page import MainPage
from pages.page_obj.prod_page import ProdPage
from pages.page_obj.login_page import LoginPage
from pages.page_obj.cart_page import CartPage
from pages.page_obj.checkout_page import CheckoutPage
from pages.page_obj.remind_pass_page import LostPasswordPage
from pages.page_obj.account_page import AccountPage


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


# @pytest.fixture()
# def navbar(page: Page):
#     return Navbar(page)


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


@pytest.fixture()
def lostPassword_page(page: Page):
    return LostPasswordPage(page)


@pytest.fixture()
def navbar(page: Page):
    return NavbarMenuOp_PL(page)


@pytest.fixture()
def contact_page(page: Page):
    return ContactPage(page)


@pytest.fixture()
def cat_page(page: Page):
    return CategoryPage(page)

@pytest.fixture()
def account_page(page: Page):
    return AccountPage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file)

        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra