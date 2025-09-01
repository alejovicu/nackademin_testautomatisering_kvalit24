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

    #Arrange
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)
    driver.delete_all_cookies()
    time.sleep(1)


    input_username = driver.find_element("xpath", '//input[@placeholder="Username"]')
    input_password = driver.find_element("xpath", '//input[@placeholder="Password"]')

    input_username.send_keys("admin_test")
    input_password.send_keys("admin123")

    submit_btn = driver.find_element("class name", "button-primary")
    submit_btn.click()
    time.sleep(5)

    input_name = driver.find_element("xpath", '//input[@placeholder="name"]')
    input_name.send_keys("Test Product")

    add_product_btn = driver.find_element("id", "add-product")
    add_product_btn.click()
    print("Product added")

    time.sleep(5)

    # Tear down
    driver.quit()

if __name__ == "__main__":
    test_add_product()