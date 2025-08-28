from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_login_admin():
    username = "admin1"
    password = "1234"
    product = "apple"
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    # find login button
    login_btn = driver.find_element("xpath", '//*[@id="root"]/div/div/button')

    # find username placeholder and enter a username
    signup_input_username = driver.find_element(
        "xpath", '//input[@placeholder="Username"]'
    )
    signup_input_username.send_keys(username)
    # find password placeholder and enter a password
    signup_input_password = driver.find_element(
        "xpath", '//input[@placeholder="Password"]'
    )
    signup_input_password.send_keys(password)

    login_btn.click()
    time.sleep(3)  # wait 3 seconds.

    # find product input
    products = driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")
    number_of_products = len(products)

    product_input = driver.find_element("xpath", '//input[@placeholder="Product Name"]')
    product_input.send_keys(product)
    # click create product
    create_product_btn = driver.find_element(
        "xpath", '//*[@id="root"]/div/div/div[2]/button'
    )
    create_product_btn.click()
    time.sleep(3)  # wait 3 seconds.

    #check so one more product has been added 
    products = driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")
    products_after = len(products)
    assert products_after == number_of_products +1

    #check so the new product added is the same as the input value
    new_product = products[-1].find_element(By.TAG_NAME, "span").text
    assert new_product == product