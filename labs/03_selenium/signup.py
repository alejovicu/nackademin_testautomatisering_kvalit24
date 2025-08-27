from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL= 'http://localhost:5173/'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def test_create_new_user():
    username = "test_user"
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)
    

    login_btn_signup = driver.find_element("id","signup")
    login_btn_signup.click()

    username_input_signup = driver.find_element("xpath", '//*[@id="root"]/div/div/input[1]')
    username_input_signup.send_keys(username)