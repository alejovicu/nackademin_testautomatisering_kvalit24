import os
import requests


BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

#Skapa admin login
create_admin = requests.post(f"{BACKEND_URL}/signup", json={
    "username": "admin",
    "password": "1234"
})


# Skapa vanlig användare
create_user = requests.post(f"{BACKEND_URL}/signup", json={
    "username": "user",
    "password": "user",
})



#Admin login
admin_login = requests.post(f"{BACKEND_URL}/login", json={
    "username": "admin",
    "password": "1234"
})
admin_login.raise_for_status()
token = admin_login.json()["access_token"]

headers = {"Authorization" : f"Bearer {token}"}

#Create product

product_create = requests.post(f"{BACKEND_URL}/products", json={"name": "Monkey"}, headers=headers)
product_create.raise_for_status()

if product_create.status_code == 200:
    print("Product 1 added to admin")
else:
    print(f"Failed to add product: {product_create.status_code}")