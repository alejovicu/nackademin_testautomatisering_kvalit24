from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from facade.users import UsersFacade


def test_signup(page: Page):

    # GIVEN I AM A NEW POTENTIAL CUSTOMER
    users_facade = UsersFacade(page)

    # WHEN I SIGN IN THE APP
    username, password = users_facade.login_as_new_user()

    # THEN I SHOULD BE ABLE TO LOG IN WITH MY NEW USER
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()


def test_login(page: Page):

    # GIVEN I AM AN AUTHENTICATED USER
    # Assumes this user already exists in the database
    username = "user_1"
    password = "pass_1"

    # WHEN I LOG INTO THE APPLICATION
    homepage = HomePage(page)

    homepage.navigate()
    homepage.login(username, password)

    # THEN I SHOULD SEE ALL MY PRODUCTS
    expect(page.get_by_role("heading", name="Your Products:")).to_be_visible()



