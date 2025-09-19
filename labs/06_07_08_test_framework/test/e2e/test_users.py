from playwright.sync_api import Page, expect
from models.ui.user import UserPage
from facade.users import UsersFacade


def test_signup(page: Page):

    # GIVEN I AM A NEW POTENTIAL CUSTOMER
    users_facade = UsersFacade(page)
    user_page = UserPage(page)

    # WHEN I SIGN IN THE APP
    username, password = users_facade.login_as_new_user()

    # THEN I SHOULD BE ABLE TO LOG IN WITH MY NEW USER
    expect(user_page.get_welcome_message(username)).to_be_visible(timeout=10000)

def test_login(page: Page):

    # GIVEN I AM AN AUTHENTICATED USER
    # Assumes this user already exists in DB and has three products assigned
    username = "user_1"
    password = "pass_1"

    # WHEN I LOG INTO THE APPLICATION
    users_facade = UsersFacade(page)
    users_facade.login_via_token(username, password)

    # THEN I SHOULD SEE ALL MY PRODUCTS
    user_page = UserPage(page)
    expect(user_page.user_headline_products).to_be_visible()

    ui_products = user_page.get_user_products()
    api_products = users_facade.get_user_products_names()
    assert sorted(ui_products) == sorted(api_products)
