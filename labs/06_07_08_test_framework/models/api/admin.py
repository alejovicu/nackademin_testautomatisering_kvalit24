import requests


class AdminAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_current_product_count(self):
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        response.raise_for_status()  # raises an error if request fails
        products = response.json()  # assume API returns a list of products
        return len(products)  # return an integer, not None

    def create_product(self, product_name):
        payload = {"name": product_name}
        response = requests.post(f"{self.base_url}/product", json=payload, headers=self.headers)
        response.raise_for_status()
        return response  # return full response so tests can check status or body

    def delete_product_by_name(self, product_name):
        resp = requests.get(f"{self.base_url}/products", headers=self.headers)
        resp.raise_for_status()
        products = resp.json()

        # Loopa igenom products för att matcha angivna namnet med ett namn i listan.
        # Vi tar den hittade produkten tar dens id och lägger den i product_id
        product_id = None
        for p in products:
            if p.get("name") == product_name:
                product_id = p.get("id")
                break

        if product_id is None:
            raise ValueError(f'Ingen produkt med namn: "{product_name}" hittades!')

        # delete request för att radera en produkt med ID.
        del_resp = requests.delete(f"{self.base_url}/product/{product_id}", headers=self.headers)
        del_resp.raise_for_status()

        return del_resp.json() if del_resp.content else {}
