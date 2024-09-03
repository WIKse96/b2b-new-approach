import pytest
from secret_conf import PASSWORD, USERNAME
from pages.page_obj.login_page import LoginPage
from playwright.sync_api import expect


# Funkcja pomocnicza do logowania i weryfikacji poprawności lub błędów
def perform_login_and_check(
        login_page: LoginPage,
        username: str,
        password: str,
        expected_email_error: str = None,
        expected_pass_error: str = None,
        expect_correct_login: bool = False
):
    login_page.load(path=login_page.path)
    login_page.login(username, password)

    if expect_correct_login:
        login_page.correct_login_info()
        login_page.save_context()
    else:
        if expected_email_error or expected_pass_error:
            errors_dict = login_page.get_errors()
            pass_error = errors_dict.get('pass_error')
            email_error = errors_dict.get('email_error')

            if expected_email_error is not None:
                expect(email_error).to_be_visible() if expected_email_error else expect(email_error).to_be_hidden()

            if expected_pass_error is not None:
                expect(pass_error).to_be_visible() if expected_pass_error else expect(pass_error).to_be_hidden()
        else:
            login_page.incorrect_login_info()


# Parametryzowane testy dla różnych przypadków logowania
@pytest.mark.parametrize("username, password, expected_email_error, expected_pass_error, expect_correct_login", [
    (USERNAME, PASSWORD, None, None, True),  # Poprawne dane logowania
    ('USERNAME', PASSWORD, True, None, False),  # Niepoprawny email
    # (USERNAME, 'PASSWORD', None, True, False),  # Niepoprawne hasło
    # ('USERNAME@op.pl', 'PASSWORD', True, True, False),  # Niepoprawny email i hasło
    ('', '', True, True, False),  # Puste pola email i hasło
    ('', 'jakieshalo123', True, None, False),  # Pusty email
    (USERNAME, '', None, True, False),  # Puste hasło
    ("USERNAME.com", '456987pdp', True, None, False),  # Brak '@' w emailu
    ("USERNAME@com", '456987pdp', True, None, False)  # Brak '.' w emailu
])
@pytest.mark.login
def test_login(login_page: LoginPage, username: str, password: str, expected_email_error: str, expected_pass_error: str,
               expect_correct_login: bool):
    perform_login_and_check(
        login_page=login_page,
        username=username,
        password=password,
        expected_email_error=expected_email_error,
        expected_pass_error=expected_pass_error,
        expect_correct_login=expect_correct_login
    )
