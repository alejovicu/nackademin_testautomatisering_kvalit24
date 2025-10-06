import requests

class AdminAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        """
        Loggar in som admin och sparar token för framtida anrop.
        """
        url = f"{self.base_url}/login"
        body = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=body)
        if response.status_code == 200:
            self.token = response.json().get("access_token")
        return response
    
    def get_current_product_count(self):
        """
        Returnerar antalet produkter i systemet.
        """
        url = f"{self.base_url}/products"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            products = response.json()
            return len(products)
        return 0

    def create_product(self, product_name):
        """
        Skapar en produkt via API.
        """
        url = f"{self.base_url}/product"  # uppdaterad endpoint
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {"name": product_name}
        response = requests.post(url, headers=headers, json=body)
        return response

    def create_product_by_api(self, product_name):
        """
        Behålls för kompatibilitet med tester.
        """
        return self.create_product(product_name)

    def delete_product_by_name(self, product_name):
        """
        Tar bort en produkt baserat på namn.
        Hämta först alla produkter, hitta rätt ID och sedan delete.
        """
        url = f"{self.base_url}/products"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None

        products = response.json()
        for product in products:
            if product.get("name") == product_name:
                product_id = product.get("id")
                delete_url = f"{self.base_url}/product/{product_id}"  # uppdaterad endpoint
                response = requests.delete(delete_url, headers=headers)
                return response

        return None
