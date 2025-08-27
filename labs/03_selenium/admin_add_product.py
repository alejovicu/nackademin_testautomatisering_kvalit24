from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


## Given I am an admin user​.
## When I add a product to the catalog​.
## Then The product is available to be used in the app. Assert thet the product is added.


def test_signup_admin():
    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    username = "Admin_user"
    password = "Automation53"
    product_name = "Asksvin"

    # Act
    login_btn_signup = driver.find_element("id", "signup")

    time.sleep(2)  # wait.

    login_btn_signup.click()

    signup_username_input = driver.find_element(
        "xpath", "//input[@placeholder='Username']"
    )
    signup_username_input.send_keys(username)

    signup_password_input = driver.find_element(
        "xpath", "//input[@placeholder='Password']"
    )
    signup_password_input.send_keys(password)

    time.sleep(5)  # wait 3 seconds.

    signup_btn_signup = driver.find_element(
        "xpath", "//button[@class='button-primary']"
    )
    signup_btn_signup.click()

    time.sleep(5)  # wait 3 seconds.

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(2)  # wait

    signup_btn_login = driver.find_element("xpath", "//button[@class='btn btn-blue']")
    signup_btn_login.click()

    login_username_input = driver.find_element(
        "xpath", "//input[@placeholder='Username']"
    )
    login_username_input.send_keys(username)

    login_password_input = driver.find_element(
        "xpath", "//input[@placeholder='Password']"
    )
    login_password_input.send_keys(password)

    time.sleep(5)  # wait 3 seconds.

    login_btn_login = driver.find_element("xpath", "//button[@class='button-primary']")
    login_btn_login.click()

    time.sleep(5)  # wait 3 seconds.

    product_name_input = driver.find_element(
        "xpath", "//input[@placeholder='Product Name']"
    )
    product_name_input.send_keys(product_name)

    time.sleep(5)  # wait 3 seconds.

    # Teardown
    driver.quit()
