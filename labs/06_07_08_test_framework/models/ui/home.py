class HomePage:
    def __init__(self, page):
        self.page = page
        # Page elements for the home page
        self.login_input_username = self.page.locator("#root > div > div > input:nth-child(1)")
        self.login_input_password = self.page.locator("#root > div > div > input[type=password]:nth-child(2)")
        self.login_btn_login = self.page.locator("#root > div > div > button")

    def navigate(self):
        """
        Navigates to the home page of the application.
        """
        self.page.goto("http://localhost:5173/")  # Replace with the actual home page URL
        self.page.wait_for_load_state("domcontentloaded")  # Wait for the page to load

    def login(self, username, password):
        """
        Logs in the user (regular or admin) by filling in the username and password fields
        and clicking the login button.
        :param username: The username of the user.
        :param password: The password of the user.
        """
        # Wait for the username input field to be visible
        self.page.wait_for_selector("#root > div > div > input:nth-child(1)")

        # Fill in the login form
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()