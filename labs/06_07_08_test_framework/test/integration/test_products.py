import requests
from models.api.admin import AdminAPI
from libs.utils import generate_string_with_prefix

import os


BASE_URL = os.getenv("BACKEND_URL") or os.getenv(
    "API_BASE_URL", "http://localhost:8000"
)


def _admin_api():
    api = AdminAPI(BASE_URL)
    r = api.login("admin", "adminadmin1234")
    assert r.status_code == 200, f"Admin login failed: {r.status_code} {r.text}"
    return api


def test_add_product_to_catalog():
    api = _admin_api()

    product_name = generate_string_with_prefix("IT_course")

    # Add a product to the catalog
    resp = api.create_product(product_name)
    assert resp.status_code in (200, 201, 409), (
        f"Create failed: {resp.status_code} {resp.text}"
    )

    # The product is available
    names = api.list_products()
    assert product_name in names


def test_remove_product_from_catalog():
    api = _admin_api()

    product_name = generate_string_with_prefix("IT_course")

    # Created product name
    create_resp = api.create_product(product_name)
    assert create_resp.status_code in (200, 201, 409), (
        f"Create failed: {create_resp.status_code} {create_resp.text}"
    )

    # Delete product
    del_resp = api.delete_product_by_name(product_name)
    assert del_resp is None or del_resp.status_code in (200, 204), (
        f"Delete failed: {getattr(del_resp, 'status_code', None)} {getattr(del_resp, 'text', '')}"
    )

    # The product is not available
    names = api.list_products()
    assert product_name not in names
