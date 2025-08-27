from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_sign_up():
    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    sign_up_btn = driver.find_element(By.XPATH, "//button[text()='Sign Up']")
    sign_up_btn.click()

    username_input = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username_input.send_keys("Hola")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_input.send_keys("Bandola")

    sign_up_btn = driver.find_element(By.XPATH, "//button[text()='Sign Up']")
    sign_up_btn.click()

    time.sleep(2)  # wait 3 seconds.

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(2)  # wait 3 seconds.

    login_btn = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_btn.click()

    time.sleep(2)  # wait 3 seconds.

    username_input = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username_input.send_keys("Hola")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_input.send_keys("Bandola")

    time.sleep(2)  # wait 3 seconds.

    login_btn = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_btn.click()

    time.sleep(2)  # wait 3 seconds.

    # Teardown
    driver.quit()
    # Act
