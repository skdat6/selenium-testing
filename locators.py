from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    MAIN_PAGE_LOGO = (By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
