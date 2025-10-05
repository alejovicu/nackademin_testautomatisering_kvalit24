import os
import requests

class Config:
    # Backend URL comes from environment (Docker/Jenkins), defaults to localhost
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

    # Users to seed
    SEED_USERS = {
        "admin": "pass1234",
        "test_1234": "test_1234"
    }


def config_signup(username: str, password: str):
    url = f"{Config.BACKEND_URL}/signup"
    payload = {"username": username, "password": password}

    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 201:
            print(f"User {username} created successfully")
        elif response.status_code == 400:
            print(f"User {username} already exists")
        else:
            print(f"Failed to create {username}: {response.status_code} {response.text}")
    except requests.RequestException as e:
        print(f"Error contacting backend: {e}")


def seed_users():
    for username, password in Config.SEED_USERS.items():
        config_signup(username, password)


if __name__ == "__main__":
    print(f"Seeding users into {Config.BACKEND_URL}...")
    seed_users()