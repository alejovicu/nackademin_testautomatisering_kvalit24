# View where an user (non admin) can Choose
# produts from the Product Catalog and/or
# remove it
import requests
import libs.utils

class UserAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.token = None # self.token en plats där vi kan spara inloggningstoken. Den sätts till none i början för vi är inte inloggade än.

    # en hjälpmetod som bygger HTTP-headers
    def _auth_headers(self):
        if self.token: # kollar om vi har token, dvs om vi loggat in.
            return {"Authorization": f"Bearer {self.token}"} # om vi är inloggade returneras en header-dict med authorization.
        return {} # om vi inte är inloggade returneras en tom dict


    def login(self, username: str, password: str):
        
        # skicka inloggning till API:t
        resp = requests.post(f"{self.base_url}/login", json={"username": username, "password": password})

        # Kontrollerar om svaret är OK, om inte kasta fel ex om servern svarar med ex 400
        resp.raise_for_status()

        # Läser svaret från request som JSON och hämtar access_token
        data = resp.json() or {}
        access_token = data.get("token") or data.get("access_token")

        # Det här gör att det stoppas här om ingen token hittades i svaret. 
        if not access_token:
            raise RuntimeError("Login successful, but no token was found in response.")
        
        # här sparas den hämtade token i ett objekt som jag sen kan användas i andra anrop
        self.token = access_token

        # Returnerar token ifall den ska användas direkt i testet. 
        return access_token
    

    def signup(self):
        # det här skapar unika användarnamn och lösen och tilldelas till username och password.
        username = libs.utils.generate_string_with_prefix("username")
        password = libs.utils.generate_string_with_prefix("password")

        # här skickas registreringen till s>z bervern (backend), skickas med en POST request
        resp = requests.post(f"{self.base_url}/signup", json={"username": username, "password": password})

        # koden avbryts här om man inte får statuskod OK
        resp.raise_for_status()

        # här returneras de genererade uppgifterna för inlogg så att testet kan logga in.
        return username, password
    

    def add_product_to_user(self, product_id: str):
        
        # skickar post request med authorization bearer token.
        resp = requests.post(f"{self.base_url}/user/product/{product_id}", headers=self._auth_headers())
        
        # kollar att vi får OK, annars bryts koden här
        resp.raise_for_status()

        # returnerar svaret i json annars i en tom dict
        return resp.json() if resp.content else {}

    def remove_product_from_user(self, product_id):
        
        resp = requests.delete(f"{self.base_url}/user/product/{product_id}", headers=self._auth_headers())

        # kollar att vi får OK, annars bryts koden här
        resp.raise_for_status()

        # returnerar svaret i json annars i en tom dict
        return resp.json() if resp.content else {}
    
    def get_profile(self):

        resp = requests.get(f"{self.base_url}/user", headers=self._auth_headers())
        resp.raise_for_status()
        return resp.json()
    
    def signup_admin(self, username, password):
        body = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/signup", json=body)
        return response