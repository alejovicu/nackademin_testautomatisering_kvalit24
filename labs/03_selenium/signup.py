from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_create_new_user():
    # Arrange
    username = "admin1"
    password = "1234"
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    # click on signup button
    login_btn_signup = driver.find_element("id", "signup")
    login_btn_signup.click()
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

    # Act
    signup_btn = driver.find_element("xpath", '//*[@id="root"]/div/div/button')
    signup_btn.click()

    time.sleep(2)  # wait 3 seconds.

    # Teardown
    # driver.quit()


def test_login_new_user():
    username = "admin1"
    password = "1234"
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

    # Act
    login_btn.click()

    time.sleep(5)  # wait 3 seconds.
