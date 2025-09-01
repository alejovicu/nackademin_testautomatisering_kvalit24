from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

APP_URL = "http://localhost:5173"


def signup(driver, wait, username, password):
    """Sign up a new user."""
    driver.get(APP_URL)
    wait.until(EC.element_to_be_clickable((By.ID, "signup"))).click()

    username_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
    )
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    signup_button = driver.find_element(
        By.XPATH, "//button[contains(text(),'Sign Up')]"
    )

    username_input.send_keys(username)
    password_input.send_keys(password)
    signup_button.click()
    time.sleep(2)  # Allow alert or confirmation
    print(f"Signup completed for user: {username}")


def login_and_add_product(driver, wait, admin_user, admin_pass, product_name):
    """Login as admin and add a product."""
    driver.get(APP_URL)

    username_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
    )
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")

    username_input.send_keys(admin_user)
    password_input.send_keys(admin_pass)
    login_button.click()

    product_input = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Product Name']")
        )
    )
    create_button = driver.find_element(
        By.XPATH, "//button[contains(text(),'Create Product')]"
    )

    product_input.send_keys(product_name)
    create_button.click()

    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "product-grid"), product_name)
    )
    print(f"Product '{product_name}' added successfully.")


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Sign up a new user
        signup(driver, wait, "testuser123", "password123")

        # Step 2: Login as admin and add a product
        login_and_add_product(driver, wait, "admin", "password", "New Product Test")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
