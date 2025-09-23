import requests

class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        



    def login(self, username, password):
        # complete logic
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        if response.status_code == 200:
            self.token = response.json().get("token")
            return response
        

    def get_all_products(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
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
        headers = {"Authorization": f"Bearer {self.token}"}
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/products", json=body, headers=headers)
        return response
        


    def delete_product_by_name(self, product_name):
        # complete logic
       for product in self.get_all_products():
            if product['name'] == product_name:
                product_id = product['id']
                headers = {"Authorization": f"Bearer {self.token}"}
                url = f"{self.base_url}/products/{product_id}"
                response = requests.delete(url, headers=headers)
                return response.status_code == 204
                 



