import requests


class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()  # Reuses in all requests
        self.token = None

    def login(self, username, password):
        body = {"username": username, "password": password}
        # Do POST-request with session
        r = self.session.post(f"{self.base_url}/login", json=body)
        # Save token i session
        self.session.headers["Authorization"] = f"Bearer {r.json()['access_token']}"
        return r

    def create_product(self, product_name):
        body = {"name": product_name}
        return self.session.post(f"{self.base_url}/products", json=body)

    def list_products(self):
        response = self.session.get(f"{self.base_url}/products")
        data = response.json()
        return [p["name"] for p in data]

    def delete_product_by_name(self, product_name):
        # complete logic
        products = self.session.get(f"{self.base_url}/products").json()
        for product in products:
            if product["name"] == product_name:
                return self.session.delete(f"{self.base_url}/product/{product['id']}")
        return None
