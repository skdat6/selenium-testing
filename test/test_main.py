# Import libraries
import logging
from datetime import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.Login import LoginPage
from pages.Main import MainPage


@pytest.mark.log
def test_valid_login():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.select_normal_user()
    login_page.select_password()
    login_page.click_login()

    main_page = MainPage(driver)
    logo_text = main_page.get_logo_text().text
    expected_text = 'Swag Labs'

    assert logo_text == expected_text, f'Expected {expected_text}, but got {logo_text}'


@pytest.mark.log
def test_invalid_login():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.select_invalid_user()
    login_page.select_password()
    login_page.click_login()

    actual_message = login_page.get_validation_message()
    expected_message = 'Epic sadface: Username and password do not match any user in this service'

    assert actual_message == expected_message, f'Expected {expected_message}, but got {actual_message}'


@pytest.mark.log
def test_locked_login():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.select_locked_user()
    login_page.select_password()
    login_page.click_login()

    actual_message = login_page.get_validation_message()
    expected_message = 'Epic sadface: Sorry, this user has been locked out.'
    assert actual_message == expected_message, f'Expected {expected_message}, but got {actual_message}'


@pytest.mark.log
def test_about_page():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.select_normal_user()
    login_page.select_password()
    login_page.click_login()

    main_page = MainPage(driver)
    main_page.open_side_menu()
    main_page.navigate_to_about()

    actual_url = driver.current_url
    expected_url = 'https://saucelabs.com/'
    assert actual_url == expected_url, f'Expected {expected_url}, but got {actual_url}'


@pytest.mark.log
def test_add_items_to_cart():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.select_normal_user()
    login_page.select_password()
    login_page.click_login()

    main_page = MainPage(driver)
    shopping_items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    for item in shopping_items:
        add_to_cart_button = item.find_element(By.CSS_SELECTOR, 'button[id^="add-to-cart-"]')
        add_to_cart_button.click()
        logging.info(f'Added item {item.find_element(By.CLASS_NAME, "inventory_item_name").text} to cart')


    # actual_url = driver.current_url
    # expected_url = 'https://saucelabs.com/'
    # assert actual_url == expected_url, f'Expected {expected_url}, but got {actual_url}'

    # const nthButtonSelector = `(//div[@class='inventory_list']//div[@class='inventory_item'])[${nthBtnIndex +
    # 1}]//div[2]//button`; const nthBtn = page.locator(nthButtonSelector); await nthBtn.click(); console.log(await
    # nthBtn.textContent()); expect(await nthBtn.textContent()).toEqual('Remove');


@pytest.mark.log
def test_cart_matches_added_items():
    # Create a new instance of the Firefox driver
    driver = webdriver.Chrome()
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.select_normal_user()
    login_page.select_password()
    login_page.click_login()

    main_page = MainPage(driver)
    shopping_items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    for item in shopping_items:
        add_to_cart_button = item.find_element(By.CSS_SELECTOR, 'button[id^="add-to-cart-"]')
        add_to_cart_button.click()
        logging.info(f'Added item {item.find_element(By.CLASS_NAME, "inventory_item_name").text} to cart')

    items_in_cart = int(main_page.cart_badge_text())
    expected_items = len(shopping_items)

    assert items_in_cart == expected_items, f'Expected {expected_items}, but got {items_in_cart}'