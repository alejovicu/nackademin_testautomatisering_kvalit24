
import uuid
import pytest
from models.home import HomePage
from models.login import LoginPage
from models.signup import SignupPage
from models.product import ProductPage   # ✅ stor bokstav, matchar klassen

def test_add_and_remove_product(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    product_page = ProductPage(page)

    home_page.navigate()

    # Skapa ny användare
    login_page.navigate_to_signup()
    username = "admin"
    password = "password123"
    signup_page.signup(username, password)

    home_page.navigate()
    login_page.login(username, password)

    # Lägg till produkt
    product_page.add_product("TestProdukt")

    assert product_page.is_product_listed("TestProdukt")

    # Ta bort produkten
    #product_page.remove_product("TestProdukt")

    #assert not product_page.is_product_listed("TestProdukt")







