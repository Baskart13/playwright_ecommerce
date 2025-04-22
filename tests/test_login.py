import time

from playwright.sync_api import expect
from pages.inventory_page import inventorypage
from pages.order_place import Orderplace


def test_loginverification(logged_in_page):
     #loginpage=Loginpage(page)
     invpage=inventorypage(logged_in_page)
     expect(invpage.inventory_container).to_be_visible()
     #time.sleep(5000)

def test_orderplacement(logged_in_page):
     order_page=Orderplace(logged_in_page)
     order_page.orderplacements()

