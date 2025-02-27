class MainPage_locators:
    SEARCH_INPUT = "//input[@id='search']"
    SEARCH_BTN = "//button[@title='Szukaj']"
    SEARCH_PROMPTS = "//li[@class='mst-searchautocomplete__item magento_catalog_product']"
    QTY_IN_CART = "//span[@class='counter-number']"
    REMOVE_PROD_FROM_CART = "//a[@title='Usuń produkt']"
    CONFIRM_CLEAR_CART = "//span[normalize-space()='OK']"
    OK_BTN = "//button[@class='action-close']"
    GOTOCHECKOUT_BTN = "//span[contains(text(),'Przejdź do kasy')]"
    CURRENCY_SWITCHER = "(//div[@id='switcher-currency-trigger']//span)[1]"
    CURRENCY_LI = "//ul[@id='ui-id-1']/li/a"

