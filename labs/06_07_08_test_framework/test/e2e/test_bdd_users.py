from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.user import UserPage
from models.ui.signup import SignupPage
import libs.utils
import pytest
from playwright.sync_api import sync_playwright

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@scenario('feature/authentication.feature', 'New user can sign up and log in successfully')
def test_new_user_can_sign_up_and_log_in_successfully():
    """New user can sign up and log in successfully."""


@given('a new user with a unique username and password')
def given_new_user(page):
    """a new user with a unique username and password."""
    username = libs.utils.generate_string_with_prefix()
    password = libs.utils.generate_string_with_prefix()
    # print(f"/username: {username}")
    # print(f"/password: {password}")


    page.username = username
    page.password = password



@when('the user logs in via the UI')
def when_login(page):
    """the user logs in via the UI."""
    username = page.username
    password = page.password
    home_page = HomePage(page)

    home_page.login(username, password)


@when('the user signs up via the UI')
def when_signup(page):
    """the user signs up via the UI."""

    username = page.username
    password = page.password

    home_page = HomePage(page)
    signup_page = SignupPage(page)

    home_page.navigate()
    home_page.go_to_signup()
    signup_page.signup(username, password)
    page.wait_for_load_state("networkidle")
    signup_page.go_to_home()


@then('the user should see a personalized welcome message')
def then_see_welcome_message(page):
    """the user should see a personalized welcome message."""
    home_page = HomePage(page)
    username = page.username

    user_page = UserPage(page)

    expect(user_page.welcome_message_with_username).to_be_visible()
    expect(user_page.welcome_message_with_username).to_contain_text(username)
    expect(home_page.login_input_username).to_be_hidden()
    expect(home_page.login_input_password).to_be_hidden()


@scenario('feature/user.feature', 'User with no products can see it has no products')
def test_user_with_no_products_can_see_it_has_no_products():
    """User with no products can see it has no products."""


@scenario('feature/user.feature', 'User with products can see their products')
def test_user_with_products_can_see_their_products():
    """User with products can see their products."""


@given('a User with username "USERNAME1" and password "PASS_USER1"')
def user1_with_authentication(page):
    """Prepare user1 has no products"""
    page.username = "user"
    page.password = "user123"


@given('a user with username "USERNAME2" and password "PASS_USER2"')
def user2_with_authentication(page):
    """Prepare user2 has products"."""
    page.username = "test"
    page.password = "test123"


@when('the user logs in')
def user_login(page):
    """the user logs in via UI"""
    home_page = HomePage(page)
    home_page.login(page.username, page.password)


@then('the product list should contain "Laptop"')
def product_list_contains_laptop(page):
    """the product list should contain "Laptop"."""
    user_page = UserPage(page)
    products = user_page.get_user_products()
    assert "Laptop" in products


@then('the user should see no products')
def user_should_see_no_products(page):
    """the user should see no products."""
    user_page = UserPage(page)
    products = user_page.get_user_products()
    assert len(products) == 0


@then('the user should see their products')
def user_should_see_their_products(page):
    """the user should see their products."""
    user_page = UserPage(page)
    products = user_page.get_user_products()
    assert len(products) > 0