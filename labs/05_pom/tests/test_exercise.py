from playwright.sync_api import Page, expect

# def test_locate_click_button(page: Page):
    
#     page.goto("https://www.qa-practice.com/elements/button/simple")

#     button_element = page.get_by_role("button", name= "Click")

#     button_element.click()

#     expect(page.get_by_text("Submitted")).to_be_visible()  


# def test_input_field(page: Page):
    
#     page.goto("https://www.qa-practice.com/elements/input/simple")

#     field_element = page.get_by_role("textbox", name="Submit me")

#     field_element.fill("HelloNahom")

#     field_element.press("Enter")

#     expect(page.get_by_text("HelloNahom")).to_be_visible()
