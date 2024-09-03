import time

import pytest
from secret_conf import EMAIL_FOR_REMIND
from pages.page_obj.remind_pass_page import LostPasswordPage


# @pytest.mark.run
def test_lost_pasword(lostPassword_page: LostPasswordPage):
    lostPassword_page.load(path=lostPassword_page.path)
    lostPassword_page.assertions()
    lostPassword_page.fillout_form(EMAIL_FOR_REMIND)


def test_lost_password_blank(lostPassword_page: LostPasswordPage):
    lostPassword_page.load(path=lostPassword_page.path)
    lostPassword_page.assertions()
    lostPassword_page.blank_inputs()


# @pytest.mark.run
def test_invalid_email(lostPassword_page: LostPasswordPage):
    lostPassword_page.load(path=lostPassword_page.path)
    lostPassword_page.assertions()
    time.sleep(1)
    lostPassword_page.invalid_email()
    lostPassword_page.invalid_capcha()
    lostPassword_page.empty_email()
    lostPassword_page.empty_captcha()
    lostPassword_page.verivy_url()
