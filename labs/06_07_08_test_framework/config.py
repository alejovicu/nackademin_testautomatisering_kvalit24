import os
import requests

backend = os.getenv("BACKEND_URL", "http://app-backend:8000")


data_admin = {"username": "admin", "password": "1234"}

try:
    requests.post(f"{backend}/signup", json=data_admin)
except:
    print("admin arleady exist.")
