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
    username = "admin_test"
    password = "admin123"
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    signup_btn = driver.find_element("id", "login")
    signup_btn.click()
    time.sleep(1)

    input_username = driver.find_element("xpath", '//input[@placeholder="Username"]')
    input_password = driver.find_element("xpath", '//input[@placeholder="Password"]')

    input_username.send_keys(username)
    input_password.send_keys(password)

    submit_btn = driver.find_element("class name", "button-primary")
    submit_btn.click()
    time.sleep(2)


    #Act
    signup_submit_btn = driver.find_element("class name", "button-primary")
    signup_submit_btn.click()
    print(f"User {username} created")

    time.sleep(5)

    #Tear down
    driver.quit()


if __name__ == "__main__":
    test_create_new_user()