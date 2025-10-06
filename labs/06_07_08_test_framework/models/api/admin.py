'''import requests


class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        
        self.token = None
    
   

    def login(self, username, password):
        # complete logic
        body = {"username":username, "password":password}
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
        return None'''

import requests
# Changed import location to the new config file for credentials and URL
from config import get_admin_credentials

class AdminAPI:
    def __init__(self, base_url, token=None):
       
        self.base_url = base_url
        self.token = token

    def login(self):
        """Logs in the admin user using credentials from the config file."""
        username, password = get_admin_credentials()
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/login", json=body)
        
        if response.status_code == 200:
            self.token = response.json().get("access_token") or response.json().get("token")
        return response
        
    def get_auth_headers(self):
        
        if not self.token:
            # Handle case where token is missing before attempting a secure call
            raise Exception("Admin user not logged in. Token is missing.")
            
        return {"Authorization": f"Bearer {self.token}"}
    
    def get_all_products(self):
        #Fetches all products from the catalog.
        response = requests.get(f"{self.base_url}/products", headers=self.get_auth_headers())
        
        if response.status_code == 200:
            return response.json()  # assuming API returns a list of products
        else:
            print(f"Failed to fetch products. Status: {response.status_code}, Body: {response.text}")
            raise Exception("Failed to fetch products")
        
    def get_current_product_count(self):
        """Returns the total number of products in the catalog."""
        products = self.get_all_products()
        return len(products)
    
    def create_product(self, product_name):
        """Creates a new product with the given name."""
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/product", json=body, headers=self.get_auth_headers())
        return response
    
    def delete_product_by_name(self, product_name):
        """Deletes a product by looking up its ID based on the name."""
        products = self.get_all_products()
  
        for product in products:
            if product.get("name") == product_name:
                # Assuming the product dictionary has an 'id' key
                product_id = product.get("id")
                if product_id is not None:
                    return requests.delete(f"{self.base_url}/product/{product_id}", headers=self.get_auth_headers())
        
        # Return a response indicating not found if the product wasn't deleted
        print(f"Product '{product_name}' not found for deletion.")
        return requests.Response() # Return a dummy response if deletion fails          




    
