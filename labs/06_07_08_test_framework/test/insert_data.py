import requests 
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

requests.post(f"{BACKEND_URL}/signup",json={
  "username": "admin1",
  "password": "1234"
})

requests.post(f"{BACKEND_URL}/signup",json={
  "username": "mimmi",
  "password": "1234"
})

# # log in as admin
# login_resp = requests.post(f"{BACKEND_URL}/login", json={"username": "admin1", "password": "1234"})
# login_resp.raise_for_status()
# token = login_resp.json()["access_token"]

# headers = {"Authorization": f"Bearer {token}"}

# # create new product
# product_resp = requests.post(f"{BACKEND_URL}/products", json={"name": "Testprodukt"}, headers=headers)
# product_resp.raise_for_status()

# if product_resp.status_code != 200:
#     print("Product creation failed:", product_resp.text)
#     raise SystemExit(1)
