from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

APP_URL='http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def test_navigate_to_signup():

    #Arrange
    username = "admin"
    password = "pass1234"
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    login_btn_signup = driver.find_element('id', "signup")
    login_btn_signup.click()

    signup_input_username = driver.find_element('xpath', '//input[@placeholder="Username"]')
    signup_input_username.send_keys(username)

    signup_input_password = driver.find_element('xpath', '//input[@placeholder="Password"]')
    signup_input_password.send_keys(password)

    login_btn_signup = driver.find_element('xpath', '//button[text()="Sign Up"]')
    login_btn_signup.click()

    # WebDriverWait to make sure it waits for the modal/alert comes up.(to avoid crash)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept() 

    login_btn_signup = driver.find_element('xpath', '//button[text()="Login"]')
    login_btn_signup.click()

    login_input_username = driver.find_element('xpath', '//input[@placeholder="Username"]')
    login_input_username.send_keys(username)

    login_input_password = driver.find_element('xpath', '//input[@placeholder="Password"]')
    login_input_password.send_keys(password)

    login_btn_signup = driver.find_element('xpath', '//button[text()="Login"]')
    login_btn_signup.click()





    time.sleep(5) # wait 3 seconds.



    # Teardown
    driver.quit()