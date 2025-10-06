from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage

username = "nermin123"
password = "nermin_123"

def test_add_product_to_catalog(page: Page):
 
    home_page = HomePage(page)
    home_page.navigate()

    home_page.login(username, password)
    expect(page.get_by_text("Product Catalog:")).to_be_visible()

    #Add product

    new_product = "class item 8"
    admin_home = AdminPage(page)

    admin_home.create_product(new_product)
    expect(page.get_by_text(new_product)).to_be_visible()

    
    
  
    
# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
 
    home_page = HomePage(page)
    home_page.navigate()

    home_page.login(username, password)
    expect(page.get_by_text("Product Catalog:")).to_be_visible()

    new_product = "class item 8"
    admin_home = AdminPage(page)
   
    admin_home.delete_product_by_name(new_product)
    expect(page.get_by_text(new_product)).not_to_be_visible()
    

   
