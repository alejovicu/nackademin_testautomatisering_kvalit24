import requests


class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url

        self.session = requests.Session()
        self.token = None

    def login(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        self.status_code = response.status_code 
        response.raise_for_status()
        data = response.json()
        self.token = data.get("token") or data.get("access_token") or data.get("jwt")
        return response

    def create_product(self, product_name):
        body = {"name": product_name}
        return self.session.post(f"{self.base_url}/product", json=body)
    
    def find_product(self, product_name):
        return self.product_list.filter(has_text=product_name)

    def list_products(self):
        response = self.session.get(f"{self.base_url}/products")
        data = response.json()
        return [p["name"] for p in data]

    def delete_product_by_name(
        self,
        product_name):
        products = self.session.get(f"{self.base_url}/products").json()
        print(products)
        for product in products:
            if product['name'] == product_name:
                return self.session.delete(f"{self.base_url}/product/{product['id']}")
        return None
