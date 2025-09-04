class UserPage:
    def __init__(self, page):
        self.logout = page.get_by_role("button").and_(page.get_by_text("Logout"))

    def logout_user(self):
        self.logout.click()
