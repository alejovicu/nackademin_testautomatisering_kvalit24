import requests


class AdminAPI:
    def __init__(self, base_url, token):
        if not token:
            raise ValueError("Token must not be None")
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        products = response.json()
        return len(products)

    def create_product(self, product):
        body = { "name": product}
        response = requests.post(f"{self.base_url}/product", json=body, headers=self.headers)
        return response
    
    def get_products(self):
        resp = requests.get(f"{self.base_url}/products", headers=self.headers)
        resp.raise_for_status()
        return resp.json()
    
    def product_exists_in_backend(self, product):
        products = self.get_products()  # returns list of products
        return any(p["name"] == product for p in products)

    def delete_product_by_name(self, product_name):
        # I did this in my test_products.py, but it seems like doing it here is more reusable,
        # so i simplified the test_products.py using this.
        #response = requests.get(f"{self.base_url}/products", headers=self.headers)
        #products = response.json()
        
        #product_id = None
        #for p in products:
        #    if p["name"] == product_name:
        #        product_id = p["id"]
        #        break
        
        #remove_product_response = requests.delete(f"{self.base_url}/product/{product_id}", headers=self.headers)
        #return remove_product_response
        products = self.get_products()  # returns list of products
    
        product_id = next((p["id"] for p in products if p["name"] == product_name), None)
        if product_id is None:
            raise ValueError(f"Product {product_name} not found in backend")
        
        response = requests.delete(f"{self.base_url}/product/{product_id}", headers=self.headers)
        response.raise_for_status()
        return response
