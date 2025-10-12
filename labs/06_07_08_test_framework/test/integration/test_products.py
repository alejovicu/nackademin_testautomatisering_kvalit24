import libs.utils
import pytest
import os
import time
from models.api.admin import AdminAPI

BACKEND_URL = os.getenv("APP_BACK_URL", "http://localhost:8000")

def test_add_product_to_catalog():
    admin_api = AdminAPI(BACKEND_URL)
    admin_api.get_admin_token()  # store token on instance

    product_name = f"product_{int(time.time())}"
    count_before = admin_api.get_current_product_count()

    resp = admin_api.create_product(product_name)
    assert resp.status_code in (200, 201), "Failed to add product"

    count_after = admin_api.get_current_product_count()
    assert count_after == count_before + 1, "List did not increase by one"

    product_list = admin_api.get_product_list()
    assert any(p.get("name") == product_name for p in product_list), "New product not found in list"


def test_remove_product_from_catalog():
    admin_api = AdminAPI(BACKEND_URL)
    admin_api.get_admin_token()

    product_name = f"delete_{int(time.time())}"
    create = admin_api.create_product(product_name)
    assert create.status_code in (200, 201)

    count_before = admin_api.get_current_product_count()
    delete = admin_api.delete_product_by_name(product_name)
    assert delete.status_code in (200, 204), "Delete did not return success status"

    count_after = admin_api.get_current_product_count()
    assert count_after == count_before - 1, "List did not decrease by one"

    product_list = admin_api.get_product_list()
    assert all(p.get("name") != product_name for p in product_list), "Deleted product still appears"