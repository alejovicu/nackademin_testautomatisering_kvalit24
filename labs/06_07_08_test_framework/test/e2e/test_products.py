import pytest
from playwright.sync_api import Page, expect
from models.ui.admin import AdminPage
from models.ui.home import HomePage
from models.api.admin import AdminAPI

BASE_URL = "http://localhost:8000/"

@pytest.fixture(scope="function")
def admin_api():
    api = AdminAPI(BASE_URL)
    response = api.login("admin", "admin1234")
    # Verifiera att login fungerade
    assert response.status_code == 200, f"Login failed: {response.text}"
    assert api.token is not None, "Token not set after login"
    return api

@pytest.fixture(scope="function")
def ensure_no_keyboard(admin_api):
    try:
        admin_api.remove_product_by_name("keyboard")
    except ValueError:
        pass
    yield
    try:
        admin_api.remove_product_by_name("keyboard")
    except ValueError:
        pass

@pytest.fixture(scope="function")
def ensure_keyboard_exists(admin_api):
    products = admin_api.list_products().json()
    if not any(p["name"] == "keyboard" for p in products):
        admin_api.create_product("keyboard")
    yield
    try:
        admin_api.remove_product_by_name("keyboard")
    except ValueError:
        pass

def test_add_product_to_catalog(page: Page, ensure_no_keyboard):
    home_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    home_page.login("admin", "admin1234")
    
    page.wait_for_load_state("networkidle")
    
    
    expect(page.get_by_text("Add new product:")).to_be_visible()
    
    initial_count = admin_page.get_current_product_count()

    product_name = "keyboard"
    admin_page.create_product(product_name)
    
    # Vänta på att produkten dyker upp
    expect(page.get_by_text(product_name).first).to_be_visible()
    assert admin_page.get_current_product_count() == initial_count + 1

def test_remove_existing_product(page: Page, ensure_keyboard_exists):
    home_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    home_page.login("admin", "admin1234")
    
    # Vänta på att admin-sidan laddas
    page.wait_for_load_state("networkidle")
    
    # Vänta på att produkten syns
    product_name = "keyboard"
    expect(page.get_by_text(product_name).first).to_be_visible()
    
    initial_count = admin_page.get_current_product_count()
    admin_page.delete_product_by_name(product_name)
    
    # Vänta på att produkten försvinner
    page.wait_for_timeout(1000)
    
    # Verifiera att produkten är borta
    assert admin_page.get_current_product_count() == initial_count - 1