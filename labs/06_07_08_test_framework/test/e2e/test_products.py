from playwright.sync_api import Page, expect

from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI
from libs.utils import generate_product_string_with_prefix


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    username = "admin"
    password = "1234"

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI("http://localhost:8000")
    product = generate_product_string_with_prefix()
    token = user_api.login(username, password)

    # Setting token through local storage to avoid logging in through the UI every time
    page.add_init_script(
        f"""
    window.localStorage.setItem("token", "{token}");
    """
    )

    home_page.navigate()
    # Adding product
    admin_page.add_product(name=product)
    page.wait_for_load_state("networkidle")

    # Making sure the product is available in the app
    assert admin_page.check_product(product).inner_text() == product
    assert admin_page.check_product(product).count() == 1


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    username = "admin"
    password = "1234"

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI("http://localhost:8000")
    product = generate_product_string_with_prefix()
    token = user_api.login(username, password)

    # Setting token through local storage to avoid logging in through the UI every time
    page.add_init_script(
        f"""
    window.localStorage.setItem("token", "{token}");
    """
    )

    home_page.navigate()
    # Adding a product before to make test repeatable
    admin_page.add_product(name=product)

    assert admin_page.check_product(product).inner_text() == product

    admin_page.delete_product(name=product)
    page.wait_for_load_state("networkidle")
    assert admin_page.check_product(product).count() == 0
