import requests

# Base class providing shared auth logic for UserAPI and AdminAPI
class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = ""

    # Fresh headers based on current token (new dict each access)
    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}" if self.token else "",
            "Content-Type": "application/json",
        }
    
    def login(self, username: str, password: str):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        # Save the response access token for later use
        self.token = response.json().get("access_token")
        return response
    
    # Helper function to get product id by supplied name
    def get_product_id(self, product_name: str) -> int | None:
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        products = response.json()
        for product in products:
            if product["name"] == product_name:
                return product["id"]
        return None