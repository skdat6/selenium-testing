# Import libraries
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects import LoginPage
import pytest


class TestLogin(object):
    @pytest.mark.log
    def test_login(self):
        # Create a new instance of the Firefox driver
        driver = webdriver.Firefox()

        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")

        # Create an instance of the login page object
        login_page = LoginPage(driver)

        # Fill in the login form and submit it
        login_page.set_username("standard_user")
        login_page.set_password("secret_sauce")
        login_page.submit_form()

        try:
            # Check that the user was successfully logged in
            element = driver.find_element(By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
            assert element
            logging.info("Element %s found successfully", element.text)
        except Exception as e:
            logging.error("Element not found: %s", e)
        finally:
            # Close the browser
            driver.quit()


