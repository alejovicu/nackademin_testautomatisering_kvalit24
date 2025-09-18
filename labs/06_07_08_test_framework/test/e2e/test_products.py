from playwright.sync_api import Page, expect
from models.ui.admin import AdminPage
from models.ui.home import HomePage
from models.ui.signup import SignupPage
import random
def test_add_product_to_catalog(page: Page):

    # Given I am an admin user​
    home_page = HomePage(page)
    product = AdminPage(page)

    home_page.navigate()
    home_page.login("testuser", "testpassword")
    page.wait_for_load_state("networkidle")


    # When I add a product to the catalog​
    product_count = product.get_current_product_count()
    page.wait_for_load_state("networkidle")
    product.create_product("TestProduct" + str(random.randint(1, 1000)))

    page.wait_for_timeout(2)

    # Then The product is available to be used in the app
    product_count_after = product.get_current_product_count()
    assert product_count_after == product_count + 1


def test_remove_product_from_catalog(page: Page):
    # Given I am an admin user​
    home_page = HomePage(page)
    product = AdminPage(page)

    home_page.navigate()
    home_page.login("testuser", "testpassword")

    #Creating a product to be deleted
    product.create_product("TestDeleteProduct123")

    # When I remove a product from the catalog​
    product_name = "TestDeleteProduct123"  
    product.delete_product_by_name(product_name)
    
    # Then The product should not be listed in the app to be used
    expect(page.locator(".product-item", has_text=product_name)).to_have_count(0)
