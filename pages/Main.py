# Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class MainPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

        # Page elements

    locators = {
        "page_logo": ('XPATH', '//*[@id="header_container"]/div[1]/div[2]/div'),
        "side_menu": ('XPATH', '//*[@id="react-burger-menu-btn"]'),
        "about_page": ('XPATH', '//*[@id="about_sidebar_link"]'),
    }

    def get_logo_text(self):
        return self.page_logo

    def open_side_menu(self):
        self.side_menu.click()

    def navigate_to_about(self):
        self.about_page.click()

