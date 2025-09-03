from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.user_admin import AdminUserPage


# def test_add_product_to_catalog(page: Page):

#     #PO usage example
#     home_page = HomePage(page)
#     login_page = LoginPage(page)
#     home_page.navigate()
#     login_page.navigate_to_signup()


def test_valid_login(page: Page):
    # Given I am an admin user​
    username = "nahom_admin"
    password = "1234"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.login(username, password)
    user_admin = AdminUserPage(page)
    user_admin.logout()


    
    # When I add a product to the catalog​
# def test_create_product(page: Page):
#     username = "nahom_admin"
#     password = "1234"
#     po_login = LoginPage(page)
#     po_login.navigate()
#     po_login.login(username, password)
#     product_name = "laptop"
#     user_admin = AdminUserPage(page)
#     user_admin.add_product(product_name)
#     user_admin.logout()

    # Then The product is available to be used in the app
def test_validate_product_in_list(page: Page):
    username = "nahom_admin"
    password = "1234"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.login(username, password)
    product_name = "gris"
    user_admin = AdminUserPage(page)
    user_admin.add_product(product_name)
    expect(user_admin.product_lists).to_contain_text(product_name)


def test_remove_product_from_catalog(page: Page):
    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
    username = "nahom_admin"
    password = "1234"
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.login(username, password)
    user_admin = AdminUserPage(page)
    user_admin.remove_product()
    expect(user_admin.empty_product_message).not_to_be_visible()