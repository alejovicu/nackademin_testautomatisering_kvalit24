import requests
import os

BASE = os.environ.get("APP_URL", "http://localhost:8000")

# create admin user
requests.post(f"{BASE}/signup", json={
    "username": "admin",
    "password": "admin"
})

# create regular user
requests.post(f"{BASE}/signup", json={
    "username": "user_account",
    "password": "user_pass"
})

# log in as admin
login_resp = requests.post(f"{BASE}/login", data={"username": "admin", "password": "adminpass"})
login_resp.raise_for_status()
token = login_resp.json()["access_token"]

headers = {"Authorization": f"Bearer {token}"}

# create product
product_resp = requests.post(f"{BASE}/products", json={"name": "Banan"}, headers=headers)
product_resp.raise_for_status()

if product_resp.status_code != 201:
    print("Product creation failed:", product_resp.text)
    raise SystemExit(1)
