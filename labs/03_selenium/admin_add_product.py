from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

#added för att köra waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


APP_URL='http://localhost:5173'

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# gör dynamiskt?

def test_verify_admin():

    # Set-up
    username = "admin"
    password = "admin123"

    new_product = "orange"

    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)

    # ATTEMPT TO LOG IN
    login_username = driver.find_element("xpath", '(//input)[@placeholder="Username"]')
    login_username.send_keys(username)

    login_password = driver.find_element("xpath", '(//input)[@placeholder="Password"]')
    login_password.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, 'button.button-primary')
    login_button.click()

    time.sleep(5)

    # PATH IF NO ADMIN EXISTS
    try:
        # Verify alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        expected_alert_text = 'Login failed: {"detail":"Incorrect username or password"}'
        assert alert_text == expected_alert_text
        alert.accept()

        #Sign up
        login_btn_signup = driver.find_element("id", "signup")
        login_btn_signup.click()

        sign_username_input_locator = driver.find_element("xpath", '(//input)[@placeholder="Username"]')
        sign_password_input_locator = driver.find_element("xpath", '(//input)[@placeholder="Password"]')
        sign_username_input_locator.send_keys(username)
        sign_password_input_locator.send_keys(password)

        signup_button_locator = driver.find_element(By.CSS_SELECTOR, 'button.button-primary')
        signup_button_locator.click()

        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        time.sleep(1)  # short pause to let the page update

        # signup_alert = driver.switch_to.alert
        # signup_alert.accept()
        # time.sleep(2)

        # back_to_login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-blue")
        # back_to_login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        back_to_login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-blue")
        back_to_login_button.click()
        # back_to_login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/p/button')
        # back_to_login_button.click()
        time.sleep(3)

        # login_username = driver.find_element("xpath", '(//input)[@placeholder="Username"]')
        login_username = driver.find_element("xpath", '//*[@id="root"]/div/div/input[1]')
        login_username.send_keys(username)

        # login_password = driver.find_element("xpath", '(//input)[@placeholder="Password"]')
        login_password = driver.find_element("xpath", '//*[@id="root"]/div/div/input[2]')
        login_password.send_keys(password)
        time.sleep(2)

        # login_button = driver.find_element(By.CSS_SELECTOR, 'button.button-primary')
        second_login_button = driver.find_element(By.CSS_SELECTOR, "button.button-primary")
        second_login_button.click()
        # second_login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')

        # second_login_button.click()



        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass


    # PATH IF ADMIN EXISTS
    except NoAlertPresentException:
        pass

    
    # # CREATE NEW PRODUCT
    # initial_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item"))

    # new_product_input = driver.find_element("xpath", '//input[@placeholder="Product Name"]')


    # new_product_input = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Product Name"]'))
    # )
    # create_product_button = driver.find_element(By.XPATH, "//button[normalize-space(text())='Create Product']")

    # # create_product_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Product')]")
    # new_product_input.send_keys(new_product)
    # create_product_button.click()
    # time.sleep(2)

    # # CHECK IF PRODUCT IS ADDED
    # updated_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item"))
    # assert updated_count == initial_count + 1

    # time.sleep(3)

    # CREATE NEW PRODUCT
    initial_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item"))

    # wait for input and button
    new_product_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Product Name"]'))
    )
    create_product_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Create Product']"))
    )

    # add product
    new_product_input.send_keys(new_product)
    create_product_button.click()
    time.sleep(2)

    # CHECK IF PRODUCT IS ADDED
    updated_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-grid .product-item"))
    assert updated_count == initial_count + 1

    # Teardown
    driver.quit()

