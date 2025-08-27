# Given I am a new potential customer
# When I signup into the app
# Then I should be able to log in with my new user

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_navigate_to_signup_and_login():
    # Arrange & Act
    username = "admin"
    password = "admin123"
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    login_btn_signup = driver.find_element("id", "signup")
    login_btn_signup.click()

    ##Signup

    signup_username_input = driver.find_element(
        "xpath", '//input[@placeholder="Username"]'
    )

    signup_username_input.send_keys(username)

    password_input = driver.find_element("xpath", "//input[@placeholder='Password']")

    password_input.send_keys(password)

    signup_btn = driver.find_element("xpath", "//button[@class='button-primary']")

    signup_btn.click()

    time.sleep(3)  # wait 3 seconds.

    ### Go to login page

    alert = driver.switch_to.alert
    alert.accept()

    signup_btn_login = driver.find_element("xpath", "//button[@class='btn btn-blue']")
    signup_btn_login.click()

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

    # Teardown
    driver.quit()
