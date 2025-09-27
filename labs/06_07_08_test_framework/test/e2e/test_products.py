from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage


def test_add_product_to_catalog(page: Page):
   # Given I am an admin user​
   username = "test_admin"
   password = "admin_test321"

   login_page = HomePage(page)
   login_page.navigate()

   login_page.login(username, password)
   expect(login_page.login_header_main_title).to_be_visible()
   expect(page.get_by_text("Logout")).to_be_visible()

   # When I add a product to the catalog​
   product_name = "Banana"
   admin_page = AdminPage(page)

   before_counting = admin_page.get_current_product_count()
   admin_page.create_product(product_name)

   # Then the product is available to be used in the app
   after_counting = admin_page.get_current_product_count()
   assert after_counting == before_counting + 1


def test_remove_product_from_catalog(page: Page):
   # Given I am an admin user​
   username = "test_admin"
   password = "admin_test321"

   login_page = HomePage(page)
   login_page.navigate()

   login_page.login(username, password)
   expect(login_page.login_header_main_title).to_be_visible()
   expect(page.get_by_text("Logout")).to_be_visible()

   # When I remove a product from the catalog​
   product_name = "Banana"
   admin_page = AdminPage(page)

   before_count = admin_page.get_current_product_count()
   admin_page.delete_product_by_name(product_name)

   # Then the product should not be listed in the app to be used
   after_count = admin_page.get_current_product_count()
   assert after_count == before_count - 1