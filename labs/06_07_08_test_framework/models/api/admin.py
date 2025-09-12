import requests


class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        products = response.json()
        return len(products)

    def create_product(self, product):
        body = { "name": product}
        response = requests.post(f"{self.base_url}/products", json=body, headers=self.headers)
        return response
    
    def get_products(self):
        resp = requests.get(f"{self.base_url}/products", headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def delete_product_by_name(self, product_name):
        # I did this in my test_products.py, but it seems like doing it here is more reusable,
        # so i simplified the test_products.py using this.
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        products = response.json()
        
        product_id = None
        for p in products:
            if p["name"] == product_name:
                product_id = p["id"]
                break
        
        remove_product_response = requests.delete(f"{self.base_url}/product/{product_id}", headers=self.headers)
        return remove_product_response
