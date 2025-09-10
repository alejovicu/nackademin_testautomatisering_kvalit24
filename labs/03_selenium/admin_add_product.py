from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

APP_URL = 'http://localhost:5173'  # adjust if different

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def admin_add_product():
    # Launch browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(APP_URL)
    time.sleep(2)

    # Login as admin
    driver.find_element(By.ID, "username").send_keys("admin")  # replace with your admin username
    driver.find_element(By.ID, "password").send_keys("adminpassword")  # replace with admin password
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Go to Add Product page
    driver.find_element(By.ID, "add-product-link").click()
    time.sleep(2)

    # Fill in product form
    driver.find_element(By.ID, "product-name").send_keys("Test Product")
    driver.find_element(By.ID, "product-price").send_keys("9.99")
    driver.find_element(By.ID, "submit-button").click()
    time.sleep(2)

    # Verify product is visible in catalog
    if "Test Product" in driver.page_source:
        print("✅ Product successfully added and visible in catalog")
    else:
        print("❌ Product not found in catalog")

    driver.quit()


if __name__ == "__main__":
    admin_add_product()


print("Opening frontend...")
driver.get(APP_URL)

print("Logging in...")
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("adminpassword")
driver.find_element(By.ID, "login-button").click()



