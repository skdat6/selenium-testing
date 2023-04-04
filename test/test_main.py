# Import libraries
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.Login import LoginPage
from pages.Main import MainPage


@pytest.mark.log
def test_login():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.select_normal_user()
    login_page.select_password()
    login_page.click_login()

    main_page = MainPage(driver)
    logo_text = main_page.get_logo_text().text
    expected_text = 'Swag Labs'

    assert logo_text == expected_text, f'Expected {expected_text}, but got {logo_text}'
