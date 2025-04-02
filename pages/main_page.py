# pages/main_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    LOGIN_LOCATOR = (By.CSS_SELECTOR, 'li[id="login"]')
    REGISTER_LOCATOR = (By.CSS_SELECTOR, 'li[id="register"]')

    def check_login_button(self):
        assert self.is_displayed(self.LOGIN_LOCATOR), "Login button not found"
        assert self.get_text(self.LOGIN_LOCATOR) == "Login", "Login button text is incorrect"
        self.click(self.LOGIN_LOCATOR)

    def check_register_button(self):
        assert self.is_displayed(self.REGISTER_LOCATOR), "Register button not found"
        assert self.get_text(self.REGISTER_LOCATOR) == "Register", "Register button text is incorrect"
        self.click(self.REGISTER_LOCATOR)
