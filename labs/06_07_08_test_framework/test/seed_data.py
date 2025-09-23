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

# create 3 default products
for name in ["Banan", "Äpple", "Päron"]:
    requests.post(f"{BASE}/user/products", json={"name": name})