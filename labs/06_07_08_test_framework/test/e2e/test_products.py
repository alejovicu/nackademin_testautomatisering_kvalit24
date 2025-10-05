from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils
import os

def test_add_product_to_catalog(page: Page, admin_credentials):
    """Test admin can add product via UI"""
    frontend_url = os.environ.get('FRONTEND_URL', 'http://app-frontend:5173')
    
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    
    home_page.navigate(frontend_url)
    home_page.login(admin_credentials['username'], admin_credentials['password'])
    expect(page.get_by_text("Product Catalog:")).to_be_visible(timeout=10000)
    
    product_name = libs.utils.generate_string_with_prefix("E2EProduct")
    initial_count = admin_page.get_current_product_count()
    admin_page.create_product(product_name)
    
    expect(page.get_by_text(product_name)).to_be_visible(timeout=5000)
    new_count = admin_page.get_current_product_count()
    assert new_count == initial_count + 1

def test_remove_product_from_catalog(page: Page, admin_credentials):
    """Test admin can remove product via UI"""
    frontend_url = os.environ.get('FRONTEND_URL', 'http://app-frontend:5173')
    
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    
    home_page.navigate(frontend_url)
    home_page.login(admin_credentials['username'], admin_credentials['password'])
    expect(page.get_by_text("Product Catalog:")).to_be_visible(timeout=10000)
    
    product_name = libs.utils.generate_string_with_prefix("E2EProduct")
    admin_page.create_product(product_name)
    expect(page.get_by_text(product_name)).to_be_visible(timeout=5000)
    
    initial_count = admin_page.get_current_product_count()
    admin_page.delete_product_by_name(product_name)
    
    expect(page.get_by_text(product_name)).not_to_be_visible(timeout=5000)
    new_count = admin_page.get_current_product_count()
    assert new_count == initial_count - 1