import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://google.com/")
