import time

from playwright.sync_api import Page, expect


class Orderplace():
    def __init__(self,page=Page):
        self.page=page

    def orderplacements(self):
        product1=self.page.locator("div.card-body",has_text="ZARA COAT 3").locator("text=Add To Cart").click()
        #product1.locator("button").click()
        self.page.locator("li",has_text="Cart").click()
        #expect(self.page.locator("div.infoWrap",has_text="ZARA COAT 3").is_visible())
        self.page.get_by_text("Checkout").click()
        self.page.get_by_placeholder("Select Country").type("India")
        self.page.wait_for_selector("text=India")
        self.page.click("text=India >> nth=1")
        time.sleep(1)
        self.page.get_by_text("Place Order").click()
        #self.page.locator("div.a",has_text="Place Order ").click()
        pageframe=self.page.locator("ng-star-inserted")
        expect(self.page.get_by_text(" Thankyou for the order. ")).to_be_visible()
        time.sleep(5)




