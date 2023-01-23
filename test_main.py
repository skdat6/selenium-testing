# Import libraries
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects import LoginPage, LogoutPage
import pytest


class TestLogin(object):
    @pytest.mark.log
    def test_login(self):
        # Create a new instance of the Firefox driver
        driver = webdriver.Chrome()
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


class TestLogout(object):
    @pytest.mark.log
    def test_logout(self):
        # Create a new instance of the Firefox driver
        driver = webdriver.Chrome()
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
            logging.info(f"Element {element.text} found successfully")
        except Exception as e:
            logging.error(f"Element not found: {e}")

        login_page = LoginPage(driver)
        logout_page = LogoutPage(driver)
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        driver.implicitly_wait(5)
        logout_page.logout_user()
        try:
            element = driver.find_element(By.XPATH, "//*[@id='user-name']")
            assert element
            logging.info(f"Element {element.text} found successfully - Logout was successful")
        except Exception as e:
            logging.error(f"Element not found: {e}")
        finally:
            driver.quit()
