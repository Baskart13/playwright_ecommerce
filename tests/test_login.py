from playwright.sync_api import expect

from pages.login_page import Loginpage
from pages.inventory_page import inventorypage

def test_loginverification(page):
     loginpage=Loginpage(page)
     invpage=inventorypage(page)

     #Navigate into page
     loginpage.navigate()

     #enter username and password
     loginpage.login()

     #verify successful login
     expect(invpage.inventory_container).to_be_visible()

