import pytest
from playwright.sync_api import expect

@pytest.mark.no_auth
@pytest.mark.smoke
def test_valid_login(login_page, page, app_url, username, password):

    login_page.open(app_url)
    login_page.login(username, password)

    expect(page).to_have_url(f"{app_url}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

@pytest.mark.no_auth
@pytest.mark.parametrize(
    "username,password,error",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("", "", "Username is required")
    ]
)
def test_negative_login(login_page, app_url, username, password, error):

    login_page.open(app_url)
    login_page.login(username, password)

    login_page.verify_error(error)