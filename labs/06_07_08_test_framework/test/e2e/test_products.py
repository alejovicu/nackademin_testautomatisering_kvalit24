
from playwright.sync_api import Page, expect
from models.ui.admin import AdminPage
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import random
import libs.utils
import os


BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")

def test_add_product_to_catalog(page: Page):
    # complete code

    # Given I am an admin user​
    home_page = HomePage(page)
    product = AdminPage(page)

    home_page.navigate()
    home_page.login("testare_arre", "testare_123")
    page.wait_for_selector('input[placeholder="Product Name"]', timeout=60000)

    # When I add a product to the catalog​
    product_count = product.get_current_product_count()
    product.create_product("TestProduct" + str(random.randint(1, 1000)))

    # Then The product is available to be used in the app
    product_count_after = product.get_current_product_count()
    assert product_count_after == product_count + 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    # complete code 
    # Given I am an admin user​
    home_page = HomePage(page)
    product = AdminPage(page)

    home_page.navigate()
    home_page.login("testare_arre", "testare_123")
    page.wait_for_selector('input[placeholder="Product Name"]', timeout=60000)

    #Creating a product to be deleted
    product.create_product("TestDeleteProduct123")

    # When I remove a product from the catalog​
    product_name = "TestDeleteProduct123"  
    product.delete_product_by_name(product_name)

    # Then The product should not be listed in the app to be used
    expect(page.locator(".product-item", has_text=product_name)).to_have_count(0)