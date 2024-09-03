from playwright.sync_api import Page


class AccountPageLocators:
    H1 = "//span[@class='base']"
    NAV_ACCOUNT = "//ul[@class='nav items']"
    CONTACT_DATA = "//div[@class='box box-information']/div[@class='box-content']/p"
    CHANGE_CONTACT_DATA = "//div[@class='box box-information']//span[contains(text(),'Zmień')]"
    DATA_P = "//div[@class='box box-information']//span[contains(text(),'Zmień')]"

    # metody dla get by text, role i label
    @staticmethod
    def name_by_label(page: Page):
        return page.get_by_label("Imię")

    @staticmethod
    def surname_by_label(page: Page):
        return page.get_by_label("Nazwisko")

    @staticmethod
    def NIP_by_label(page: Page):
        return page.get_by_label("NIP")

    @staticmethod
    def save_data(page: Page):
        return page.get_by_role("button", name="Zapisz")

    @staticmethod
    def data_saved_info(page: Page):
        return page.get_by_text("Dane konta zostały zapisane.")
