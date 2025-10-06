from playwright.sync_api import Page,expect
from libs.utils import generate_product_with_prefix

from models.ui.home import HomePage
from models.ui.admin import AdminPage
from config import ADMIN_USERNAME, ADMIN_PASSWORD
  



# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_create_product_to_catalog(page: Page):
    username = ADMIN_USERNAME
    password = ADMIN_PASSWORD
    product_name = generate_product_with_prefix("product")
    # Login as admin
    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    expect(home_page.page_title).to_have_text("Nackademin Course App")

    admin_page = AdminPage(page)
    admin_page.navigate()

    prev_count = admin_page.get_current_product_count()
    products_list=admin_page.create_product(product_name)
    print(products_list)
    expect(page.get_by_text(product_name)).to_be_visible()
    current_count = admin_page.get_current_product_count()
    assert current_count == prev_count + 1

    



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_delete_product_from_catalog(page: Page):
    pass
    # complete code
   # Given I am an admin user
    username = ADMIN_USERNAME
    password = ADMIN_PASSWORD
    product = generate_product_with_prefix("product")

    # Login as admin
    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    expect(home_page.page_title).to_have_text("Nackademin Course App")

    admin_page = AdminPage(page)
    admin_page.navigate()


    # Create a product to later delete
    product = generate_product_with_prefix(product)
    admin_page.create_product(product)
    expect(page.get_by_text(product)).to_be_visible()

    #to delete 
   
    admin_page.delete_product(product)
    # Verify product is no longer in the list
    expect(page.get_by_text(product)).not_to_be_visible()
