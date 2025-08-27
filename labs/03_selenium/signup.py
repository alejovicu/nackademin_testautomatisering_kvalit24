# Given I am a potential customer
# When I signup in the app
# Then I should be able to log in with my new user
# Given I am an authenticated user
# When I log in into the application
# Then I should see all my products

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

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

    # Act
    #

    time.sleep(10)

    # Teardown
    driver.quit()
