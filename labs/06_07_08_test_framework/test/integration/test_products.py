import libs.utils
import requests
import os
from models.api.admin import AdminAPI

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
ADMIN_USER = os.getenv("ADMIN_USERNAME", "nahom_admin")
ADMIN_PASS = os.getenv("ADMIN_PASSWORD", "1234")

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

"""
1. Logga in som admin.
2. Skapa en produkt.
3. Verifiera att produkten syns i katalogen.
4. Ta bort den skapade produkten.
"""

def test_add_product_to_catalog():
    admin_api = AdminAPI(BASE_URL, token=None) # skapar ett AdminAPI-objekt. inte inloggade än drf token=None

    admin_api.login(ADMIN_USER, ADMIN_PASS) # loggar in och hämtar en token.

    product_name = libs.utils.generate_string_with_prefix("Prod") # skapar ett unikt produktnamn.

    created_product = admin_api.create_product(product_name) # skapar en produkt får en json tbx (en dict)

    product_id = created_product["id"]
    assert product_id

    try:
        # Verifiera att produkten syns i katalogen (GET /products)
        resp = requests.get(f"{BASE_URL}/products", headers=admin_api._auth_headers())
        resp.raise_for_status()
        items = resp.json()
        names = [p.get("name") for p in items]
        assert product_name in names, "Produkten syns inte i katalogen efter skapande"
    finally:
        # Städ: radera produkten
        try:
            admin_api.delete_product_by_name(product_name)
        except Exception:
            pass


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog():
    admin_api = AdminAPI(BASE_URL, token=None)
    admin_api.login(ADMIN_USER, ADMIN_PASS)

    # Skapa först en unik produkt som vi sedan tar bort
    product_name = libs.utils.generate_string_with_prefix("Prod")
    created = admin_api.create_product(product_name)
    assert isinstance(created, dict) and created.get("id"), f"Oväntat create-svar: {created!r}"
    product_id = created["id"]

    try:
        # WHEN: ta bort produkten
        admin_api.delete_product_by_name(product_name)

        # THEN: verifiera att produkten inte längre finns i katalogen
        resp = requests.get(f"{BASE_URL}/products", headers=admin_api._auth_headers())
        resp.raise_for_status()
        items = resp.json()

        ids = [p.get("id") for p in items]
        names = [p.get("name") for p in items]
        assert product_id not in ids and product_name not in names, "Produkten fanns kvar i katalogen efter radering"
    finally:
        # Extra städ: om produkten trots allt finns kvar, försök ta bort igen
        try:
            resp = requests.get(f"{BASE_URL}/products", headers=admin_api._auth_headers())
            resp.raise_for_status()
            items = resp.json()
            if any(p.get("id") == product_id for p in items):
                admin_api.delete_product_by_name(product_name)
        except Exception:
            pass