from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

APP_URL='http://localhost:5173'

# Setup Chrome options to avoid unnecessary logs
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def test_admin_add_product():
    driver = webdriver.Chrome(options=options)
    driver.get(APP_URL)              
    wait = WebDriverWait(driver, 10)

    #login as admin
    wait.until(EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Username"]'))).send_keys("admin")
    driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys("admin")
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    time.sleep(5)


    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Create Product"]')))
    #add product
    product_name = "chairs"
    product_input = driver.find_element(By.XPATH,'//input[@placeholder="Product Name"]')
    product_input.send_keys(product_name)

    driver.find_element(By.XPATH, '//button[text()="Create Product"]').click()
   
   
    time.sleep(2)
   
    driver.quit()

test_admin_add_product()
    
