import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


APP_URL = "http://localhost:5173"


@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_admin_add_product(driver):
    username = "admin"
    password = "123"
    product = "bord"

    driver.get(APP_URL)

    
    login_input_username = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
    login_input_username.send_keys(username)

    login_input_password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
    login_input_password.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Product Name"]'))
    )

    
    products_before = driver.find_elements(By.XPATH, "//div[contains(@class, 'product-item')]")
    count_before = len(products_before)

   
    create_product_input = driver.find_element(By.XPATH, '//input[@placeholder="Product Name"]')
    create_product_input.clear()
    create_product_input.send_keys(product)

    create_product_button = driver.find_element(By.XPATH, "//button[text()='Create Product']")
    create_product_button.click()

    
    WebDriverWait(driver, 5).until(
        lambda d: len(d.find_elements(By.XPATH, "//div[contains(@class, 'product-item')]")) == count_before + 1
    )

    
    products_after = driver.find_elements(By.XPATH, "//div[contains(@class, 'product-item')]")
    count_after = len(products_after)

    
    assert count_after == count_before + 1, f"Expected {count_before+1} products, but found {count_after}"

   
    product_spans = driver.find_elements(By.XPATH, "//div[contains(@class, 'product-item')]/span")
    product_names = [span.text.strip() for span in product_spans]
    
    assert product_names[-1] == product, f"Last product should be '{product}', but found '{product_names[-1]}'"
