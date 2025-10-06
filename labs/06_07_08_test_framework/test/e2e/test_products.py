from playwright.sync_api import Page, expect
# from models.login import LoginPage
from models.ui.home import HomePage
from models.ui.admin import AdminPage
import libs.utils
import os

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

    
    expect(admin.rows.filter(has_text=product_name).first).to_be_visible()
    assert admin.get_current_product_count() == product_count + 1

    # Städa, ta bort den skapade produkten.
    admin.delete_product_by_name(product_name)
    assert admin.get_current_product_count() == product_count





# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    home = HomePage(page)
    admin = AdminPage(page)

    home.navigate()

    home.login(ADMIN_USER, ADMIN_PASS)

    product_count = admin.get_current_product_count()

    product_name = libs.utils.generate_string_with_prefix("prod")
    admin.create_product(product_name)

    admin.delete_product_by_name(product_name)
    assert admin.get_current_product_count() == product_count


    