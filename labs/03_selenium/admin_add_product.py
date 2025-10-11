import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ============================================
# TEST: Verify admin can create product
# ============================================

APP_URL = "http://localhost:5173"  # adjust if frontend runs on different port


class AdminAddProductTest(unittest.TestCase):

    def setUp(self):
        """Set up ChromeDriver with options and open the app"""
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.username = "admin"
        self.password = "admin123"
        self.new_product_name = f"product_{int(time.time())}"
        self.driver.get(APP_URL)

    def tearDown(self):
        """Close browser even if test fails"""
        self.driver.quit()

    def test_admin_adds_product(self):
        """Full scenario: Sign up, log in, add product, verify product appears"""

        d = self.driver
        w = self.wait

        # --- SIGN UP ---
        w.until(EC.element_to_be_clickable((By.ID, "signup"))).click()

        username_field = w.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        password_field = d.find_element(By.XPATH, "//input[@placeholder='Password']")
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        d.find_element(By.CSS_SELECTOR, "button.button-primary").click()

        # Wait for alert (account created)
        w.until(EC.alert_is_present())
        d.switch_to.alert.accept()

        # --- LOGIN ---
        w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-blue"))).click()

        w.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys(self.username)
        d.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(self.password)
        d.find_element(By.CSS_SELECTOR, "button.button-primary").click()

        # --- VERIFY ADMIN ACCESS ---
        create_buttons = w.until(lambda drv: drv.find_elements(By.XPATH, "//button[contains(text(),'Create Product')]"))
        self.assertGreater(len(create_buttons), 0, "Admin privileges missing — 'Create Product' not found")

        # --- GET INITIAL PRODUCT COUNT ---
        initial_products = d.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")
        initial_count = len(initial_products)

        # --- CREATE NEW PRODUCT ---
        product_input = w.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Product Name']")))
        create_button = w.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Create Product']")))

        product_input.send_keys(self.new_product_name)
        create_button.click()

        # --- VERIFY PRODUCT ADDED ---
        w.until(lambda drv: len(drv.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")) > initial_count)

        updated_products = d.find_elements(By.CSS_SELECTOR, ".product-grid .product-item")
        last_product = updated_products[-1]
        product_name = last_product.text.strip()

        self.assertIn(self.new_product_name, product_name, "Newly added product name mismatch")

        print(f"✅ Product '{self.new_product_name}' successfully added by admin!")

if __name__ == "__main__":
    unittest.main()
