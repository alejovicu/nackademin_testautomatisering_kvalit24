class UserPage:
    def __init__(self, page):
        self.page = page
        # Correct way to find a button with role + text
        self.logout = page.get_by_role("button", name="Logout")
        # Alternative: self.logout = page.get_by_text("Logout")

    def logout_user(self):
        """Click the logout button"""
        self.logout.click()
