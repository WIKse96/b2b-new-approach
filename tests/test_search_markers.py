import pytest

from pages.page_obj.main_page import MainPage

@pytest.mark.search
def test_search(main_page: MainPage, pytestconfig: pytest.Config) -> None:
    search_query = 'PRI-80x160'

    main_page.load(path=main_page.path)
    main_page.search(search_query)