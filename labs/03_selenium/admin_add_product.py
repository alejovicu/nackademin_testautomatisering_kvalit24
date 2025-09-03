# Given I am an admin user

# When I add a product to the catalog

# Then the product is available to be used in the app
#----------------------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP_URL = "http://localhost:5173/"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def test_create_user():
    username = "test_nermin"
    password = "pass_1223"
    product_name = "Wallet"

    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)
    time.sleep(2)

    login_btn_signup = driver.find_element("id", "signup")
    login_btn_signup.click()
    time.sleep(3)
    
    signup_input_username = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
    signup_input_username.send_keys(username)

    signup_input_password = driver.find_element('xpath', '//input[@placeholder="Password"]')
    signup_input_password.send_keys(password)

    signup_btn = driver.find_element('xpath', '//button[text()="Sign Up"]')
    signup_btn.click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    
    time.sleep(3)
    
    alert.accept()

# Test for login as a new user
    login_btn = driver.find_element('xpath', '//button[text()="Login"]')
    login_btn.click()

    login_input_username = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
    login_input_username.send_keys(username)

    login_input_password = driver.find_element('xpath', '//input[@placeholder="Password"]')
    login_input_password.send_keys(password)

    login_btn = driver.find_element('xpath', '//button[text()="Login"]')
    login_btn.click()
    
    time.sleep(5)

# Test to add product
    product_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Product Name"]')))

    product_input.send_keys(product_name)

    add_product_btn = driver.find_element(By.XPATH, '//button[text()="Create Product"]')
    add_product_btn.click()

    show_product_list = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='{product_name}']")))

    assert show_product_list is not None, "The product could not be added"
    time.sleep(5)

    driver.quit()
