from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignUpPage
from models.admin import AdminPage
from models.user import UserPage


def test_add_user(page: Page):
    home_page = HomePage(page)
    signup_page = SignUpPage(page)
    login_page = LoginPage(page)
    user_page = UserPage(page)

    home_page.navigate()
    # create new user.
    login_page.nav_to_signup()
    signup_page.sign_up("user", "Pass123")
    # login new user.
    signup_page.nav_to_login()
    login_page.login("user", "Pass123")
    # the users can not see the avalible products! (bug? to be implemnted?)
    # logout user
    user_page.logout_user()


def test_add_product_to_catalog(page: Page):
    product = "apple"
    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    home_page.navigate()
    # Given I am an admin user​
    login_page.login("Admin_user", "Automation53")
    # When I add a product to the catalog​
    expect(admin_page.product_item.filter(has_text=product)).not_to_be_visible()
    admin_page.create_product(product)
    # Then The product is available to be used in the app
    expect(admin_page.product_item.filter(has_text=product)).to_be_visible()
    admin_page.logout_admin()


def test_remove_product_from_catalog(page: Page):
    product = "apple"
    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    home_page.navigate()
    # Given I am an admin user​
    login_page.login("Admin_user", "Automation53")
    # When I remove a product from the catalog​
    expect(admin_page.product_item.filter(has_text=product)).to_be_visible()
    admin_page.delete_product(product)
    # Then The product should not be listed in the app to be used
    expect(admin_page.product_item.filter(has_text=product)).not_to_be_visible()
    admin_page.logout_admin()
