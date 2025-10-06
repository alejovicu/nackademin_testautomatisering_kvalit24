
import requests

class ProductAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}


    def list_products(self):
        r = requests.get(f"{self.base_url}/products", headers=self.headers)
        r.raise_for_status()
        return r.json()

    def delete_product(self, product_id):
        r = requests.delete(f"{self.base_url}/product/{product_id}", headers=self.headers)
        r.raise_for_status()
        return r.json()
