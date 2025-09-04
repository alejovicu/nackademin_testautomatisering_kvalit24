from playwright.sync_api import Page


def test_open_google(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_element = page.get_by_placeholder("Submit me")
    input_element.fill("HelloClass")
    page.keyboard.press("Enter")