from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage


# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    # Given I am an admin user​
    username = "nermin123"
    password = "nermin_123"
 
    home_page = HomePage(page)
    home_page.navigate()

    home_page.login(username, password)
    expect(page.get_by_text("Products available:")).to_be_visible()

    #Add product

    new_product = "Jumper"
    admin_home = AdminPage(page)
    
    prev_count = admin_home.get_current_product_count()
    admin_home.create_product(new_product)

    current_count = admin_home.get_current_product_count()
    assert current_count == prev_count + 1
    
  
    
# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    username = "nermin123"
    password = "nermin_123"
 
    home_page = HomePage(page)
    home_page.navigate()

    home_page.login(username, password)
    expect(page.get_by_text("Products available:")).to_be_visible()

    new_product = "Jumper"
    admin_home = AdminPage(page)
    
    # remove product
    prev_count = admin_home.get_current_product_count()
    admin_home.delete_product_by_name(new_product)

    current_count = admin_home.get_current_product_count()
    assert current_count == prev_count - 1
