#!/usr/bin/env python3
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP_URL = "http://localhost:5173"
API_URL = "http://127.0.0.1:8000"

# >>> Use your admin login <<<
ADMIN_USER = "Daniel-Adminuser"
ADMIN_PASS = "admin123"

# Product name required by the lab validation
TARGET_PRODUCT_NAME = "test product 02"

TIMEOUT = 20
def W(d): return WebDriverWait(d, TIMEOUT)

def api_login_get_token(username: str, password: str) -> str:
    r = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
    r.raise_for_status()
    return r.json()["access_token"]

def api_create_product(token: str, name: str) -> dict:
    r = requests.post(
        f"{API_URL}/products",
        json={"name": name},
        headers={"Authorization": f"Bearer {token}"},
        timeout=10
    )
    r.raise_for_status()
    return r.json()

def test_admin_add_product():
    # --- Start browser
    opts = Options()
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

    try:
        # --- Open app & login
        driver.get(APP_URL)

        user = W(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']")))
        pwd = W(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']")))
        user.clear(); user.send_keys(ADMIN_USER)
        pwd.clear(); pwd.send_keys(ADMIN_PASS)

        # Click Login (try common selectors)
        try:
            W(driver).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        except:
            W(driver).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'], button.button-primary"))).click()

        # Wait for a post-login signal (Logout button present)
        W(driver).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Logout']")))

        # --- Create product via API using fresh admin token
        token = api_login_get_token(ADMIN_USER, ADMIN_PASS)
        api_create_product(token, TARGET_PRODUCT_NAME)

        # --- Refresh UI and assert product is visible
        driver.refresh()
        W(driver).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(normalize-space(.), '{TARGET_PRODUCT_NAME}')]")))

        assert TARGET_PRODUCT_NAME in driver.page_source, f"Product '{TARGET_PRODUCT_NAME}' not visible after creation"
        print(f"✅ SUCCESS: Created and found product: {TARGET_PRODUCT_NAME}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_admin_add_product()
