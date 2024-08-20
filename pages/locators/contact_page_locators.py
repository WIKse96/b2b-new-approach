class ContactPageLocators:
    COMPANY_NAME_INPUT = "//input[@name='name']"
    SUBJECT_INPUT = "//input[@name='subject']"
    EMAIL_INPUT = "//input[@name='email']"
    PHONE_NR_INPUT = "//input[@name='telephone']"
    MESSAGE_INPUT = "//textarea[@name='comment']"
    RODO_CHECKBOX = "//input[@type='checkbox' and @name='rodo']"
    SUBMIT_BTN = "//button[@type='submit' and @title='Wyślij']"
    SPAN1 = "//span[normalize-space()='Napisz do nas']"
    SPAN2 = "//div[@class='contacts-title']"
    PHONE_ICON = "//i[@class='porto-icon-mobile']"
    PHONE_NR_LINK = "//div[@class='row']/div[@class='col-md-12']/a[@href='tel:+48661215912']"
    EMAIL_ICON = "//i[@class='porto-icon-mail-alt']"
    EMAIL_LINK = "//div[@class='row']/div[@class='col-md-12']/a[@href='mailto:cooperation@seartgroup.com']"

   # errors in contact forms
    NAME_ERROR = "//div[@id='name-error']"
    SUBJECT_ERROR = "//div[@id='subject-error']"
    COMMENT_ERROR = "//div[@id='comment-error']"
    EMAIL_ERROR = "//div[@id='email-error']"
    RODO_ERROR = "//div[@id='rodo-error']"
