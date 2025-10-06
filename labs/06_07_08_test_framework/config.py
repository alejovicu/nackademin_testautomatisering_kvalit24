import os
import time
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://app-backend:8000")


def sign_up_admin():
    url = f"{BACKEND_URL}/signup"
    payload = {
        "username": "admin",
        "password": "pass123"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Admin user signed up successfully.")
        elif response.status_code == 400 and "already exists" in response.text:
            print("Admin user already exists.")
        else:
            print(f"Failed to sign up admin user: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the backend: {e}")

        

def sign_up_user():
    url = f"{BACKEND_URL}/signup"
    payload = {
        "username": "user1",
        "password": "123"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("User signed up successfully.")
        elif response.status_code == 400 and "already exists" in response.text:
            print("User already exists.")
        else:
            print(f"Failed to sign up admin user: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the backend: {e}")





sign_up_admin()
sign_up_user()

if __name__ == "__main__":
    time.sleep(2)  # Wait for 2 seconds to ensure the backend is ready