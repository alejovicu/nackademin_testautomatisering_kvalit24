import requests

class AdminAPI:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token
    
    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            self.token = response.json().get("access_token")
            if self.token is None:
                raise ValueError("Login succeeded but authorization token missing!")
        return response
    
    def _headers(self):
        if not self.token:
            raise ValueError("Token missing!")
        return {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def list_products(self):
        return requests.get(f"{self.base_url}/products", headers=self._headers())
    
    def create_product(self, product_name):
        body = {"name": product_name}
        return requests.post(f"{self.base_url}/product", json=body, headers=self._headers())
    
    def remove_product_by_name(self, product_name):
        list_response = self.list_products()
        products = list_response.json()
        product = next((p for p in products if p.get("name") == product_name), None)
        if not product:
            raise ValueError(f"Product '{product_name}' not found")
        product_id = product.get("id")
        return requests.delete(f"{self.base_url}/product/{product_id}", headers=self._headers())

