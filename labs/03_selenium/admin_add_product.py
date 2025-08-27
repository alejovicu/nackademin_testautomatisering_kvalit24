from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

APP_URL='http://localhost:5173'
driver.get(APP_URL)

def test_add_product_as_admin():
    username = "admin"
    password = "admin1234"

    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username_field.send_keys(username)
    time.sleep(3)

    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_field.send_keys(password)
    time.sleep(3)


    driver.find_element(By.CSS_SELECTOR,"button.button-primary").click()

    time.sleep(3)

    product_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Product Name']")
    product_field.send_keys("Apple")

    time.sleep(3)

    create_product_button = driver.find_element(By.XPATH, "//button[text()='Create Product']")
    create_product_button.click()

    time.sleep(3)

    product_list = driver.find_element(By.ID, "product-list")
    assert "Apple" in product_list.text, "Product was not added successfully"



    driver.quit()


test_add_product_as_admin()

print("Success")