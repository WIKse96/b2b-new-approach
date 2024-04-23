import pytest
from secret_conf import PASSWORD, USERNAME
from pages.page_obj.login_page import LoginPage


@pytest.mark.login
def test_login(login_page: LoginPage):
    login_page.load(path=login_page.path)
    login_page.login(USERNAME, PASSWORD)
    login_page.save_context()

# @pytest.mark.run
def test_login_incorrect_email(login_page: LoginPage):
    pass

# @pytest.mark.run
def test_login_icorrect_password(login_page: LoginPage):
    pass


