# Given I am an admin user​

# When I add a product to the catalog​

# Then The product is available to be used in the app


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


####     RUN signup.py to add admin credentials     ####


def test_sign_in_and_add_and_validate_product():
    # Arrange & Act
    username = "admin"
    password = "admin123"
    product_name = "Laptop"
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    #### Sign in
    signin_username_input = driver.find_element(
        "xpath", '//input[@placeholder="Username"]'
    )

    signin_username_input.send_keys(username)

    password_input = driver.find_element("xpath", "//input[@placeholder='Password']")

    password_input.send_keys(password)

    login_btn = driver.find_element("xpath", "//button[@class='button-primary']")

    login_btn.click()

    time.sleep(2)  # wait 2 seconds.

    #### Add product

    product_input = driver.find_element(
        By.XPATH, "//input[@placeholder='Product Name']"
    )

    product_input.send_keys(product_name)

    create_product_btn = driver.find_element(
        "xpath", "//button[text()='Create Product']"
    )

    create_product_btn.click()

    # Assert

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{product_name}']"))
        )
    except TimeoutException:
        raise AssertionError("Product was not added successfully")

    # Teardown
    driver.quit()
