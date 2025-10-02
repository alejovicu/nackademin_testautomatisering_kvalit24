import requests

BACKEND_URL = "http://localhost:8000"


def create_test_user(username="admin", password="admin"):
    payload = {"username": username, "password": password}
    resp = requests.post(f"{BACKEND_URL}/signup", json=payload)
    if resp.status_code == 201:
        print(f"User {username} created")
    elif resp.status_code == 400:
        print(f"User {username} already exists, skipping")
    else:
        resp.raise_for_status()


if __name__ == "__main__":
    create_test_user()
