import os
import requests

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")


def create_user(username: str, password: str) -> requests.Response:
    response = requests.post(f"{BACKEND_URL}/signup", json={
        "user1": username,
        "user1234": password,
    })
    response.raise_for_status()
    return response


def login(username: str, password: str) -> str:
    response = requests.post(f"{BACKEND_URL}/login", json={
        "user1": username,
        "user1234": password,
    })
    response.raise_for_status()
    return response.json()["access_token"]


def create_product(name: str, token: str) -> requests.Response:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_URL}/products", json={"name": name}, headers=headers)
    response.raise_for_status()
    return response



if __name__ == "__main__":
    
    user_resp = create_user("user1", "user")
    print(f"User created: {user_resp.status_code}")

    
    admin_token = login("admin", "admin1234")
    print("Admin logged in successfully")

    
    product_resp = create_product("Monkey", admin_token)
    print(f"Product created: {product_resp.status_code}")
