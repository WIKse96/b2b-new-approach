import pytest
from secret_conf import PASSWORD, USERNAME
from pages.page_obj.login_page import LoginPage


@pytest.mark.login
def test_login(login_page: LoginPage):
    login_page.load(path=login_page.path)
    login_page.login(USERNAME, PASSWORD)
    login_page.assert_correcnt_login()
    login_page.save_context()

# @pytest.mark.run
def test_login_incorrect_email(login_page: LoginPage):
    login_page.load(path=login_page.log_out_path)
    login_page.load(path=login_page.path)

    login_page.login('USERNAME', PASSWORD)
    login_page.assert_incorrecnt_login()
    login_page.login('dsaosad@op.pl', PASSWORD)
    login_page.assert_incorrecnt_login()
    login_page.login('4566455456', PASSWORD)
    login_page.assert_incorrecnt_login()

# @pytest.mark.run
def test_login_incorrect_password(login_page: LoginPage):
    login_page.load(path=login_page.log_out_path)
    login_page.load(path=login_page.path)
    login_page.login(USERNAME, 'PASSWORD')
    login_page.assert_incorrecnt_login()
    login_page.login(USERNAME, 'dsaosad@op.pl')
    login_page.assert_incorrecnt_login()
    login_page.login(USERNAME, '6576768768768')
    login_page.assert_incorrecnt_login()


