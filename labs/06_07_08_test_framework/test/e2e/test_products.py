from libs.utils import generate_product_string_with_prefix
from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.admin import AdminAPI
from models.api.user import UserAPI
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "1234")

def setup():
    try:
        user_api = UserAPI(BACKEND_URL)
        user_api.signup(ADMIN_USERNAME, ADMIN_PASSWORD)
    except:
        print("Admin already exist.")


def _admin_api():
    api = AdminAPI(BACKEND_URL)
    api.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    return api



def test_add_product_to_catalog(page: Page):
   
    setup()
    api = _admin_api()
    

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI(BACKEND_URL)
    product = generate_product_string_with_prefix()
    
 

  
    response = user_api.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    token = user_api.token

    # Inject the token into localStorage before loading the page
    page.add_init_script(f"""
    window.localStorage.setItem("token", "{token}");
""")

    
    home_page.navigate()
    page.wait_for_load_state("networkidle")

    
    admin_page.create_product(product_name=product)
    page.wait_for_load_state("networkidle")

    page.get_by_text(product).wait_for(state="visible")

 
    assert admin_page.check_product(product).inner_text() == product
    assert admin_page.check_product(product).count() == 1



# Given I am an admin user
# When I remove a product from the catalog
# Then The product should not be listed in the app to be used

def test_remove_product_from_catalog(page: Page):
    api = _admin_api()
    product = generate_product_string_with_prefix()

    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI(BACKEND_URL)

   
    response = user_api.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    token = user_api.token

   
    page.add_init_script(f"""
    window.localStorage.setItem("token", "{token}");
""")

    
    home_page.navigate()
    page.wait_for_load_state("networkidle")

   
    admin_page.create_product(product_name=product)
    page.wait_for_load_state("networkidle")

    page.get_by_text(product).wait_for(state="visible")

    admin_page.delete_product_by_name(product_name=product)
    expect(admin_page.check_product(product)).to_be_hidden()
   