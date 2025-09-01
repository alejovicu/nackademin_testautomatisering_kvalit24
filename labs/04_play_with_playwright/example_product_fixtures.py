# This is an example about how to use Playwright with explicit Fixtures
# to understand that we could say in code which
# browser to use and/or which mode to run it
# In the course we will use the built in page fixture instead but is important
# to understand the difference.

import re
from playwright.sync_api import sync_playwright, expect

def test_has_title_fixtures():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)  # set headless=True to hide UI

        # Create a new browser context (like a fresh browser profile)
        context = browser.new_context()

        # Open a new page in that context
        page = context.new_page()

        # Navigate
        page.goto("https://playwright.dev/")

        # Assertion
        expect(page).to_have_title(re.compile("Playwright"))

        # Cleanup
        context.close()
        browser.close()