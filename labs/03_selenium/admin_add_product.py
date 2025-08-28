from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


## Given I am an admin user​.
def test_signup_admin():
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)
    # Arrange
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

    time.sleep(2)  # wait

    signup_btn_signup = driver.find_element(
        "xpath", "//button[@class='button-primary']"
    )
    signup_btn_signup.click()

    time.sleep(2)  # wait

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

    time.sleep(2)  # wait

    login_btn_login = driver.find_element("xpath", "//button[@class='button-primary']")
    login_btn_login.click()

    time.sleep(2)  # wait

    ## When I add a product to the catalog​.
    product_name_input = driver.find_element(
        "xpath", "//input[@placeholder='Product Name']"
    )
    product_name_input.send_keys(product_name)

    time.sleep(2)  # wait

    create_product_btn = driver.find_element(
        "xpath", "//button[text()='Create Product']"
    )
    create_product_btn.click()
    # Create Product
    time.sleep(2)  # wait

    ## Then The product is available to be used in the app. Assert thet the product is added. assertEqual(a,b) = product-item or assertIn(a,b) b=product-item
    product_item = driver.find_element(
        "xpath", "//span[text()= '" + product_name + "' ]"
    )
    assert product_item.text == product_name

    time.sleep(2)  # wait

    # Teardown
    driver.quit()
