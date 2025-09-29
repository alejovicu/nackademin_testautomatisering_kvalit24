import os
import requests


BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")


#Admin login
admin_login = requests.post(f"{BACKEND_URL}/login", json={
    "username": "admin",
    "password": "1234"
})

if admin_login.status_code != 200:
    # Create new admin if login fails
    requests.post(f"{BACKEND_URL}/signup", json={
        "username": "admin",
        "password": "1234"
    })
    # log in  again
    admin_login = requests.post(f"{BACKEND_URL}/login", json={
        "username": "admin",
        "password": "1234"
    })

admin_login.raise_for_status()
token = admin_login.json()["access_token"]
headers = {"Authorization" : f"Bearer {token}"}




# create user
requests.post(f"{BACKEND_URL}/signup", json={
    "username": "malle",
    "password": "1234",
})



# check if product already exists
products = requests.get(f"{BACKEND_URL}/products", headers=headers).json()
if any(p["name"] == "Monkey" for p in products):
    print("Product 'Monkey' already exists, skipping.")
    #if product don't exists ,then post as new product
else:
    product_create = requests.post(f"{BACKEND_URL}/product", json={"name": "Monkey"}, headers=headers)
    product_create.raise_for_status()
    print("Product 'Monkey' added")