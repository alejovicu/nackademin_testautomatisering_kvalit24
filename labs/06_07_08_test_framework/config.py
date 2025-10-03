import requests
import os

BASE = os.environ.get("BACKEND_URL", "http://localhost:8000")

# log in as admin
login_resp = requests.post(f"{BASE}/login", json={"username": "admin", "password": "admin123"})

# If login succeeds
if login_resp.ok:
    print("Admin account already exists, proceeding with product creation")
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # fetch all products
    get_product_resp = requests.get(f"{BASE}/products", headers=headers)
    get_product_resp.raise_for_status()
    products = get_product_resp.json()

    # check if "Ipad" already exists
    if any(p.get("name") == "Ipad" for p in products):
        print('"Ipad" already exists—skipping creation.')
    else:
        # create the product
        product_resp = requests.post(
            f"{BASE}/product",
            json={"name": "Ipad"},
            headers=headers,
        )
        product_resp.raise_for_status()
        print('Created product "Ipad"')
    
# If login fails
else:
    print("Admin login failed, creating default users…")
    # create admin user
    admin_creation_resp = requests.post(f"{BASE}/signup", json={
        "username": "admin",
        "password": "admin123"
    })
    admin_creation_resp.raise_for_status()

    # create regular user
    user_creation_resp = requests.post(f"{BASE}/signup", json={
        "username": "test",
        "password": "test123"
    })
    user_creation_resp.raise_for_status()

    # login as admin
    login_resp = requests.post(f"{BASE}/login", json={"username": "admin", "password": "admin123"})
    login_resp.raise_for_status()
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
   
    # create the product
    product_resp = requests.post(
        f"{BASE}/product",
        json={"name": "Ipad"},
        headers=headers,
    )
    product_resp.raise_for_status()
    print('Created product "Ipad"')