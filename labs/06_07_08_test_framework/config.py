import requests
import os

# Hämta backend-URL, default till localhost
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

# Försök skapa admin-användaren först
admin_signup = requests.post(f"{BACKEND_URL}/signup", json={
    "username": "admin",
    "password": "test123"
})

if admin_signup.status_code == 200:
    print("Admin user created.")
elif admin_signup.status_code == 400:
    print("Admin user already exists.")
else:
    admin_signup.raise_for_status()
    print("Unexpected response during admin signup")

# Logga in med admin
admin_login = requests.post(f"{BACKEND_URL}/login", json={
    "username": "admin",
    "password": "test123"
})

if admin_login.status_code != 200:
   print("login failed")

# Extrahera token
admin_token = admin_login.json().get("access_token")
headers = {"Authorization": f"Bearer {admin_token}"}

# Skapa en ny användare
user_signup = requests.post(f"{BACKEND_URL}/signup", json={
    "username": "användare",
    "password": "Flagga123"
})

if user_signup.status_code == 200:
    print("User created.")
elif user_signup.status_code == 400:
    print("User already exists.")
else:
    print("Unexpected response during user signup")

# Hämta produkter
product_list_response = requests.get(f"{BACKEND_URL}/products", headers=headers)
product_list = product_list_response.json()

# Skapa produkt om den inte redan finns
if any(product["name"] == "English" for product in product_list):
    print("Product already exists.")
else:
    create_product = requests.post(
        f"{BACKEND_URL}/product", json={"name": "English"}, headers=headers
    )
    if create_product.status_code == 200:
        print("Product created.")
    else:
        print("Failed to create product")
