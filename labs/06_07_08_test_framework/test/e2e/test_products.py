from playwright.sync_api import Page, expect
# from models.login import LoginPage
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils
import os
import time

ADMIN_USER = os.getenv("ADMIN_USERNAME", "nahom_admin")
ADMIN_PASS = os.getenv("ADMIN_PASSWORD", "1234")

# ADMIN_USER = "nahom_admin"
# ADMIN_PASS = "1234"

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    home = HomePage(page)
    admin = AdminPage(page)

    # navigera till appen i webbläsaren, kommer till startsidan. 
    home.navigate()

    # gör loginfunktionen med fill och click. 
    home.login(ADMIN_USER, ADMIN_PASS)
    
    # räkna antalet produkter innan för att sen se om produkten skapats.
    product_count = admin.get_current_product_count()

    # Skapa produkt
    product_name = libs.utils.generate_string_with_prefix("prod")
    admin.create_product(product_name)

    
    is_added = False
    for attempt in range(3):
        if admin.get_current_product_count() == product_count + 1 :
            is_added= True
            break
        else:
            print("Product not added yet.")
            time.sleep(1)

    assert is_added, "Product was not added"



# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    admin = AdminPage(page)

    home.navigate()

    home.login(ADMIN_USER, ADMIN_PASS)


    product_name = libs.utils.generate_string_with_prefix("prod")
    admin.create_product(product_name)

    product_count = admin.get_current_product_count()
    admin.delete_product_by_name(product_name)
    expect(page.get_by_text(product_name)).to_be_hidden()
    
    is_deleted = False
    for attempt in range(3):
        current_prod_count = admin.get_current_product_count()
        expected_prod_count = product_count - 1
        if current_prod_count == expected_prod_count:
            is_deleted= True
            break
        else:
            print(f"Product not deleted yet. current_prod_count: {current_prod_count} expected_prod_count: {expected_prod_count}")
            time.sleep(1)

    assert is_deleted, "Product was not deleted"
  

    