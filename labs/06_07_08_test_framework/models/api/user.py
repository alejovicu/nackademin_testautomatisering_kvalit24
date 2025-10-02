# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
#import requests


#class UserAPI:
    #def __init__(self, base_url):
        #self.base_url = base_url

    #def login(self, username, password):
        #body = { "username": username, "password": password }
        #response = requests.post(f"{self.base_url}/login", json=body)
        #return response

    #def signup(self, username, password):
        #body = { "username": username, "password": password }
        #response = requests.post(f"{self.base_url}/signup", json=body)
        #return response


    #def add_product_to_user(self, product_name):
        # complete code
        #return None

    #def remove_product_from_user(self, product_name):
        # complete code
        #return None

# models/api/user.py

# models/api/user.py

import requests

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
    
    def set_token(self, token):
        self.token = token

    def _headers(self):
        if self.token:
            return {"Authorization": f"Bearer {self.token}"}
        return {}

    def signup(self, username, password):
        url = f"{self.base_url}/signup"
        body = {"username": username, "password": password}
        res = requests.post(url, json=body)
        res.raise_for_status()
        return res.json()

    def login(self, username, password):
        url = f"{self.base_url}/login"
        body = {"username": username, "password": password}
        res = requests.post(url, json=body)
        res.raise_for_status()
        return res.json()  # Expecting token in response

    
    def get_user(self):
        # Use self.token automatically
        response = requests.get(f"{self.base_url}/user", headers=self._headers())
        return response.json()