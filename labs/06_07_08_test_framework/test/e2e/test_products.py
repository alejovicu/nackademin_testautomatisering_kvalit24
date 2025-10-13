from playwright.sync_api import Page
import libs.utils
from playwright.sync_api import Page, expect
import os, time, requests
from models.ui.admin import AdminPage
import re

APP_URL = os.getenv("APP_FRONT_URL", "http://localhost:5173")
BACK_URL = os.getenv("APP_BACK_URL", "http://localhost:8000")

def _api_login(username: str, password: str) -> str:
    resp = requests.post(f"{BACK_URL}/login", json={"username": username, "password": password})
    resp.raise_for_status()
    token = resp.json().get("access_token")
    assert token, "No access_token in login response"
    return token

def _open_as_admin(page: Page):
    # Login via API and inject token before first navigation
    token = _api_login("admin", "admin123")
    page.add_init_script(f"window.localStorage.setItem('token', '{token}');")
    page.goto(APP_URL)
    # sanity: we should not be on /login
    expect(page).not_to_have_url(re.compile(r"/login\b"))
    return token


# Given I am an admin user
# When I add a product to the catalog
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    _open_as_admin(page)
    admin_page = AdminPage(page)

    before = admin_page.get_current_product_count()
    name = f"product_{int(time.time())}"

    admin_page.create_product(name)

    expect(admin_page.products).to_have_count(before + 1)
    expect(admin_page.products.filter(has_text=name)).to_have_count(1)


# Given I am an admin user
# When I remove a product from the catalog
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    _open_as_admin(page)
    admin_page = AdminPage(page)

    # Seed a product via UI to keep this a full E2E
    seed = f"delete_{int(time.time())}"
    before = admin_page.get_current_product_count()
    admin_page.create_product(seed)
    expect(admin_page.products).to_have_count(before + 1)

    # Delete and verify
    admin_page.delete_product_by_name(seed)
    expect(admin_page.products).to_have_count(before)
    expect(admin_page.products.filter(has_text=seed)).to_have_count(0)