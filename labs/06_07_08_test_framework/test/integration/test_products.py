from models.api.user import UserAPI
from models.api.admin import AdminAPI
import libs.utils
import requests


# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

BASE_URL = "http://localhost:5173"


def _admin_api():
    api = AdminAPI(BASE_URL)
    api.login("admin", "1234")
    return api


def test_add_product_to_catalog():
    username = "admin"
    password = "1234"
    product_name = libs.utils.generate_product_string_with_prefix("apple", 4)
    user_api = UserAPI("http://localhost:5173")

    user_api.login(username, password)
    assert user_api.status_code == 200

    admin_api = AdminAPI("http://localhost:5173", token=user_api.token)
    count_before = admin_api.get_current_product_count()
    admin_api.create_product(product_name)
    assert admin_api.status_code == 200

    count_after = admin_api.get_current_product_count()

    assert count_after == count_before + 1, "Product count did not increase "
    "by 1"

    product_names = []
    for product in admin_api.get_product_list():
        product_names.append(product.get("name"))
    assert product_name in product_names, "The added product is not in the list"


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used


def test_remove_product_from_catalog():
    username = "admin"
    password = "1234"
    product_name = generate_product_string_with_prefix("apple", 4)

    user_api = UserAPI("http://localhost:8000")

    user_api.login(username, password)
    assert user_api.status_code == 200

    admin_api = AdminAPI("http://localhost:8000", token=user_api.token)
    admin_api.create_product(product_name)

    assert admin_api.status_code == 200

    count_before = admin_api.get_current_product_count()

    admin_api.delete_product_by_name(product_name)

    count_after = admin_api.get_current_product_count()

    product_names = []
    for product in admin_api.get_product_list():
        product_names.append(product.get("name"))

    assert product_name not in product_names, (
        "The added product is still in the list after removal"
    )
    assert count_after == count_before - 1, "Product count did not decrease by 1"
