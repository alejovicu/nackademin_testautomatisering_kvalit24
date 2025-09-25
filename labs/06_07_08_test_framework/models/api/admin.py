import requests

class AdminAPI:
    def __init__(self, base_url, token: str):
        self.base_url = base_url
        self.token = token

    # en hjälpmetod som bygger HTTP-headers
    def _auth_headers(self):
        if self.token: # kollar om vi har token, dvs om vi loggat in.
            return {"Authorization": f"Bearer {self.token}"} # om vi är inloggade returneras en header-dict med authorization.
        return {} # om vi inte är inloggade returneras en tom dict

    def login(self, username: str, password: str):
        resp = requests.post(f"{self.base_url}/login", json={"username": username, "password": password})
        resp.raise_for_status()
        data = resp.json() or {}
        token = data.get("token") or data.get("access_token")
        if not token:
            raise RuntimeError("Login successful, but no token found in response.")
        self.token = token
        return token

    def get_current_product_count(self):
        # skickar get request med authorization bearer token
        resp = requests.get(f"{self.base_url}/products", headers=self._auth_headers())

        # kollar att det är OK
        resp.raise_for_status()
        
        # tolkar svaret som json
        data = resp.json()

        # if isinstance berättar vilken typ ett objekt är i detta fall är data en list, och len räknar antalet element i då den listan. 
        if isinstance(data, list):
            return len(data)
        
        # om api:et inte returnerar en lista. 
        raise ValueError(f"Oväntat svar: {data}")
    

    def create_product(self, product_name):
        
        resp = requests.post(f"{self.base_url}/products", headers=self._auth_headers(), json={"name": product_name})

        resp.raise_for_status()

        return resp.json() if resp.content else {}


    # behöver först loopa igenom listan med produkter för att matcha det med angivna produktnamnet och plocka ut dens ID.
    def delete_product_by_name(self, product_name):
        
        # Get request för att lista produkterna
        resp = requests.get(f"{self.base_url}/products", headers=self._auth_headers())
        resp.raise_for_status()
        products = resp.json()

        # Loopa igenom products för att matcha angivna namnet med ett namn i listan. Vi tar den hittade produkten tar dens id och lägger den i product_id
        product_id = None
        for p in products:
            if p.get("name") == product_name:
                product_id = p.get("id")
                break

        if product_id is None:
            raise ValueError(f'Ingen produkt med namn: "{product_name}" hittades!')
        
        # delete request för att radera en produkt med ID. 
        del_resp = requests.delete(f"{self.base_url}/product/{product_id}", headers=self._auth_headers())
        del_resp.raise_for_status()

        return del_resp.json() if del_resp.content else {}
    
