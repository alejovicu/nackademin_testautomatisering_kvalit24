import requests

class UserAPI:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    # LOGIN
    def login(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/login", json=body)
        self.token = response.json().get("access_token")
        return response
    
    # SIGNUP
    def signup(self, username, password):
        body = { "username": username, "password": password }
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response
    
    # GET USER PRODUCTS & RETURN API RESPONSE
    def get_user_products(self):
        response = requests.get(f"{self.base_url}/user", headers={"Authorization": f"Bearer {self.token}"})
        return response

    # ADD PRODUCT TO USER VIA PRODUCT ID (not used right now)
    def add_product_to_user_via_id(self, product_id):
        response = requests.post(f"{self.base_url}/user/products/{product_id}", headers={"Authorization": f"Bearer {self.token}"})
        return response
    
    # DELETE PRODUCT FROM USER VIA PRODUCT ID (not used right now)
    def remove_product_from_user_via_id(self, product_id):
        response = requests.delete(f"{self.base_url}/user/product/{product_id}", headers={"Authorization": f"Bearer {self.token}"})
        return response
    
    # ASSIGN PRODUCT TO USER VIA NAME (not used right now)
    def add_product_to_user(self, product_name):
        
        # Get all products currently in list
        response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
        products = response.json()
        product_id = None

        # Search for product name and find its ID
        for product in products:
            if product["name"] == product_name:
                product_id = product["id"]
                break

        if product_id is None:
            raise ValueError("Product name not found")
        
        response = requests.post(f"{self.base_url}/user/products/{product_id}", headers={"Authorization": f"Bearer {self.token}"})
        return response
    
    # DELETE PRODUCT FROM USER VIA NAME (not used right now)
    def remove_product_from_user(self, product_name):
        response = self.get_user_products()
        data = response.json()

        if "products" not in data:
            raise ValueError("Products key not found in user data")

        product_id = None
        for product in data["products"]:
            if product["name"] == product_name:
                product_id = product["id"]
                break

        if product_id is None:
            raise ValueError(f"Product with name '{product_name}' not found for user")

        delete_response = requests.delete(f"{self.base_url}/user/product/{product_id}", headers={"Authorization": f"Bearer {self.token}"}
        )
        return delete_response