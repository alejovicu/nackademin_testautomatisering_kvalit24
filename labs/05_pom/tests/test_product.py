import time
from playwright.sync_api import Page, expect
from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage  



def test_add_product_to_catalog(page: Page):
    home = HomePage(page)
    login = LoginPage(page)
    product_name = "test"

    
    home.navigate()
    login.login_as_admin("testare_arre", "testare_123")  


    
    home.add_product(product_name)
    product_row = page.locator(".product-item", has_text=product_name).first
    expect(product_row).to_be_visible(timeout=5000)



def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    login = LoginPage(page)

    product_name = "test123"
    
    home.navigate()
    login.login_as_admin("testare_arre", "testare_123")
    home.add_product(product_name)  
    
    
    home.remove_product(product_name)
    product_row = page.locator(".product-item", has_text=product_name).first
    expect(product_row).not_to_be_visible(timeout=5000)

   
