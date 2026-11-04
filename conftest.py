
import pytest
from pathlib import Path
from playwright.sync_api import expect

from config import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="session")
def app_url(pytestconfig):
    return pytestconfig.getini("base_url")


@pytest.fixture(scope="session")
def username():
    return USERNAME


@pytest.fixture(scope="session")
def password():
    return PASSWORD


@pytest.fixture(scope="session")
def auth_state(browser, app_url):

    auth_dir = Path("playwright/.auth")
    auth_dir.mkdir(parents=True, exist_ok=True)

    auth_file = auth_dir / "user.json"

    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)

    login_page.open(app_url)
    login_page.login(USERNAME, PASSWORD)

    expect(page).to_have_url(f"{app_url}/inventory.html")

    context.storage_state(path=str(auth_file))

    context.close()

    return str(auth_file)


@pytest.fixture
def browser_context_args(browser_context_args, request, auth_state):

    if request.node.get_closest_marker("no_auth"):
        return browser_context_args

    return {
        **browser_context_args,
        "storage_state": auth_state
    }


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
