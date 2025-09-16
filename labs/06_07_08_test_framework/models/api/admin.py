import requests

class AdminAPI:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    # RETURN LENGTH OF PRODUCT LIST
    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
        return len(response.json())
    
    # RETURN PRODUCT LIST AS IT IS
    def get_product_list(self):
        response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
        return response.json()

    # CREATE PRODUCT, RETURN API RESPONSE
    def create_product(self, product_name):
        body = {"name": product_name}
        response = requests.post(f"{self.base_url}/products", json=body, headers={"Authorization": f"Bearer {self.token}"})
        return response

    # DELETE PRODUCT, RETURN API RESPONSE
    def delete_product_by_name(self, product_name):

        # Get all products currently in list
        response = requests.get(f"{self.base_url}/products", headers={"Authorization": f"Bearer {self.token}"})
        products = response.json()
        product_id = None

        # Search for product name and find its ID
        for product in products:
            if product["name"] == product_name:
                product_id = product["id"]
                break
        
        # Use the id to delete product
        delete_response = requests.delete(f"{self.base_url}/product/{product_id}", headers={"Authorization": f"Bearer {self.token}"})
        return delete_response
    
    # LOG IN AS ADMIN AND RETURN TOKEN
    # Works even if database is cleared and no admin exists
    # BUT need to run test_products.py BEFORE test_users.py, otherwise a user will have id==1 and be considered admin
    def get_admin_token(self, username="admin", password="admin123"):

        login_body = {"username": username, "password": password}
        login_response = requests.post(f"{self.base_url}/login", json=login_body)

        if login_response.status_code == 200:
            self.token = login_response.json().get("access_token")
            return self.token

        signup_body = {"username": username, "password": password}
        requests.post(f"{self.base_url}/signup", json=signup_body) 
        login_response = requests.post(f"{self.base_url}/login", json=login_body)

        self.token = login_response.json().get("access_token")
        return self.token
