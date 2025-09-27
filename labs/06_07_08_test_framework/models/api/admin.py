import requests

class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def auth_token(self, token):
        self.token = token

    def admin_login(self, username, password):
        data = {"username": username, "password": password}
        login_response = requests.post(f"{self.base_url}/login", json=data)

        if login_response.status_code == 200:
            self.auth_token(login_response.json().get("access_token"))
            return login_response
    
    def get_all_products(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        create_product_resp = requests.get(f"{self.base_url}/products", headers=headers)
        products = create_product_resp.json()

        return products

    def product_count(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        create_product_resp = requests.get(f"{self.base_url}/products", headers=headers)
        products = create_product_resp.json()

        return len(products)
        
    
    def create_product(self, product_name):
        data = {"name": product_name}
        headers = {"Authorization": f"Bearer {self.token}"}
        create_product_resp = requests.post(f"{self.base_url}/products", json=data, headers=headers)
        
        return create_product_resp

    def delete_product_by_name(self, product_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        delete_product = requests.delete(f"{self.base_url}/product/{product_id}", headers=headers)
        
        return delete_product



    