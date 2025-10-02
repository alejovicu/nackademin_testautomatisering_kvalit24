from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import requests

def login_and_set_token(page: Page, username: str, password: str):
    url_login = "http://localhost:8000/login"
    response = requests.post(url_login, json={"username": username, "password": password})
    response.raise_for_status()
    jwt = response.json()["access_token"]
    page.add_init_script(f"window.localStorage.setItem('token', '{jwt}');")

def test_add_product_to_catalog(page: Page):
    username = "admin"
    password = "1234"
    product = "Chips"

    home_page = HomePage(page)
    admin_page = AdminPage(page)

    login_and_set_token(page, username, password)
    home_page.navigate()
    admin_page.create_product_by_api(product)
    expect(admin_page.admin_products.filter(has_text=product)).to_have_count(1)

def test_remove_product_from_catalog(page: Page):
    username = "admin"
    password = "1234"
    product = "Chips"

    home_page = HomePage(page)
    admin_page = AdminPage(page)

    login_and_set_token(page, username, password)
    home_page.navigate()
    admin_page.delete_product_by_name_by_api(product)
    expect(admin_page.admin_products.filter(has_text=product)).to_have_count(0)
