
import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_add_products_and_verify_cart(inventory_page, cart_page, page, app_url):

    page.goto(f"{app_url}/inventory.html")

    inventory_page.add_products_to_cart()

    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.open_cart()

    actual_items = cart_page.get_cart_items()

    expected_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ]

    assert actual_items == expected_items


@pytest.mark.regression
def test_remove_product_and_verify_inventory(inventory_page, cart_page, page, app_url):

    page.goto(f"{app_url}/inventory.html")

    inventory_page.add_products_to_cart()

    inventory_page.open_cart()

    cart_page.remove_backpack_from_cart()

    expect(cart_page.cart_items).to_have_count(1)

    expect(inventory_page.cart_badge).to_have_text("1")

    cart_page.continue_shopping_to_inventory()

    expect(inventory_page.add_backpack).to_be_visible()
    expect(inventory_page.cart_badge).to_have_text("1")
