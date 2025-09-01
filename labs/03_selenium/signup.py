# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL='http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def test_create_new_user():

    #Arrange
    username = "test_user"
    password = 'testtest123'
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    login_btn_signup = driver.find_element("id", "signup")
    login_btn_signup.click()

    signup_input_username = driver.find_element('xpath','//input[@placeholder="Username"]')
    signup_input_username.send_keys(username)

    signup_input_password = driver.find_element('xpath','//input[@placeholder="Password"]')
    signup_input_password.send_keys(password)

    #Act
    

    time.sleep(5)