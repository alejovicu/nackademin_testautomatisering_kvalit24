from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 28/8: DONE (simplified logic + added some explicit waits to practice)

APP_URL='http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def test_verify_admin():

    # SET-UP
    username = "admin"
    password = "admin123"
    new_product = f"product_{int(time.time())}"

    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    # SIGN UP
    login_btn_signup = driver.find_element(By.ID, "signup")
    login_btn_signup.click()

    sign_username_input_locator = driver.find_element(By.XPATH, '(//input)[@placeholder="Username"]')
    sign_password_input_locator = driver.find_element(By.XPATH, '(//input)[@placeholder="Password"]')
    sign_username_input_locator.send_keys(username)
    sign_password_input_locator.send_keys(password)

    signup_button_locator = driver.find_element(By.CSS_SELECTOR, 'button.button-primary')
    signup_button_locator.click()

    # WAIT FOR ALERT AND ACCEPT
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # LOG IN
    back_to_login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-blue")
    back_to_login_button.click()

    login_username = driver.find_element(By.XPATH, '(//input)[@placeholder="Username"]')
    login_username.send_keys(username)

    login_password = driver.find_element(By.XPATH, '(//input)[@placeholder="Password"]')
    login_password.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, 'button.button-primary')
    login_button.click()

    time.sleep(2)

    # CHECK IF ADMIN
    create_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Create Product')]")
    assert len(create_buttons) > 0, "No create-button found - user is not admin"

    # CREATE NEW PRODUCT
    initial_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item"))

    new_product_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Product Name"]')))
    create_product_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Create Product']")))

    new_product_input.send_keys(new_product)
    create_product_button.click()

    time.sleep(1)

    # CHECK IF PRODUCT IS ADDED
    updated_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item"))
    assert updated_count == initial_count + 1, "List length is not as expected"

    updated_products = driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")
    newly_added = updated_products[-1]
    product_name_text = newly_added.text
    assert new_product in product_name_text, "New product name is not as expected"

    # TEARDOWN
    driver.quit()