from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL = "http://localhost:5173"

Options = Options()
Options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_admin_add_product():
    # Arrange
    driver = webdriver.Chrome(options=Options)
    driver.get(APP_URL)

    admin_username ="test_user"
    admin_password = "testtest123"

    # login as admin

    driver.find_element("xpath", '//input[@placeholder="Username"]').send_keys(
        admin_username
    )

    driver.find_element("xpath", '//input[@placeholder="Password"]').send_keys(
        admin_password
    )

    driver.find_element("xpath", '//button[text()="Login"]').click()

    time.sleep(5)

    # Act - add new product
   
    driver.find_element("xpath", '//input[@type="text" and @placeholder="Product Name"]').send_keys("Test Product")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)

    # validate product added
    products = driver.find_elements("xpath", '//div[contains(text(), "Testprodukt")]')
    assert len(products) > 0, "Product was not added successfully"

    print("Product added successfully")
    


if __name__ == "__main__":
    test_admin_add_product()