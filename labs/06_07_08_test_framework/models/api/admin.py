
import requests

class AdminAPI:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers
    

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        response.raise_for_status()
        return response


    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers=self._headers())
        response.raise_for_status()
        products = response.json()
        return len(products)

    def create_product(self, product_name):
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/product", json=body, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def delete_product_by_id(self, product_id):
        response = requests.delete(
            f"{self.base_url}/product/{product_id}", headers=self._headers()
        )
        response.raise_for_status()
        return response.status_code == 200