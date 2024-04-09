class CheckoutPage_locators:
    ADDRESS = "//div[@class='shipping-address-item selected-item']"
    NEW_ADDRESS_BTN = "//span[normalize-space()='Nowy adres']"
    DELVERY_METH_OWN_TR = "//td[@id='label_carrier_flatrate_flatrate']"
    DELVERY_METH_DPD = "//td[@id='label_carrier_Dpdshipping_Dpdshipping']"
    COMMENT_INPUT = "//textarea[@name='customer_notes']"
    NEXT_BTN = "//span[contains(text(),'Następne')]"
    PAYMENT_METH = "//span[@data-bind='text: getTitle()']"
    ORDER_BTN = "//span[contains(text(),'Złóż zamówienie')]"
    STATUS_PAYMENT = "//span[contains(text(),'Podsumowanie i płatność')]" #KLASy complete i active
    STATUS_DELIVERY = "//li[@class='opc-progress-bar-item _complete']//span[contains(text(),'Dostawa')]"
    DISCOUNT_CODE_INPUT = "//input[@id='discount-code']"
    SUBMIT_DISCOUNT = "//span[contains(text(),'Zastosuj zniżkę')]"