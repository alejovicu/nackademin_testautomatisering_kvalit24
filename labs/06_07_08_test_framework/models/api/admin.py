import requests


class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.session = requests.Session()

    def login(self, username, password):
        body = {"username": username, "password": password}
        r = self.session.post(f"{self.base_url}/login", json=body)
        if r.status_code == 200:
            token = r.json().get("access_token")
            if token:
                self.session.headers["Authorization"] = f"Bearer {token}"
        return r

    def list_products(self):
        response = self.session.get(f"{self.base_url}/products")
        if response.status_code != 200:
            return []
        data = response.json() or []
        return [p.get("name") for p in data]

    def create_product(self, product_name):
        body = {"name": product_name}
        r = self.session.post(f"{self.base_url}/product", json=body)
        if r.status_code == 404:
            r = self.session.post(f"{self.base_url}/products", json=body)
        return r

    def delete_product_by_name(self, product_name):
        resp = self.session.get(f"{self.base_url}/products")
        if resp.status_code != 200:
            return resp
        products = resp.json() or []
        for product in products:
            if product.get("name") == product_name:
                r = self.session.delete(f"{self.base_url}/product/{product['id']}")
                if r.status_code == 404:
                    r = self.session.delete(f"{self.base_url}/products/{product['id']}")
                return r
        return None

    def get_current_product_count(self):
        return len(self.list_products())
