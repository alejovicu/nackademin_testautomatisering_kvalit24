import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException


APP_URL = "http://localhost:5173/" 


class AdminAddProductTest(unittest.TestCase):

    def setUp(self):
        """Set up ChromeDriver with options and open the app"""
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.username = "admin"
        self.password = "123456789"
        self.new_product_name = f"product_{int(time.time())}"
        self.driver.get(APP_URL)

    def tearDown(self):
        """Close browser even if test fails"""
        self.driver.quit()

    def handle_alert_if_present(self):
        """Accept any alert and print its text (for debugging)"""
        try:
            alert = self.driver.switch_to.alert
            print("Alert text:", alert.text)
            alert.accept()
        except NoAlertPresentException:
            pass

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

        # Wait for alert and accept
        try:
            w.until(EC.alert_is_present())
            self.handle_alert_if_present()
        except TimeoutException:
            self.fail("Ingen alert dök upp efter registrering – registreringen kan ha misslyckats.")

        # --- LOGIN ---
        w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-blue"))).click()

        w.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys(self.username)
        d.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(self.password)
        d.find_element(By.CSS_SELECTOR, "button.button-primary").click()

        # Kolla om login misslyckades och en alert visades
        try:
            short_wait = WebDriverWait(d, 3)
            short_wait.until(EC.alert_is_present())
            self.handle_alert_if_present()
            self.fail("Inloggning misslyckades")
        except TimeoutException:
            pass

        # --- VERIFY ADMIN ACCESS ---
        try:
            create_buttons = w.until(lambda drv: drv.find_elements(By.XPATH, "//button[contains(text(),'Create Product')]"))
        except TimeoutException:
            self.fail("'Create Product'-knappen hittades inte – troligen inte inloggad som admin.")

        self.assertGreater(len(create_buttons), 0, "Admin privileges saknas – 'Create Product' inte synlig.")

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

        self.assertIn(self.new_product_name, product_name, "Ny produkt visas inte i listan.")

        print(f"Product '{self.new_product_name}' lades till av admin!")

if __name__ == "__main__":
    unittest.main()