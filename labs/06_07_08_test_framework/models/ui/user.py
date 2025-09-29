# models/ui/user.py
class UserPage:
    def __init__(self, page):
        self.page = page
        self.welcome_message = page.get_by_text("Welcome,")
        self.your_products_header = page.get_by_text("Your Products:")
        self.logout_button = page.get_by_role("button", name="Logout")
        self.no_products_message = page.get_by_text("No products assigned.")
        
    def is_logged_in(self):
        return self.logout_button.is_visible()
    
    def get_username_from_welcome(self):
        welcome_text = self.welcome_message.text_content()
        return welcome_text.replace("Welcome, ", "").replace("!", "")
    
    def logout(self):
        self.logout_button.click()