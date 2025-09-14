import requests

class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None


    def set_admin_token(self, token):
        self.token = token


    def admin_login(self, username, password):
        
        body = {"username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)

         # set token to object
        if response.status_code == 200:
            self.set_admin_token(response.json().get("access_token"))

        return response


    def get_all_products(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/products", headers=headers)
        products = response.json()

        return products


    def get_current_product_count(self):
        # return number of total products displayed
        headers = {"Authorization": f"Bearer {self.token}"}
        product_response = requests.get(f"{self.base_url}/products", headers=headers)
        products = product_response.json()

        return len(products)


    def create_product(self, product_name):

        body = {"name": product_name}
        headers = {"Authorization": f"Bearer {self.token}"}
        product_response = requests.post(f"{self.base_url}/products", json=body, headers=headers)
        
        return product_response


    def delete_product_by_name(self, product_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        delete_product_response = requests.delete(f"{self.base_url}/product/{product_id}", headers=headers)

        return delete_product_response