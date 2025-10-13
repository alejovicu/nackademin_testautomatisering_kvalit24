from playwright.sync_api import Page
from facade.users import UsersFacade


def test_signup(page: Page):
    # Given I am a new potential customer​
    # When I signup in the app​
    # Then I should be able to log in with my new user
    UsersFacade(page).login_as_new_user()


def test_products_signup(page: Page):
    # Given I am an authenticated user​
    # When I log in into the application​
    # Then I should see all my products
    UsersFacade(page).check_product_list()