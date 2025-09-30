from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
import libs.utils


# Given I am a new potential customer​
# When I signup in the app​
# Then I should be able to log in with my new user
def test_signup(page: Page):
    username = libs.utils.generate_string_with_prefix()
    password = "1234"

    # check for the alert that a singup is successful
    # def handle_dialog(dialog):
    #    assert "User registered OK." in dialog.message
    #    dialog.accept()

    # page.on("dialog", handle_dialog)

    home_page = HomePage(page)
    home_page.navigate()
    home_page.go_to_signup()
    signup_page = SignupPage(page)

    with page.expect_response(lambda r: r.url.endswith("/signup") and r.status == 200):
        signup_page.signup(username, password)

    signup_page.go_to_home()
    home_page.login(username, password)
    # check so login is successfull
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()


# Given I am an authenticated user​
# When I log in into the application​
# Then I should see all my products
def test_login(page: Page):
    username = "mimmi"
    password = "1234"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    # check so login is successfull
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()
    # check so the product list h3 is visible. best way i could check this since there is not list element to look for.
    expect(page.locator('h3:has-text("Your Products:")')).to_be_visible()


# Given I am an authenticated user
# When I assign a product to myself
# Then the product should be assigned to me
def test_assign_product_to_user(page: Page):
    username = "mimmi"
    password = "1234"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    user_page = UserPage(page)
    user_page.add_product_to_user("Testprodukt")
    expect(user_page.user_products.filter(has_text="Testprodukt")).to_be_visible()


# Given I am an authenticated user
# When I unassign a product from myself
# Then the product should be unassigned from me
def test_unassign_product_from_user(page: Page):
    username = "mimmi"
    password = "1234"

    home_page = HomePage(page)
    home_page.navigate()
    home_page.login(username, password)
    user_page = UserPage(page)
    user_page.remove_product_from_user("Testprodukt")
    expect(user_page.user_products.filter(has_text="Testprodukt")).not_to_be_visible()
