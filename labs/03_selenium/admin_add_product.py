from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL='http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# Helper function to login as admin
def admin_login(driver:webdriver):

    # Username and pass should be put in an .env-file in real world scenarios
    username = "admin"
    password = "admin"
    
    # Act
    username_input_login = driver.find_element("xpath", '//input[@placeholder="Username"]')
    username_input_login.send_keys(username)
    password_input_login = driver.find_element("xpath", '//input[@placeholder="Password"]')
    password_input_login.send_keys(password)

    signup_button = driver.find_element("xpath", "//button[text()='Login']")
    signup_button.click()

    time.sleep(5)

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

def test_admin_add_product():

    # Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    product = "Banan"

    admin_login(driver)
    
    # Get the list of available products and store how long it is
    products = driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")
    number_of_products = len(products)

    # Act

    # Create a product
    product_input = driver.find_element("xpath", '//input[@placeholder="Product Name"]')
    product_input.send_keys(product)
    create_product_button = driver.find_element("xpath", "//button[text()='Create Product']")
    create_product_button.click()

    # Wait for the product to show up on the webpage
    time.sleep(3)
    

    # Assert 
    
    # Get the list of available products again and assert that it has gotten longer
    products = driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")
    number_of_products_after = len(products)
    assert number_of_products_after == number_of_products + 1

    # Get the last element in the list of products and assert that it's product name matches our input product name
    added_product = products[-1].find_element(By.TAG_NAME, "span").text
    assert added_product == product

    time.sleep(2)


