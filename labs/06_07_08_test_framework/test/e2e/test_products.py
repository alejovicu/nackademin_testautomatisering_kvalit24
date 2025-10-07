from libs.utils import generate_product_string_with_prefix
from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage
from models.api.admin import AdminAPI
from models.api.user import UserAPI
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def _admin_api():
    api = AdminAPI(BACKEND_URL)
    api.login("admin", "1234")
    return api



def test_add_product_to_catalog(page: Page):
   
    api = _admin_api()
    
    home_page = HomePage(page)
    admin_page = AdminPage(page)
    user_api = UserAPI(BACKEND_URL)
    product = generate_product_string_with_prefix()
  
    response = user_api.login("admin", "1234")
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

   
    response = user_api.login("admin", "1234")
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
   