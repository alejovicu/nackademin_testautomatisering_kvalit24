import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def set_token(self, token: str):
        self.token = token

    def _auth_headers(self) -> dict:
        if not self.token:
            raise ValueError("No token set - log in or use set_token().")
        return {"Authorization": f"Bearer {self.token}"}

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response.json()

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        response.raise_for_status()
        self.token = response.json()["token"]
        return response.json()

    def get_user_products(self):
        headers = self._auth_headers()
        return requests.get(f"{self.base_url}/user", headers=headers)
