from playwright.sync_api import Page, expect

from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
from models.admin import AdminPage


def test_add_product_to_catalog(page: Page):
    #########################################################
    # Given I am an admin user​
    # When I add a product to the catalog​
    # Then The product is available to be used in the app
    ##########################################################
    ### ARRANGE
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    admin_page = AdminPage(page)
    product_name = "Cykelstyre"

    ### ACT
    home_page.navigate()
    login_page.navigate_to_signup()
    signup_page.signup_user("admin", "admin123")
    signup_page.navigate_to_login()
    login_page.login_user("admin", "admin123")

    ### ASSERT
    # Check if user has admin privilages by asserting if create product button
    create_product_button = admin_page.button_create_product
    expect(create_product_button).to_be_visible()

    ### ACT
    # Fetch pre-addition stock count
    current_stock_count = admin_page.product_item_in_list.count()

    # Add product
    admin_page.add_product(product_name)

    # Fetch post-addition stock count
    post_addition_stock = admin_page.product_item_in_list.count()

    ## ASSERT
    # Does product name appear in stock?
    latest_product = admin_page.locate_latest_product_name()
    expect(latest_product).to_have_text(product_name)

    # Has stock count increased by 1?
    assert post_addition_stock == current_stock_count + 1


def test_remove_product_from_catalog(page: Page):
    #############################################################
    # Given I am an admin user​
    # When I remove a product from the catalog​
    # Then The product should not be listed in the app to be used
    ##############################################################
    ### ARRANGE
    home_page = HomePage(page)
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    product_name = "Bildäck"

    ### ACT
    home_page.navigate()

    login_page.login_user("admin", "admin123")

    # Add product to be removed
    admin_page.add_product(product_name)

    # Fetch pre-removal stock count
    current_stock_count = admin_page.product_item_in_list.count()

    admin_page.delete_latest_product()

    # Fetch post-removal stock count
    post_addition_stock = admin_page.product_item_in_list.count()

    ### ASSERT
    # Does the product name no longer appear in stock?
    latest_product = admin_page.locate_latest_product_name()
    expect(latest_product).not_to_contain_text(product_name)

    # Has stock count decreased by 1?
    assert post_addition_stock == current_stock_count - 1
