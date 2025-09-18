from libs.utils import generate_product_string_with_prefix
from playwright.sync_api import Page
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.user import UserAPI


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    username = "admin_user"
    password = "pass_1234"

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI("http://localhost:8000")
    product = generate_product_string_with_prefix("mango", 8)

    # Get token from the API and verify that login is successful
    response = user_api.login(username, password)
    assert response.status_code == 200, f"Admin login failed: {response.text}"
    token = user_api.token

    # Inject the token into localStorage before loading the page
    page.add_init_script(f"""
    window.localStorage.setItem("token", "{token}");
""")

    # Navigate directly to the home page
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    # Create a new product using the AdminPage
    admin_page.create_product(product_name=product)
    page.wait_for_load_state("networkidle")

    # Verify the product is visible and has right text
    product_locator = admin_page.find_product(product)
    assert product_locator.count() == 1, (
        f"Expected 1 product, found {product_locator.count()}"
    )
    assert product_locator.first.inner_text() == product, (
        f"Expected product text '{product}', got '{product_locator.first.inner_text()}'"
    )


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    username = "admin_user"
    password = "pass_1234"

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI("http://localhost:8000")
    product = generate_product_string_with_prefix("mango", 8)

    # Get token from the API and verify that login is successful
    response = user_api.login(username, password)
    assert response.status_code == 200, f"Admin login failed: {response.text}"
    token = user_api.token

    # Inject the token into localStorage before loading the page
    page.add_init_script(f"""
    window.localStorage.setItem("token", "{token}");
""")

    # Navigate to the home page
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    # Add the product (to make the test repeatable)
    admin_page.create_product(product_name=product)
    page.wait_for_load_state("networkidle")

    # Verify the product is visible and has the correct text
    product_locator = admin_page.find_product(product)
    assert product_locator.count() == 1, (
        f"Expected 1 product, found {product_locator.count()}"
    )
    assert product_locator.first.inner_text() == product, (
        f"Expected product text '{product}', got '{product_locator.first.inner_text()}'"
    )

    # Delete the product and verify it is gone
    admin_page.delete_product_by_name(product_name=product)
    page.wait_for_load_state("networkidle")
    assert admin_page.find_product(product).count() == 0
