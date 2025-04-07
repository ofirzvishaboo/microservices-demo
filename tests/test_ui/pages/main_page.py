# pages/main_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

class MainPage(BasePage):
    LOGIN_LOCATOR = (By.CSS_SELECTOR, 'li[id="login"]')
    REGISTER_LOCATOR = (By.CSS_SELECTOR, 'li[id="register"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def check_login_button(self):
        assert self.is_displayed(self.LOGIN_LOCATOR), "Login button not found"
        assert self.get_text(self.LOGIN_LOCATOR) == "Login", "Login button text is incorrect"
        # self.click(self.LOGIN_LOCATOR)

    def check_register_button(self):
        assert self.is_displayed(self.REGISTER_LOCATOR), "Register button not found"
        assert self.get_text(self.REGISTER_LOCATOR) == "Register", "Register button text is incorrect"
        # self.click(self.REGISTER_LOCATOR)

    def click_login(self):
        login_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li[id='login'] a"))
        )
        assert login_button.is_displayed(), "Login button is not displayed"
        login_button.click()
        return LoginPage(self.driver)

    def click_register(self):
        register_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "register-button"))
        )
        assert register_button.is_displayed(), "Register button is not displayed"
        register_button.click()
        return RegisterPage(self.driver)

    def is_logged_in(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li[id='howdy']"))
            )
            return True
        except:
            return False
