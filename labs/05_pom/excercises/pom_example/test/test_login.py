from playwright.sync_api import Page
from models.login import LoginPage


def test_valid_login(page: Page):
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.login('test','test_pass')