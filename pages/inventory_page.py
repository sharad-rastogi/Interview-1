from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator(".product_sort_container")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.add_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.add_bike_light = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.remove_backpack = page.locator("#remove-sauce-labs-backpack")

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    def get_product_names(self):
        return self.product_names.all_text_contents()

    def get_product_prices(self):
        prices = self.product_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in prices]

    def add_products_to_cart(self):
        self.add_backpack.click()
        self.add_bike_light.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()

    def open_cart(self):
        self.cart_icon.click()

    def remove_backpack_from_inventory(self):
        self.remove_backpack.click()