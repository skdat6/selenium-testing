# Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import the page object for the page you want to test
from page_objects import LoginPage

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

# Check that the user was successfully logged in
assert driver.find_element(By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")

# Close the browser
driver.quit()


