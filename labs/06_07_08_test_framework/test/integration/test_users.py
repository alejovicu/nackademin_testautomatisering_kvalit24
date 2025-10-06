# complete imports
import libs.utils
from models.api.user import UserAPI
from models.api.admin import AdminAPI
import os
import pytest 
import requests

# BASE_URL pekar på API-server localhost:8000
BASE_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
ADMIN_USER = os.getenv("ADMIN_USERNAME", "nahom_admin")
ADMIN_PASS = os.getenv("ADMIN_PASSWORD", "1234")


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup():
    user_api = UserAPI(BASE_URL)

    username, password = user_api.signup()

    token = user_api.login(username, password)
    
    assert isinstance(token, str) and token


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_list_products():

    """
    1. En admin loggar in för att skapa en produkt (endast admin-behörighet kan skapa produkt).
    2. Sedan plockas produkt-id från den skapade produkten för att man assignar med produkt-id.
    3. En non-admin user skapas/signup och loggas in.
    4. Nya användaren kan koppla/assigna produkten till sig/sin produkt-lista
    5. Användaren listar sin produkt-lista med GET/user för att kunna se sina produkter
    6. Testet städar efter sig den tar bort kopplade/assignade produkten.
    
    """

    # Först loggar admin in och skapar en produkt
    admin_api = AdminAPI(BASE_URL, token=None) # skapar ett AdminAPI-objekt, token=None betyder att vi inte är inloggade än. 
    
    # Vi anropar login metoden med adminuppgifterna från ovan. Metoden sparar token i admin_api så att _auth_headers() kan skicka Authorization i alla senare anrop. 
    admin_api.login(ADMIN_USER, ADMIN_PASS) # 

    # Skapar ett unikt produktamn ex prod-ab12cd
    product_name = libs.utils.generate_string_with_prefix("prod")

    # Skapar produkt som admin med metoden från AdminAPI klassen. 
    created_product = admin_api.create_product(product_name)

    # Sedan få fram produkt-ID och lägg in i variabel product_id.
    product_id = created_product["id"]
    assert product_id # kollar att id finns annars stoppar testet här. 

    # 2) Vanlig användare signar upp & loggar in
    user_api = UserAPI(BASE_URL) # skapar objektet mot adressen till API:t
    username, password = user_api.signup() # registrerar användare med UserAPI metoden signup
    user_api.login(username, password) # loggar in användaren med UserAPI metoden login. 
    assert user_api.token # Verifiera att vi är inloggade.

    try: # betyder försök först med den här koden om ngt går fel ex serverfel då hoppar den till finally.
        # 3) Assign produkt till användaren (POST /user/products/{product_id})
        user_api.add_product_to_user(product_id)

        # 4) Lista produkter för användaren via profil (GET /user)
        profile = user_api.get_profile()  # hämtar användarens produktlista med GET request. 
        user_product_ids = [] # tillsätter tom lista
        for p in profile.get("products", []): # gå igenom varje produkt i listan. 
            product_id = p.get("id") 
            user_product_ids.append(product_id)
        assert product_id in user_product_ids, "Produkten saknas på användaren efter assign"

    finally:
        # 5) Unassign och städa
        try:
            # DELETE /user/product/{product_id}
            user_api.remove_product_from_user(product_id)
        except Exception:
            pass
        try:
            # DELETE /product/{product_id} (singular enligt din Swagger)
            admin_api.delete_product_by_name(product_name)
        except Exception:
            pass

