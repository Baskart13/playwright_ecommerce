
from playwright.sync_api import Page

class Loginpage:

    def __init__(self,page:Page):
        self.page=page

    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client')

    def login(self):
        self.page.get_by_placeholder("email@example.com").fill("b4baskarthiyagarajan@gmail.com")
        self.page.get_by_placeholder("enter your passsword").fill("Connect@123")
        self.page.get_by_role("button", name='Login').click()



