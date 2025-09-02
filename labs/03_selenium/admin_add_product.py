# Given I am an admin user
# When I add a product to the catalog
# Then The product is available to be used in the app

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL='http://localhost:5173'
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
def test_add_product():

    username = "admin"
    password = "admin123"
    product_name = "Iphone 14 Pro Max"

    #Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)
    

    input_username = driver.find_element("xpath", '//input[@placeholder="Username"]')
    input_username.send_keys(username)
    input_password = driver.find_element("xpath", '//input[@placeholder="Password"]')
    input_password.send_keys(password)

    login_btn = driver.find_element("class name", "button-primary")
    login_btn.click()
    print("Login successful")
    time.sleep(2)

    input_product = driver.find_element("xpath", '//input[@placeholder="Product Name"]')
    input_product.send_keys(product_name)
    print("Product name entered")
    time.sleep(2)

    product_list = driver.find_element("class name", "product-grid")
    assert product_name in product_list.text
    print("Product name found in the list")


    # Tear down
    driver.quit()

if __name__ == "__main__":
    test_add_product()