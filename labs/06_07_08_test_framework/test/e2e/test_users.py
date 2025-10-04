from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.signup import SignupPage
from models.ui.user import UserPage
from models.ui.admin import AdminPage
import libs.utils


def test_signup(page: Page):
    home = HomePage(page)
    home.navigate()
    home.go_to_signup()

    signup = SignupPage(page)
    username = libs.utils.generate_string_with_prefix("user", 8)
    password = libs.utils.generate_string_with_prefix("pw", 12)
    signup.signup(username, password)

    signup.go_to_home()

    home.login(username, password)
    page.reload(wait_until="domcontentloaded")

    page.locator("button:has-text('Logout'), a:has-text('Logout')").first.wait_for(
        timeout=7000
    )
    assert page.get_by_text("Your products:").count() > 0


def test_user_can_add_and_remove_product(page: Page):
    home = HomePage(page)
    home.navigate()
    home.login("admin", "1234")

    admin = AdminPage(page)
    name = libs.utils.generate_string_with_prefix("e2e", 6)
    admin.create_product(name)
    expect(page.locator("div.product-item").filter(has_text=name)).to_be_visible(
        timeout=7000
    )

    page.locator("button:has-text('Logout'), a:has-text('Logout')").first.click()

    home.go_to_signup()
    signup = SignupPage(page)
    username = libs.utils.generate_string_with_prefix("user", 8)
    password = libs.utils.generate_string_with_prefix("pw", 12)
    signup.signup(username, password)
    signup.go_to_home()

    home.login(username, password)
    page.reload(wait_until="domcontentloaded")
    page.get_by_text("Your Products:").wait_for(timeout=7000)

    user = UserPage(page)
    user.add_product_to_user(name)

    user.remove_product_from_user(name)
