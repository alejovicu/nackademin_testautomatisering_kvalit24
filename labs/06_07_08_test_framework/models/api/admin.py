import requests

class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        # complete logic
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            self.token = response.json().get("token")
            return response

    def get_auth_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get_all_products(self):
        response = requests.get(f"{self.base_url}/products", headers = self.get_auth_headers())
        if response.status_code == 200:
            return response.json()  # assuming API returns a list of products
        else:
            raise Exception("Failed to fetch products")

    def get_current_product_count(self):
        # complete logic
        # return number of total products displayed
        products=self.get_all_products()
        return len(products)

    def create_product(self, product_name):
        # complete logic
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/products", json=body, headers=self.get_auth_headers())
        return response
                    
    def delete_product_by_name(self, product_name):
        # complete logic
        products = self.get_all_products()
  
        for product in products:
            if product["name"] == product_name:
                return requests.delete(f"{self.base_url}/product/{product['id']}", headers=self.get_auth_headers())
        
        return None
       
                 



