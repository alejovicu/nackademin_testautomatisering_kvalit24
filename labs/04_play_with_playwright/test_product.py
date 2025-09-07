import re
from playwright.sync_api import Page, expect

site_url='http://localhost:5173/'

# Given I am an admin user​

# When I add a product to the catalog​

# Then The product is available to be used in the app

def test_add_product(page: Page):

    username = "admin"
    password = "1234"
    product = "apple"

    #Login in Admin
    page.goto(site_url)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role('button',  name= 'Login' ).click()


    #Add product as Admin

    products = page.locator('.product-item')
    expect(products.first).to_be_visible()  # säkerställ att minst en produkt syns
    number_of_products_before = products.count()

    page.get_by_placeholder("Product Name").fill(product)
    page.get_by_role('button',  name= 'Create Product' ).click()


    products_after = page.locator('.product-item')
    number_of_products_after = products_after.count()

    assert number_of_products_after == number_of_products_before + 1


# Given I am an admin user​

# When I remove a product from the catalog​

# Then The product should not be listed in the app to be used


    
def test_remove_product(page: Page):
    username = "admin"
    password = "1234"
    product_name = "apple"  # produkten vi vill ta bort

    # Given I am an admin user
    page.goto(site_url)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role('button', name='Login').click()

    # Wait until the product list is visible
    product = page.locator(".product-item", has_text=product_name)
    expect(product).to_be_visible()  # säkerställ att produkten finns

    # When I remove a product from the catalog
    product.get_by_role("button", name="Delete").click()


    # Then The product should not be listed in the app to be used
    expect(page.locator(".product-item", has_text=product_name)).to_have_count(0)

