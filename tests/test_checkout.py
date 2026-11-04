
import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_end_to_end_checkout(
        inventory_page, cart_page, checkout_page, page, app_url):

    page.goto(f"{app_url}/inventory.html")

    inventory_page.add_products_to_cart()

    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.open_cart()

    expected_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ]

    assert cart_page.get_cart_items() == expected_items

    cart_page.proceed_to_checkout()

    checkout_page.enter_checkout_details(
        "Rushikesh",
        "Thete",
        "411001"
    )

    checkout_page.continue_checkout()

    item_total = checkout_page.get_amount(checkout_page.item_total)
    tax = checkout_page.get_amount(checkout_page.tax)
    total = checkout_page.get_amount(checkout_page.total)

    assert item_total + tax == pytest.approx(total, abs=0.01)

    checkout_page.finish_checkout()

    expect(checkout_page.complete_message).to_have_text(
        "Thank you for your order!"
    )


@pytest.mark.parametrize(
    "first_name,last_name,postal_code,error",
    [
        ("", "Thete", "411001", "Error: First Name is required"),
        ("Rushikesh", "", "411001", "Error: Last Name is required"),
        ("Rushikesh", "Thete", "", "Error: Postal Code is required")
    ]
)
@pytest.mark.regression
def test_checkout_form_validation(
        inventory_page, cart_page, checkout_page, page, app_url,
        first_name, last_name, postal_code, error):

    page.goto(f"{app_url}/inventory.html")

    inventory_page.add_products_to_cart()

    inventory_page.open_cart()

    cart_page.proceed_to_checkout()

    checkout_page.enter_checkout_details(
        first_name, last_name, postal_code
    )

    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_have_text(error)
