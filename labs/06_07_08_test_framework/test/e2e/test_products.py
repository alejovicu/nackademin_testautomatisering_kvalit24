from playwright.sync_api import Page, expect
from models.ui.home import HomePage
from models.ui.admin import AdminPage

# Given I am an admin user​
# When I add a product to the catalog​
# Then The product is available to be used in the app
def test_add_product_to_catalog(page: Page):
    # complete code
    username = "admin"
    password = "test123"

    login_home_page = HomePage (page)
    login_home_page.navigate()
    #Skapar ett objekt för hemsidan och navigerar till den

    login_home_page.login(username, password)
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()

    item = "Mango"
    admin_home_page = AdminPage(page)

    admin_home_page.create_product(item)
    expect(page.get_by_text(item)).to_be_visible()


# Given I am an admin user​
# When I remove a product from the catalog​
# Then The product should not be listed in the app to be used
def test_remove_product_from_catalog(page: Page):
    
    username = "admin"
    password = "test123"

    login_home_page = HomePage(page)
    login_home_page.navigate()

    login_home_page.login(username, password)
    expect(page.get_by_text(f"Welcome, {username}!")).to_be_visible()

    item = "Mango"
    admin_home_page = AdminPage(page)

    admin_home_page.delete_product_by_name(item)
    expect(page.get_by_text(item)).not_to_be_visible()