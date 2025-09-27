# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests


class UserAPI:
   def __init__(self, base_url):
       self.base_url = base_url
       self.token = None


   def set_token(self, token):
       self.token = token


   def login(self, username, password):
      
       body = {"username": username, "password": password }
       response = requests.post(f"{self.base_url}/login", json=body)

       # set token to object
       if response.status_code == 200:
           self.set_token(response.json().get("access_token"))

       return response
      

   def signup(self, username, password):
       body = {"username": username, "password": password }
       response = requests.post(f"{self.base_url}/signup", json=body)

       return response


   def add_product_to_user(self, product_id):

       headers = {"Authorization": f"Bearer {self.token}"}
       add_product_response = requests.post(f"{self.base_url}/user/products/{product_id}", headers=headers)
      
       return add_product_response


   def remove_product_from_user(self, product_id):

       headers = {"Authorization": f"Bearer {self.token}"}
       remove_product_response = requests.delete(f"{self.base_url}/user/product/{product_id}", headers=headers)

       return remove_product_response