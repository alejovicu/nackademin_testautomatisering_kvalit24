import requests

# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    # LOGIN & RETURN API RESPONSE
    def login(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        return response
    
    # SIGNUP & RETURN API RESPONSE
    def signup(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response
    
    # GET USER PRODUCTS & RETURN API RESPONSE
    def get_user_products(self, token):
        response = requests.get(f"{self.base_url}/user", headers={"Authorization": f"Bearer {token}"})
        return response

    def add_product_to_user(self, product_name):
        # complete code
        return None

    def remove_product_from_user(self, product_name):
        # complete code
        return None