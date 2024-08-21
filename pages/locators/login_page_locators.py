class LoginPage_locators:
    EMAIL_INPUT = "//input[@id='email']"
    PASS_INPUT = "//fieldset[@class='fieldset login']//input[@id='pass']"
    LOGIN_BTN = "(//div[@class='actions-toolbar']/div[@class='primary']/button[@id='send2' and @name='send'])[1]"
    GOTO_CHECKOUT_BTN = "//span[contains(text(),'Przejdź do kasy')]"
    ERROR_LOGIN = "//div[@data-bind='html: message.text']"
    EMAIL_ERROR = "//div[@id='email-error']"
    PASS_ERROR = "//div[@id='pass-error']"
