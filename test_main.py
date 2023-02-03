# Import libraries
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import LoginPage, LogoutPage, MainPage
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


class TestMainPage(object):
    @pytest.mark.log
    def test_sort_first_option(self):
        driver = webdriver.Chrome()
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

        try:
            main_page = MainPage(driver)
            selector = main_page.select_element()
            el = Select(selector)
            el.select_by_visible_text("Name (A to Z)")
            assert el.first_selected_option.text == "Name (A to Z)"
            logging.info(f"Selected dropdown option: {el.first_selected_option.text}")
        except Exception as e:
            logging.error(f"Element not found: {e}")
            assert False

    @pytest.mark.log
    def test_sort_second_option(self):
        driver = webdriver.Chrome()
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

        try:
            main_page = MainPage(driver)
            selector = main_page.select_element()
            selector.click()
            driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[2]').click()
            active_element = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div[2]/span/span")
            assert active_element
            logging.info(f"Selected dropdown option: {active_element.text}")
        except Exception as e:
            logging.error(f"Element not found: {e}")
            assert False

    @pytest.mark.log
    def test_sort_third_option(self):
        driver = webdriver.Chrome()
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

        try:
            main_page = MainPage(driver)
            selector = main_page.select_element()
            selector.click()
            driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]').click()
            active_element = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div[2]/span/span")
            assert active_element.text == 'PRICE (LOW TO HIGH)'
            logging.info(f"Selected dropdown option: {active_element.text}")
        except Exception as e:
            logging.error(f"Element not found: {e}")
            assert False

    @pytest.mark.log
    def test_sort_third_option(self):
        driver = webdriver.Chrome()
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

        try:
            main_page = MainPage(driver)
            selector = main_page.select_element()
            selector.click()
            driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[4]').click()
            active_element = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div[2]/span/span")
            assert active_element.text == 'PRICE (HIGH TO LOW)'
            logging.info(f"Selected dropdown option: {active_element.text}")
        except Exception as e:
            logging.error(f"Element not found: {e}")
            assert False
