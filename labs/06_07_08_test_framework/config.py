import requests
import os 

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

# Admin credentials
admin_username = "nermin123"
admin_password = "nermin_123"

signup_admin = requests.post(f"{BACKEND_URL}/signup", json={
    "username": admin_username,
    "password": admin_password
})

if signup_admin.status_code == 200:
    print("Admin skapad")
else:
    print("Admin finns redan")

admin_login = requests.post(f"{BACKEND_URL}/login", json={
    "username": admin_username,
    "password": admin_password
})

admin_login.raise_for_status()  # stoppa samt visa felet om inlogg misslyckas
admin_token = admin_login.json()["access_token"]
headers = {"Authorization": f"Bearer {admin_token}"}


user_signup = requests.post(f"{BACKEND_URL}/signup", json={
    "username": "test123",
    "password": "test_123"
})

if user_signup.status_code == 200:
    print("Testanvändare skapad")
else:
    print("Testanvändare finns redan")


product_list = requests.get(f"{BACKEND_URL}/products", headers=headers).json()

if any(product["name"] == "item 1" for product in product_list):
    print("Product already exists")
else:
    create_product = requests.post(
        f"{BACKEND_URL}/product",
        json={"name": "item 1"},
        headers=headers
    )
    create_product.raise_for_status()
    print("Product created")
