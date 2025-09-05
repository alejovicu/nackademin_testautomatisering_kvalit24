# models/home.py
class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:5173/")
        self.page.wait_for_load_state("domcontentloaded")
