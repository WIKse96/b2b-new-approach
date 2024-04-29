from playwright.sync_api import Page
from pages.locators.base_page_locators import BasePageLocators


class BasePage:
    URL: str
    URL = 'https://b2b.seartgroup.com'

    def __init__(self, page: Page) -> None:
        self.page = page

    # Metoda używana do otwarcia danej strony. lngVersion - kod językowy sklepu. Na razie oprogramowany jest tylko pl
    def load(self, path: str = '', lngVersion: str = 'pl') -> None:
        # Zwraca ścieżkę pełnego url. Baza/wersja językowa/reszta ścieżki podana w klasie definiującej obiekty.
        full_url = f'{self.URL}/{lngVersion}/{path}'  # Pełny adres URL
        self.page.goto(full_url)
