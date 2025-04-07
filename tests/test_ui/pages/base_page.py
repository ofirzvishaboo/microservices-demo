# pages/base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_displayed(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def open(self, url):
        self.driver.get(url)
