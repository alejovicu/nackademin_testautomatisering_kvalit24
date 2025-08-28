from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL='http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# Given I am a new potential customer
# When I signup in the app
# Then I should be able to log in with my new user

def test_registration():
    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    username = "admin"
    password = "admin"
    
    # Act
    login_btn_signup = driver.find_element("id", "signup")
    login_btn_signup.click()
    time.sleep(2)
    username_input_signup = driver.find_element("xpath", '//input[@placeholder="Username"]')
    username_input_signup.send_keys(username)
    password_input_signup = driver.find_element("xpath", '//input[@placeholder="Password"]')
    password_input_signup.send_keys(password)

    signup_button = driver.find_element("xpath", "//button[text()='Sign Up']")
    signup_button.click()

    time.sleep(5)
    
    # Teardown
