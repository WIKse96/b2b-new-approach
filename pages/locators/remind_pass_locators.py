class Remind_pass_locator:
    SUBMIT_BTN = "//button[@type='submit'][@class='action submit primary']"
    EMAIL_INPUT = "//input[@id='email_address']"
    CAPCHA_INPUT = "//input[@id='captcha_user_forgotpassword']"
    TITLE = "//span[@data-ui-id='page-title-wrapper']"
    CAPCHA = "//img[@class='captcha-img']"
    RELOAD_CAPCHA_BTN = "//button[@type='button'][@class='action reload captcha-reload']/span"
    EMAIL_ERROR = "//div[@id='email_address-error']"
    CAPCHA_ERROR = "//div[@id='captcha_user_forgotpassword-error']"
