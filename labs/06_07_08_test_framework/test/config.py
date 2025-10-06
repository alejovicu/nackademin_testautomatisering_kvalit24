import os
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://app-backend:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://app-frontend:5173")


def sign_up_admin():
    url = f"{BACKEND_URL}/signup"
    payload = {
        "username": "admin",
        "password": "pass123"
    }
    try:
        response = requests.post(url, json=payload)

        if response.status_code in [200, 201]:
            print("✅ Admin user signed up successfully.")
        elif response.status_code == 400 and (
            "already exists" in response.text
            or "Username already registered" in response.text
        ):
            print("ℹ️ Admin user already exists. Continuing...")
        else:
            print(f"⚠️ Failed to sign up admin user: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to the backend: {e}")


def sign_up_user():
    url = f"{BACKEND_URL}/signup"
    payload = {
        "username": "user1",
        "password": "123"
    }
    try:
        response = requests.post(url, json=payload)

        if response.status_code in [200, 201]:
            print("✅ User signed up successfully.")
        elif response.status_code == 400 and (
            "already exists" in response.text
            or "Username already registered" in response.text
        ):
            print("ℹ️ User already exists. Continuing...")
        else:
            print(f"⚠️ Failed to sign up user: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to the backend: {e}")


if __name__ == "__main__":
    print("Starting setup...")
    sign_up_admin()
    sign_up_user()
    print("Setup complete.")
