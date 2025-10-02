from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import requests
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")

#Helpfunction login via API and set token in localStorage
def login_and_set_token(page: Page, username: str, password: str):
    
    url_login = f"{BACKEND_URL}/login"
    response = requests.post(url_login, json={
        "username": username,
        "password": password
    })
    #Raise error if login fails
    response.raise_for_status()
    jwt = response.json()["access_token"]

    #Sets the jwt token in localstorage before loading page
    page.add_init_script(f"window.localStorage.setItem('token', '{jwt}');")

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    username = "admin"
    password = "1234"
    product = "Chips"

    
    admin_page = AdminPage(page)

    login_and_set_token(page, username, password)

    page.goto(FRONTEND_URL)


    admin_page.create_product(product)

    #Verifying  that product exists in catalog
    expect(admin_page.admin_products.filter(has_text=product)).to_have_count(1)


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    username = "admin"
    password = "1234"
    product = "Chips"

    
    admin_page = AdminPage(page)

    login_and_set_token(page, username, password)

    page.goto(FRONTEND_URL)


    admin_page.delete_product_by_name(product)

    #Verifying  that product no longer exists
    expect(admin_page.admin_products.filter(has_text=product)).to_have_count(0)
