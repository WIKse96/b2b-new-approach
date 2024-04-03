class ProdCardPage_locators:
    # locators for grouped products
    SKU_GROUPED = "//div[@class='value']"
    SKU_SIMPLE_marked = "//div[@class='sku sku-grupped']/mark"
    # locators for simple products
    PRICE_SIMPLE = "//span[@class='price']"
    ADDTOCART_BTN = "//button[@type='submit'][@id='product-addtocart-button']"
    QTY_INPUT = "//input[@id='qty'][@type='number']"
    QTY_UP_ARROW = "//i[@class='porto-icon-up-dir']"
    QTY_DOWN_ARROW = "//i[@class='porto-icon-down-dir']"
