from playwright.sync_api import Page, expect
from models.login import LoginPage
from models.home import HomePage
from models.product import ProductPage
import random
import string


def random_product_name(length=8):
    return "Product_" + "".join(random.choices(string.ascii_letters + string.digits, k=length))

def test_admin_adds_products_and_user_sees_them(page: Page):
    
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    
    home_page.navigate()
    login_page.login("admin", "admin123")

    
    product_names = [random_product_name() for _ in range(2)]
    for name in product_names:
        product_page.add_product(name)

    
    for name in product_names:
        expect(page.get_by_text(name)).to_be_visible()

    
    login_page.logout()

    
    home_page.navigate()
    login_page.login("user", "user123")

    
    for name in product_names:
        expect(page.locator(f"text={name}")).not_to_be_visible()

    
    expect(product_page.button_add_product).not_to_be_visible()
    expect(product_page.button_delete_product).not_to_be_visible()



