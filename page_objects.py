# Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import LoginPageLocators, MainPageLocators


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    # Page elements
    username_input = LoginPageLocators.USERNAME_INPUT
    password_input = LoginPageLocators.PASSWORD_INPUT
    login_button = LoginPageLocators.LOGIN_BUTTON

    def set_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit_form(self):
        self.driver.find_element(*self.login_button).click()


class LogoutPage(object):
    def __init__(self, driver):
        self.driver = driver

    # Page elements
    logout_button = MainPageLocators.LOGOUT_BUTTON

    def logout_user(self):
        self.driver.find_element(*self.logout_button).click()


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver

    selector = MainPageLocators.SORT_SELECT

    def select_element(self):
        return self.driver.find_element(*self.selector)

