# todo: Asercje czy wszystko się wyświetla. Dodanie nowego adresu, dodawnie nowego adresu rozliczeniowego, sprawdzenie zamówień, podgląd zamówień, zamów ponownie, usunięcie adresu, edycja adresu,
import pytest

from pages.page_obj.account_page import AccountPage

@pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [{'storage_state': './state_login.json'}])
def test_change_data(account_page: AccountPage):
    account_page.load(account_page.path, wait='domcontentloaded')
    # Podaj podstronę na której jesteś żeby sprawdzić czy ma klasę "current"
    account_page.verify_nav("Moje konto")
    account_page.change_contact_data("rikor", "wiktorowicz", 'nowy nip', False)

# @pytest.mark.run
@pytest.mark.parametrize("browser_context_args", [{'storage_state': './state_login.json'}])
def test_set_default(account_page: AccountPage):
    account_page.load(account_page.path, wait='domcontentloaded')

    account_page.change_contact_data("wiktor", "TEST", 'ze sklepu PL', True)