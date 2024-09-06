from playwright.sync_api import Page


class AccountPageLocators:
    H1 = "//span[@class='base']"
    NAV_ACCOUNT = "//ul[@class='nav items']"
    CONTACT_DATA = "//div[@class='box box-information']/div[@class='box-content']/p"
    CHANGE_CONTACT_DATA = "//div[@class='box box-information']//span[contains(text(),'Zmień')]"
    DATA_P = "//div[@class='box box-information']//span[contains(text(),'Zmień')]"
    H2_PASS_OR_EMAIL = "//span[@class='change-email-password']"
    CURRENT_PASSW_ERROR = "//div[@id='current-password-error']"
    CURRENT_EMAIL_ERROR = "//div[@id='email-error']"
    NEW_PASSW_ERROR = "//div[@id='password-error']"
    CONFIRM_PASSW_ERROR = "//div[@id='password-confirmation-error']"

    # metody dla get by text, role i label
    @staticmethod
    def confirm_passw_input(page: Page):
        return page.get_by_label("Potwierdź nowe hasło")
    @staticmethod
    def save_data_btn(page: Page):
        return page.get_by_role("button", name="Zapisz")
    @staticmethod
    def email_input(page: Page):
        return page.get_by_label("E-mail", exact=True)
    @staticmethod
    def new_password_input(page: Page):
        return page.get_by_text("Zmień hasło")
    @staticmethod
    def current_password_input(page: Page):
        return page.get_by_label("Bieżące hasło")
    @staticmethod
    def passw_input(page: Page):
        return page.get_by_label("Bieżące hasło")
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

    @staticmethod
    def change_email_checkbox(page: Page):
        return page.get_by_label('Zmień adres email')

    @staticmethod
    def change_password_checkbox(page: Page):
        return page.get_by_label('Zmień hasło')
