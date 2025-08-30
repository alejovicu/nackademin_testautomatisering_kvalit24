from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


## LAB ASSIGNMENT 3 - SIGN UP AS ADMIN, LOGIN, ADD PRODUCT AND VALIDATE PRODUCT EXISTS (both UI and Backend)
APP_URL='http://localhost:5173'
API_URL='http://localhost:8000'
API_LOGIN_URL = "http://localhost:8000/login"
API_PRODUCTS_URL = "http://localhost:8000/products"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_navigate_to_signup():

    # My variables.
    username = "admin"
    password = "pass1234"
    product = "Test_course"

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(APP_URL)

        #Finds signup button and clicks it
        login_btn_signup = driver.find_element('id', "signup")
        login_btn_signup.click()

        #Finds username input and sends it.
        signup_input_username = driver.find_element('xpath', '//input[@placeholder="Username"]')
        signup_input_username.send_keys(username)
        #Finds password input and sends it.
        signup_input_password = driver.find_element('xpath', '//input[@placeholder="Password"]')
        signup_input_password.send_keys(password)

        # Clicks signup button
        login_btn_signup = driver.find_element('xpath', '//button[text()="Sign Up"]')
        login_btn_signup.click()

        # WebDriverWait to make sure it waits for the modal/alert comes up.(to avoid crash)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept() 

        #Finds login button and clicks it
        login_btn_signup = driver.find_element('xpath', '//button[text()="Login"]')
        login_btn_signup.click()

        #Fins username input and enters it/clicks it.
        login_input_username = driver.find_element('xpath', '//input[@placeholder="Username"]')
        login_input_username.send_keys(username)
        #Fins password input and enters it/clicks it.
        login_input_password = driver.find_element('xpath', '//input[@placeholder="Password"]')
        login_input_password.send_keys(password)

            #Clicks login button
        login_btn_signup = driver.find_element('xpath', '//button[text()="Login"]')
        login_btn_signup.click()

            #LOGGED INTO USER PAGE
        #Here I use the newer way of doing it with By.XPATH instead.
        wait = WebDriverWait(driver, 10)
        product_input = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Product Name"]'))
        )
        product_input.send_keys(product)
            #In this way it waits for the elements to appear and then enters input.

        wait = WebDriverWait(driver, 10)
        create_product_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Create Product"]'))
        )
        create_product_btn.click()

        # This is only an assert on the UI side, not backend.
        product_element = wait.until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='product-item']/span[text()='{product}']"))
        )
        assert product_element.is_displayed(), f"Product '{product}' not found in UI!"

        # Here we get the access token from a "log in" api call
        login_response = requests.post(
            API_LOGIN_URL,
            json={"username": username, "password": password}
        )
        login_response.raise_for_status()
        token = login_response.json()["access_token"]

        # Here we verify the backend
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(API_PRODUCTS_URL, headers=headers)
        response.raise_for_status()
        products = response.json()

        #print(products)

        # Does the product exist? IF not, we assert product was not found.
        product_names = [p["name"] for p in products]
        assert product in product_names, f"Product '{product}' not found in backend."

        # just to make it exra clear the product exists, run as -> pytest -s admin_add_product.py
        print(f"{product} found in backend! All products: {product_names}")

        time.sleep(2)
    
    finally:
        driver.quit()