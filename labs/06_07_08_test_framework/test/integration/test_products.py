from playwright.sync_api import Page, expect
from models.api.admin import AdminAPI
import os

# Hämtar backend-URL från miljövariabler,sätter upp APier o URLR, lagrar lösenord
BACKEND_URL = os.environ.get("BACKEND_URL","http://127.0.0.1:8000")
admin_page = AdminAPI(BACKEND_URL)
product_name = "Pasta"
username = "admin"
password = "test123" 

def test_add_product_to_catalog():

    admin_page.admin_login(username, password)
    
     # Hämtar antalet produkter innan vi lägger till en ny
    initial_count = admin_page.get_current_product_count()

    admin_page.create_product_by_api(product_name)
    
    # Hämtar uppdaterat antal produkter
    updated_count = admin_page.get_current_product_count()
    
    # Validerar att antalet produkter har ökat med 1
    assert updated_count == initial_count + 1

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app

def test_remove_product_from_catalog():
    product_id = 2
    
    admin_page.admin_login(username, password) #logar in som admin
    
    initial_count = admin_page.get_current_product_count() #Hämtar antalet produkter innan borttagning


    admin_page.delete_product_by_id(product_id)
    updated_count = admin_page.get_current_product_count() #hämta det nuvarande antalet produkter

    #Validera att antalet produkter har tagits bort
    assert updated_count == initial_count - 1, (f"Expected {initial_count - 1} products, but got {updated_count}")