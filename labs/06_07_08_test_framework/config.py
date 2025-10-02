import requests

BACKEND_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:5173"
ADMIN_USER = {"username": "admin", "password": "admin"}


def reset_database():
    resp = requests.post(f"{BACKEND_URL}/reset-db")
    resp.raise_for_status()
    print("Database reset")


def create_test_user(username="testuser", password="password"):
    payload = {"username": username, "password": password}
    resp = requests.post(f"{BACKEND_URL}/signup", json=payload)
    if resp.status_code == 201:
        print(f"User {username} created")
    elif resp.status_code == 400:
        print(f"ℹUser {username} already exists, skipping")
    else:
        resp.raise_for_status()


def setup_environment():
    reset_database()
    create_test_user()


if __name__ == "__main__":
    setup_environment()
