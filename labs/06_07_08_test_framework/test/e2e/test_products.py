import pytest
from playwright.sync_api import Page, expect
from models.ui.admin import AdminPage
from models.ui.home import HomePage
from models.api.admin import AdminAPI
import os

BASE_URL = os.getenv("BACKEND_URL","http://localhost:8000/")


def test_add_product_to_catalog(page):
    home_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    home_page.login("admin", "admin1234")
    
    page.wait_for_load_state("networkidle")
    
    
    expect(page.get_by_text("Add new product:")).to_be_visible()
    
    initial_count = admin_page.get_current_product_count()

    product_name = "keyboard"
    admin_page.create_product(product_name)
    
    expect(page.get_by_text(product_name).first).to_be_visible()
    assert admin_page.get_current_product_count() == initial_count + 1


def test_remove_existing_product(page: Page):
    home_page = HomePage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    home_page.login("admin", "admin1234")
    
    
    page.wait_for_load_state("networkidle")
    

    product_name = "keyboard"
    expect(page.get_by_text(product_name).first).to_be_visible()
    
    initial_count = admin_page.get_current_product_count()
    admin_page.delete_product_by_name(product_name)
    
    
    page.wait_for_timeout(1000)
    
    assert admin_page.get_current_product_count() == initial_count - 1