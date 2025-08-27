# ```
# Given I am an admin user​

# When I add a product to the catalog​

# Then The product is available to be used in the app
# ```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL='http://localhost:5173'


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def add_product_as_admin():
    
    driver = webdriver.ChromeOptions(options=options)
    driver.get(APP_URL)

    