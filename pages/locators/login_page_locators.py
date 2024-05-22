class LoginPage_locators:
    EMAIL_INPUT = "//input[@id='email']"
    PASS_INPUT = "//fieldset[@class='fieldset login']//input[@id='pass']"
    LOGIN_BTN = "//button[@id='send2']"
    GOTO_CHECKOUT_BTN = "//span[contains(text(),'Przejdź do kasy')]"
    ERROR_LOGIN = "//div[@data-bind='html: message.text']"