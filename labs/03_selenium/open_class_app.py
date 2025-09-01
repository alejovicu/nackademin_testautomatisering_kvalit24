from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL='http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def test_navigate_to_signup():

    #Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    login_btn_signup = driver.find_element("id", "signup")

    #Act
    time.sleep(5) # wait 3 seconds.
    login_btn_signup.click()

    time.sleep(5) # wait 3 seconds.



    # Teardown
    driver.quit()
