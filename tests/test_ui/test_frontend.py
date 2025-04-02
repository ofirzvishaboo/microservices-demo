# tests/test_frontend.py
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage

driver_path = os.environ.get('DRIVER_PATH')
options = Options()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=Service(driver_path))
driver.implicitly_wait(10)

try:
    main_page = MainPage(driver)
    main_page.open("http://localhost")

    # Run tests
    main_page.check_login_button()
    main_page.check_register_button()

finally:
    driver.quit()
