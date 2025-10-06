import os
import requests

backend = os.getenv("BACKEND_URL", "http://app-backend:8000")


data_admin = {"username": "admin", "password": "adminadmin1234"}


response = requests.post(f"{backend}/signup", json=data_admin)
if response.status_code == 200:
    print("admin created.")
else:
    print("admin arleady exist.")
