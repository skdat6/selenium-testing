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
    }

    def get_logo_text(self):
        return self.page_logo


