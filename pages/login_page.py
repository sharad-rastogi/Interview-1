
from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_error(self, message):
        expect(self.error_message).to_contain_text(message)
