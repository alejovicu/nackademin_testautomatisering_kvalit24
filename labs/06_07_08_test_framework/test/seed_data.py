import requests
import os

BASE = os.environ.get("APP_URL", "http://localhost:8000")

# log in as admin
login_resp = requests.post(f"{BASE}/login", json={"username": "admin", "password": "admin"})

# If login succeeds
if login_resp.ok:
    print("Admin account already exists, proceeding with product creation")
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # fetch all products
    get_product_resp = requests.get(f"{BASE}/products", headers=headers)
    get_product_resp.raise_for_status()
    products = get_product_resp.json()

    # check if "Banan" already exists
    if any(p.get("name") == "Banan" for p in products):
        print('"Banan" already exists—skipping creation.')
    else:
        # create the product
        product_resp = requests.post(
            f"{BASE}/product",
            json={"name": "Banan"},
            headers=headers,
        )
        product_resp.raise_for_status()
        print('Created product "Banan"')
    
# If login fails
else:
    print("Admin login failed, creating default users…")
    # create admin user
    admin_creation_resp = requests.post(f"{BASE}/signup", json={
        "username": "admin",
        "password": "admin"
    })
    admin_creation_resp.raise_for_status()

    # create regular user
    user_creation_resp = requests.post(f"{BASE}/signup", json={
        "username": "user_account",
        "password": "user_pass"
    })
    user_creation_resp.raise_for_status()

    # login as admin
    login_resp = requests.post(f"{BASE}/login", json={"username": "admin", "password": "admin"})
    login_resp.raise_for_status()
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
   
    # create the product
    product_resp = requests.post(
        f"{BASE}/product",
        json={"name": "Banan"},
        headers=headers,
    )
    product_resp.raise_for_status()
    print('Created product "Banan"')


