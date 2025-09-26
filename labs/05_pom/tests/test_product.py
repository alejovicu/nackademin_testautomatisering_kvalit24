from playwright.sync_api import Page, expect

from facade.auth_facade import AuthFacade
from models.product_page import ProductPage
import time


#SET UP
BASE_URL = "http://localhost:5173/"
username = "admin"
password = "admin123"


def test_add__remove_product(page: Page):

    # Skapar objekt
    product_page = ProductPage(page)
    auth_facade = AuthFacade(page)

    # Genererar produktnamn
    new_product = f"product_{int(time.time())}"

    # Signup/Login (facade) + assert admin
    auth_facade.signup_and_login(username, password)
    expect(page.get_by_role("button", name="Create Product")).to_be_visible()

    # Add product + assert
    count_before_adding = product_page.add_product(new_product)
    expect(product_page.product.nth(-1)).to_contain_text(new_product)
    expect(product_page.product).to_have_count(count_before_adding + 1)

    # Delete product + assert
    deleted_product = product_page.delete_product(new_product)
    expect(deleted_product).to_have_count(0)