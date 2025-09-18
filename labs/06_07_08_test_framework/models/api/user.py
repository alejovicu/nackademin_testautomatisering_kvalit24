import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = ""


    def login(self, username, password):
        # complete code
        # set token to object
        # return token
        body = {"username":username, "password":password}
        response = requests.post(f"{self.base_url}/login", json=body)
        self.token = response.json().get("access_token")
        return response

    
    def signup(self, username, password):
        # complete code
        # return username and password
        body = {"username":username, "password":password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response

    
    def get_user_profile(self): 
        response = requests.get(f"{self.base_url}/user", headers = self.headers)
        return response

    def assign_product_to_user(self, product_id):
        response = requests.post(f"{self.base_url}/user/products/{product_id}", headers = self.headers)
        return response

    def remove_product_from_user(self, product_id):
        response = requests.delete(f"{self.base_url}/user/product/{product_id}", headers = self.headers)
        return response