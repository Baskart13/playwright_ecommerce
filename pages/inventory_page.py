from playwright.sync_api import Page

class inventorypage:

    def __init__(self,page:Page):
        self.page=page
        self.inventory_container=page.locator("#products")