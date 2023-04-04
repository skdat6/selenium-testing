# Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    # Page elements
    locators = {
        "login_validation_message": ('XPATH', '//*[@id="login_button_container"]/div/form/div[3]/h3'),
        "username": ('ID', 'user-name'),
        "password": ('ID', 'password'),
        "login_button": ('ID', 'login-button'),
    }

    def select_normal_user(self):
        self.username.set_text("standard_user")

    def select_invalid_user(self):
        self.username.set_text("standard_user2222")

    def select_locked_user(self):
        self.username.set_text("locked_out_user")

    def select_password(self):
        self.password.set_text("secret_sauce")

    def click_login(self):
        self.login_button.click_button()
