# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP_URL = 'http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_create_new_user():
    username = "testuser"
    password = "testpassword"
    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    login_btn_signup = driver.find_element("id", "signup")
    login_btn_signup.click()

    signup_input_username = driver.find_element(
        'xpath', '//input[@placeholder="Username"]')
    signup_input_username.send_keys(username)

    signup_input_password = driver.find_element(
        'xpath', '//input[@placeholder="Password"]')
    signup_input_password.send_keys(password)

    signup_btn = driver.find_element('xpath', '//button[text()="Sign Up"]')
    signup_btn.click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Acceptera alerten
    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(2)

    login_btn_signup = driver.find_element("xpath", '//button[text()="Login"]')
    login_btn_signup.click()

    login_input_username = driver.find_element(
        'xpath', '//input[@placeholder="Username"]')
    login_input_username.send_keys(username)

    login_input_password = driver.find_element(
        'xpath', '//input[@placeholder="Password"]')
    login_input_password.send_keys(password)

    login_btn = driver.find_element('xpath', '//button[text()="Login"]')
    login_btn.click()
    time.sleep(2)
    product_name = "Test Product"

    product_input = driver.find_element(
        'xpath', '//input[@placeholder="Product Name"]')
    product_input.send_keys(product_name)

    add_product_btn = driver.find_element(
        'xpath', '//button[text()="Create Product"]')
    add_product_btn.click()

    product_in_list = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            ('xpath', f"//*[text()='{product_name}']"))
    )
    assert product_in_list is not None, "Product was not added successfully"

    time.sleep(5)

    # Teardown
    driver.quit()
