import requests
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

# Admin signup and login
data = {"username": "test_admin", "password": "admin_test321"}

admin_signup = requests.post(f"{BACKEND_URL}/signup", json=data)
if admin_signup.status_code == 200:
    print("Admin user created")
elif admin_signup.status_code == 400:
    print("Admin user already exists")
else:
    admin_signup.raise_for_status()

admin_login = requests.post(f"{BACKEND_URL}/login", json=data)
admin_login.raise_for_status()  # Stops if it's fails
print("Login successful")

admin_token = admin_login.json()["access_token"]
headers = {"Authorization" : f"Bearer {admin_token}"}


# User signup
user_signup = requests.post(f"{BACKEND_URL}/signup", json={
    "username": "test_user",
    "password": "user_test321"
})


# Product
product_list = requests.get(f"{BACKEND_URL}/products", headers=headers).json()
if any(product["name"] == "Course 1" for product in product_list):
    print("Product already exists")

else:
    create_product = requests.post(f"{BACKEND_URL}/product", json={"name": "Course 1"}, headers=headers)
    create_product.raise_for_status()
    print("Product created")