from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

APP_URL = "http://localhost:5173/"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


@pytest.fixture
def driver():
    d = webdriver.Chrome(options=options)
    d.set_window_size(1280, 900)
    yield d
    d.quit()


def test_signup_typing_password(driver):
    driver.get(APP_URL)

    signup_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signup"))
    )
    signup_btn.click()

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys("pass1234")
    assert password_input.get_attribute("value") == "pass1234"


def test_login_with_username_and_password(driver):
    driver.get(APP_URL)

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    password = driver.find_element(By.ID, "password")

    login_btn = driver.find_element(By.ID, "login")

    username.clear()
    username.send_keys("admin")
    password.clear()
    password.send_keys("pass1234")
    login_btn.click()

    add_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder= 'Product Name']")
        )
    )
    create_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Create Product')]")
        )
    )

    add_product.send_keys("Apple")
    create_button.click()

    add_product = driver.find_element("xpath", '//span[contains(text(),"Apple")]')
    assert add_product.text.strip() == "Apple"

    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
