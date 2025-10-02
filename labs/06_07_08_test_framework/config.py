import requests
import os
import time

BASE_URL = os.environ.get("APP_BACK_URL", "http://localhost:8000")

# CREATE ADMIN
login_response = requests.post(f"{BASE_URL}/login", json= {"username": "admin", "password": "admin123"})
if login_response.status_code != 200:
    requests.post(f"{BASE_URL}/signup", json={"username": "admin", "password": "admin123"})
    login_response = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "admin123"})
admin_token = login_response.json()["access_token"]

# CREATE PRODUCTS
headers = {"Authorization": f"Bearer {admin_token}"}

product_name_1 = f"product_1_{int(time.time()*1000)}"
product_name_2 = f"product_2_{int(time.time()*1000)}"

requests.post(f"{BASE_URL}/product", json={"name": product_name_1}, headers=headers)
requests.post(f"{BASE_URL}/product", json={"name": product_name_2}, headers=headers)

# CREATE USER
user_signup_response = requests.post(f"{BASE_URL}/signup", json={"username": "user_1", "password": "pass_1"})
if user_signup_response.status_code != 200:
    print("user_1 already exists, skipping creation.")

user_login_resp = requests.post(f"{BASE_URL}/login", json={"username": "user_1", "password": "pass_1"})
if user_login_resp.status_code != 200:
    raise Exception("Failed to login user_1")

user_token = user_login_resp.json()["access_token"]

# ASSIGN PRODUCTS TO USER
headers_user = {"Authorization": f"Bearer {user_token}"}
product_names = [product_name_1, product_name_2]

for product_name in product_names:

    # Get all products
    response = requests.get(f"{BASE_URL}/products", headers=headers_user)
    products = response.json()
    product_id = None

    # Find product ID
    for product in products:
        if product["name"] == product_name:
            product_id = product["id"]
            break

    if product_id is None:
        raise ValueError(f"Product {product_name} not found")

    # Assign product to user
    assign_resp = requests.post(f"{BASE_URL}/user/products/{product_id}", headers=headers_user)
    assign_resp.raise_for_status()
