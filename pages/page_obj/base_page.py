from playwright.sync_api import Page
from pages.locators.base_page_locators import BasePageLocators


class BasePage:
    URL: str
    URL = 'https://b2b.seartgroup.com'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self, path: str = '', lngVersion: str = 'pl') -> None:
        full_url = f'{self.URL}/{lngVersion}/{path}'  # Pełny adres URL
        print('**********************************************')
        print(full_url)
        self.page.goto(full_url)
