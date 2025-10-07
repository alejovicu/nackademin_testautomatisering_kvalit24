import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.status_code = None

    def set_token(self, token: str):
        self.token = token

    def _auth_headers(self) -> dict:
        if not self.token:
            raise ValueError("No token set - log in or use set_token().")
        return {"Authorization": f"Bearer {self.token}"}

    def signup(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        self.status_code = response.status_code
        return response
        #return response.json()
       

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        self.status_code = response.status_code 
        response.raise_for_status()
        data = response.json()
        # <-- FIX: don't KeyError if token missing / named differently
        self.token = data.get("token") or data.get("access_token") or data.get("jwt")
        return response
        #return data

    def get_user_products(self):
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.get(f"{self.base_url}/user", headers=headers)
        self.status_code = response.status_code
        data = response.json()

        if isinstance(data, list):
            return data
        if isinstance(data, dict) and isinstance(data.get("products"), list):
            return data["products"]
        return []
