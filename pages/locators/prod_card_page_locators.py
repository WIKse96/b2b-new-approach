class ProdCardPage_locators:
    # Locators for grouped products
    SKU_GR = "//div[@class='value']"
    SKU_SIMPLE_marked = "//div[@class='sku sku-grupped']/mark"
    QTY_CONTROL_PRGR_1ST = "//div[@class='control qty']"

    SPEC_GR = '//div[contains(@class, "grouped-product-specyfication")]'
    SPEC_CONTAINER = "//dib[@id='newsPreview']"
    SPEC_CLOSE_BTN = "//div[@class='specification-close']"
    SPEC_BODY = "//div[@id='newsPreview']/table/tbody"
    DOWNLOAD = "//span[@class='mp-attachment-tab__item__name']"

    # Locators for simple products
    PRICE= "//span[@class='price']"

    ADDTOCART_BTN = "//button[@type='submit'][@id='product-addtocart-button']"
    ADDTOCART_BTN_PRGR = "//button[@type='submit'][@id='product-addtocart-button']"
    QTY_INPUT = "//input[@id='qty'][@type='number']"
    QTY_UP_ARROW = "//i[@class='porto-icon-up-dir']"
    QTY_DOWN_ARROW = "//i[@class='porto-icon-down-dir']"
