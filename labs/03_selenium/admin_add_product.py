
# Given I am an admin user​

# When I add a product to the catalog​

# Then The product is available to be used in the app


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL='http://localhost:5173/'



options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_admin_add_product():

    username = "admin"
    password = "1234"
    product_name = "Laddare"


    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    username_input = driver.find_element(By.XPATH,"//input[@placeholder='Username']")
    username_input.send_keys(username)
    password_input = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
    password_input.send_keys(password)

    login_btn = driver.find_element(By.XPATH,"//button[text()='Login']")
    login_btn.click()

    time.sleep(5)


    product_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Product Name']")
    
    product_input.send_keys(product_name)

    time.sleep(5)

    create_btn = driver.find_element(By.XPATH, "//button[text()='Create Product']")
    create_btn.click()

    time.sleep(5)

    product_list = driver.find_element(By.CLASS_NAME, "product-grid")
    assert product_name in product_list.text, "Product was not added successfully"

    
    driver.quit()

