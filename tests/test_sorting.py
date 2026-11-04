
import pytest


@pytest.mark.regression
def test_sort_price_low_to_high(inventory_page, page, app_url):

    page.goto(f"{app_url}/inventory.html")

    inventory_page.sort_products("lohi")

    actual_prices = inventory_page.get_product_prices()
    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices


@pytest.mark.regression
def test_sort_name_z_to_a(inventory_page, page, app_url):

    page.goto(f"{app_url}/inventory.html")

    inventory_page.sort_products("za")

    actual_names = inventory_page.get_product_names()
    expected_names = sorted(actual_names, reverse=True)

    assert actual_names == expected_names
