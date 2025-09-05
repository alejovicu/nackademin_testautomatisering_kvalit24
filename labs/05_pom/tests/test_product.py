from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.admin import AdminPage



def test_add_product_to_catalog(page: Page):

     #PO usage example
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.navigate()
    login_page.navigate_to_signup()
    admin_page = AdminPage(page)
    product = "Bord"

    home_page.navigate()
    login_page.admin_login()
    
    expect(admin_page.products.first).to_be_visible()
    
    num_of_products_before = admin_page.count_products()
    admin_page.create_product(product)

    expect(admin_page.products).to_have_count(num_of_products_before + 1)



def test_remove_product_from_catalog(page: Page):
    
    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    home_page.navigate()
    login_page.admin_login()

    expect(admin_page.products.first).to_be_visible()


    num_of_products_before = admin_page.count_products()
    admin_page.remove_last_product()

    expect(admin_page.products).to_have_count(num_of_products_before - 1)
    