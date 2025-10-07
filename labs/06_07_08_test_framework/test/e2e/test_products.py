from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import requests
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    product = "mobil"

    response = requests.post(
        f"{BACKEND_URL}/login", json={"username": "admin1", "password": "1234"}
    )
    response.raise_for_status()
    jwt = response.json()["access_token"]

    # inject jwt into localstorage
    page.add_init_script(f"""window.localStorage.setItem('token', '{jwt}');""")

    home_page.navigate()

    # When I add a product to the catalog​
    expect(admin_page.products.first).to_be_visible()
    before_new_product = admin_page.get_current_product_count()
    admin_page.create_product(product)

    # Then The product is available to be used in the app
    expect(admin_page.products).to_have_count(before_new_product + 1)


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    product = "mobil"
    response = requests.post(
        f"{BACKEND_URL}/login", json={"username": "admin1", "password": "1234"}
    )
    response.raise_for_status()
    jwt = response.json()["access_token"]

    # inject jwt into localstorage
    page.add_init_script(f"""window.localStorage.setItem('token', '{jwt}');""")

    home_page.navigate()

    expect(admin_page.products.first).to_be_visible()

    # When I remove a product from the catalog​
    before_new_product = admin_page.get_current_product_count()
    admin_page.delete_product_by_name(product)

    # Then The product should not be listed in the app to be used
    expect(admin_page.products).to_have_count(before_new_product - 1)
