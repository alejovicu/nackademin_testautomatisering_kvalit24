import requests

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        """
        Loggar in användaren och sparar JWT-token.
        """
        url = f"{self.base_url}/login"
        response = requests.post(url, json={"username": username, "password": password})
        if response.status_code == 200:
            self.token = response.json().get("access_token")
        return response

    def signup(self, username, password):
        """
        Registrerar en ny användare.
        """
        url = f"{self.base_url}/signup"
        body = {"username": username, "password": password}
        response = requests.post(url, json=body)
        return response

    def add_product_to_user(self, product_id):
        """
        Lägger till en produkt för användaren via API.
        """
        url = f"{self.base_url}/user/product/{product_id}"  # uppdaterad endpoint
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers)
        return response

    def remove_product_from_user(self, product_id):
        """
        Tar bort en produkt från användaren via API.
        """
        url = f"{self.base_url}/user/product/{product_id}"  # uppdaterad endpoint
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.delete(url, headers=headers)
        return response
