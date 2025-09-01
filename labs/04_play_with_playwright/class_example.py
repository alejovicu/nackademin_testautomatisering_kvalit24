import re
from playwright.sync_api import sync_playwright, expect, Page


def test_open_google(page: Page):
    page.goto("https://google.com/", wait_until="networkidle")
