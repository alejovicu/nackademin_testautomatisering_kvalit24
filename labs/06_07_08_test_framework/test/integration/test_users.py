from playwright.sync_api import Page
import libs.utils
from models.api.user import UserAPI


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    # Given I am a new potential customer​
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI("http://localhost:8000")

    # When I signup in the app​
    user_api.signup(username, password)
    assert user_api.status_code == 200

    # Then I should be able to log in with my new user
    user_api.login(username, password)
    assert user_api.status_code == 200


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login():
    # Given I am an authenticated user​
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    user_api = UserAPI("http://localhost:8000")
    user_api.signup(username, password)
    assert user_api.status_code == 200

    # When I log in into the application​
    user_api.login(username, password)
    assert user_api.status_code == 200

    # Then I should see all my products
    user_list = user_api.display_user_products()
    assert "products" in user_list, "User JSON does not contain products key"
    assert len(user_list["products"]) == 0, "New user should have no products"


# Extra: Add a product to user and check that it appears in the list
def test_add_product_to_user():
    username = libs.utils.generate_string_with_prefix()
    password = "1234"
    product_name = "Banan"  # Question: Product doesn't have to be generated and added if its in the test data right?

    user_api = UserAPI("http://localhost:8000")
    # Create user
    user_api.signup(username, password)

    # Login user
    user_api.login(username, password)

    # Add product
    user_api.add_product_to_user(product_name)

    # Asserts
    assert user_api.status_code == 200, "Product was not added successfully"
    user_list = user_api.display_user_products()  # Refreshing the product list
    products = user_list["products"]
    assert len(products) > 0, "Product list is empty"  # At least one product

    product_names = []
    for product in products:
        product_names.append(product["name"])
    assert product_name in product_names, (
        "The added product could not be found in the list"
    )  # Checking that the right product was added in the list

    user_api.remove_product_from_user(product_name)
    assert user_api.status_code == 200, "Product was not removed successfully"
    user_list = user_api.display_user_products()  # Refreshing the product list
    products = user_list["products"]
    assert len(products) == 0, "Product list is not empty after removal"

    product_names = []
    for product in products:
        product_names.append(product["name"])
    assert product_name not in product_names, "The removed product is still in the list"


# Extra: Remove a product from user and check that it does not appear in list
def test_remove_product_from_user():
    username = libs.utils.generate_string_with_prefix()
    password = "1234"
    product_name = "Banan"

    user_api = UserAPI("http://localhost:8000")
    # Create user
    user_api.signup(username, password)

    # Login user
    user_api.login(username, password)

    # Add product
    user_api.add_product_to_user(product_name)

    # Remove product
    user_api.remove_product_from_user(product_name)

    # Asserts
    assert user_api.status_code == 200, "Product was not removed successfully"
    user_list = user_api.display_user_products()  # Refreshing the product list
    products = user_list["products"]
    assert len(products) == 0, "Product list is not empty after removal"

    product_names = []
    for product in products:
        product_names.append(product["name"])
    assert product_name not in product_names, "The removed product is still in the list"
