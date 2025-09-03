from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_admin_add_product():
    driver = webdriver.Chrome(options=options)

    driver.get(APP_URL)
    time.sleep(2)

    # Login as admin
    username_input = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
    password_input = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')

    login_btn = driver.find_element(By.XPATH, '//button[normalize-space()="Login"]')

    username_input.send_keys("admin")
    password_input.send_keys("1234")
    login_btn.click()
    time.sleep(2)

    # Add product
    product_name = "IT course"
    name_input = driver.find_element(By.XPATH, '//input[@placeholder="Product Name"]')
    create_btn = driver.find_element(By.XPATH, '//button[text()="Create Product"]')

    name_input.send_keys(product_name)
    create_btn.click()
    time.sleep(2)

    # Assert: product is visible in the app
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert product_name in body_text

    driver.quit()
