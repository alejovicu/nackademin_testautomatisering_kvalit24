import requests
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

    # === 1. Skapa admin (signup) ===
admin_username = "admin"
admin_password = "1234"

signup_admin_resp = requests.post(
    f"{BACKEND_URL}/signup",
    json={"username": admin_username, "password": admin_password}
    )
if signup_admin_resp.status_code == 200:
    print(f"Admin signup passed: {signup_admin_resp}")

elif signup_admin_resp.status_code == 400:
    print(f"Admin already exists")
else:
    signup_admin_resp.raise_for_status()

# === 2. Logga in som admin ===
login_resp = requests.post(
    f"{BACKEND_URL}/login",
    json={"username": admin_username, "password": admin_password}
)
login_resp.raise_for_status()
print(f"Admin login success: {login_resp}")

token = login_resp.json().get("access_token")
admin_headers = {"Authorization" : f"Bearer {token}"}

# === 3. Skapa en vanlig user (signup) ===
user_username = "user"
user_password = "1234"

signup_user_resp = requests.post(
    f"{BACKEND_URL}/signup",
    json={"username": user_username, "password": user_password},
    headers={"Authorization": f"Bearer {token}"}
)
if signup_user_resp.status_code == 200:
    print(f"User signup passed: {signup_user_resp}")
elif signup_user_resp.status_code == 400:
    print(f"User already exists")
else:
    signup_user_resp.raise_for_status()

print("✅ Admin and user created successfully")
print(f"Admin: {admin_username}")
print(f"User: {user_username}")

# === 4. Skapa en produkt (product) ===
products_resp = requests.get(f"{BACKEND_URL}/products", headers=admin_headers)
products = products_resp.json()

print(products)

products_list = products if isinstance(products, list) else products.get("products", [])

for product in products_list:
    if product.get("name") == "Sample Product":
        print("⚠️ Sample product already exists")
        break
else:
    print("✅ Product does not exist yet")
    create_product_resp = requests.post(
        f"{BACKEND_URL}/product",
        json={"name": "Sample Product"},
        headers=admin_headers
    )
    if create_product_resp.status_code == 200:
        print("Sample product created")
    else:
        create_product_resp.raise_for_status()