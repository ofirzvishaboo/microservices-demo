# tests/test_frontend.py
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage

@pytest.fixture(scope="session")
def driver():
    driver_path = os.environ.get('DRIVER_PATH')
    options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(service=Service(driver_path))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open("http://localhost")
    return page

def test_homepage_elements(main_page):
    """Test that homepage elements are present"""
    main_page.check_login_button()
    main_page.check_register_button()

# def test_successful_registration(main_page):
#     """Test successful user registration flow"""
#     register_page = main_page.click_register()
#     register_page.register(
#         username="testuser",
#         email="test@example.com",
#         password="Test123!"
#     )
#     assert main_page.is_logged_in(), "User should be logged in after registration"

def test_successful_login(main_page):
    """Test successful login flow"""
    login_page = main_page.click_login()
    login_page.login(
        username="ofir",
        password="123"
    )
    assert main_page.is_logged_in(), "User should be logged in after login"
    login_page.logout()

def test_invalid_login(main_page):
    """Test login with invalid credentials"""
    login_page = main_page.click_login()
    login_page.login(
        username="wronguser",
        password="wrongpass"
    )
    login_page.unclick_login()
    error_message = login_page.get_error_message()
    assert error_message is not None, "Error message should be displayed for invalid login"
    assert not main_page.is_logged_in(), "User should not be logged in with invalid credentials"

# def test_duplicate_registration(main_page):
#     """Test registration with existing username"""
#     register_page = main_page.click_register()
#     register_page.register(
#         username="testuser",  # Using same username as in successful registration
#         email="test2@example.com",
#         password="Test123!"
#     )
#     error_message = register_page.get_error_message()
#     assert error_message is not None, "Error message should be displayed for duplicate registration"
#     assert not main_page.is_logged_in(), "User should not be logged in after failed registration"
