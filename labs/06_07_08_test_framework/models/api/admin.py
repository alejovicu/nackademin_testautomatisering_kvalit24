import requests

class AdminAPI:
    def __init__(self, base_url, token):
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
