import requests
import os

BASE = os.environ.get("APP_URL", "http://localhost:8000")

# create admin user
requests.post(f"{BASE}/signup", json={
    "username": "admin",
    "password": "admin"
})

# # create some products
# for name in ["Widget", "Gadget"]:
#     requests.post(f"{BASE}/products", json={"name": name})