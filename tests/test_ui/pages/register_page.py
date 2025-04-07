from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    USERNAME_LOCATOR = (By.ID, "register-username")
    EMAIL_LOCATOR = (By.ID, "register-email")
    PASSWORD_LOCATOR = (By.ID, "register-password")
    CONFIRM_PASSWORD_LOCATOR = (By.ID, "register-confirm-password")
    SUBMIT_LOCATOR = (By.ID, "register-submit")
    ERROR_MESSAGE_LOCATOR = (By.CLASS_NAME, "error-message")

    def enter_username(self, username):
        self.type_text(self.USERNAME_LOCATOR, username)

    def enter_email(self, email):
        self.type_text(self.EMAIL_LOCATOR, email)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_LOCATOR, password)

    def enter_confirm_password(self, password):
        self.type_text(self.CONFIRM_PASSWORD_LOCATOR, password)

    def click_submit(self):
        self.click(self.SUBMIT_LOCATOR)

    def register(self, username, email, password):
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_submit()

    def get_error_message(self):
        try:
            return self.get_text(self.ERROR_MESSAGE_LOCATOR)
        except:
            return None