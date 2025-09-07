import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP_URL = 'http://localhost:5173'

@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navigate_to_signup(driver):
    # Arrange
    driver.get(APP_URL)

    # Act
    signup_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "signup"))
    )
    signup_btn.click()

    # Assert (kontrollera att vi faktiskt hamnat på signup-sidan)
    header = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Sign up')]"))
    )
    assert header.is_displayed()

# def test_input_username(driver):
#     # Arrange
#     driver.get(APP_URL)

#     # Act
#     username_input = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
#     )
#     username_input.send_keys("testuser")

#     # Assert (verifiera att värdet är inskrivet)
#     assert username_input.get_attribute("value") == "testuser"
