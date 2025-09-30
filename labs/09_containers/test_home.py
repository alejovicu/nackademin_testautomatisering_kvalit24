from playwright.sync_api import Page, expect
import os

APP_FRONT_URL=os.environ.get('APP_FRONT_URL')

def test_home_load(page: Page):
    page.goto(APP_FRONT_URL)
    expect(page.get_by_text('Nackademin Course App')).to_be_visible()