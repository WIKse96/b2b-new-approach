from playwright.sync_api import Page
from pages.locators.checkout_page_locators import CheckoutPage_locators as cp_loc
from pages.page_obj.base_page import BasePage
from faker import Faker

class CheckoutPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.page = page
        self.new_address_btn = page.locator(cp_loc.NEW_ADDRESS_BTN)
        self.address = page.locator(cp_loc.ADDRESS)
        self.dpd = page.locator(cp_loc.DELVERY_METH_DPD)
        self.flatrate = page.locator(cp_loc.DELVERY_METH_OWN_TR)
        self.comment_input = page.locator(cp_loc.COMMENT_INPUT)
        self.next_btn = page.locator(cp_loc.NEXT_BTN)
        self.payment_meth = page.locator(cp_loc.PAYMENT_METH)
        self.order_btn = page.locator(cp_loc.ORDER_BTN)
        self.status_payment = page.locator(cp_loc.STATUS_PAYMENT)
        self.status_delivery = page.locator(cp_loc.STATUS_DELIVERY)
        self.discout_input = page.locator(cp_loc.DISCOUNT_CODE_INPUT)
        self.submit_discount_btn = page.locator(cp_loc.SUBMIT_DISCOUNT)

    def simple_order(self, delivery: str='dpd', comment: str='testSDCSDSFDf', discount: int=1):
        if delivery not in ['dpd', 'flatrate']:
            raise ValueError("Argument powinien być 'dpd' albo 'flatrate'")
        if delivery == 'dpd':
            self.dpd.click()
        else:
            self.flatrate.click()
        if discount > 1 or discount < 0:
            raise ValueError("Argument powinien być >0 i <=1")
        if comment:
            Faker().text()
        self.next_btn.click()
        self.payment_meth.click()
        self.order_btn.click()

    def add_new_address(self,country:str ,save_address:bool):
        pass
        #