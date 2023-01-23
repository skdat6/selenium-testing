# Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    # Page elements
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    submit_button = (By.ID, "login-button")

    def set_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
