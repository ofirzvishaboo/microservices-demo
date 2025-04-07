from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_LOCATOR = (By.ID, "username-modal")
    PASSWORD_LOCATOR = (By.ID, "password-modal")
    SUBMIT_LOCATOR = (By.CSS_SELECTOR, "p button[class='btn btn-primary']")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "div[id='login-message'] div")
    UNCLICK_LOGIN_LOCATOR = (By.CSS_SELECTOR, "button[class='close']")
    LOGOUT_LOCATOR = (By.CSS_SELECTOR, "li[id='logout'] a")

    def enter_username(self, username):
        self.type_text(self.USERNAME_LOCATOR, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_LOCATOR, password)

    def click_submit(self):
        self.click(self.SUBMIT_LOCATOR)

    def unclick_login(self):
        self.click(self.UNCLICK_LOGIN_LOCATOR)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def logout(self):
        self.click(self.LOGOUT_LOCATOR)

    def get_error_message(self):
        try:
            return self.get_text(self.ERROR_MESSAGE_LOCATOR)
        except:
            return None