class CategoryPage_locators:
    ADD_TO_CART_BTNS = "//button[@title='Dodaj do koszyka']"
    SHOW_AMOUNT = "(//select[@data-role='limiter'])[1]"
    SORTING_LIST = "//div[@class='toolbar-sorter sorter']/select[@id='sorter'][1]"
    SORTING_ARROW_malejacy = "//a[@title='Ustaw kierunek malejący']"
    SORTING_ARROW_rosnacy = "//a[@title='Ustaw kierunek rosnący']"
    PRODS_ON_LISTING = "//div[@class='product-item-info type1']"
    PAGINATION = "//ul[@class='items pages-items']"

    FILTER_PRICE = "//div[normalize-space()='Cena']"
    FILTER_MATERIAL = "//div[contains(text(),'Materiał')]"
    FILTER_KOLEKCJA = "//div[normalize-space()='Kolekcja']"
    FILER_TIME = "//div[normalize-space()='Czas realizacji']"
    FILTER_WYKONCZENIE = "//div[contains(text(),'Rodzaj wykończenia')]"

    PRICES_ON_LISTING = "//span[@class='price-wrapper ']/span[@class='price']"
    PROD_NAMES = "//strong[@class='product name product-item-name']/a[@class='product-item-link']"

    NEXT_PAGE = "(//li[@class='item pages-item-next'])[2]"

    PRICE = "(//span[@class='price-wrapper ']//span[@class='price'])[1]"