from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_login_and_add_product():
    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    username_input = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username_input.send_keys("admin")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_input.send_keys("1234")

    login_btn = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_btn.click()

    time.sleep(3)  # wait 3 seconds.

    product_input = driver.find_element(
        By.XPATH, "//input[@placeholder='Product Name']"
    )

    product_name = "Lydias smörgås"
    product_input.send_keys(product_name)

    time.sleep(3)  # wait 3 seconds.

    create_btn = driver.find_element(By.XPATH, "//button[text()='Create Product']")
    create_btn.click()

    time.sleep(3)  # wait 3 seconds.

    product_in_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='{product_name}']"))
    )
    assert product_in_list is not None, "Product was not added successfully"

    time.sleep(3)  # wait 3 seconds.

    driver.quit()
