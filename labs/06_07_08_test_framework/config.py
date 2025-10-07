import requests
import os

BASE = os.environ.get("BACKEND_URL", "http://localhost:8000")

# log in as admin
login_resp = requests.post(f"{BASE}/login", json={"username": "admin", "password": "admin1234"})



if login_resp.ok:
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    product_resp = requests.get(f"{BASE}/products", headers=headers)
    products = product_resp.json()

    if any(p.get("name")== "Banan" for p in products):
        print("Banan already exists")
    else:
        product_resp = requests.post(
        f"{BASE}/product",
        json={"name": "Banan"},
        headers=headers,
    )
    product_resp.raise_for_status()
    print("Create product Banan")


else:
# create admin user
    requests.post(f"{BASE}/signup", json={
        "username": "admin",
        "password": "admin1234"
    })

    # create regular user
    requests.post(f"{BASE}/signup", json={
        "username": "user1",
        "password": "user1234"
    })

        # log in as admin
    login_resp = requests.post(f"{BASE}/login", json={"username": "admin", "password": "admin1234"})
    login_resp.raise_for_status()
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}



    # create product
    product_resp = requests.post(f"{BASE}/product", json={"name": "Banan"}, headers=headers)
    product_resp.raise_for_status()

    if product_resp.status_code != 200:
        print("Product creation failed:", product_resp.text)
        raise SystemExit(1)