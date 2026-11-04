from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.product_names = page.locator(".inventory_item_name")
        self.remove_backpack = page.locator("#remove-sauce-labs-backpack")
        self.continue_shopping = page.locator("#continue-shopping")
        self.checkout_button = page.locator("#checkout")

    def get_cart_items(self):
        return self.product_names.all_text_contents()

    def remove_backpack_from_cart(self):
        self.remove_backpack.click()

    def continue_shopping_to_inventory(self):
        self.continue_shopping.click()

    def proceed_to_checkout(self):
        self.checkout_button.click()